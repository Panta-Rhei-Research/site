---
{
  "projection_kind": "taulib_declaration",
  "title": "geo_topology",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geo-topology/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::geo_topology",
  "declaration_slug": "geo-topology",
  "kind": "theorem",
  "name": "geo_topology",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 262,
  "source_line_end": 263,
  "registry_ids": [
    "II.D77"
  ],
  "related_registry_items": [
    {
      "id": "II.D77",
      "title": "Geometric Bi-Square",
      "url": "/registry/object/II.D77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L262-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L262-L263",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L262-L263)
- Source range: L262-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D77` — Geometric Bi-Square

## Immediate Comment / Docstring

```lean
-- Individual geometric components [II.D77]
```

## Source Excerpt

```lean
theorem geo_topology :
    (compute_geometric_bisquare 3 15).topology_earned = true := by native_decide
```
