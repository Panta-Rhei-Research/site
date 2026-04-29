---
{
  "projection_kind": "taulib_declaration",
  "title": "scaling_level_index",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level-index/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::scaling_level_index",
  "declaration_slug": "scaling-level-index",
  "kind": "def",
  "name": "scaling_level_index",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 195,
  "source_line_end": 198,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L195-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L195-L198",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L195-L198)
- Source range: L195-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R34` — Scaling Chain Forward

## Immediate Comment / Docstring

```lean
/-- [II.R34] The scaling chain: algebraic < geometric < enriched.
    Each level adds geometric content to the bi-square. -/
```

## Source Excerpt

```lean
def scaling_level_index : ScalingLevel → Nat
  | .E0_algebraic => 0
  | .E1_geometric => 1
  | .E2_enriched  => 2
```
