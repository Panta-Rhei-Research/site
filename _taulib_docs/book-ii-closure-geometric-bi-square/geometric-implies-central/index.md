---
{
  "projection_kind": "taulib_declaration",
  "title": "geometric_implies_central",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geometric-implies-central/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::geometric_implies_central",
  "declaration_slug": "geometric-implies-central",
  "kind": "theorem",
  "name": "geometric_implies_central",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 322,
  "source_line_end": 329,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L322-L329",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L322-L329",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L322-L329)
- Source range: L322-L329
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T49` — Geometric Bi-Square Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T49] The geometric bi-square implies the Central Theorem is earned.
    If the full check passes, the central_theorem_earned field is true. -/
```

## Source Excerpt

```lean
theorem geometric_implies_central (db bound : TauIdx) :
    geometric_bisquare_check db bound = true →
    central_theorem_check db bound = true := by
  intro h
  simp only [geometric_bisquare_check, geometric_bisquare_complete,
             compute_geometric_bisquare] at h
  revert h
  cases central_theorem_check db bound <;> simp
```
