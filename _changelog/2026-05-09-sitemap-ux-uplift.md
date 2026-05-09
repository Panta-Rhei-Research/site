---
title: "Sitemap UX uplift — instant search, lane jump-nav, per-lane counts"
date: 2026-05-09
change_type: "site-release"
summary_short: "Frontier-level UX layer on /sitemap/: client-side instant search across all 184 canonical pages (with /-to-focus, Esc-to-clear, ?q= deep-links), sticky lane jump-nav with scroll-spy, per-lane page counts, totals chip, and an empty-state with suggestion buttons. Pure progressive enhancement — page is fully usable without JS."
affected_lanes:
  - support
right_rail:
  toc: false
  related:
    - title: "Sitemap"
      url: /sitemap/
    - title: "Changelog"
      url: /changelog/
    - title: "Discover"
      url: /discover/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

The `/sitemap/` page lifts to a frontier-level directory experience. Lands on top of the L1/L2 sync wave that ships 184 canonical anchors across 8 primary lanes + a support layer.

### Instant search

- Search input above the lane grid with placeholder "Search 184 pages — try 'tau', 'dark matter', 'verify'…".
- Live-filters all 184 mini-cards by case-insensitive substring match against link title.
- Hides whole lane cards when all their links are filtered out.
- Status chip below the input shows "<n> of 184 pages match '<query>'" or "Showing all 184 pages." when empty.
- Deep-linkable: filter state syncs to URL via `?q=<query>` so reviewers can share filtered views.
- Empty state ("No pages match your search.") with three suggestion buttons (`results`, `verify`, `challenge`) that apply the suggestion on click.
- Clear button (×) inside the input resets state.
- Keyboard: <kbd>/</kbd> focuses the input from anywhere on the page; <kbd>Esc</kbd> while focused clears the query, then blurs.
- Debounced (80 ms) — no jank while typing.

### Lane jump-nav with scroll-spy

- Sticky pill-row above the lane grid: 8 lane pills + a Support pill.
- Each pill is an in-page anchor (`#lane-discover`, `#lane-program`, …, `#lane-support`).
- Active state syncs to scroll position via `IntersectionObserver` — the pill for the lane currently in the viewport gets highlighted with the brand colour.
- Mobile: jump-nav becomes horizontally scrollable.

### Per-lane counts and totals

- Each lane card header now carries an "<count> entries" chip (e.g. "20 entries" for Impact, "34 entries" for Results).
- Intro section gains a totals chip strip: "<strong>8</strong> primary lanes · <strong>184</strong> canonical pages".

### Validation hardening

`scripts/assert_v4_sitemap.py` extended with assertions for:

- `id="sitemap-search-input"` and `role="search"` present.
- `class="sitemap-jump"` with ≥9 pills covering all 8 lanes + support.
- `data-sitemap-lane-count` attribute on each lane card.
- `data-sitemap-link-title` attribute on each mini-card (drives client-side search).
- `/assets/js/sitemap-search.js` script tag loaded.
- `id="sitemap-empty"` empty-state container present.
- `class="sitemap-totals"` chip in intro.

### Progressive enhancement

The page is fully usable without JavaScript:

- All 184 mini-cards render server-side.
- Without JS, the search input is inert (filter doesn't apply) but the input doesn't break the page.
- Jump-nav pills are plain anchor links — they still scroll to lane sections without JS.
- Reduced-motion users get all CSS transitions disabled.

### Files touched

- `sitemap.md` — Liquid additions for search, jump-nav, totals, count chips, empty state.
- `_sass/_sitemap.scss` — styles for all UX components, including a `prefers-reduced-motion` override.
- `assets/js/sitemap-search.js` (new, 200 lines vanilla JS) — search filter, URL sync, jump-nav scroll-spy, keyboard shortcuts.
- `_layouts/program-doc.html` — conditional script load gated by `page.support_type == "sitemap"` so no global JS bundle change.
- `scripts/assert_v4_sitemap.py` — UX-component assertions.
