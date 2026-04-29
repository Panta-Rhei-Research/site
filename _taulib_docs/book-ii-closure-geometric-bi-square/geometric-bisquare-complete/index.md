---
{
  "projection_kind": "taulib_declaration",
  "title": "geometric_bisquare_complete",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-complete/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::geometric_bisquare_complete",
  "declaration_slug": "geometric-bisquare-complete",
  "kind": "def",
  "name": "geometric_bisquare_complete",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 104,
  "source_line_end": 112,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L104-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L104-L112",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L104-L112)
- Source range: L104-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D77` — Geometric Bi-Square

## Immediate Comment / Docstring

```lean
/-- [II.D77] Check that all eight components are earned. -/
```

## Source Excerpt

```lean
def geometric_bisquare_complete (gbs : GeometricBiSquareData) : Bool :=
  gbs.topology_earned &&
  gbs.continuity_earned &&
  gbs.geometry_earned &&
  gbs.torus_degeneration_earned &&
  gbs.calibration_earned &&
  gbs.spectral_algebra_earned &&
  gbs.central_theorem_earned &&
  gbs.hartogs_earned
```
