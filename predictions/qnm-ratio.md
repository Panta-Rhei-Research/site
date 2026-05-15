---
layout: "prediction-page"
title: "Quasinormal Mode Frequency Ratio"
title_plain: "Quasinormal Mode Frequency Ratio"
permalink: "/predictions/qnm-ratio/"
lane: "results"
prediction_id: "pred-054"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "QNM ratio"
observable_mathml: "<math><mi>ι<sub>τ</sub>⁻¹</mi></math>"
formula_plain: "ι<sub>τ</sub>⁻¹"
formula_mathml: "<math><mi>ι<sub>τ</sub>⁻¹</mi></math>"
formula_display: "f₍₀,₁₎/f₍₁,₀₎ = ι<sub>τ</sub>⁻¹ = (π+e)/2 ≈ 2.929"
tau_value: "2.929"
observed: "(pending)"
observed_value: "(pending)"
deviation: "–"
precision_tier: "structural"
cascade_tier: "A"
precision_display: "Structural"
registry_id: "V.T168"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Quasinormal Mode Frequency Ratio: τ-value 2.929, released-corrected; tests the leading-order T² ratio, not mass-only Kerr ringdown."
right_rail:
  toc: false
  related:
    -
      title: "Predictions Browse"
      url: "/results/predictions/browse/"
    -
      title: "Falsification Pack"
      url: "/results/falsifications/browse/"
    -
      title: "Results Overview"
      url: "/results/"
  meta:
    type: "Physics Prediction"
    domain: "Astrophysics"
    precision: "Structural"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookV.Gravity.BHTopoModes"
    formalization: "formalized"
    registry_id_origin: "V.T168"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**f₍₀,₁₎/f₍₁,₀₎ = ι<sub>τ</sub>⁻¹ = (π+e)/2 ≈ 2.929**

## Derivation

Book V separates the ordinary Kerr primary ringdown scale from the
proposed τ topological ratio. The Kerr primary mode depends on the
remnant mass and spin. The τ claim is narrower: if the $T^2$ secondary
ringdown readout is present, the leading-order frequency ratio cancels
the common mass/spin scale and satisfies
$f_{(0,1)}/f_{(1,0)} = ι<sub>τ</sub>⁻¹$.

The ratio comes from the primitive outer and inner torus cycles with
shape ratio $r/R = ι<sub>τ</sub>$. Their eigenvalue ratio is
$λ_{0,1}/λ_{1,0} = ι<sub>τ</sub>⁻²$; taking the square root gives the
frequency ratio $ι<sub>τ</sub>⁻¹ ≈ 2.929$.

This is a released structural prediction, but it is not a claim that
current ringdown data already detect a τ mode or validate the black-hole
sector. It is a calibration and falsification surface for high-SNR
ringdown spectroscopy.

## Source

This prediction is derived in Book V, Chapters 41 and 50, with Registry
anchor V.T168 and related ringdown refinement V.T223. See
[ERRATUM-005](/publications/books/book-v/errata/) for the 2026-05-15
correction of mass/spin wording and generated-page contamination.
