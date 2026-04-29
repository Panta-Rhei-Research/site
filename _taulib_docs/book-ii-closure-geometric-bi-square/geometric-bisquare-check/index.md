---
{
  "projection_kind": "taulib_declaration",
  "title": "geometric_bisquare_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::geometric_bisquare_check",
  "declaration_slug": "geometric-bisquare-check",
  "kind": "def",
  "name": "geometric_bisquare_check",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 120,
  "source_line_end": 121,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L120-L121",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L120-L121",
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

- Module: [TauLib.BookII.Closure.GeometricBiSquare](/verify/taulib/docs/book-ii-closure-geometric-bi-square/)
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L120-L121)
- Source range: L120-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T49` — Geometric Bi-Square Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T49] The Geometric Bi-Square Theorem: compute and verify
    that all eight geometric components are earned. -/
```

## Source Excerpt

```lean
def geometric_bisquare_check (db bound : TauIdx) : Bool :=
  geometric_bisquare_complete (compute_geometric_bisquare db bound)
```
