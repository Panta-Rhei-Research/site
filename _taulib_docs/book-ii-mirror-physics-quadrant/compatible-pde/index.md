---
{
  "projection_kind": "taulib_declaration",
  "title": "compatible_pde",
  "permalink": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/compatible-pde/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::compatible_pde",
  "declaration_slug": "compatible-pde",
  "kind": "def",
  "name": "compatible_pde",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 113,
  "source_line_end": 114,
  "registry_ids": [
    "II.D74"
  ],
  "related_registry_items": [
    {
      "id": "II.D74",
      "title": "The Unification Obstruction",
      "url": "/registry/object/II.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L113-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L113-L114",
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

- Module: [TauLib.BookII.Mirror.PhysicsQuadrant](/verify/taulib/docs/book-ii-mirror-physics-quadrant/)
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L113-L114)
- Source range: L113-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D74` — The Unification Obstruction

## Immediate Comment / Docstring

```lean
/-- [II.D74] Check if two quadrants have compatible (same) PDE type. -/
```

## Source Excerpt

```lean
def compatible_pde (q1 q2 : PhysicsQuadrant) : Bool :=
  q1.pde == q2.pde
```
