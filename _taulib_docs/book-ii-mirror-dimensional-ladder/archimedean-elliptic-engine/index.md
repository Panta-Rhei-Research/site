---
{
  "projection_kind": "taulib_declaration",
  "title": "ArchimedeanEllipticEngine",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/archimedean-elliptic-engine/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::ArchimedeanEllipticEngine",
  "declaration_slug": "archimedean-elliptic-engine",
  "kind": "structure",
  "name": "ArchimedeanEllipticEngine",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 281,
  "source_line_end": 289,
  "registry_ids": [
    "II.D75"
  ],
  "related_registry_items": [
    {
      "id": "II.D75",
      "title": "Archimedean-Elliptic Engine",
      "url": "/registry/object/II.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L281-L289",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L281-L289",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L281-L289)
- Source range: L281-L289
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D75` — Archimedean-Elliptic Engine

## Immediate Comment / Docstring

```lean
/-- [II.D75] The Archimedean-elliptic engine: the mechanism that generates
    the orthodox SCV dimensional ladder.

    The engine requires two ingredients:
    1. Archimedean metric → continuous manifold with variable dimension
    2. Elliptic PDE type → CR overdeterminacy increases with dimension

    The interaction of these two features creates qualitatively new phenomena
    at each dimension step. Without BOTH ingredients, no ladder is generated. -/
```

## Source Excerpt

```lean
structure ArchimedeanEllipticEngine where
  /-- Archimedean metric gives continuous manifolds with meaningful dimension. -/
  has_metric_dimension : Bool
  /-- Elliptic CR equations are increasingly overdetermined for n ≥ 2. -/
  has_elliptic_cr : Bool
  /-- The engine generates the dimensional ladder only when both are active. -/
  generates_ladder : Bool
  /-- Ladder generation requires both ingredients. -/
  ladder_requires_both : generates_ladder = (has_metric_dimension && has_elliptic_cr)
```
