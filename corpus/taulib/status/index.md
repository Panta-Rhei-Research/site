---
layout: program-doc
title: "TauLib Projection Status"
permalink: /corpus/taulib/status/
lane: corpus
v2_lane: corpus
type: "Corpus Projection Status"
status: "Canonical"
summary_short: "Counts and boundaries for the current Corpus-owned TauLib projection."
---

{% assign summary = site.data.taulib.summary %}

## Projection status

| Metric | Current value |
|---|---:|
| Modules | {{ summary.module_count }} |
| Lean files | {{ summary.lean_file_count }} |
| Lean source lines | {{ summary.total_lean_lines }} |
| Declarations / evals | {{ summary.declaration_count }} |
| Registry links | {{ summary.registry_link_count }} |
| Registry items with TauLib links | {{ summary.registry_item_count_with_taulib_links }} |
| Sorry assignments detected | {{ summary.sorry_assignment_count }} |

## Boundary

This page reports the Corpus projection status. It does not by itself establish semantic adequacy, empirical truth, bridge sufficiency, or external acceptance. Those questions are routed through [Verify]({{ '/verify/' | relative_url }}).

## Source pin

The projection is generated from the imported TauLib source snapshot in `corpus/taulib-sources`. Use the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) for public release reconciliation and review context.
