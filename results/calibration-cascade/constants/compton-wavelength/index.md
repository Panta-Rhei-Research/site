---
layout: "calibration-constant-page"
title: "Compton Wavelength λ_C"
permalink: "/results/calibration-cascade/constants/compton-wavelength/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays a downstream SI readout route and preserves source-vintage comparison status."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "ccompton"
constant_key: "compton-wavelength"
constant_id: "CL-19"
node_id: "si-readouts"
slug: "compton-wavelength"
overview_order: 9
symbol: "λ_C"
formula_tex: "\\lambda_C = \\hbar/(m_e c)"
formula_display: "λ_C = ℏ/(m_e c)"
formula_text: "lambda_C = hbar / (m_e * c)"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L3"
unit_context: "si_readout"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "tab:ch69-complete-ledger"
dependency_nodes:
  - "electron-mass"
dependency_labels:
  - "m_e"
  - "ℏ"
  - "c"
registry_refs: []
taulib_modules: []
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-05"
  deviation: "0.025 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays a downstream SI readout route and preserves source-vintage comparison status."
diagram_mmd: "data/calibration/diagrams/compton-wavelength.mmd"
diagram_svg: "compton-wavelength.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Compton Wavelength λ_C cascade"
  description: "Directed dependency cascade for λ_C from the Calibration Cascade metadata."
  text_equivalent: "ℏ, m_e, and c converge into λ_C; λ_C feeds the CODATA 2018 comparison."
diagram:
  source_mmd: "data/calibration/diagrams/compton-wavelength.mmd"
  rendered_svg: "compton-wavelength.svg"
  alt_text: "ℏ, m_e, and c converge into λ_C; λ_C feeds the CODATA 2018 comparison."
  accessible_title: "Compton Wavelength λ_C cascade"
  accessible_description: "Directed dependency cascade for λ_C from the Calibration Cascade metadata."
  orientation: "TD"
  render_status: "rendered"
diagram_mmd_source: "flowchart TD\n  me[\"m_e\"] --> compton[\"λ_C = ℏ/(m_e c)\"]\n  hbar[\"ℏ\"] --> compton\n  c[\"c\"] --> compton\n  compton --> compare[\"CODATA 2018 comparison\"]\n"
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

Dependency summary: `m_e`, `ℏ`, `c`
