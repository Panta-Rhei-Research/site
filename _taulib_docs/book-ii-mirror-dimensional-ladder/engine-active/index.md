---
{
  "projection_kind": "taulib_declaration",
  "title": "engine_active",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/engine-active/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::engine_active",
  "declaration_slug": "engine-active",
  "kind": "def",
  "name": "engine_active",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 292,
  "source_line_end": 293,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L292-L293",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L292-L293",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L292-L293)
- Source range: L292-L293
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D75` — Archimedean-Elliptic Engine

## Immediate Comment / Docstring

```lean
/-- [II.D75] Check if the Archimedean-elliptic engine is active in a given quadrant. -/
```

## Source Excerpt

```lean
def engine_active (q : PhysicsQuadrant) : Bool :=
  q.pde == .Elliptic && q.metric == .Archimedean
```
