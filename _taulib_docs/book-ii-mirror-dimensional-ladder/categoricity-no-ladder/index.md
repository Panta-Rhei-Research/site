---
{
  "projection_kind": "taulib_declaration",
  "title": "categoricity_no_ladder",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-no-ladder/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::categoricity_no_ladder",
  "declaration_slug": "categoricity-no-ladder",
  "kind": "def",
  "name": "categoricity_no_ladder",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 403,
  "source_line_end": 404,
  "registry_ids": [
    "II.R31"
  ],
  "related_registry_items": [
    {
      "id": "II.R31",
      "title": "Categoricity Implies No Ladder",
      "url": "/registry/object/II.R31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L403-L404",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L403-L404",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L403-L404)
- Source range: L403-L404
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R31` — Categoricity Implies No Ladder

## Immediate Comment / Docstring

```lean
/-- [II.R31] A singleton moduli space cannot support a dimension-indexed family. -/
```

## Source Excerpt

```lean
def categoricity_no_ladder : Bool :=
  tau_moduli_count == 1  -- singleton → no family
```
