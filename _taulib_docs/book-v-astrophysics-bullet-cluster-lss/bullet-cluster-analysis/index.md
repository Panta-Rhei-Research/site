---
{
  "projection_kind": "taulib_declaration",
  "title": "BulletClusterAnalysis",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bullet-cluster-analysis/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::BulletClusterAnalysis",
  "declaration_slug": "bullet-cluster-analysis",
  "kind": "structure",
  "name": "BulletClusterAnalysis",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 68,
  "source_line_end": 85,
  "registry_ids": [
    "V.D140"
  ],
  "related_registry_items": [
    {
      "id": "V.D140",
      "title": "Boundary-Mass Offset (tau)",
      "url": "/registry/object/V.D140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L68-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BulletClusterLSS",
        "url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L68-L85",
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

- Module: [TauLib.BookV.Astrophysics.BulletClusterLSS](/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/)
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L68-L85)
- Source range: L68-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D140` — Boundary-Mass Offset (tau)

## Immediate Comment / Docstring

```lean
/-- [V.D140] Bullet cluster τ-analysis: reinterpretation of the
    lensing-gas offset without invoking dark matter particles. -/
```

## Source Excerpt

```lean
structure BulletClusterAnalysis where
  /-- Lensing mass (10¹⁴ M_☉, scaled × 10). -/
  lensing_mass : Nat
  /-- Lensing mass positive. -/
  lensing_pos : lensing_mass > 0
  /-- Gas mass (same units). -/
  gas_mass : Nat
  /-- Stellar mass (same units). -/
  stellar_mass : Nat
  /-- Boundary correction mass equivalent (same units). -/
  boundary_correction : Nat
  /-- Lensing ≈ gas + stellar + boundary correction. -/
  mass_decomposition :
    lensing_mass ≤ gas_mass + stellar_mass + boundary_correction + 1 ∧
    gas_mass + stellar_mass + boundary_correction ≤ lensing_mass + 1
  /-- Offset between lensing peak and gas peak (kpc). -/
  offset_kpc : Nat
  deriving Repr
```
