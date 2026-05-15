---
layout: "prediction-page"
title: "GW Cycle-Delay Ratio"
title_plain: "GW Cycle-Delay Ratio"
permalink: "/predictions/echo-ratio/"
lane: "results"
prediction_id: "pred-057"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "Cycle-delay ratio"
observable_mathml: "<math><mi>t_outer/t_inner = ι<sub>τ</sub>⁻²</mi></math>"
formula_plain: "t_outer/t_inner = ι<sub>τ</sub>⁻²"
formula_mathml: "<math><mi>t_outer/t_inner = ι<sub>τ</sub>⁻²</mi></math>"
formula_display: "t_outer/t_inner = ι<sub>τ</sub>⁻² ≈ 8.57"
tau_value: "8.57"
observed: "(pending)"
observed_value: "(pending)"
deviation: "–"
precision_tier: "structural"
cascade_tier: "A"
precision_display: "Structural"
registry_id: "V.D243"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "GW Cycle-Delay Ratio: τ-value 8.57, deviation –; not a reflective-surface ECO echo claim."
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
    registry_id_origin: "V.D243"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**t_outer/t_inner = ι<sub>τ</sub>⁻² ≈ 8.57**

## Derivation

Book V defines two $T^2$ cycle-delay readouts:
$t_{\mathrm{inner}} = 4GMι<sub>τ</sub>/c^3$ and
$t_{\mathrm{outer}} = 4GMι<sub>τ</sub>^{-1}/c^3$.
Their ratio is
$t_{\mathrm{outer}}/t_{\mathrm{inner}} = ι<sub>τ</sub>^{-2} ≈ 8.57$.

This page intentionally uses cycle-delay language. It is not an exotic
compact object or reflective-surface echo claim, and it does not say
orthodox Kerr ringdowns should exhibit such echoes. The prediction is a
τ topology-readout candidate whose public status remains released and
testable.

## Source

This prediction is derived in Book V, Chapters 41, 50, and 51, with
Registry anchors V.T169 and V.D243. See
[ERRATUM-005](/publications/books/book-v/errata/) for the 2026-05-15
correction of echo terminology, ratio direction, and generated-page
contamination.
