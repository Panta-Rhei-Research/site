---
{
  "projection_kind": "taulib_declaration",
  "title": "psh_has_terminal",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/psh-has-terminal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::psh_has_terminal",
  "declaration_slug": "psh-has-terminal",
  "kind": "theorem",
  "name": "psh_has_terminal",
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 174,
  "source_line_end": 175,
  "registry_ids": [
    "I.T24"
  ],
  "related_registry_items": [
    {
      "id": "I.T24",
      "title": "Grothendieck Topos",
      "url": "/registry/object/I.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L174-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L174-L175",
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
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L174-L175)
- Source range: L174-L175
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T24` — Grothendieck Topos

## Immediate Comment / Docstring

```lean
/-- [I.T24] PSh(Cat_τ) is a Grothendieck topos.
    Standard result: for any small category C, PSh(C) is a Grothendieck topos.
    Cat_τ is small (countable objects, thin morphisms).

    We encode this as: PSh(Cat_τ) has a terminal object, products,
    equalizers, and a subobject classifier. -/
```

## Source Excerpt

```lean
theorem psh_has_terminal :
    terminal_presheaf.presheaf.support 0 = true := rfl
```
