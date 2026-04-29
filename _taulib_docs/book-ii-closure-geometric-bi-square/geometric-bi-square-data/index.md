---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricBiSquareData",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bi-square-data/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::GeometricBiSquareData",
  "declaration_slug": "geometric-bi-square-data",
  "kind": "structure",
  "name": "GeometricBiSquareData",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 65,
  "source_line_end": 82,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L65-L82",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L65-L82",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L65-L82)
- Source range: L65-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D77` — Geometric Bi-Square

## Immediate Comment / Docstring

```lean
/-- [II.D77] The Geometric Bi-Square: Book I's algebraic bi-square (I.T41)
    annotated with boolean witnesses recording that each geometric
    component has been earned in Book II.

    Eight witnesses correspond to eight geometric "earnings":
    1. topology_earned: Stone space structure on tau^3 (II.T07)
    2. continuity_earned: Hol implies Continuous (II.T06)
    3. geometry_earned: Tarski axioms verified (II.T16-T20)
    4. torus_degeneration_earned: T^2 -> S^1 v S^1 (II.T13)
    5. calibration_earned: H_tau calibrated with pi, e, j (II.D35)
    6. spectral_algebra_earned: A_spec(L) ring structure (II.D60)
    7. central_theorem_earned: O(tau^3) = A_spec(L) (II.T40)
    8. hartogs_earned: Mutual determination (II.T27) -/
```

## Source Excerpt

```lean
structure GeometricBiSquareData where
  /-- Stone space structure on tau^3 (II.T07). -/
  topology_earned : Bool
  /-- Hol implies Continuous (II.T06). -/
  continuity_earned : Bool
  /-- Tarski axioms verified (II.T16-T20). -/
  geometry_earned : Bool
  /-- T^2 -> S^1 v S^1 via pinch map (II.T13). -/
  torus_degeneration_earned : Bool
  /-- H_tau calibrated with pi, e, j (II.D35). -/
  calibration_earned : Bool
  /-- A_spec(L) ring/tower structure (II.D60). -/
  spectral_algebra_earned : Bool
  /-- Central Theorem O(tau^3) = A_spec(L) (II.T40). -/
  central_theorem_earned : Bool
  /-- Mutual determination / Hartogs (II.T27). -/
  hartogs_earned : Bool
  deriving Repr, DecidableEq
```
