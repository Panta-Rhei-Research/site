---
{
  "projection_kind": "taulib_declaration",
  "title": "ScalingLevel",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::ScalingLevel",
  "declaration_slug": "scaling-level",
  "kind": "inductive",
  "name": "ScalingLevel",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 187,
  "source_line_end": 191,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L187-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L187-L191",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L187-L191)
- Source range: L187-L191
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.R34` — Scaling Chain Forward

## Immediate Comment / Docstring

```lean
/-- [II.R34] The three enrichment levels at which the bi-square lives.
    - E0_algebraic: Book I (finite cyclic groups, no topology)
    - E1_geometric: Book II (Stone space, continuity, torus degeneration)
    - E2_enriched: Book III (spectral forces, preview only) -/
```

## Source Excerpt

```lean
inductive ScalingLevel where
  | E0_algebraic : ScalingLevel
  | E1_geometric : ScalingLevel
  | E2_enriched  : ScalingLevel
  deriving Repr, DecidableEq
```
