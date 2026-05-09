---
layout: "calibration-constant-page"
title: "Planck Mass m_P"
permalink: "/results/calibration-cascade/constants/planck-mass/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays a Planck-mass readout downstream of the G route. It does not make Planck units the calibration anchor."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "cmp"
constant_key: "planck-mass"
constant_id: "CL-23"
node_id: "si-readouts"
slug: "planck-mass"
overview_order: 6
symbol: "m_P"
formula_tex: "m_P = \\sqrt{\\hbar c/G}"
formula_display: "m_P = sqrt(ℏc/G)"
formula_text: "m_P = sqrt(hbar * c / G)"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L2"
unit_context: "si_after_g_readout"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "tab:ch69-complete-ledger"
dependency_nodes:
  - "g-readout"
dependency_labels:
  - "G"
  - "ℏ"
  - "c"
registry_refs: []
taulib_modules:
  - "TauLib.BookV.Coda.GAlphaBridge"
  - "TauLib.BookV.Coda.CalibrationChain"
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-06"
  deviation: "~3 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays a Planck-mass readout downstream of the G route. It does not make Planck units the calibration anchor."
diagram_mmd: "data/calibration/diagrams/planck-mass.mmd"
diagram_svg: "planck-mass.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Planck Mass m_P cascade"
  description: "Directed dependency cascade for m_P from the Calibration Cascade metadata."
  text_equivalent: "G, ℏ, and c converge into m_P; m_P feeds the CODATA 2018 comparison."
diagram:
  source_mmd: "data/calibration/diagrams/planck-mass.mmd"
  rendered_svg: "planck-mass.svg"
  alt_text: "G, ℏ, and c converge into m_P; m_P feeds the CODATA 2018 comparison."
  accessible_title: "Planck Mass m_P cascade"
  accessible_description: "Directed dependency cascade for m_P from the Calibration Cascade metadata."
  orientation: "TD"
  render_status: "rendered"
diagram_mmd_source: "flowchart TD\n  alpha[\"α\"] --> alphaG[\"α_G\"]\n  alphaG --> G[\"G readout\"]\n  hbar[\"ℏ\"] --> mp[\"m_P = sqrt(ℏc/G)\"]\n  c[\"c\"] --> mp\n  G --> mp\n  mp --> compare[\"CODATA 2018 comparison\"]\n"
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

Dependency summary: `G`, `ℏ`, `c`
