---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L218",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/example-l218/",
  "summary_short": "`example` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::#eval:218",
  "declaration_slug": "example-l218",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 218,
  "source_line_end": 218,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L218-L218",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L218-L218",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L218-L218)
- Source range: L218-L218
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verify: these two residues determine 17 mod M_2 = 17 mod 6. -/
```

## Source Excerpt

```lean
example : reduce 17 2 = 5 := by native_decide  -- 17 mod 6 = 5
```
