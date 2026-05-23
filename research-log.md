---
layout: research-log
title: "Research Progress Log"
subtitle: "A dated public ledger of meaningful research updates, artifacts, formalization milestones, result-status changes, and inspection routes."
lane: support
shell: home
type: support_page
support_type: research_log
status: canonical
last_updated: 2026-05-23
updated: "May 2026"
permalink: /research-log/
section: "Research Log"
summary: "The Research Progress Log is the program's dated public ledger of meaningful research-stream events — new artifacts, registry additions, result-status changes, falsification updates, formalization milestones, errata, release packets, and inspection-route refinements."
summary_short: "The program's dated public ledger of meaningful research-stream events — distinct from the Changelog and the Corpus Changelog."
summary_cards:
- title: "Typed and dated"
  body: "Every entry carries a stable id, a date, a type drawn from the IA §4.4 enum, and a status. Entries are appended; nothing is silently rewritten."
- title: "Not a blog"
  body: "Not a newsletter, not a press feed, not a marketing surface. Operational ledger language only, sized for reviewers and journalists."
- title: "Distinct from /changelog/"
  body: "The Changelog records site, layout, and release changes. The Corpus Changelog records semantic corpus corrections. This log records the active research stream."
right_rail:
  related:
  - title: Publications
    url: /publications/
  - title: Latest Publications
    url: /publications/latest/
  - title: Changelog
    url: /changelog/
  - title: Corpus Changelog
    url: /corpus-changelog/
  - title: About this Site
    url: /about-site/
  meta:
    type: "Support page"
    scope: "Research progress ledger"
    status: "Canonical"
    updated: "May 2026"
---

<!--
  Research Progress Log — v5 next-wave W5 (IA §4).
  Source: atlas/website/v5/panta-rhei-ia-doctrine-v5.md §4.
  Entries live in _data/research_log/entries.yml.
  Distinction from Changelog and Corpus Changelog per IA §4.5.
-->

## What this page records

This page records **meaningful research-stream events** — new publications, registry additions, result-status changes, falsification-pack updates, formalization milestones, errata, release packets, and refinements to the inspection routes that let readers check claims. Each entry is typed, dated, and pinned by a stable identifier so future references resolve.

## What it does not record

This page is **not** a blog, not a newsletter, not a press feed, and not a replacement for [Publications]({{ '/publications/' | relative_url }}). Three near-adjacent surfaces deliberately do not overlap:

| Surface | Records |
|---|---|
| [Changelog]({{ '/changelog/' | relative_url }}) | Site, layout, infrastructure, release, navigation, feature changes |
| [Corpus Changelog]({{ '/corpus-changelog/' | relative_url }}) | Semantic corpus corrections, status changes, bridge-boundary updates |
| [Publications]({{ '/publications/' | relative_url }}) / [Latest]({{ '/publications/latest/' | relative_url }}) | Stable citable artifact stream |
| **Research Log** *(this page)* | Active research progress and artifact / process updates |

If you are tracking a single published artifact, start at [Publications]({{ '/publications/' | relative_url }}). If you want the program's near-term progress, this is the right page.

## How entries are constructed

Each entry follows the [IA Doctrine v5 §4.4](https://github.com/Panta-Rhei-Research/atlas) schema: a stable `rlog-YYYY-MM-DD-NNN` id, an ISO date, one of nine type values (`publication` · `registry` · `taulib` · `result-status` · `pre-registration` · `falsification` · `erratum` · `release` · `website`), a status (`recorded` · `updated` · `superseded` · `corrected`), a title, a short operational summary, optional linked artifacts, and related lanes. Entries are appended; older entries are not silently rewritten.

The current backfill starts in late April 2026. The cadence is intentional — not a daily log, not a release-engineering ticker, but a record of events the program judges worth reading later.
