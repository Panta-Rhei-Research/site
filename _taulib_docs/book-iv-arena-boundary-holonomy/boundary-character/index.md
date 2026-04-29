---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryCharacter",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/boundary-character/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::BoundaryCharacter",
  "declaration_slug": "boundary-character",
  "kind": "structure",
  "name": "BoundaryCharacter",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 106,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L106-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L106-L113",
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
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L106-L113)
- Source range: L106-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A boundary character with its type classification. -/
```

## Source Excerpt

```lean
structure BoundaryCharacter where
  /-- Which type of character. -/
  char_type : CharacterType
  /-- Scaled value (numerator at 10⁶ scale). -/
  value_numer : Nat
  value_denom : Nat
  denom_pos : value_denom > 0
  deriving Repr
```
