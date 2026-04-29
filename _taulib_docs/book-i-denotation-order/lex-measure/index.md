---
{
  "projection_kind": "taulib_declaration",
  "title": "lex_measure",
  "permalink": "/verify/taulib/docs/book-i-denotation-order/lex-measure/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::lex_measure",
  "declaration_slug": "lex-measure",
  "kind": "def",
  "name": "lex_measure",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/verify/taulib/docs/book-i-denotation-order/",
  "source_line_start": 138,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L138-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Order",
        "url": "/verify/taulib/docs/book-i-denotation-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L138-L138",
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

- Module: [TauLib.BookI.Denotation.Order](/verify/taulib/docs/book-i-denotation-order/)
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L138-L138)
- Source range: L138-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The lexicographic measure for well-foundedness: (seed.toNat, depth). -/
```

## Source Excerpt

```lean
private def lex_measure (x : TauObj) : Nat × Nat := (x.seed.toNat, x.depth)
```
