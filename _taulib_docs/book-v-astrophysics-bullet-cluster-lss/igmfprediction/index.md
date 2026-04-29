---
{
  "projection_kind": "taulib_declaration",
  "title": "IGMFPrediction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/igmfprediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::IGMFPrediction",
  "declaration_slug": "igmfprediction",
  "kind": "structure",
  "name": "IGMFPrediction",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 298,
  "source_line_end": 305,
  "registry_ids": [
    "V.P157"
  ],
  "related_registry_items": [
    {
      "id": "V.P157",
      "title": "IGMF Magnitude",
      "url": "/registry/object/V.P157/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L298-L305",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L298-L305",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L298-L305)
- Source range: L298-L305
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P157` — IGMF Magnitude

## Immediate Comment / Docstring

```lean
/-- [V.P157] IGMF magnitude: 10-100 nG in filaments, ≪ 1 nG in voids. -/
```

## Source Excerpt

```lean
structure IGMFPrediction where
  /-- Filament field (nG × 10). -/
  b_fil_ng_x10 : Nat
  /-- Void field (nG × 10). -/
  b_void_ng_x10 : Nat
  /-- Filament > void. -/
  fil_gt_void : b_fil_ng_x10 > b_void_ng_x10
  deriving Repr
```
