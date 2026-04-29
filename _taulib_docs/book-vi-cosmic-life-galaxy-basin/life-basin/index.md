---
{
  "projection_kind": "taulib_declaration",
  "title": "LifeBasin",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/life-basin/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::LifeBasin",
  "declaration_slug": "life-basin",
  "kind": "structure",
  "name": "LifeBasin",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 29,
  "source_line_end": 38,
  "registry_ids": [
    "VI.D62"
  ],
  "related_registry_items": [
    {
      "id": "VI.D62",
      "title": "Life Basin",
      "url": "/registry/object/VI.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L29-L38",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.GalaxyBasin",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L29-L38",
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

- Module: [TauLib.BookVI.CosmicLife.GalaxyBasin](/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/)
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L29-L38)
- Source range: L29-L38
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D62` — Life Basin

## Immediate Comment / Docstring

```lean
/-- [VI.D62] Life Basin: spatial region anchored by a central carrier.
    Triple (B, C_anc, F) where B is basin region, C_anc is anchor,
    F is carrier family. Boundary at virial radius. -/
```

## Source Excerpt

```lean
structure LifeBasin where
  /-- Basin region is gravitationally bound. -/
  grav_bound : Bool := true
  /-- Anchor carrier satisfies Distinction + SelfDesc. -/
  anchor_alive : Bool := true
  /-- Carrier family: collection of all carriers in basin. -/
  has_carrier_family : Bool := true
  /-- Basin boundary = virial radius. -/
  virial_boundary : Bool := true
  deriving Repr
```
