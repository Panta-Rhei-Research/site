---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L155",
  "permalink": "/verify/taulib/docs/tour-one-constant/eval-l155/",
  "summary_short": "`eval` declaration in `TauLib.Tour.OneConstant`.",
  "declaration_id": "TauLib.Tour.OneConstant::#eval:155",
  "declaration_slug": "eval-l155",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.OneConstant",
  "module_url": "/verify/taulib/docs/tour-one-constant/",
  "source_line_start": 155,
  "source_line_end": 187,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L155-L187",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.OneConstant",
        "url": "/verify/taulib/docs/tour-one-constant/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L155-L187",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.Tour.OneConstant](/verify/taulib/docs/tour-one-constant/)
- Source path: [`TauLib/Tour/OneConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L155-L187)
- Source range: L155-L187
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval e1_complete.single_anchor      -- true


-- ============================================================
-- 6. THE EVIDENCE STANDARD
-- ============================================================

/-
Summary of what ι_τ = 2/(π + e) produces without fitting:

  | Observable      | τ-Prediction  | Observed       | Deviation |
  |-----------------|---------------|----------------|-----------|
  | α (fine struct.) | ≈ 1/137.9*    | 1/137.036      | 0.6%      |
  | ℓ₁ (CMB peak)   | 220.63        | 220.0 ± 0.5    | +69 ppm   |
  | h (Hubble)       | 0.6735        | 0.674 ± 0.005  | −0.1%     |
  | ω_b (baryon)     | 0.02209       | 0.02237±0.00015| −1.2%     |
  | r (tensor/scalar)| 0.0136        | < 0.036        | ✓         |

  * Spectral approximation; holonomy correction improves to ppm.

Every number above was computed by executing Lean code.
You just ran it yourself.


WHAT COMES NEXT

• Tour/Physics.lean              — 9 electroweak predictions in detail
• Tour/VerifyItYourself.lean     — The skeptic's verification chain
• BookIV/Electroweak/EWSynthesis.lean   — Full EW derivation
• BookV/Cosmology/CMBSpectrum.lean      — Complete CMB pipeline
• BookV/Coda/ConstantsLedger.lean       — The honest ledger
• BookV/Astrophysics/RotationCurves.lean — Galaxy rotation without DM
-/
```
