---
{
  "projection_kind": "taulib_declaration",
  "title": "FilamentBFieldAlignment",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-alignment/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::FilamentBFieldAlignment",
  "declaration_slug": "filament-bfield-alignment",
  "kind": "structure",
  "name": "FilamentBFieldAlignment",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 276,
  "source_line_end": 285,
  "registry_ids": [
    "V.D292"
  ],
  "related_registry_items": [
    {
      "id": "V.D292",
      "title": "Filament B-Field Alignment",
      "url": "/registry/object/V.D292/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L276-L285",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L276-L285",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L276-L285)
- Source range: L276-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D292` — Filament B-Field Alignment

## Immediate Comment / Docstring

```lean
/-- [V.D292] Filament B-Field Alignment: magnetic field in cosmic filaments
    is aligned with the filament axis, from 1D Wilson loop topology. -/
```

## Source Excerpt

```lean
structure FilamentBFieldAlignment where
  /-- Alignment direction. -/
  direction : String := "parallel to filament axis"
  /-- Topological origin (1 = yes). -/
  topo_origin : Nat := 1
  /-- Coherence length comparable to filament length (1 = yes). -/
  long_coherence : Nat := 1
  deriving Repr

instance : Inhabited FilamentBFieldAlignment := ⟨{}⟩
```
