---
{
  "projection_kind": "taulib_declaration",
  "title": "ProductObj",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/product-obj/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::ProductObj",
  "declaration_slug": "product-obj",
  "kind": "structure",
  "name": "ProductObj",
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 61,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L61-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.LimitsSites",
        "url": "/verify/taulib/docs/book-i-topos-limits-sites/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L61-L67",
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

- Module: [TauLib.BookI.Topos.LimitsSites](/verify/taulib/docs/book-i-topos-limits-sites/)
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L61-L67)
- Source range: L61-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D55b] Product object in Cat_τ via Cantor pairing. -/
```

## Source Excerpt

```lean
structure ProductObj where
  /-- First factor. -/
  fst : TauIdx
  /-- Second factor. -/
  snd : TauIdx
  /-- The encoded product index. -/
  prod : TauIdx := cantor_pair fst snd
```
