---
layout: "calibration-constant-page"
title: "Rydberg Constant R_∞"
permalink: "/results/calibration-cascade/constants/rydberg-constant/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays an SI readout route downstream of alpha and electron mass. It does not update external metrology datasets."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "crydberg"
constant_key: "rydberg-constant"
constant_id: "CL-17"
node_id: "si-readouts"
slug: "rydberg-constant"
overview_order: 7
symbol: "R_∞"
formula_tex: "R_\\infty = \\alpha^2 m_e c/(2\\hbar)"
formula_display: "R_∞ = α^2 m_e c/(2ℏ)"
formula_text: "R_infinity = alpha^2 * m_e * c / (2 * hbar)"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L3"
unit_context: "si_readout"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "tab:ch69-complete-ledger"
dependency_nodes:
  - "fine-structure-alpha"
  - "electron-mass"
dependency_labels:
  - "α"
  - "m_e"
  - "ℏ"
  - "c"
registry_refs: []
taulib_modules: []
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-03"
  deviation: "0.025 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays an SI readout route downstream of alpha and electron mass. It does not update external metrology datasets."
diagram_mmd: "data/calibration/diagrams/rydberg-constant.mmd"
diagram_svg: "rydberg-constant.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Rydberg Constant R_∞ cascade"
  description: "Directed dependency cascade for R_∞ from the Calibration Cascade metadata."
  text_equivalent: "α, m_e, c, and ℏ converge into R_∞; R_∞ feeds the CODATA 2018 comparison."
diagram:
  source_mmd: "data/calibration/diagrams/rydberg-constant.mmd"
  rendered_svg: "rydberg-constant.svg"
  alt_text: "α, m_e, c, and ℏ converge into R_∞; R_∞ feeds the CODATA 2018 comparison."
  accessible_title: "Rydberg Constant R_∞ cascade"
  accessible_description: "Directed dependency cascade for R_∞ from the Calibration Cascade metadata."
  orientation: "TD"
  render_status: "rendered"
diagram_mmd_source: "flowchart TD\n  alpha[\"α\"] --> rydberg[\"R_∞ = α² m_e c/(2ℏ)\"]\n  me[\"m_e\"] --> rydberg\n  c[\"c\"] --> rydberg\n  hbar[\"ℏ\"] --> rydberg\n  rydberg --> compare[\"CODATA 2018 comparison\"]\n"
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

Dependency summary: `α`, `m_e`, `ℏ`, `c`
