---
{
  "projection_kind": "taulib_declaration",
  "title": "is_non_archimedean",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-physics-quadrant/is-non-archimedean/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::is_non_archimedean",
  "declaration_slug": "is-non-archimedean",
  "kind": "def",
  "name": "is_non_archimedean",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 184,
  "source_line_end": 185,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L184-L185",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.PhysicsQuadrant",
        "url": "/corpus/taulib/docs/book-ii-mirror-physics-quadrant/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L184-L185",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Mirror.PhysicsQuadrant](/corpus/taulib/docs/book-ii-mirror-physics-quadrant/)
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L184-L185)
- Source range: L184-L185
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check if a quadrant is in the non-Archimedean column. -/
```

## Source Excerpt

```lean
def is_non_archimedean (q : PhysicsQuadrant) : Bool :=
  q.metric == .NonArchimedean
```
