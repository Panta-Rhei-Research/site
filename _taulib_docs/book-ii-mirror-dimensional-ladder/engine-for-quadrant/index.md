---
{
  "projection_kind": "taulib_declaration",
  "title": "engine_for_quadrant",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/engine-for-quadrant/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::engine_for_quadrant",
  "declaration_slug": "engine-for-quadrant",
  "kind": "def",
  "name": "engine_for_quadrant",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 296,
  "source_line_end": 302,
  "registry_ids": [
    "II.D75"
  ],
  "related_registry_items": [
    {
      "id": "II.D75",
      "title": "Archimedean-Elliptic Engine",
      "url": "/registry/object/II.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L296-L302",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L296-L302",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L296-L302)
- Source range: L296-L302
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D75` — Archimedean-Elliptic Engine

## Immediate Comment / Docstring

```lean
/-- [II.D75] Construct the engine state for a quadrant. -/
```

## Source Excerpt

```lean
def engine_for_quadrant (q : PhysicsQuadrant) : ArchimedeanEllipticEngine :=
  let metric_dim := q.metric == .Archimedean
  let elliptic_cr := q.pde == .Elliptic
  { has_metric_dimension := metric_dim
  , has_elliptic_cr := elliptic_cr
  , generates_ladder := metric_dim && elliptic_cr
  , ladder_requires_both := rfl }
```
