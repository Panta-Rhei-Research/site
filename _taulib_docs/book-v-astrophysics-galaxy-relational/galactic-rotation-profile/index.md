---
{
  "projection_kind": "taulib_declaration",
  "title": "GalacticRotationProfile",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-rotation-profile/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::GalacticRotationProfile",
  "declaration_slug": "galactic-rotation-profile",
  "kind": "structure",
  "name": "GalacticRotationProfile",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 152,
  "source_line_end": 163,
  "registry_ids": [
    "V.D121"
  ],
  "related_registry_items": [
    {
      "id": "V.D121",
      "title": "Cosmic Web as Capacity Skeleton --- V.D54",
      "url": "/registry/object/V.D121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L152-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
        "url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L152-L163",
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/verify/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L152-L163)
- Source range: L152-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D121` — Cosmic Web as Capacity Skeleton --- V.D54

## Immediate Comment / Docstring

```lean
/-- [V.D121] Galactic rotation profile: radial dependence of the
    circular velocity in a galaxy.

    The flat regime at large r is the hallmark prediction that
    orthodox physics attributes to dark matter but that τ explains
    through boundary corrections. -/
```

## Source Excerpt

```lean
structure GalacticRotationProfile where
  /-- Associated galaxy. -/
  galaxy : GalacticDefectBundle
  /-- Asymptotic velocity (km/s). -/
  v_flat : Nat
  /-- Velocity is positive. -/
  v_pos : v_flat > 0
  /-- Transition radius (kpc, scaled × 10). -/
  r_transition : Nat
  /-- Outer regime. -/
  outer_regime : RotationRegime := .Flat
  deriving Repr
```
