---
layout: program-doc
title: "Predictions"
permalink: /results/predictions/
lane: results
v2_lane: results
type: "Prediction Surface"
status: "Canonical"
summary_short: "Zero-parameter numerical predictions from the single master constant ι_τ = 2/(π+e), with precision tiers and current observational comparisons."
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: false
---

## The Numerical Physics Ledger

The Numerical Physics Ledger compiles **{% include release-metric.html id="predictions.records" %} quantitative predictions** derived from the single master constant ι<sub>τ</sub> = 2/(π+e), with **zero free continuous parameters**. Each prediction compares a τ-derived value to experimental measurement — no ontological bridge claims needed.

<div class="notice note">
  <strong>The cascade.</strong> Two inputs (the algebraic posit ι<sub>τ</sub> = 2/(π+e) and a single SI anchor m<sub>n</sub>) feed a four-layer pipeline:
  {% include sequence-flow.html id="calibration_cascade" class="sequence-flow--notice" %}
  Every number in the prediction catalogue is traceable to those two inputs. There are no additional free parameters.
</div>

## Precision tiers

Predictions carry Corpus Wave 2 metadata along two separate axes:

- **Precision tier** — sub-10 ppm, 10–1000 ppm, 1–5%, or structural.
- **Cascade tier** — Tier A, Tier B, Tier C, or binary.

These tiers describe internal readout sharpness. They are distinct from public **status grammar** (Internally addressed / Partial / Qualitative / Contradicted / Not addressed), formal verification state, and external acceptance.

## Where to go

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/predictions/browse/' | relative_url }}">
    <strong>Browse all {% include release-metric.html id="predictions.records" %} predictions</strong>
    <span>Filterable grid by domain, precision, scope, and canonical book.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/predictions/timing/' | relative_url }}">
    <strong>Predictions · Timing</strong>
    <span>When each prediction is expected to be testable or settled.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/predictions/fit-space-argument/' | relative_url }}">
    <strong>Fit-space argument</strong>
    <span>Why the zero-parameter prediction catalogue amounts to a strong claim.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/falsifications/' | relative_url }}">
    <strong>Falsifications (N1–N30)</strong>
    <span>{% include release-metric.html id="falsifications.records" %} sharp falsification points with named experiments and timelines.</span>
  </a>
</div>

## Read next

- [Predictions — full grid]({{ '/results/predictions/browse/' | relative_url }})
- [Falsifications — N1–N30]({{ '/results/falsifications/' | relative_url }})
- [Calibration cascade]({{ '/results/world-readout/physics/' | relative_url }})
- [How to read a result page]({{ '/results/how-to-read-a-result-page/' | relative_url }})
