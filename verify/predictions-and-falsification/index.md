---
layout: program-doc
title: "Predictions & Falsification"
permalink: /verify/predictions-and-falsification/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: falsification_path
status: "Canonical"
summary_short: "How the program exposes possible failure modes and testable consequences."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix with obligations, construction steps, results, formal proof checking, bridge adequacy, predictions, falsification, and external assessment."
summary_cards:
  - title: "Predictions"
    body: "Derived consequences that can serve as accountability surfaces for the program."
  - title: "Falsification paths"
    body: "Explicit routes by which a result, bridge, or domain claim could fail."
  - title: "Falsification packs"
    body: "Structured bundles for checking numeric, structural, or empirical accountability surfaces."
right_rail:
  related:
    - title: "Physics Verification"
      url: /verify/domain-verification/physics/
    - title: "Results"
      url: /results/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "Predictions & Falsification"
    status: "Canonical"
    updated: "April 2026"
---

## Accountability, Not Decoration

Predictions and falsification are not merely outputs of the program. They are accountability structures for Results.

Predictions and falsification are Verify-owned accountability surfaces.

The Results lane provides world-facing interpretation and result-family context. Verify owns the accountability grammar: prediction IDs, target results, failure conditions, timing assumptions, falsification paths, and pack structure.

Publication artifacts such as the Numerical Physics Ledger may package these surfaces for reading and review.

## Falsification inside the verification matrix

{% capture falsification_plate_caption %}Predictions and falsification are one layer of verification. They do not replace formal proof, bridge adequacy, domain interpretation, or external assessment.{% endcapture %}
{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" class="scientific-plate--compact" caption=falsification_plate_caption loading="lazy" %}

Predictions and falsification are inspection routes for empirical claims. They complement formal proof checking and bridge adequacy; they do not replace them.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/predictions/' | relative_url }}">
    <strong>Predictions</strong>
    <span>Derived consequences that can be inspected as verification targets.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/falsification-paths/' | relative_url }}">
    <strong>Falsification Paths</strong>
    <span>Ways current claims could be challenged, contradicted, or broken.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/falsification-packs/' | relative_url }}">
    <strong>Falsification Packs</strong>
    <span>Structured audit bundles for manual, computational, or assisted review.</span>
  </a>
</div>

## Cross-Lane Reading

The [Results lane]({{ '/results/' | relative_url }}) presents what the program currently derives. This Verify subtree asks how those results could be checked or defeated. For physics, the first concrete surfaces are the [Predictions browse]({{ '/results/predictions/browse/' | relative_url }}), the [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}), and the [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}).
