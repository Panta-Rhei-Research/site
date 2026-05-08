---
layout: "program-doc"
title: "Calibration Cascade Constants"
permalink: "/results/calibration-cascade/constants/"
lane: "results"
v2_lane: "results"
type: "Calibration Constants Index"
status: "Review-Facing"
summary_short: "Seeded constant/readout pages for the Calibration Cascade."
generated_from: "corpus/exports/public/calibration/constant-pages.yml"
projection_version: "v0.1"
canonical_source: "corpus/data/calibration/constant-pages.yml"
do_not_edit: true
constant_page_count: 9
---

> Generated index for the nine seeded Calibration Cascade constant/readout pages.

These pages expose public inspection routes for the current seeded constants only. They do not recompute CODATA 2022 values or change the existing numerical prediction artifact.

<div class="notice note">
  <strong>Scope label.</strong> Tau-effective means τ-effective. Metadata keeps the stable value <code>tau_effective</code>; public pages render the visible label as <strong>τ-effective</strong>.
</div>

<div class="calibration-key-node-grid">
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/alpha/">
  <span class="eyebrow">L1 · τ-effective</span>
  <strong>Fine-Structure Constant α</strong>
  <code>α = (11/15)^2 ι_τ^4</code>
  <span>This page displays the τ-internal alpha readout and comparison route. It does not establish external acceptance.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/r1/">
  <span class="eyebrow">L1 · τ-effective</span>
  <strong>Level 1+ Mass Ratio R1</strong>
  <code>R1 = ι_τ^-7 - (√3 + π^3α^2)ι_τ^-2</code>
  <span>This page displays the source-mapped mass-ratio route that feeds the electron-mass readout. It is not a standalone metrology claim.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/electron-mass/">
  <span class="eyebrow">L2 · τ-effective</span>
  <strong>Electron Mass m_e</strong>
  <code>m_e = m_n/R1</code>
  <span>This page displays an anchored SI readout after the neutron mass enters. It does not make the neutron-mass anchor itself a prediction.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/alpha-g/">
  <span class="eyebrow">L1 · τ-effective</span>
  <strong>Gravitational Coupling α_G</strong>
  <code>α_G = α^18√3(1 - (3/π)α)</code>
  <span>This page displays the dimensionless bridge quantity separately from the SI G readout.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/g/">
  <span class="eyebrow">L2 · τ-effective</span>
  <strong>Newton Constant G</strong>
  <code>G = (ℏ c / m_n^2) · α_G</code>
  <span>This page displays the SI G readout only with explicit unit-context guardrails. It does not claim current CODATA recomputation.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/planck-mass/">
  <span class="eyebrow">L2 · τ-effective</span>
  <strong>Planck Mass m_P</strong>
  <code>m_P = sqrt(ℏc/G)</code>
  <span>This page displays a Planck-mass readout downstream of the G route. It does not make Planck units the calibration anchor.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/rydberg-constant/">
  <span class="eyebrow">L3 · τ-effective</span>
  <strong>Rydberg Constant R_∞</strong>
  <code>R_∞ = α^2 m_e c/(2ℏ)</code>
  <span>This page displays an SI readout route downstream of alpha and electron mass. It does not update external metrology datasets.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/bohr-radius/">
  <span class="eyebrow">L3 · τ-effective</span>
  <strong>Bohr Radius a_B</strong>
  <code>a_B = ℏ/(α m_e c)</code>
  <span>This page uses Bohr radius notation a_B and avoids ambiguous zero-subscript radius notation.</span>
</a>
<a class="calibration-key-node-card" href="/results/calibration-cascade/constants/compton-wavelength/">
  <span class="eyebrow">L3 · τ-effective</span>
  <strong>Compton Wavelength λ_C</strong>
  <code>λ_C = ℏ/(m_e c)</code>
  <span>This page displays a downstream SI readout route and preserves source-vintage comparison status.</span>
</a>
</div>
