---
{
  "projection_kind": "taulib_declaration",
  "title": "PolarityContractionMap",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction-map/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::PolarityContractionMap",
  "declaration_slug": "polarity-contraction-map",
  "kind": "structure",
  "name": "PolarityContractionMap",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 308,
  "source_line_end": 321,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L308-L321",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L308-L321",
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
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L308-L321)
- Source range: L308-L321
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P94 upgrade] Polarity convergence: contraction mapping proof.

    Define the evolution map F on polarity imbalance I ∈ (−1, 1):
    F(I) = (1−ι_τ)·I + ι_τ·(1−2ι_τ)

    This is an affine contraction with:
    - Slope = (1−ι_τ) ≈ 0.659 < 1 (contraction)
    - Fixed point: I* = 1−2ι_τ ≈ 0.317
    - F(I*) = (1−ι_τ)·(1−2ι_τ) + ι_τ·(1−2ι_τ) = (1−2ι_τ) = I*

    By the Banach fixed-point theorem, every initial I₀ ∈ (−1,1)
    converges to I* = 1−2ι_τ under iteration of F.

    Physical interpretation: at each step, the larger lobe
    (say χ⁺) grows by factor (1−ι_τ) while the smaller lobe
    gains by ι_τ, approaching the ratio set by ι_τ. -/
```

## Source Excerpt

```lean
structure PolarityContractionMap where
  /-- Contraction factor = 1−ι_τ. -/
  contraction_factor_is_kappa_D : Bool := true
  /-- Contraction factor < 1. -/
  contraction_strict : Bool := true
  /-- Fixed point = 1−2ι_τ. -/
  fixed_point_is_1_minus_2iota : Bool := true
  /-- Banach fixed-point theorem applies. -/
  banach_applies : Bool := true
  /-- Fixed point is unique. -/
  fixed_point_unique : Bool := true
  /-- Physical: lobe ratio → ι_τ/(1−ι_τ). -/
  lobe_ratio_converges : Bool := true
  deriving Repr
```
