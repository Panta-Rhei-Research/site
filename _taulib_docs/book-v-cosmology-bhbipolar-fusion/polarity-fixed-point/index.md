---
{
  "projection_kind": "taulib_declaration",
  "title": "PolarityFixedPoint",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::PolarityFixedPoint",
  "declaration_slug": "polarity-fixed-point",
  "kind": "structure",
  "name": "PolarityFixedPoint",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 122,
  "source_line_end": 131,
  "registry_ids": [
    "V.P94"
  ],
  "related_registry_items": [
    {
      "id": "V.P94",
      "title": "Polarity Convergence",
      "url": "/registry/object/V.P94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L122-L131",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L122-L131",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L122-L131)
- Source range: L122-L131
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P94` — Polarity Convergence

## Immediate Comment / Docstring

```lean
/-- [V.P94] Polarity convergence: as a BH evolves, its polarity
    imbalance converges to the fixed point 1 − 2ι_τ.

    The fixed-point imbalance value:
    1 − 2ι_τ ≈ 1 − 2(0.341304) ≈ 0.317082

    Encoded as 317082 / 1000000. -/
```

## Source Excerpt

```lean
structure PolarityFixedPoint where
  /-- Fixed-point numerator. -/
  fp_numer : Nat
  /-- Fixed-point denominator. -/
  fp_denom : Nat
  /-- Denominator positive. -/
  denom_pos : fp_denom > 0
  /-- Value in (0, 1). -/
  in_range : fp_numer > 0 ∧ fp_numer < fp_denom
  deriving Repr
```
