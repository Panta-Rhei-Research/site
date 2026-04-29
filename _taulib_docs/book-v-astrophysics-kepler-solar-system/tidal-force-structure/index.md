---
{
  "projection_kind": "taulib_declaration",
  "title": "TidalForceStructure",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::TidalForceStructure",
  "declaration_slug": "tidal-force-structure",
  "kind": "structure",
  "name": "TidalForceStructure",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 147,
  "source_line_end": 158,
  "registry_ids": [
    "V.D119"
  ],
  "related_registry_items": [
    {
      "id": "V.D119",
      "title": "Lensing Character --- V.D52",
      "url": "/registry/object/V.D119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L147-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
        "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L147-L158",
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L147-L158)
- Source range: L147-L158
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D119` — Lensing Character --- V.D52

## Immediate Comment / Docstring

```lean
/-- [V.D119] Tidal force structure: the gradient of the D-sector
    coupling across an extended defect bundle.

    Tidal acceleration ∝ M·d/r³ where d is the object size. -/
```

## Source Excerpt

```lean
structure TidalForceStructure where
  /-- Source mass index. -/
  source_mass : Nat
  /-- Object size index. -/
  object_size : Nat
  /-- Orbital distance index. -/
  orbital_distance : Nat
  /-- Distance must be positive. -/
  distance_pos : orbital_distance > 0
  /-- Whether tidal locking has occurred. -/
  tidally_locked : Bool
  deriving Repr
```
