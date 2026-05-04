---
layout: program-doc
title: "Search"
permalink: /search/
lane: support
v2_lane: support
type: "Support page"
status: "Canonical"
updated: "May 2026"
summary_short: "Search the entire Panta Rhei Research Program site — corpus, results, verify, publications, agenda, impact, engage, program."
right_rail:
  toc: false
  related:
    - title: "Lane root"
      url: /
    - title: "Sitemap"
      url: /sitemap/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Support page"
    scope: "Site search"
    status: "Canonical"
    updated: "May 2026"
---

## Search the site

Search across the entire site — corpus pages, registry items, TauLib modules, results, verification surfaces, publications, agenda items, the structural challenge ledger, impact essays, and engage routes. Filter by lane and content type.

<noscript>
<div class="notice note">
<p><strong>Search requires JavaScript.</strong> Use the lane navigation in the left rail or the <a href="https://www.google.com/search?q=site%3Apanta-rhei.site">site search via Google</a> as alternatives.</p>
</div>
</noscript>

<div id="page-search-container" class="page-search-container"></div>

<p class="page-search-fallback"><a id="page-search-google-link" href="https://www.google.com/search?q=site%3Apanta-rhei.site" target="_blank" rel="noopener">Broader site search with Google</a></p>

<style>
.page-search-container {
  margin: 1.5rem 0 1rem;
  min-height: 320px;
}
.page-search-fallback {
  margin-top: 1rem;
  font-size: 0.88rem;
  color: var(--text-muted, #5b6772);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  function initPageSearch(attemptsRemaining) {
    if (typeof PagefindUI !== 'undefined') {
      new PagefindUI({
        element: "#page-search-container",
        showSubResults: true,
        showImages: false,
        showEmptyFilters: true,
        openFilters: ["lane", "type"],
      });
      var input = document.querySelector('#page-search-container .pagefind-ui__search-input');
      if (input) {
        // Auto-focus on landing
        setTimeout(function() { input.focus(); }, 50);
        input.addEventListener('input', syncPageGoogleLink);
      }
      syncPageGoogleLink();
      // If a `?q=` query param was passed (e.g. from external search redirect), pre-fill
      try {
        var params = new URLSearchParams(window.location.search);
        var initial = params.get('q');
        if (initial && input) {
          input.value = initial;
          input.dispatchEvent(new Event('input', { bubbles: true }));
        }
      } catch (e) { /* noop */ }
      return;
    }
    if (attemptsRemaining > 0) {
      setTimeout(function() { initPageSearch(attemptsRemaining - 1); }, 100);
      return;
    }
    document.getElementById('page-search-container').innerHTML =
      '<p style="padding:16px;color:#5b6772;font-size:0.88rem;">Search index is still loading. If this persists, use the <a href="https://www.google.com/search?q=site%3Apanta-rhei.site">site search via Google</a> as a fallback.</p>';
  }

  function syncPageGoogleLink() {
    var link = document.getElementById('page-search-google-link');
    if (!link) return;
    var input = document.querySelector('#page-search-container .pagefind-ui__search-input');
    var term = input && input.value ? input.value.trim() : '';
    var query = 'site:panta-rhei.site' + (term ? ' ' + term : '');
    link.href = 'https://www.google.com/search?q=' + encodeURIComponent(query);
  }

  initPageSearch(20);
});
</script>

## How search works

This site is searched with [Pagefind](https://pagefind.app/), a static-site search engine that runs entirely in your browser. The search index is built at deploy time from the rendered pages and ships as plain JSON shards loaded on demand. No queries are sent to a third-party server.

Results are filtered by lane (Discover, Program, Agenda, Corpus, Results, Verify, Impact, Engage, Support) and by content type (lane root, monograph part, registry item, TauLib module, paper, white paper, briefing, structural challenge entry, etc.). Use the filter panel on the left of the result list to narrow down.

If a search term doesn't surface what you are looking for here, the **broader site search via Google** below covers anything Google has indexed (often more recent than the deploy-time Pagefind index for very fresh content).
