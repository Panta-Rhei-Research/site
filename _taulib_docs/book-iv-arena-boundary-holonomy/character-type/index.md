---
{
  "projection_kind": "taulib_declaration",
  "title": "CharacterType",
  "permalink": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/character-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::CharacterType",
  "declaration_slug": "character-type",
  "kind": "inductive",
  "name": "CharacterType",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 100,
  "source_line_end": 103,
  "registry_ids": [
    "IV.D259"
  ],
  "related_registry_items": [
    {
      "id": "IV.D259",
      "title": "Boundary character",
      "url": "/registry/object/IV.D259/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L100-L103",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L100-L103",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L100-L103)
- Source range: L100-L103
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D259` — Boundary character

## Immediate Comment / Docstring

```lean
/-- [IV.D259] A boundary character χ: L → ℂ_τ. Characters encode
    how the lemniscate boundary responds to each sector.
    Split into multiplicative (χ₊) and additive (χ₋) components. -/
```

## Source Excerpt

```lean
inductive CharacterType where
  | ChiPlus  : CharacterType  -- multiplicative/spreading
  | ChiMinus : CharacterType  -- additive/tightening
  deriving Repr, DecidableEq, BEq
```
