---
{
  "projection_kind": "taulib_declaration",
  "title": "MetricAxis",
  "permalink": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/metric-axis/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::MetricAxis",
  "declaration_slug": "metric-axis",
  "kind": "inductive",
  "name": "MetricAxis",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 59,
  "source_line_end": 64,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L59-L64",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L59-L64",
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

- Module: [TauLib.BookII.Mirror.PhysicsQuadrant](/verify/taulib/docs/book-ii-mirror-physics-quadrant/)
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L59-L64)
- Source range: L59-L64
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D73` — The Physics Quadrant Matrix

## Immediate Comment / Docstring

```lean
/-- [II.D73] Metric axis for physics classification. -/
```

## Source Excerpt

```lean
inductive MetricAxis where
  | Archimedean    -- orthodox: real-valued distances, epsilon-delta
  | NonArchimedean -- tau: primorial distances, finite stages
  deriving DecidableEq, Repr

open PDEAxis MetricAxis
```
