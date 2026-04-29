---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_gr_not_obstructed",
  "permalink": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/tau-gr-not-obstructed/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::tau_gr_not_obstructed",
  "declaration_slug": "tau-gr-not-obstructed",
  "kind": "theorem",
  "name": "tau_gr_not_obstructed",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/verify/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 159,
  "source_line_end": 160,
  "registry_ids": [
    "II.T46"
  ],
  "related_registry_items": [
    {
      "id": "II.T46",
      "title": "Fourth Quadrant Resolution",
      "url": "/registry/object/II.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L159-L160",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L159-L160",
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

- Module: [TauLib.BookII.Mirror.PhysicsQuadrant](/verify/taulib/docs/book-ii-mirror-physics-quadrant/)
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L159-L160)
- Source range: L159-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T46` — Fourth Quadrant Resolution

## Immediate Comment / Docstring

```lean
/-- [II.T46] The unification obstruction does NOT apply to tau and GR. -/
```

## Source Excerpt

```lean
theorem tau_gr_not_obstructed :
    unification_obstructed tau_quadrant gr_local_quadrant = false := by native_decide
```
