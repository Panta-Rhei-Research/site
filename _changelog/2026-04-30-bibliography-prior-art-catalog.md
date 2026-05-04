---
title: "Bibliography & Prior-Art Catalog"
date: 2026-04-30
change_type: "publications"
summary_short: "Promoted the Bibliography to a full prior-art catalog with structured cross-links into the registry, monograph parts, and verify surfaces."
affected_lanes:
  - publications
  - corpus
  - verify
right_rail:
  toc: false
  related:
    - title: "Bibliography"
      url: /bibliography/
    - title: "Publications"
      url: /publications/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

## Changes

- **Bibliography lane**: Promoted to a full prior-art catalog at `/bibliography/` with structured author / topic / discipline browse routes.
- **Cross-links**: Each bibliography entry surfaces its connections into the registry items, monograph parts, and verify surfaces that cite it.
- **Source pipeline**: Bibliography entries live in the corpus repo at `corpus/bibliography/` as the source of truth, projected to the site at build time.
