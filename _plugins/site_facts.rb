# Site facts generator — emits build-time stats for the Colophon page.
#
# Source: atlas/website/v5/panta-rhei-ia-doctrine-v5.md §9.4 ("Site facts
# schema"). The Colophon page renders this hash as a table at section 10
# ("Site facts at last build").
#
# Why a plugin (not a static data file): the facts have to be CURRENT at
# every build — total page count, lane counts, and release version drift
# every release. Hand-editing them would silently rot. The plugin walks
# site.pages + site.documents and _data/* once per build and emits a hash
# at site.data["site_facts"].
#
# What the plugin can NOT measure inside Jekyll, and why:
#   · pagefind_index_size — Pagefind runs after Jekyll (npm exec pagefind),
#     so the index file doesn't exist when this plugin runs. Emitted as nil;
#     the template falls back to a "(see Pagefind index in /pagefind/)"
#     link.
#   · build_time_seconds — Jekyll plugins can hook :site, :post_write to
#     measure their own runtime, but the surrounding `bundle exec jekyll
#     build` + post-build steps (asset_fingerprint, pagefind, etc.) are
#     outside the measurement window. Approximated as "Jekyll generation
#     time" (the time from :site, :pre_render to :site, :post_write) so
#     readers don't get a misleadingly small number.
#
# Liquid access:
#   {{ site.data.site_facts.release_version }}
#   {{ site.data.site_facts.total_pages }}
#   {% for lane in site.data.site_facts.lane_counts %}{{ lane[0] }}: {{ lane[1] }}{% endfor %}
#
# v5 next-wave W4b · 2026-05-23.

require "time"

