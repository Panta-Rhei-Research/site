---
{
  "projection_kind": "taulib_declaration",
  "title": "compute_geometric_bisquare",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/compute-geometric-bisquare/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::compute_geometric_bisquare",
  "declaration_slug": "compute-geometric-bisquare",
  "kind": "def",
  "name": "compute_geometric_bisquare",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 91,
  "source_line_end": 101,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L91-L101",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L91-L101",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L91-L101)
- Source range: L91-L101
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D77` — Geometric Bi-Square

## Immediate Comment / Docstring

```lean
/-- [II.D77] Compute the Geometric Bi-Square by evaluating all
    eight geometric check functions from Book II.
    Parameters db, bound control verification depth. -/
```

## Source Excerpt

```lean
def compute_geometric_bisquare (db bound : TauIdx) : GeometricBiSquareData :=
  { topology_earned := stone_space_check bound db
  , continuity_earned := hol_cont_check id_stage db bound
  , geometry_earned := tarski_complete_check bound db
  , torus_degeneration_earned :=
      pinch_surjective_check && gauge_survival_check && fund_group_check
  , calibration_earned := calibration_consistency_check
  , spectral_algebra_earned := spectral_algebra_stage_ring_check db bound
  , central_theorem_earned := central_theorem_check db bound
  , hartogs_earned := hartogs_check bound db
  }
```
