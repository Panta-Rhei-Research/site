---
layout: "calibration-constant-page"
title: "Bohr Radius a_B"
permalink: "/results/calibration-cascade/constants/bohr-radius/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page uses Bohr radius notation a_B and avoids ambiguous zero-subscript radius notation."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "cbohr"
constant_key: "bohr-radius"
constant_id: "CL-18"
node_id: "si-readouts"
slug: "bohr-radius"
overview_order: 8
symbol: "a_B"
formula_tex: "a_B = \\hbar/(\\alpha m_e c)"
formula_display: "a_B = ℏ/(α m_e c)"
formula_text: "a_B = hbar / (alpha * m_e * c)"
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
  comparison_id: "VC-04"
  deviation: "0.025 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page uses Bohr radius notation a_B and avoids ambiguous zero-subscript radius notation."
diagram_mmd: "data/calibration/diagrams/bohr-radius.mmd"
diagram_svg: "bohr-radius.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Bohr Radius a_B cascade"
  description: "Directed dependency cascade for a_B from the Calibration Cascade metadata."
  text_equivalent: "ℏ, α, m_e, and c converge into a_B; a_B feeds the CODATA 2018 comparison."
diagram:
  source_mmd: "data/calibration/diagrams/bohr-radius.mmd"
  rendered_svg: "bohr-radius.svg"
  alt_text: "ℏ, α, m_e, and c converge into a_B; a_B feeds the CODATA 2018 comparison."
  accessible_title: "Bohr Radius a_B cascade"
  accessible_description: "Directed dependency cascade for a_B from the Calibration Cascade metadata."
  orientation: "TD"
  render_status: "rendered"
diagram_mmd_source: "flowchart TD\n  alpha[\"α\"] --> bohr[\"a_B = ℏ/(α m_e c)\"]\n  me[\"m_e\"] --> bohr\n  hbar[\"ℏ\"] --> bohr\n  c[\"c\"] --> bohr\n  bohr --> compare[\"CODATA 2018 comparison\"]\n"
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
