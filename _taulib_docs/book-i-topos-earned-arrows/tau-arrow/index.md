---
{
  "projection_kind": "taulib_declaration",
  "title": "TauArrow",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-arrows/tau-arrow/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::TauArrow",
  "declaration_slug": "tau-arrow",
  "kind": "structure",
  "name": "TauArrow",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 47,
  "source_line_end": 50,
  "registry_ids": [
    "I.D50"
  ],
  "related_registry_items": [
    {
      "id": "I.D50",
      "title": "Tau-Arrow",
      "url": "/registry/object/I.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L47-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedArrows",
        "url": "/verify/taulib/docs/book-i-topos-earned-arrows/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L47-L50",
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

- Module: [TauLib.BookI.Topos.EarnedArrows](/verify/taulib/docs/book-i-topos-earned-arrows/)
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L47-L50)
- Source range: L47-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D50` — Tau-Arrow

## Immediate Comment / Docstring

```lean
/-- [I.D50] A τ-arrow from source to target, carrying a HolFun.
    Two τ-arrows are equal iff their underlying HolFuns agree extensionally. -/
```

## Source Excerpt

```lean
structure TauArrow where
  source : TauIdx
  target : TauIdx
  holfun : HolFun
```
