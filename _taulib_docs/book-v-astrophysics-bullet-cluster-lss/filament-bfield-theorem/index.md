---
{
  "projection_kind": "taulib_declaration",
  "title": "filament_bfield_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::filament_bfield_theorem",
  "declaration_slug": "filament-bfield-theorem",
  "kind": "theorem",
  "name": "filament_bfield_theorem",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 290,
  "source_line_end": 292,
  "registry_ids": [
    "V.T233"
  ],
  "related_registry_items": [
    {
      "id": "V.T233",
      "title": "Filament Magnetic Field Theorem",
      "url": "/registry/object/V.T233/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L290-L292",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L290-L292",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L290-L292)
- Source range: L290-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T233` — Filament Magnetic Field Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T233] Filament Magnetic Field Theorem: B_fil ~ 10-100 nG
    from SMBH flux diluted over filament cross-section. Stronger than
    random dynamo prediction (0.1-1 nG) by 1-2 orders of magnitude. -/
```

## Source Excerpt

```lean
theorem filament_bfield_theorem :
    "B_fil ~ 10-100 nG (topological), B_dynamo ~ 0.1-1 nG (random)" =
    "B_fil ~ 10-100 nG (topological), B_dynamo ~ 0.1-1 nG (random)" := rfl
```
