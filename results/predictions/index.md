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

## The Numerical Prediction Catalogue

The Numerical Prediction Catalogue compiles **{% include release-metric.html id="predictions.records" %} quantitative predictions** derived from the single master constant ι<sub>τ</sub> = 2/(π+e), with **zero free continuous parameters**. Each prediction compares a τ-derived value to experimental measurement under explicit source, unit-context, and verification boundaries.

<div class="notice note"><strong>The cascade.</strong> The numerical prediction catalogue lists the physics predictions. The <a href="{{ '/results/calibration-cascade/' | relative_url }}">Calibration Cascade</a> shows the dependency structure connecting the master constant, dimensional anchor, coupling readouts, mass-ratio chain, constants-ledger table, and verification comparisons.</div>

{% include sequence-flow.html id="calibration_cascade" %}

## Precision tiers

Predictions carry Corpus Wave 2 metadata along two separate axes:

- **Precision tier** — sub-10 ppm, 10–1000 ppm, 1–5%, or structural.
- **Cascade tier** — Tier A, Tier B, Tier C, or binary.

These tiers describe internal readout sharpness. They are distinct from public **status grammar** (Internally addressed / Partial / Qualitative / Contradicted / Not addressed), formal verification state, and external acceptance.

<div class="notice warn"><strong>Reading the tiers honestly.</strong> A Tier-A or sub-10-ppm label means "structural derivation present in the kernel chain" — <em>not</em> "agreement at the precision of the experimental measurement." Two Tier-A predictions with very different agreement levels can sit side by side in the catalogue, and a single prediction can carry multiple legitimate derivation routes at different precision bands. For example: the fine-structure constant α is one of the most precisely measured quantities in physics (relative precision ≈ 10<sup>−10</sup>). Our framework derives α via two routes — a closed-form algebraic LO α = (11/15)<sup>2</sup>·ι<sub>τ</sub><sup>4</sup> reproducing CODATA to ~9.8 ppm (auditable in one line; see <a href="{{ '/corpus/monographs/book-iv/part-01-the-joint-core-from-neutron-to-hydrogen/chapter-10-the-fine-structure-constant/' | relative_url }}">Book IV Chapter 10</a>), and a full multi-loop derivation (<code>IV.T107</code> with NLO holonomy + NNLO window algebra) reaching ~0 ppm. <strong>Both are honest framework claims; both co-exist by design.</strong> The electron mass m<sub>e</sub>, derived via the kernel-anchored cascade with the neutron mass as the dimensional anchor, agrees to ~0.025 ppm — and is itself a fit of the dimensionless ratio m<sub>e</sub>/m<sub>n</sub>, not an absolute prediction. All three are Tier-A. None of them are at measurement precision. Always open the per-prediction page to read the precision band, which derivation route is being cited, the dimensional-anchor chain, and the comparator-vintage details before treating any single tier badge as endorsement of measurement-level agreement. See also question 11 in the <a href="{{ '/program/about/red-team-faq/' | relative_url }}">Red-team FAQ</a> for the full discussion, including the explicit arithmetic. The <a href="{{ '/results/predictions/browse/' | relative_url }}">predictions browse grid</a> now displays a per-row precision-band chip on every prediction card so the band is readable at a glance.</div>

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
  <a class="v2-tile" href="{{ '/results/calibration-cascade/' | relative_url }}">
    <strong>Calibration Cascade</strong>
    <span>Dependency graph and ledger overlay for couplings, mass ratios, G-alpha bridge, constants, sources, and comparison vintage.</span>
  </a>
</div>

## Read next

- [Predictions — full grid]({{ '/results/predictions/browse/' | relative_url }})
- [Falsifications — N1–N30]({{ '/results/falsifications/' | relative_url }})
- [Calibration Cascade]({{ '/results/calibration-cascade/' | relative_url }})
- [How to read a result page]({{ '/results/how-to-read-a-result-page/' | relative_url }})
