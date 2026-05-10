---
layout: program-doc
title: "Key Results"
lane: discover
v2_lane: discover
permalink: /discover/key-results/
type: "Result Gateway"
status: "Canonical"
summary_short: "A curated flagship-result entry surface for readers who want substance before the full ledger."
tags:
  - discover
  - landmark-results
  - world-readout
  - progress-against-agenda
  - results
hero_ctas:
  - label: "Results Lane"
    url: /results/
    primary: true
  - label: "Landmark Results"
    url: /results/landmark-results/
  - label: "World Readout"
    url: /results/world-readout/
  - label: "Progress Against Agenda"
    url: /results/progress-against-agenda/
right_rail:
  related:
    - title: "Results"
      url: /results/
    - title: "Verify"
      url: /verify/
    - title: "Corpus Registry"
      url: /corpus/registry/
  meta:
    type: "Result Gateway"
    status: "Canonical"
    updated: "April 2026"
---

## Curated First Set

This page is the Discover entry into the Results lane's Landmark Results surface.

This is not the full Results lane. It is a small, high-signal entry surface for readers who want to see landmark consequences before entering the full Results structure: Landmark Results, World Readouts, Challenge Responses, Core Semantics Status, Additional Derived Results, and Progress Against Agenda.

Use [AI-Assisted Discovery]({{ '/discover/ai-assisted-discovery/' | relative_url }}) if you want a structured outside-in assessment of these landmark result surfaces before reading in depth.

## Worked example — Hubble tension, in 200 words

Of the cards below, the [Hubble tension result]({{ '/results/problem/hubble-tension-resolved-h-formula/' | relative_url }}) is the most accessible to a non-specialist reader. The argument compresses to:

The Hubble constant $h$ measures how fast the universe expands. Two independent measurement methods disagree by ~5σ: the Planck CMB (early-universe) gives $h \approx 0.674$; SH0ES/Cepheid/JWST (late-universe) gives $h \approx 0.730$. This 5σ tension has resisted explanation within ΛCDM and motivated extensive new-physics proposals.

The τ-framework derives $h = \tfrac{2}{3} + \iota_\tau^2 / 17 = 0.6735$ from two structurally fixed components: $\tfrac{2}{3}$ is the matter-dominated Einstein–de Sitter base value, and $\iota_\tau^2 / 17$ is the holonomy correction where $17 = W_3(3)$ is the sum of three consecutive partial quotients of the continued-fraction expansion of $\iota_\tau$ starting at index 3. Both terms are **fixed once $\iota_\tau$ is posited** — neither is fitted to data.

The result lands at –120 ppm from the SH0ES/JWST measurement and is consistent with Planck CMB. **Falsification condition:** any joint Planck-and-SH0ES tightening that rules out $h = 0.6735$ at >5σ falsifies the readout. The readout sits in [V.T259]({{ '/registry/object/V.T259/' | relative_url }}); the integer divisor $17 = W_3(3)$ is Lean-certified at `Tau.CF.w3_at_3 : windowSum cf_head 3 3 = 17` in [`TauLib.BookV.Astrophysics.H0TensionLCDM`](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/BookV/Astrophysics/H0TensionLCDM.lean) (uniqueness wrapper: `Tau.BookV.Astrophysics.hubble_uniqueness`).

This is the orientation, not the proof. The full derivation, dependencies, and falsification path live in the linked result page below — but the sketch above is enough to know what the claim actually is.

<div class="v2-grid v2-grid-2">
  <a class="v2-tile" href="{{ '/results/problem/hubble-tension-resolved-h-formula/' | relative_url }}">
    <h3>Hubble tension</h3>
    <p>A zero-continuous-parameter readout for the Hubble constant: <em>h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735</em>, –120 ppm from SH0ES/JWST.</p>
    <p><small><strong>Theorem:</strong> V.T259 · Lean: <code>Tau.CF.w3_at_3</code> · <strong>Falsifier:</strong> any joint Planck-and-SH0ES tightening that rules out <em>h = 0.6735</em> at &gt;5σ.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Physics</span><span class="v2-badge">Prediction</span></div>
  </a>
  <a class="v2-tile" href="{{ '/results/problem/no-dark-matter-particle/' | relative_url }}">
    <h3>No dark matter particle</h3>
    <p>A structural exhaustion claim rather than a new-particle hypothesis: the four primitive sectors plus ω exhaust all positions in Category τ.</p>
    <p><small><strong>Theorem:</strong> V.P69 (Sector Exhaustion) · <strong>Falsifier:</strong> direct detection of a non-baryonic massive particle that requires its own sector position, or rotation curves the V.T85 capacity-gradient mechanism cannot reproduce.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Cosmology</span><span class="v2-badge">Falsifiable</span></div>
  </a>
  <a class="v2-tile" href="{{ '/results/problem/hinge-theorem-no-knobs/' | relative_url }}">
    <h3>Hinge theorem</h3>
    <p>A no-knobs route from the formal build to the claimed physical readout: 10 inter-sector couplings as rational functions of ι<sub>τ</sub> alone.</p>
    <p><small><strong>Theorem:</strong> III.T41 (Hinge) + III.T42 (No Knobs) · <strong>Falsifier:</strong> any inter-sector coupling measured to depend on a continuous free parameter, i.e. not a rational function of ι<sub>τ</sub>.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Structural</span><span class="v2-badge">Corpus-linked</span></div>
  </a>
  <a class="v2-tile" href="{{ '/results/problem/homochirality-universality-12-step-derivation/' | relative_url }}">
    <h3>Homochirality</h3>
    <p>A life-sector derivation path tied back to the formal corpus: 12-step chain K0–K6 → ι<sub>τ</sub> → weak sector → Parity Bridge → universal L-amino-acid chirality.</p>
    <p><small><strong>Theorem:</strong> VI.T43 (via VI.T01 Parity Bridge) · <strong>Falsifier:</strong> discovery of a persistence-sector lineage with the opposite universal chirality, or a chirality-mixed lineage that satisfies SelfDesc closure.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Life</span><span class="v2-badge">Derivation</span></div>
  </a>
  <a class="v2-tile" href="{{ '/results/problem/consciousness-global-section/' | relative_url }}">
    <h3>Consciousness as global section</h3>
    <p>A metaphysical readout surface for mind, binding, and self-model structure — at the E₂ binding layer, not the E₃ Hard Problem.</p>
    <p><small><strong>Theorem:</strong> VII.T41 (binding = sheaf gluing; CC1–CC3 from VI.D86) · <strong>Falsifier:</strong> a system satisfying CC1–CC3 that empirically lacks unified cognitive binding, or a binding-unified system that fails CC1–CC3.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Metaphysics</span><span class="v2-badge">World Readout</span></div>
  </a>
  <a class="v2-tile" href="{{ '/results/problem/categorical-imperative-fixed-point/' | relative_url }}">
    <h3>Categorical imperative</h3>
    <p>An ethics result surface framed as a fixed-point and commitment structure: CI as the unique j-closed fixed point of the τ-digestion operator.</p>
    <p><small><strong>Theorem:</strong> VII.T35 + VII.P21 (Stage CI; Knaster–Tarski uniqueness) · <strong>Falsifier:</strong> exhibition of a second j-closed fixed point of <em>j_dig</em> distinct from CI.</small></p>
    <div class="v2-badge-row"><span class="v2-badge">Ethics</span><span class="v2-badge">Interpretive</span></div>
  </a>
</div>

## Read Carefully

These cards are orientation, not endorsement. Every result must be read through its status, supporting corpus, verification route, and falsification posture where applicable.
