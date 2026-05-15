---
{
  "projection_kind": "taulib_declaration",
  "title": "qft_gr_obstructed",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-physics-quadrant/qft-gr-obstructed/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.PhysicsQuadrant`.",
  "declaration_id": "TauLib.BookII.Mirror.PhysicsQuadrant::qft_gr_obstructed",
  "declaration_slug": "qft-gr-obstructed",
  "kind": "theorem",
  "name": "qft_gr_obstructed",
  "module_name": "TauLib.BookII.Mirror.PhysicsQuadrant",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-physics-quadrant/",
  "source_line_start": 131,
  "source_line_end": 132,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L131-L132",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L131-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookII/Mirror/PhysicsQuadrant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L131-L132)
- Source range: L131-L132
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D74` — The Unification Obstruction

## Immediate Comment / Docstring

```lean
/-- [II.D74] QFT/GR unification IS obstructed. -/
```

## Source Excerpt

```lean
theorem qft_gr_obstructed :
    unification_obstructed qft_quadrant gr_local_quadrant = true := by native_decide
```
