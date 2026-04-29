---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_rigidity",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/tau-rigidity/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::tau_rigidity",
  "declaration_slug": "tau-rigidity",
  "kind": "def",
  "name": "tau_rigidity",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 368,
  "source_line_end": 372,
  "registry_ids": [
    "II.D76"
  ],
  "related_registry_items": [
    {
      "id": "II.D76",
      "title": "Dimensional Rigidity",
      "url": "/registry/object/II.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L368-L372",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L368-L372",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L368-L372)
- Source range: L368-L372
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D76` — Dimensional Rigidity

## Immediate Comment / Docstring

```lean
/-- [II.D76] The unique rigidity parameters for τ. -/
```

## Source Excerpt

```lean
def tau_rigidity : DimensionalRigidity :=
  { fibration_index := 3
  , refinement_dim := 4
  , base_factors := 1
  , fiber_factors := 2 }
```
