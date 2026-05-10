---
layout: program-doc
title: "Predictions"
permalink: /verify/predictions-and-falsification/predictions/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: prediction
status: "Canonical"
summary_short: "Derived consequences that can serve as accountability surfaces for the program."
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

**Prediction:** [20-galaxy BTFR]({{ '/predictions/20-galaxy-btfr/' | relative_url }}) — slope τ = 3.991, observed = 3.97 ± 0.10, deviation 0.067 dex (1–5% precision tier).

**Registry object:** [V.D258 — 20-Galaxy Benchmark]({{ '/registry/object/V.D258/' | relative_url }}) — references `V.T85 (Planck)`, tested across galaxies from dwarfs through massive disks.

**TauLib module:** [`TauLib.BookV.Astrophysics.RotationCurves`](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/BookV/Astrophysics/RotationCurves.lean)

**Lean theorem:** `Tau.BookV.Astrophysics.benchmark_T85_planck`

To audit independently: `lake build TauLib.BookV.Astrophysics.RotationCurves` resolves `benchmark_T85_planck` against the formal kernel (0 sorry, 3 disclosed custom axioms; check via `#print axioms Tau.BookV.Astrophysics.benchmark_T85_planck`).

### What the chain does and does not establish

The chain says: every public prediction lands on a named theorem, in a named module, in a public repo. The Lean work is not parallel to the predictions; it underwrites them. The derivation is version-controlled and pinned to the [release manifest]({{ '/verify/release-manifest/' | relative_url }}) — auditable independently from the empirical adjudication.

The chain does **not** say: that the τ-framework is empirically true, that any single prediction has been confirmed, or that formal-kernel correctness implies physical correctness. Those are separate claims under separate verification regimes — see [Scientific Rigor]({{ '/verify/scientific-rigor/' | relative_url }}) for the boundary discipline.
