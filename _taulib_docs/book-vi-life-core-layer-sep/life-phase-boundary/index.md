---
{
  "projection_kind": "taulib_declaration",
  "title": "LifePhaseBoundary",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/life-phase-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::LifePhaseBoundary",
  "declaration_slug": "life-phase-boundary",
  "kind": "structure",
  "name": "LifePhaseBoundary",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 75,
  "source_line_end": 78,
  "registry_ids": [
    "VI.P05"
  ],
  "related_registry_items": [
    {
      "id": "VI.P05",
      "title": "Canonical Life Phase Boundary",
      "url": "/registry/object/VI.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L75-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.LayerSep",
        "url": "/verify/taulib/docs/book-vi-life-core-layer-sep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L75-L78",
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

- Module: [TauLib.BookVI.LifeCore.LayerSep](/verify/taulib/docs/book-vi-life-core-layer-sep/)
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L75-L78)
- Source range: L75-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P05` — Canonical Life Phase Boundary

## Immediate Comment / Docstring

```lean
/-- [VI.P05] Canonical life phase boundary: NS-to-BH transition. -/
```

## Source Excerpt

```lean
structure LifePhaseBoundary where
  is_sharp : Bool := true
  topology_change : Bool := true
  deriving Repr
```
