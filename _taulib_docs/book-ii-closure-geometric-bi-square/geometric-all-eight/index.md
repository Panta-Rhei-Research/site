---
{
  "projection_kind": "taulib_declaration",
  "title": "geometric_all_eight",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geometric-all-eight/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::geometric_all_eight",
  "declaration_slug": "geometric-all-eight",
  "kind": "theorem",
  "name": "geometric_all_eight",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 258,
  "source_line_end": 259,
  "registry_ids": [
    "II.T49"
  ],
  "related_registry_items": [
    {
      "id": "II.T49",
      "title": "Geometric Bi-Square Theorem",
      "url": "/registry/object/II.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L258-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.GeometricBiSquare",
        "url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L258-L259",
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

- Module: [TauLib.BookII.Closure.GeometricBiSquare](/verify/taulib/docs/book-ii-closure-geometric-bi-square/)
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L258-L259)
- Source range: L258-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T49` — Geometric Bi-Square Theorem

## Immediate Comment / Docstring

```lean
-- All eight components [II.T49]
```

## Source Excerpt

```lean
theorem geometric_all_eight :
    geometric_component_count (compute_geometric_bisquare 3 15) = 8 := by native_decide
```
