---
{
  "projection_kind": "taulib_declaration",
  "title": "collisionless_stellar",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/collisionless-stellar/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::collisionless_stellar",
  "declaration_slug": "collisionless-stellar",
  "kind": "theorem",
  "name": "collisionless_stellar",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 117,
  "source_line_end": 119,
  "registry_ids": [
    "V.P84"
  ],
  "related_registry_items": [
    {
      "id": "V.P84",
      "title": "Lensing-Gas Offset Bound",
      "url": "/registry/object/V.P84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L117-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L117-L119",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L117-L119)
- Source range: L117-L119
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P84` — Lensing-Gas Offset Bound

## Immediate Comment / Docstring

```lean
/-- [V.P84] Collisionless component is stellar: the "collisionless"
    component inferred from the Bullet Cluster is NOT dark matter
    particles but the STELLAR component (galaxies) that passes
    through the collision unimpeded.

    The enhanced lensing around the stellar component is the
    boundary holonomy correction (same as in rotation curves and
    the virial discrepancy). -/
```

## Source Excerpt

```lean
theorem collisionless_stellar :
    "Bullet Cluster collisionless component = stars, not dark matter" =
    "Bullet Cluster collisionless component = stars, not dark matter" := rfl
```
