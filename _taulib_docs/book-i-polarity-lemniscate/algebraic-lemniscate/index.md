---
{
  "projection_kind": "taulib_declaration",
  "title": "AlgebraicLemniscate",
  "permalink": "/verify/taulib/docs/book-i-polarity-lemniscate/algebraic-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::AlgebraicLemniscate",
  "declaration_slug": "algebraic-lemniscate",
  "kind": "structure",
  "name": "AlgebraicLemniscate",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/verify/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 44,
  "source_line_end": 58,
  "registry_ids": [
    "I.D18"
  ],
  "related_registry_items": [
    {
      "id": "I.D18",
      "title": "Algebraic Lemniscate",
      "url": "/registry/object/I.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L44-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Lemniscate",
        "url": "/verify/taulib/docs/book-i-polarity-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L44-L58",
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

- Module: [TauLib.BookI.Polarity.Lemniscate](/verify/taulib/docs/book-i-polarity-lemniscate/)
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L44-L58)
- Source range: L44-L58
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D18` — Algebraic Lemniscate

## Immediate Comment / Docstring

```lean
/-- [I.D18] The algebraic lemniscate: a triple (algebra, crossing point, involution).
    This is the pre-geometric boundary structure of Category τ. -/
```

## Source Excerpt

```lean
structure AlgebraicLemniscate where
  /-- The bipolar spectral algebra H_τ, represented by its unit j. -/
  j_unit : SplitComplex
  /-- j² = 1 (split-complex identity). -/
  j_sq : SplitComplex.mul j_unit j_unit = SplitComplex.one
  /-- The crossing-point germ ω_L (sector-balanced: both components equal). -/
  crossing_point : SectorPair
  /-- The crossing point has equal sector components (balance). -/
  crossing_balanced : crossing_point.b_sector = crossing_point.c_sector
  /-- The polarity involution σ. -/
  involution : SplitComplex → SplitComplex
  /-- σ² = id. -/
  involution_sq : ∀ z, involution (involution z) = z
  /-- σ(j) = -j. -/
  involution_j : involution j_unit = SplitComplex.neg j_unit
```
