---
title: "Lane Refactors + Right-Rail / Left-Rail Doctrines"
date: 2026-05-04
change_type: "site-release"
summary_short: "Refactored the Program / Agenda / Verify / Discover / Impact / Engage lanes and applied site-wide right-rail and left-rail doctrines for consistent navigation, metadata cross-links, and feedback affordances."
affected_lanes:
  - program
  - corpus
  - results
  - verify
  - publications
  - impact
  - engage
right_rail:
  toc: false
  related:
    - title: "Engage"
      url: /engage/
    - title: "Discover"
      url: /discover/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

- **Six lane refactors**: Program, Agenda, Verify, Discover, Impact, and Engage lane roots refreshed with current scope statements, navigation maps, and cross-lane handoffs aligned to the v4 Construction Spine state.
- **Right-rail doctrine**: Authored at `atlas/website/doctrine/right-rail.md`. Six standardized positions — On-this-page TOC, Last updated, Related pages, Previous/Next navigation, Metadata cross-links (registry / TauLib / monograph parts), Page actions (share icons + "Comment on this page" / "Raise an issue" GitHub deep-links). Visible on all spine step pages and being swept across remaining content templates.
- **Left-rail doctrine**: Authored at `atlas/website/doctrine/left-rail.md`. Lane-local navigation tree with selective expansion of the current page's parent branch. The 8 major lanes locked: Discover, Program, Agenda, Corpus, Results, Verify, Impact, Engage. Publications, Bibliography, Cite, Media, Brand, Changelog, Credits, Impressum, Datenschutz, Sitemap fold into a virtual support lane.
- **Feedback affordances**: Right-rail "Comment on this page" deep-links to GitHub Discussions; "Raise an issue" deep-links to GitHub Issues. Both pre-populate page title + URL.
- **Footer split**: Combined External/Legal column split into separate Legal (Impressum, Datenschutz, Credits) and External (TauLib documentation, GitHub organization, source code) columns.
- **README style guide**: Authored at `atlas/website/doctrine/readme-style.md` for upcoming GitHub org README polish.
