---
{
  "projection_kind": "taulib_declaration",
  "title": "complete_means_eight",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/complete-means-eight/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::complete_means_eight",
  "declaration_slug": "complete-means-eight",
  "kind": "theorem",
  "name": "complete_means_eight",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 303,
  "source_line_end": 318,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L303-L318",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L303-L318",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L303-L318)
- Source range: L303-L318
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T49` — Geometric Bi-Square Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T49] A complete geometric bi-square has all 8 components.
    This is the structural statement that completeness implies count = 8. -/
```

## Source Excerpt

```lean
theorem complete_means_eight (gbs : GeometricBiSquareData) :
    geometric_bisquare_complete gbs = true →
    geometric_component_count gbs = 8 := by
  intro h
  simp only [geometric_bisquare_complete] at h
  simp only [geometric_component_count]
  revert h
  cases gbs.topology_earned <;>
  cases gbs.continuity_earned <;>
  cases gbs.geometry_earned <;>
  cases gbs.torus_degeneration_earned <;>
  cases gbs.calibration_earned <;>
  cases gbs.spectral_algebra_earned <;>
  cases gbs.central_theorem_earned <;>
  cases gbs.hartogs_earned <;>
  simp
```
