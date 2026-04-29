---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicsQuadrant",
  "permalink": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/physics-quadrant/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::PhysicsQuadrant",
  "declaration_slug": "physics-quadrant",
  "kind": "structure",
  "name": "PhysicsQuadrant",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 67,
  "source_line_end": 71,
  "registry_ids": [
    "II.D73"
  ],
  "related_registry_items": [
    {
      "id": "II.D73",
      "title": "The Physics Quadrant Matrix",
      "url": "/registry/object/II.D73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L67-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.PhysicsQuadrant",
        "url": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L67-L71",
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

- Module: [TauLib.BookII.Mirror.PhysicsQuadrant](/verify/taulib/docs/book-ii-mirror-physics-quadrant/)
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L67-L71)
- Source range: L67-L71
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D73` — The Physics Quadrant Matrix

## Immediate Comment / Docstring

```lean
/-- [II.D73] A physics quadrant: a point in the PDE x Metric classification. -/
```

## Source Excerpt

```lean
structure PhysicsQuadrant where
  pde : PDEAxis
  metric : MetricAxis
  description : String
  deriving Repr
```
