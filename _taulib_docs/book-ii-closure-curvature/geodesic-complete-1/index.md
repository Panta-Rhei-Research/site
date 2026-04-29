---
{
  "projection_kind": "taulib_declaration",
  "title": "geodesic_complete_1",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/geodesic-complete-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::geodesic_complete_1",
  "declaration_slug": "geodesic-complete-1",
  "kind": "theorem",
  "name": "geodesic_complete_1",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 181,
  "source_line_end": 182,
  "registry_ids": [
    "II.P17"
  ],
  "related_registry_items": [
    {
      "id": "II.P17",
      "title": "Geodesic Completeness",
      "url": "/registry/object/II.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L181-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L181-L182",
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
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L181-L182)
- Source range: L181-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P17` — Geodesic Completeness

## Immediate Comment / Docstring

```lean
/-- [II.P17] Geodesic completeness at stage 1. -/
```

## Source Excerpt

```lean
theorem geodesic_complete_1 :
    geodesic_completeness_check 1 = true := by native_decide
```
