---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryHolonomyCorrection",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/boundary-holonomy-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::BoundaryHolonomyCorrection",
  "declaration_slug": "boundary-holonomy-correction",
  "kind": "structure",
  "name": "BoundaryHolonomyCorrection",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 86,
  "source_line_end": 99,
  "registry_ids": [
    "V.D123"
  ],
  "related_registry_items": [
    {
      "id": "V.D123",
      "title": "Galactic Capacity Profile --- V.D56",
      "url": "/registry/object/V.D123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L86-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L86-L99",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L86-L99)
- Source range: L86-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D123` — Galactic Capacity Profile --- V.D56

## Immediate Comment / Docstring

```lean
/-- [V.D123] Boundary holonomy correction: the modification of the
    D-sector coupling at galactic scales due to boundary holonomy.

    In the Newtonian regime (g >> a₀), the correction is negligible.
    In the deep MOND regime (g << a₀), the effective force transitions
    from 1/r² to 1/r, producing flat rotation curves. -/
```

## Source Excerpt

```lean
structure BoundaryHolonomyCorrection where
  /-- MOND acceleration scale a₀ (in 10⁻¹⁰ m/s², scaled × 100). -/
  a0_scaled : Nat
  /-- a₀ positive. -/
  a0_pos : a0_scaled > 0
  /-- Current acceleration regime. -/
  regime : AccelerationRegime
  /-- Newtonian acceleration (same units). -/
  g_newtonian : Nat
  /-- Effective (corrected) acceleration (same units). -/
  g_effective : Nat
  /-- In Newtonian regime, g_eff ≈ g_N. -/
  newtonian_approx : regime = .Newtonian → g_effective = g_newtonian
  deriving Repr
```
