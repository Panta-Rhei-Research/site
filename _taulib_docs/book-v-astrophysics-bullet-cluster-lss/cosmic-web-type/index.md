---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmicWebType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/cosmic-web-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::CosmicWebType",
  "declaration_slug": "cosmic-web-type",
  "kind": "inductive",
  "name": "CosmicWebType",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 146,
  "source_line_end": 155,
  "registry_ids": [
    "V.D142"
  ],
  "related_registry_items": [
    {
      "id": "V.D142",
      "title": "Wilson Skeleton (Cosmic Web)",
      "url": "/registry/object/V.D142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L146-L155",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L146-L155",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L146-L155)
- Source range: L146-L155
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D142` — Wilson Skeleton (Cosmic Web)

## Immediate Comment / Docstring

```lean
/-- [V.D142] Cosmic web morphological type: classification of
    large-scale structure elements. -/
```

## Source Excerpt

```lean
inductive CosmicWebType where
  /-- Cluster: 3D density peak (node). -/
  | Cluster
  /-- Filament: 1D density ridge (edge). -/
  | Filament
  /-- Wall/Sheet: 2D density plane (face). -/
  | Wall
  /-- Void: 3D underdensity (cell). -/
  | Void
  deriving Repr, DecidableEq, BEq
```
