---
layout: "calibration-constant-page"
title: "Level 1+ Mass Ratio R1"
permalink: "/results/calibration-cascade/constants/r1/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays the source-mapped mass-ratio route that feeds the electron-mass readout. It is not a standalone metrology claim."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "cr1"
constant_key: "r1"
constant_id: "CL-14"
node_id: "mass-ratio-chain"
slug: "r1"
overview_order: 2
symbol: "R1"
formula_tex: "R_1 = \\iota_\\tau^{-7}-(\\sqrt{3}+\\pi^3\\alpha^2)\\iota_\\tau^{-2}"
formula_display: "R1 = ι_τ^-7 - (√3 + π^3α^2)ι_τ^-2"
formula_text: "R1 = iota_tau^-7 - (sqrt(3) + pi^3 * alpha^2) * iota_tau^-2"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L1"
unit_context: "dimensionless"
source_chapter: "book-iv-mass-ratio-chain"
source_label: "eq:R1"
dependency_nodes:
  - "iota-tau"
  - "fine-structure-alpha"
dependency_labels:
  - "ι_τ"
  - "α"
registry_refs:
  - "IV.T381"
taulib_modules:
  - "TauLib.BookIV.Calibration.MassRatioFormula"
comparison:
  dataset_id: ""
  comparison_id: ""
  deviation: "0.025 ppm route"
  status: "feeds_electron_mass"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays the source-mapped mass-ratio route that feeds the electron-mass readout. It is not a standalone metrology claim."
diagram_mmd: "data/calibration/diagrams/r1.mmd"
diagram_svg: "r1.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Level 1+ Mass Ratio R1 cascade"
  description: "Directed dependency cascade for R1 from the Calibration Cascade metadata."
  text_equivalent: "ι_τ -> α -> R1"
diagram_mmd_source: ""
right_rail:
  related:
    -
      title: "Calibration Cascade"
      url: "/results/calibration-cascade/"
    -
      title: "Constants Index"
      url: "/results/calibration-cascade/constants/"
    -
      title: "Numerical Prediction Catalogue"
      url: "/results/predictions/"
---

> Generated constant/readout inspection page from the Corpus Calibration Cascade projection.

Dependency summary: `ι_τ`, `α`
