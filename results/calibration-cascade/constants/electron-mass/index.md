---
layout: "calibration-constant-page"
title: "Electron Mass m_e"
permalink: "/results/calibration-cascade/constants/electron-mass/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays an anchored SI readout after the neutron mass enters. It does not make the neutron-mass anchor itself a prediction."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "cme"
constant_key: "electron-mass"
constant_id: "CL-15"
node_id: "electron-mass"
slug: "electron-mass"
overview_order: 3
symbol: "m_e"
formula_tex: "m_e = m_n/R_1"
formula_display: "m_e = m_n/R1"
formula_text: "m_e = m_n / R1"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L2"
unit_context: "si_after_neutron_mass_anchor"
source_chapter: "book-iv-mass-ratio-chain"
source_label: "thm:electron-mass"
dependency_nodes:
  - "neutron-mass-anchor"
  - "mass-ratio-chain"
dependency_labels:
  - "m_n"
  - "R1"
registry_refs:
  - "IV.T218"
taulib_modules:
  - "TauLib.BookIV.Calibration.MassRatioFormula"
comparison:
  dataset_id: "codata-2018"
  comparison_id: "VC-01"
  deviation: "0.025 ppm"
  status: "source_chapter_comparison"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays an anchored SI readout after the neutron mass enters. It does not make the neutron-mass anchor itself a prediction."
diagram_mmd: "data/calibration/diagrams/electron-mass.mmd"
diagram_svg: "electron-mass.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Electron Mass m_e cascade"
  description: "Directed dependency cascade for m_e from the Calibration Cascade metadata."
  text_equivalent: "m_n -> R1 -> m_e"
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

Dependency summary: `m_n`, `R1`
