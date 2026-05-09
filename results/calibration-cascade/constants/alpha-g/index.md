---
layout: "calibration-constant-page"
title: "Gravitational Coupling α_G"
permalink: "/results/calibration-cascade/constants/alpha-g/"
lane: "results"
v2_lane: "results"
type: "Calibration Constant Page"
status: "ready"
summary_short: "This page displays the dimensionless bridge quantity separately from the SI G readout."
tags:
  - "calibration-cascade"
  - "constants-ledger"
  - "numerical-predictions"
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_id: "calphag"
constant_key: "alpha-g"
constant_id: "CL-26"
node_id: "alpha-g"
slug: "alpha-g"
overview_order: 4
symbol: "α_G"
formula_tex: "\\alpha_G = \\alpha^{18}\\sqrt{3}(1-(3/\\pi)\\alpha)"
formula_display: "α_G = α^18√3(1 - (3/π)α)"
formula_text: "alpha_G = alpha^18 * sqrt(3) * (1 - (3/pi) * alpha)"
scope_key: "tau_effective"
scope_label: "τ-effective"
layer: "L1"
unit_context: "dimensionless"
source_chapter: "book-v-constants-g-alpha-bridge"
source_label: "thm:ch70-bridge"
dependency_nodes:
  - "fine-structure-alpha"
dependency_labels:
  - "α"
registry_refs:
  - "V.T154"
taulib_modules:
  - "TauLib.BookV.Coda.GAlphaBridge"
  - "TauLib.BookV.Coda.CalibrationChain"
comparison:
  dataset_id: ""
  comparison_id: ""
  deviation: "~3 ppm route"
  status: "dimensionless_bridge"
related_predictions:
  - "/results/predictions/"
related_falsifications:
  - "/results/falsifications/"
public_boundary: "This page displays the dimensionless bridge quantity separately from the SI G readout."
diagram_mmd: "data/calibration/diagrams/alpha-g.mmd"
diagram_svg: "alpha-g.svg"
diagram_svg_status: "rendered"
diagram_accessibility:
  title: "Gravitational Coupling α_G cascade"
  description: "Directed dependency cascade for α_G from the Calibration Cascade metadata."
  text_equivalent: "α feeds α_G through the source bridge formula; α_G is kept as a dimensionless bridge before any SI G readout."
diagram:
  source_mmd: "data/calibration/diagrams/alpha-g.mmd"
  rendered_svg: "alpha-g.svg"
  alt_text: "α feeds α_G through the source bridge formula; α_G is kept as a dimensionless bridge before any SI G readout."
  accessible_title: "Gravitational Coupling α_G cascade"
  accessible_description: "Directed dependency cascade for α_G from the Calibration Cascade metadata."
  orientation: "TD"
  render_status: "rendered"
diagram_mmd_source: "flowchart TD\n  alpha --> alphaG[\"α_G = α^18√3(1-(3/π)α)\"]\n  sqrt3[\"√3\"] --> alphaG\n  correction[\"1-(3/π)α\"] --> alphaG\n  alphaG --> G[\"G SI readout\"]\n  alphaG --> boundary[\"Dimensionless bridge\"]\n"
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

Dependency summary: `α`
