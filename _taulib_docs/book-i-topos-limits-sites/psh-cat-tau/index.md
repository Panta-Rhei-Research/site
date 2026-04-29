---
{
  "projection_kind": "taulib_declaration",
  "title": "PShCatTau",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/psh-cat-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::PShCatTau",
  "declaration_slug": "psh-cat-tau",
  "kind": "structure",
  "name": "PShCatTau",
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 152,
  "source_line_end": 154,
  "registry_ids": [
    "I.D57"
  ],
  "related_registry_items": [
    {
      "id": "I.D57",
      "title": "Presheaf Topos",
      "url": "/registry/object/I.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L152-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L152-L154",
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
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L152-L154)
- Source range: L152-L154
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D57` — Presheaf Topos

## Immediate Comment / Docstring

```lean
/-- [I.D57] The presheaf topos PSh(Cat_τ).
    A presheaf assigns to each object a set (modeled as a predicate).
    The topos structure includes limits, colimits, exponentials,
    and a subobject classifier. -/
```

## Source Excerpt

```lean
structure PShCatTau where
  /-- A presheaf in PSh(Cat_τ). -/
  presheaf : Presheaf
```
