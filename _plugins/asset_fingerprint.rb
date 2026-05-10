# Content-hash fingerprinting for /assets/css/*.css and /assets/js/*.js.
#
# Why: production CSS/JS at panta-rhei.site is served behind a Cloudflare cache
# rule with `cache-control: public, max-age=31536000, immutable`. The
# `immutable` directive is intended for content-hashed URLs — without one,
# browsers treat the cached copy as fresh for a full year and skip
# revalidation, so style/script changes can take 12+ hours to propagate
# (observed on the v4 footer change merged via #171, where the rebuilt CSS
# wasn't visible until a manual cache purge ~15h later).
#
# This plugin computes a 10-char SHA-256 of each fingerprintable file's bytes
# after Jekyll has written the destination tree, renames the file to embed
# the hash (`main.<hash>.css`), and rewrites every reference inside generated
# `_site/` outputs to use the fingerprinted URL. Because the URL changes
# whenever the content changes, the long-lived `immutable` cache lifetime
# becomes safe again — browsers fetch the new URL on the next page load.
#
# Out of scope:
#   · /pagefind/* — built outside Jekyll's pipeline (npm exec pagefind);
#     handled separately if the same cache problem affects it.
#   · /assets/fonts, /assets/data, /assets/og, etc. — content-stable
#     filenames already, no need for hashing.

require "digest"
require "fileutils"
require "pathname"

module PantaRhei
  module AssetFingerprint
    FINGERPRINT_LENGTH = 10

    # Paths whose `_site/` output we fingerprint. Patterns match canonical URL
    # form (leading slash, forward separators).
    URL_PATTERNS = [
      %r{\A/assets/css/.+\.css\z},
      %r{\A/assets/js/.+\.js\z}
    ].freeze

    # Output extensions we rewrite to swap original URLs for fingerprinted
    # ones. Anything text-shaped that might embed an asset reference.
    REWRITE_EXTS = %w[.html .xml .css .js .json .txt].freeze

    # Skip files that already look fingerprinted — defensive, in case a build
    # somehow re-runs over an already-processed tree.
    ALREADY_FINGERPRINTED = /\.[a-f0-9]{#{FINGERPRINT_LENGTH}}\.(?:css|js)\z/.freeze

    module_function

    def fingerprintable?(url)
      return false if url =~ ALREADY_FINGERPRINTED
      URL_PATTERNS.any? { |re| url =~ re }
    end

    def inject(url, digest)
      ext = File.extname(url)
      base = url[0, url.length - ext.length]
      "#{base}.#{digest}#{ext}"
    end

    def hex(bytes)
      Digest::SHA256.hexdigest(bytes)[0, FINGERPRINT_LENGTH]
    end
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  dest = site.dest
  dest_pn = Pathname.new(dest)

  # 1) Discover fingerprintable files that Jekyll just wrote.
  candidates = Dir.glob(File.join(dest, "assets", "css", "**", "*.css")) +
               Dir.glob(File.join(dest, "assets", "js",  "**", "*.js"))

  fingerprints = {}
  renames = []
  candidates.each do |abs_path|
    rel_url = "/" + Pathname.new(abs_path).relative_path_from(dest_pn).to_s
    next unless PantaRhei::AssetFingerprint.fingerprintable?(rel_url)
    digest = PantaRhei::AssetFingerprint.hex(File.binread(abs_path))
    fingerprinted_url = PantaRhei::AssetFingerprint.inject(rel_url, digest)
    fingerprinted_path = File.join(dest, fingerprinted_url.sub(%r{\A/}, ""))
    fingerprints[rel_url] = fingerprinted_url
    renames << [abs_path, fingerprinted_path]
  end

  next if fingerprints.empty?

  # 2) Move each file to its fingerprinted location. Removing the original
  #    forces every consumer to migrate to the fingerprinted URL — the smoke
  #    test catches anything we missed.
  renames.each do |src, dst|
    FileUtils.mkdir_p(File.dirname(dst))
    FileUtils.mv(src, dst)
  end

  # 3) Rewrite every text output in _site/ to reference the fingerprinted URL.
  #    Scope: only paths sitting inside an HTML/XML attribute value (i.e.
  #    quoted with " or '). This avoids touching prose mentions like
  #    `<code>/assets/js/foo.js</code>` in changelog entries — the source
  #    file's name on disk is still `foo.js`, the fingerprint only applies
  #    to the served URL.
  pattern_keys = fingerprints.keys.sort_by { |k| -k.length }
  attr_re = %r{(["'])(#{pattern_keys.map { |k| Regexp.escape(k) }.join('|')})(\?[^"']*)?\1}

  rewrites = 0
  Dir.glob(File.join(dest, "**", "*"), File::FNM_DOTMATCH).each do |path|
    next unless File.file?(path)
    next unless PantaRhei::AssetFingerprint::REWRITE_EXTS.include?(File.extname(path).downcase)
    original = File.binread(path)
    next unless original.match?(attr_re)
    rewritten = original.gsub(attr_re) do
      quote = Regexp.last_match(1)
      orig_path = Regexp.last_match(2)
      "#{quote}#{fingerprints[orig_path]}#{quote}"
    end
    next if rewritten == original
    File.binwrite(path, rewritten)
    rewrites += 1
  end

  Jekyll.logger.info "Fingerprint:",
    "renamed #{fingerprints.size} asset(s); rewrote refs in #{rewrites} file(s)"
end
