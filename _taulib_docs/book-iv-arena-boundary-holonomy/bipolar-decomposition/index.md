---
{
  "projection_kind": "taulib_declaration",
  "title": "BipolarDecomposition",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/bipolar-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::BipolarDecomposition",
  "declaration_slug": "bipolar-decomposition",
  "kind": "structure",
  "name": "BipolarDecomposition",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 122,
  "source_line_end": 129,
  "registry_ids": [
    "IV.D260"
  ],
  "related_registry_items": [
    {
      "id": "IV.D260",
      "title": "Bipolar decomposition of characters",
      "url": "/registry/object/IV.D260/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L122-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L122-L129",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L122-L129)
- Source range: L122-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D260` — Bipolar decomposition of characters

## Immediate Comment / Docstring

```lean
/-- [IV.D260] Bipolar decomposition: every boundary character splits
    as χ = χ₊ + χ₋ (multiplicative + additive components).
    The split is canonical: determined by the lemniscate geometry. -/
```

## Source Excerpt

```lean
structure BipolarDecomposition where
  /-- Multiplicative component. -/
  chi_plus : BoundaryCharacter
  plus_is_plus : chi_plus.char_type = .ChiPlus
  /-- Additive component. -/
  chi_minus : BoundaryCharacter
  minus_is_minus : chi_minus.char_type = .ChiMinus
  deriving Repr
```
