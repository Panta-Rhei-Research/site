---
{
  "projection_kind": "taulib_declaration",
  "title": "LSSData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lssdata/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::LSSData",
  "declaration_slug": "lssdata",
  "kind": "structure",
  "name": "LSSData",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 127,
  "source_line_end": 138,
  "registry_ids": [
    "V.D141"
  ],
  "related_registry_items": [
    {
      "id": "V.D141",
      "title": "Handle-Scale Event",
      "url": "/registry/object/V.D141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L127-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L127-L138",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L127-L138)
- Source range: L127-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D141` — Handle-Scale Event

## Immediate Comment / Docstring

```lean
/-- [V.D141] Large-scale structure data: summary of the galaxy
    distribution at cosmological scales. -/
```

## Source Excerpt

```lean
structure LSSData where
  /-- Number of galaxies in survey (millions). -/
  num_galaxies_millions : Nat
  /-- Survey volume (Gpc³, scaled × 10). -/
  survey_volume : Nat
  /-- Volume positive. -/
  volume_pos : survey_volume > 0
  /-- Characteristic BAO scale (Mpc). -/
  bao_scale_mpc : Nat
  /-- Mean galaxy separation (Mpc). -/
  mean_separation_mpc : Nat
  deriving Repr
```
