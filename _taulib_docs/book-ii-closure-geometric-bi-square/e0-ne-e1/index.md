---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_ne_e1",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/e0-ne-e1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::e0_ne_e1",
  "declaration_slug": "e0-ne-e1",
  "kind": "theorem",
  "name": "e0_ne_e1",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 332,
  "source_line_end": 333,
  "registry_ids": [
    "II.R34"
  ],
  "related_registry_items": [
    {
      "id": "II.R34",
      "title": "Scaling Chain Forward",
      "url": "/registry/object/II.R34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L332-L333",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L332-L333",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L332-L333)
- Source range: L332-L333
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.R34` — Scaling Chain Forward

## Immediate Comment / Docstring

```lean
/-- [II.R34] E0 and E1 are distinct scaling levels. -/
```

## Source Excerpt

```lean
theorem e0_ne_e1 : ScalingLevel.E0_algebraic ≠ ScalingLevel.E1_geometric := by
  intro h; cases h
```
