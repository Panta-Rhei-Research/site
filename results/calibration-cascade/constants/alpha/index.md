---
layout: "calibration-constant-page"
title: "Fine-Structure Constant α"
permalink: "/results/calibration-cascade/constants/alpha/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays the τ-internal alpha readout and comparison route. It does not establish external acceptance."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "calpha"
constant_key: "alpha"
constant_id: "CL-11"
node_id: "fine-structure-alpha"
slug: "alpha"
overview_order: 1
symbol: "α"
formula_tex: "\\alpha = (11/15)^2\\iota_\\tau^4"
formula_display: "α = (11/15)^2 ι_τ^4"
formula_text: "alpha = (11/15)^2 * iota_tau^4"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L1"
unit_context: "dimensionless"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "tab:ch69-complete-ledger"
dependency_nodes:
  - "iota-tau"
  - "coupling-ledger"
dependency_labels:
  - "ι_τ"
  - "coupling ledger"
registry_refs: []
taulib_modules:
  - "TauLib.BookIV.Calibration.DimensionlessAlpha"
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-07"
  deviation: "9.8 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays the τ-internal alpha readout and comparison route. It does not establish external acceptance."
diagram_mmd: "data/calibration/diagrams/alpha.mmd"
diagram_svg: "alpha.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Fine-Structure Constant α cascade"
  description: "Directed dependency cascade for α from the Calibration Cascade metadata."
  text_equivalent: "ι_τ -> coupling ledger -> α"
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

Dependency summary: `ι_τ`, `coupling ledger`