module PantaRhei
  module SiteFacts
    # Lane keys recognised on the public site. Mirrors the 8 epistemic
    # lanes in the top navigation + footer §5.2 (W2). Extra keys (support,
    # registry, bibliography, publications) collapse into "other" so they
    # don't pollute the lane signal.
    PRIMARY_LANES = %w[
      discover program agenda corpus results verify impact engage
    ].freeze

    # Publication-class keys mirror _data/publication_classes.yml (W1).
    PUBLICATION_CLASSES = %w[
      monograph hinge_paper research_note research_dossier research_code
    ].freeze

    class << self
      def build_for(site)
        {
          "generated_at"        => Time.now.utc.iso8601,
          "release_version"     => release_version(site),
          "manifest_hash"       => manifest_hash(site),
          "total_pages"         => total_pages(site),
          "lane_counts"         => lane_counts(site),
          "publication_counts"  => publication_counts(site),
          "faq_entries"         => faq_entries(site),
          "pagefind_index_size" => nil, # measured outside Jekyll
          "build_time_seconds"  => nil, # filled in by post_write hook
          "pdf_dossiers"        => count_pdf_dossiers(site),
          "markdown_dossiers"   => count_markdown_dossiers(site),
        }
      end

      private

      def release_version(site)
        site.data.dig("release", "current", "release_id")
      end

      def manifest_hash(site)
        # Per IA §9.4 the manifest_hash should identify the exact release
        # bundle. The atlas commit is the orchestrating SHA across all
        # downstream repos; the site commit (this repo) is what actually
        # generated this build. Prefer atlas for cross-repo identity,
        # fall back to site.
        atlas_sha = site.data.dig("release", "current", "sources", "atlas", "commit")
        site_sha  = site.data.dig("release", "current", "sources", "site", "commit")
        atlas_sha || site_sha
      end

      def total_pages(site)
        # Standard pages + all collection documents (corpus monographs,
        # registry entries, glossary, etc.). Excludes redirect/sitemap
        # entries that wouldn't be reader-visible.
        documents_count = site.collections.values.sum { |c| c.docs.size }
        site.pages.size + documents_count
      end

      def lane_counts(site)
        counts = PRIMARY_LANES.each_with_object({}) { |k, h| h[k] = 0 }
        each_indexable(site) do |page|
          lane = page_lane(page)
          counts[lane] += 1 if counts.key?(lane)
        end
        counts
      end

      def publication_counts(site)
        counts = PUBLICATION_CLASSES.each_with_object({}) { |k, h| h[k] = 0 }
        each_indexable(site) do |page|
          klass = page_publication_class(page)
          counts[klass] += 1 if klass && counts.key?(klass)
        end
        counts
      end

      def faq_entries(site)
        total = 0
        Dir.glob(File.join(site.source, "_data", "faqs", "*.yml")).each do |path|
          data = safe_yaml_load(path)
          next unless data.is_a?(Hash)
          faqs = data["faqs"]
          total += faqs.size if faqs.is_a?(Array)
        end
        total
      end

      def count_pdf_dossiers(site)
        pdf_glob = File.join(site.source, "assets", "downloads", "*.pdf")
        Dir.glob(pdf_glob).size
      end

      def count_markdown_dossiers(site)
        # Markdown dossiers (.dossier.md) are generated downstream by the
        # dossier pipeline; not all of them live in /assets/. Use the
        # /assets/downloads/*.md glob as a proxy. Returns 0 if the
        # convention isn't in use yet.
        md_glob = File.join(site.source, "assets", "downloads", "*.md")
        Dir.glob(md_glob).size
      end

      # ── helpers ────────────────────────────────────────────────────────

      def each_indexable(site, &block)
        site.pages.each(&block)
        site.collections.each_value do |c|
          c.docs.each(&block)
        end
      end

      def page_lane(page)
        data = page.respond_to?(:data) ? page.data : {}
        return data["lane"] if data["lane"].is_a?(String)
        return data["v2_lane"] if data["v2_lane"].is_a?(String)
        # Fall back to URL-prefix matching, mirroring the heuristic in
        # _layouts/default.html (search_lane assignment).
        url = page.respond_to?(:url) ? page.url.to_s : ""
        PRIMARY_LANES.each do |lane|
          return lane if url.include?("/#{lane}/")
        end
        nil
      end

      def page_publication_class(page)
        data = page.respond_to?(:data) ? page.data : {}
        # Prefer the v5 publication_class field (W7 will populate it). For
        # now, derive from publication_type + URL prefix so the counts are
        # meaningful even before the W7 migration completes.
        return data["publication_class"] if data["publication_class"].is_a?(String)

        ptype = data["publication_type"].to_s.downcase
        url   = page.respond_to?(:url) ? page.url.to_s : ""

        return "monograph"        if ptype.include?("monograph_book") || ptype == "book"
        return "hinge_paper"      if url.include?("/publications/research-papers/")
        return "research_note"    if ptype == "research note" || url.include?("/publications/research-notes/")
        return "research_dossier" if url.include?("/publications/dossiers/")
        return "research_code"    if url.include?("/verify/taulib/")
        nil
      end

      def safe_yaml_load(path)
        require "yaml"
        # Jekyll runs on multiple Ruby versions; allow aliases for
        # _data/faqs/* files that use YAML anchors.
        YAML.safe_load(File.read(path), permitted_classes: [Date, Time], aliases: true)
      rescue StandardError
        nil
      end
    end
  end
end

# ── Wire into Jekyll's build lifecycle ────────────────────────────────────
#
# :post_read runs after all _data/* and front-matter is loaded but before
# pages are rendered, so the facts are visible to every page that includes
# the colophon block at render time.
#
# A second hook (:post_render) measures the elapsed Jekyll generation time
# and patches it into site_facts after-the-fact. The colophon page caches
# the hash on its own render path; if build_time_seconds shows nil that's
# fine — the template handles it gracefully.

Jekyll::Hooks.register :site, :post_read do |site|
  site.data ||= {}
  site.data["site_facts"] = PantaRhei::SiteFacts.build_for(site)
  site.config["__site_facts_t0"] = Time.now
end

Jekyll::Hooks.register :site, :post_write do |site|
  t0 = site.config["__site_facts_t0"]
  next unless t0.is_a?(Time)
  elapsed = (Time.now - t0).round(2)
  facts = site.data["site_facts"]
  facts["build_time_seconds"] = elapsed if facts.is_a?(Hash)
end
