---
{
  "projection_kind": "taulib_declaration",
  "title": "lensing_gas_offset",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lensing-gas-offset/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::lensing_gas_offset",
  "declaration_slug": "lensing-gas-offset",
  "kind": "theorem",
  "name": "lensing_gas_offset",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 101,
  "source_line_end": 103,
  "registry_ids": [
    "V.T97"
  ],
  "related_registry_items": [
    {
      "id": "V.T97",
      "title": "Bullet Cluster Without Dark Matter",
      "url": "/registry/object/V.T97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L101-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L101-L103",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L101-L103)
- Source range: L101-L103
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T97` — Bullet Cluster Without Dark Matter

## Immediate Comment / Docstring

```lean
/-- [V.T97] Lensing-gas offset from boundary correction: the
    spatial offset between the lensing signal and the X-ray gas
    arises because the boundary holonomy correction is centered
    on the collisionless (stellar) component, not the gas.

    During the cluster collision:
    - Gas is shock-heated and decelerated (collisional)
    - Stars pass through (collisionless)
    - Boundary correction follows stars (not gas)
    - Lensing peak aligns with stars + correction, offset from gas -/
```

## Source Excerpt

```lean
theorem lensing_gas_offset :
    "Lensing-gas offset = boundary correction centered on stars, not gas" =
    "Lensing-gas offset = boundary correction centered on stars, not gas" := rfl
```
