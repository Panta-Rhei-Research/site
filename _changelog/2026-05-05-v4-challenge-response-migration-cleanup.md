---
title: "v4 Structural Challenge Migration Cleanup"
date: 2026-05-05
change_type: "site-release"
summary_short: "Completed the migration from the retired v1 Problem Ledger / Problem Answers vocabulary to the v4 Structural Challenge Ledger / Challenge Responses architecture across all canonical pages, with template deduplication, dashboard model update, route rationalization, and browse-surface clarification."
affected_lanes:
  - agenda
  - results
  - discover
  - verify
right_rail:
  toc: false
  related:
    - title: "Structural Challenge Ledger"
      url: /agenda/structural-challenge-ledger/
    - title: "Challenge Responses"
      url: /results/challenge-responses/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

Completed the migration from the retired v1 Problem Ledger / Problem Answers vocabulary to the v4 Structural Challenge Ledger / Challenge Responses architecture. Six waves shipped:

- **Terminology cleanup** (Wave 1) — replaced "Problem Ledger" labels, links, and CTAs with "Structural Challenge Ledger" on canonical surfaces (Agenda root, Results root cross-cutting card, plate captions + alt text, Discover gateway, Verify how-to and bridge-verification pages). v1 terms now appear only in explicit archive/provenance contexts.
- **Challenge Response template deduplication** (Wave 2) — stripped ~9,200 lines of duplicate Markdown body across all 214 Challenge Response pages. The `challenge-response-entry` layout already renders every canonical section from frontmatter; the embedded body was a verbatim duplicate, producing double sections + duplicate TOC entries on every published page. Frontmatter preserved; body emptied.
- **Progress Against Agenda dashboard model update** (Wave 3) — migrated the dashboard from the v1 hybrid model to a separated-panels model. New "Obligation surfaces" section with four panels (214 Challenge Responses · Core Semantics / Recovery · Mathematical Refusals · Legacy v1 raw-feed archive) preserves the underlying data feed totals without rolling them up into a single confusing total. Item-kind labels render as v4 terms ("Structural Challenge", "Core Semantics / Recovery", "Mathematical Refusal") via a Liquid `case` transform.
- **Route rationalization** (Wave 4) — converted `/results/by-problem/` (234-claim alphabetical browse), `/results/problem-ledger/` (v2 compatibility bridge), and `/program/research-agenda/problem-ledger-source-policy/` to single-hop redirects pointing at the canonical SCL surfaces. Updated 6 inbound surfaces (sitemap, results/by-book + by-domain right-rails, 3 research notes pointing at non-existent deep URLs).
- **Browse-surface clarification** (Wave 5) — clarified `/results/browse/` as the Generic Result Catalogue (distinct from Challenge Responses), added a notice block on `/results/classifications/` explaining the typing grammar applies to the generic catalogue (not to Challenge Response status), and refined `/results/additional-derived-results/` framing to position it as Corpus consequences outside the SCL.
- **QA + cross-link template fix** (Wave 6) — fixed the `result-page-crosslinks.html` partial that still rendered "Problem Ledger item" labels on cross-referenced result pages; runs the briefing's count reconciliation check (38 + 117 + 29 + 30 = 214 ✓ matches Challenge Responses root); confirms canonical pages clean of v1 terminology except in permitted archive/provenance contexts.

The website now reads as one coherent v4 architecture: the Agenda states structural obligations via the Structural Challenge Ledger; the Results lane reports Challenge Responses (not settlements); Verify exposes inspection routes; legacy v1 raw feeds are preserved only for provenance.
