---
layout: "prediction-page"
title: "Gravitational-Wave Cycle-Delay Time"
title_plain: "Gravitational-Wave Cycle-Delay Time"
permalink: "/predictions/gw-echo-time/"
lane: "results"
prediction_id: "pred-056"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "GW cycle-delay time"
observable_mathml: "<math><mi>t_outer = 4GMι<sub>τ</sub>⁻¹/c³; t_inner = 4GMι<sub>τ</sub>/c³</mi></math>"
formula_plain: "t_outer = 4GMι<sub>τ</sub>⁻¹/c³; t_inner = 4GMι<sub>τ</sub>/c³"
formula_mathml: "<math><mi>t_outer = 4GMι<sub>τ</sub>⁻¹/c³; t_inner = 4GMι<sub>τ</sub>/c³</mi></math>"
formula_display: "t_outer = 4GM·ι<sub>τ</sub>⁻¹/c³; t_inner = 4GM·ι<sub>τ</sub>/c³"
tau_value: "see text"
observed: "(pending)"
observed_value: "(pending)"
deviation: "–"
precision_tier: "structural"
cascade_tier: "binary"
precision_display: "Structural"
registry_id: "V.T169"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Gravitational-Wave Cycle-Delay Time: τ-value see text, deviation –; not a reflective-surface ECO echo claim."
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
    registry_id_origin: "V.T169"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**t_outer = 4GM·ι<sub>τ</sub>⁻¹/c³; t_inner = 4GM·ι<sub>τ</sub>/c³**

## Derivation

For a $T^2$-topology black hole of mass $M$, Book V defines two
cycle-delay readouts:
$t_{\mathrm{outer}} = 4GMι<sub>τ</sub>^{-1}/c^3$ and
$t_{\mathrm{inner}} = 4GMι<sub>τ</sub>/c^3$.
The separation is
$Δt = t_{\mathrm{outer}} - t_{\mathrm{inner}}
= 4GM(ι<sub>τ</sub>^{-1} - ι<sub>τ</sub>)/c^3$.

These are topology-readout candidates, not exotic-compact-object
reflective-surface echoes. They remain released predictions because
their absolute scale and ratio can be searched for in high-SNR ringdown
data, but no current public result validates the τ black-hole sector.

## Source

This prediction is derived in Book V, Chapters 41, 50, and 51, with
Registry anchor V.T169 and ratio refinement V.D243. See
[ERRATUM-005](/publications/books/book-v/errata/) for the 2026-05-15
correction of echo terminology and generated-page contamination.
