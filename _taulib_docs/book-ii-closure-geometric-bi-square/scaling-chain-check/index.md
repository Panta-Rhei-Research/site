---
{
  "projection_kind": "taulib_declaration",
  "title": "scaling_chain_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/scaling-chain-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::scaling_chain_check",
  "declaration_slug": "scaling-chain-check",
  "kind": "def",
  "name": "scaling_chain_check",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 201,
  "source_line_end": 203,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L201-L203",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L201-L203",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L201-L203)
- Source range: L201-L203
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R34` — Scaling Chain Forward

## Immediate Comment / Docstring

```lean
/-- [II.R34] Scaling chain monotonicity: E0 < E1 < E2. -/
```

## Source Excerpt

```lean
def scaling_chain_check : Bool :=
  scaling_level_index .E0_algebraic < scaling_level_index .E1_geometric &&
  scaling_level_index .E1_geometric < scaling_level_index .E2_enriched
```
