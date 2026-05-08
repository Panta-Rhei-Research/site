---
layout: "calibration-constant-page"
title: "Newton Constant G"
permalink: "/results/calibration-cascade/constants/g/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays the SI G readout only with explicit unit-context guardrails. It does not claim current CODATA recomputation."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "cg"
constant_key: "g"
constant_id: "CL-20"
node_id: "g-readout"
slug: "g"
overview_order: 5
symbol: "G"
formula_tex: "G = \\frac{\\hbar c}{m_n^2}\\alpha_G"
formula_display: "G = (ℏ c / m_n^2) · α_G"
formula_text: "G = (hbar * c / m_n^2) * alpha_G"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L2"
unit_context: "si_after_neutron_mass_anchor"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "eq:ch70-bridge"
dependency_nodes:
  - "alpha-g"
  - "neutron-mass-anchor"
dependency_labels:
  - "α_G"
  - "m_n"
  - "ℏ"
  - "c"
registry_refs:
  - "V.T154"
taulib_modules:
  - "TauLib.BookV.Coda.GAlphaBridge"
  - "TauLib.BookV.Coda.CalibrationChain"
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-02"
  deviation: "~3 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays the SI G readout only with explicit unit-context guardrails. It does not claim current CODATA recomputation."
diagram_mmd: "data/calibration/diagrams/g.mmd"
diagram_svg: "g.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Newton Constant G cascade"
  description: "Directed dependency cascade for G from the Calibration Cascade metadata."
  text_equivalent: "α_G -> m_n -> ℏ -> c -> G"
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

Dependency summary: `α_G`, `m_n`, `ℏ`, `c`
