---
{
  "projection_kind": "taulib_declaration",
  "title": "AlgebraicPDESplit",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/algebraic-pdesplit/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::AlgebraicPDESplit",
  "declaration_slug": "algebraic-pdesplit",
  "kind": "structure",
  "name": "AlgebraicPDESplit",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 1046,
  "source_line_end": 1057,
  "registry_ids": [
    "V.D337"
  ],
  "related_registry_items": [
    {
      "id": "V.D337",
      "title": "Algebraic–PDE Split for Rotation Curves",
      "url": "/registry/object/V.D337/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1046-L1057",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1046-L1057",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1046-L1057)
- Source range: L1046-L1057
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D337` — Algebraic–PDE Split for Rotation Curves

## Immediate Comment / Docstring

```lean
/-- [V.D337] Algebraic–PDE Split for Rotation Curves.

    Algebraic layer (τ-effective):
    1. Shape: capacity equation → K₀ profile → flat curves
    2. Amplitude: v⁴ = GM·a₀, a₀ = c²/(2ℓ_τ) algebraic
    3. Fit: 20 galaxies, RMS 0.067 dex, BTFR slope 3.991
    4. Interpolation: μ_τ(x) = x/√(1+x²) derived

    PDE layer (conjectural):
    1. Full nonlinear τ-Einstein unsolved at galactic scales
    2. Linearized gives v_screen ~ 0.07 km/s (4 OOM below obs)
    3. Cocycle amplification A_NL ~ 4×10¹² blocks perturbation -/
```

## Source Excerpt

```lean
structure AlgebraicPDESplit where
  /-- Number of τ-effective algebraic results. -/
  algebraic_results : Nat := 4
  /-- Number of conjectural PDE gaps. -/
  pde_gaps : Nat := 3
  /-- Galaxy catalog size. -/
  galaxies : Nat := 20
  /-- RMS in dex (×1000). -/
  rms_dex_x1000 : Nat := 67
  /-- BTFR slope (×1000). -/
  btfr_slope_x1000 : Nat := 3991
  deriving Repr
```
