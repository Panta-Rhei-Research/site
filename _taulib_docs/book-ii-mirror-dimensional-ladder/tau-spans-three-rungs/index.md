---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_spans_three_rungs",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/tau-spans-three-rungs/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::tau_spans_three_rungs",
  "declaration_slug": "tau-spans-three-rungs",
  "kind": "theorem",
  "name": "tau_spans_three_rungs",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 241,
  "source_line_end": 242,
  "registry_ids": [
    "II.T47"
  ],
  "related_registry_items": [
    {
      "id": "II.T47",
      "title": "Simultaneous Rung Theorem",
      "url": "/registry/object/II.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L241-L242",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L241-L242",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L241-L242)
- Source range: L241-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T47` — Simultaneous Rung Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T47] τ³ features originate from exactly 3 distinct rungs. -/
```

## Source Excerpt

```lean
theorem tau_spans_three_rungs :
    tau_distinct_rungs.length = 3 := by native_decide
```
