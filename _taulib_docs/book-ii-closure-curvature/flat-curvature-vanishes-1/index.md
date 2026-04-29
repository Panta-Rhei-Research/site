---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_curvature_vanishes_1",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/flat-curvature-vanishes-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::flat_curvature_vanishes_1",
  "declaration_slug": "flat-curvature-vanishes-1",
  "kind": "theorem",
  "name": "flat_curvature_vanishes_1",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 165,
  "source_line_end": 166,
  "registry_ids": [
    "II.T51"
  ],
  "related_registry_items": [
    {
      "id": "II.T51",
      "title": "Flat Curvature Vanishing",
      "url": "/registry/object/II.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L165-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Curvature",
        "url": "/verify/taulib/docs/book-ii-closure-curvature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L165-L166",
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

- Module: [TauLib.BookII.Closure.Curvature](/verify/taulib/docs/book-ii-closure-curvature/)
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L165-L166)
- Source range: L165-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T51` — Flat Curvature Vanishing

## Immediate Comment / Docstring

```lean
/-- [II.T51] Flat curvature vanishes at stage 1. -/
```

## Source Excerpt

```lean
theorem flat_curvature_vanishes_1 :
    curvature_check flat_connection 1 = true := by native_decide
```
