---
layout: program-doc
title: "Predictions"
permalink: /verify/predictions-and-falsification/predictions/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: prediction
status: "Canonical"
summary_short: "Predictions as verification targets — every public prediction traceable through a registry object to a named Lean theorem in TauLib."
og_image: /assets/og/png/verify__predictions-and-falsification__predictions.png
twitter_image: /assets/og/png/verify__predictions-and-falsification__predictions.png
og_image_alt: "Panta Rhei preview card for Predictions, with the Material Symbols track-changes bullseye-and-tracking-arrow icon as a soft accent on the dark observatory background; eyebrow reads VERIFY · PREDICTIONS · LEAN CHAIN, body says every public prediction is traceable through a registry object to a named Lean theorem in TauLib."
right_rail:
  related:
    - title: "Results Predictions Browse"
      url: /results/predictions/browse/
    - title: "Prediction Timing Ledger"
      url: /results/predictions/timing/
    - title: "Physics Verification"
      url: /verify/domain-verification/physics/
  meta:
    type: "Prediction Surface"
    status: "Canonical"
    updated: "May 2026"
---

## What This Page Catalogs

This page frames predictions as verification targets. The detailed current prediction catalogue remains in the Results lane, where each prediction is part of a result family and can be read with its domain context.

## Required Metadata for a Prediction Target

For each prediction surface, the program should expose:

- prediction ID
- related result ID
- related Corpus support
- domain
- type: structural, empirical, or hybrid
- current status
- linked falsification path where available

## Current Public Surfaces

- [Physics Predictions Browse]({{ '/results/predictions/browse/' | relative_url }})
- [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }})
- [Fit-Space Argument]({{ '/results/predictions/fit-space-argument/' | relative_url }})
- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }})

## Predictions ↔ Lean linkage (transitive chain)

Every public prediction in the program references a Corpus registry object via its `registry_id` frontmatter. Every referenced registry object names a TauLib Lean module and a specific Lean theorem name. **The prediction → registry → TauLib chain is end-to-end traceable for 100% of currently public predictions.**

| Layer | Field | Coverage |
|---|---|---|
| Prediction page (`/predictions/{slug}/`) | `registry_id:` | every public prediction carries a `registry_id` ({% include release-metric.html id="predictions.records" %} total predictions, all linked) |
| Registry object (`/registry/object/{id}/`) | `lean_module:` + `lean_name:` | every referenced registry object carries both fields |
| TauLib (`github.com/Panta-Rhei-Research/taulib`) | Lean theorem | all `lean_name` identifiers resolve in the pinned release manifest |

The chain is **transitive** (prediction → registry → Lean), not direct (prediction → Lean) — by design. The Corpus registry is the canonical naming layer; predictions are the empirical-projection layer; TauLib is the formal-evidence layer. Linking predictions directly to Lean would couple two layers that should remain independently revisable.

### Worked example — the chain in full

One prediction, four hops, no hand-waving. Read top-to-bottom; every line is the canonical identifier.

| Hop | Layer | Identifier |
|---|---|---|
| 1 | Prediction page | [`/predictions/20-galaxy-btfr/`]({{ '/predictions/20-galaxy-btfr/' | relative_url }}) — τ-BTFR slope = 3.991 (zero free parameters), observed = 3.97 ± 0.10, RMS scatter 0.067 dex across 20 galaxies (DDO 154 dwarf through NGC 2841 giant) |
| 2 | Registry `registry_id` | [`V.D258`]({{ '/registry/object/V.D258/' | relative_url }}) — *20-Galaxy Benchmark Table* (definition object); `depends_on: [V.T85, V.D257]` |
| 3 | Registry hinge theorem | [`V.T85`]({{ '/registry/object/V.T85/' | relative_url }}) — *Flat Rotation Curve Theorem* (the actual physical content) |
| 4 | TauLib `lean_module` | [`TauLib.BookV.Astrophysics.RotationCurves`](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/BookV/Astrophysics/RotationCurves.lean) |
| 5 | TauLib `lean_name` (benchmark binding) | `Tau.BookV.Astrophysics.benchmark_T85_planck` |
| 5′ | TauLib `lean_name` (hinge theorem) | `Tau.BookV.Astrophysics.FlatRotationCurveTheoremVt37` |

**What the theorem actually says (V.T85, plain reading).** For a disk galaxy with exponential surface density, the rotation velocity satisfies `v_c(r) → v_∞ = (G · M_b · c² / (2 · ℓ_τ))^(1/4)` at large radius — i.e. asymptotically flat rotation curves emerge from the τ-capacity gradient without invoking a dark-matter halo. Raising both sides to the fourth power gives the BTFR `v_∞⁴ ∝ M_b` with τ-fixed slope = 4 (kernel value; `3.991` is the benchmark-fit estimator over the 20-galaxy table, distinct from the kernel slope by `< 0.01`). The benchmark binding `benchmark_T85_planck` discharges V.T85 against the Planck-anchored mass calibration used in V.D258.

**Falsification condition (1 line).** A pre-registered re-fit on a comparable rotation-curve sample (≥ 20 galaxies, similar mass span) returning a BTFR slope outside `[3.85, 4.15]`, or an RMS scatter > 0.15 dex once measurement floors are subtracted, kills V.T85 at this scope and propagates upward — the τ-BTFR derivation has no free parameter to absorb the residual. Cross-reference the [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) for the corresponding falsification record.

**To audit independently.** `lake build TauLib.BookV.Astrophysics.RotationCurves` resolves both `benchmark_T85_planck` and `FlatRotationCurveTheoremVt37` against the formal kernel; `#print axioms Tau.BookV.Astrophysics.benchmark_T85_planck` enumerates the disclosed custom axioms (TauLib commits to `0 sorry`, with custom axioms tracked in the [release manifest]({{ '/verify/release-manifest/' | relative_url }})). Pin to the manifest commit SHA to reproduce.

### What the chain does and does not establish

The chain says: every public prediction lands on a named theorem, in a named module, in a public repo. The Lean work is not parallel to the predictions; it underwrites them. The derivation is version-controlled and pinned to the [release manifest]({{ '/verify/release-manifest/' | relative_url }}) — auditable independently from the empirical adjudication.

The chain does **not** say: that the τ-framework is empirically true, that any single prediction has been confirmed, or that formal-kernel correctness implies physical correctness. Those are separate claims under separate verification regimes — see [Scientific Rigor]({{ '/verify/scientific-rigor/' | relative_url }}) for the boundary discipline.
