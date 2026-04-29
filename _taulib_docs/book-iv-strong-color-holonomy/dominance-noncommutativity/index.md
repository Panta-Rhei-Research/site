---
{
  "projection_kind": "taulib_declaration",
  "title": "DominanceNoncommutativity",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/dominance-noncommutativity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::DominanceNoncommutativity",
  "declaration_slug": "dominance-noncommutativity",
  "kind": "structure",
  "name": "DominanceNoncommutativity",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 178,
  "source_line_end": 185,
  "registry_ids": [
    "IV.P91"
  ],
  "related_registry_items": [
    {
      "id": "IV.P91",
      "title": "χ₋-Dominance Forces Non-Commutativity",
      "url": "/registry/object/IV.P91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L178-L185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.ColorHolonomy",
        "url": "/verify/taulib/docs/book-iv-strong-color-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L178-L185",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L178-L185)
- Source range: L178-L185
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P91` — χ₋-Dominance Forces Non-Commutativity

## Immediate Comment / Docstring

```lean
/-- [IV.P91] Chi_minus-dominant sector has non-commutative endomorphism
    algebra, forcing a non-abelian gauge group. -/
```

## Source Excerpt

```lean
structure DominanceNoncommutativity where
  /-- Chi_minus dominance implies non-abelian. -/
  chi_minus_implies_nonabelian : Bool := true
  /-- The polarity involution acts as negation on the dominant lobe. -/
  polarity_negation : Bool := true
  /-- Resulting gauge group is non-abelian. -/
  gauge_nonabelian : Bool := true
  deriving Repr
```
