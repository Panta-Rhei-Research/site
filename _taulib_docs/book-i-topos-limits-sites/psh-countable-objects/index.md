---
{
  "projection_kind": "taulib_declaration",
  "title": "psh_countable_objects",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/psh-countable-objects/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::psh_countable_objects",
  "declaration_slug": "psh-countable-objects",
  "kind": "theorem",
  "name": "psh_countable_objects",
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 207,
  "source_line_end": 207,
  "registry_ids": [
    "I.P26"
  ],
  "related_registry_items": [
    {
      "id": "I.P26",
      "title": "Countable Topos",
      "url": "/registry/object/I.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L207-L207",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L207-L207",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L207-L207)
- Source range: L207-L207
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P26` — Countable Topos

## Immediate Comment / Docstring

```lean
/-- [I.P26] PSh(Cat_τ) is countable because Cat_τ has countable objects
    and at most one morphism between each pair (thin).
    The set of presheaves is indexed by functions TauIdx → Bool,
    which is uncountable as a set but countably generated
    (each presheaf is determined by a countable family of values). -/
```

## Source Excerpt

```lean
theorem psh_countable_objects : True := trivial
```
