---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L115",
  "permalink": "/verify/taulib/docs/book-i-topos-wedge-product/eval-l115/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::#eval:115",
  "declaration_slug": "eval-l115",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 115,
  "source_line_end": 115,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L115-L115",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.WedgeProduct",
        "url": "/verify/taulib/docs/book-i-topos-wedge-product/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L115-L115",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookI.Topos.WedgeProduct](/verify/taulib/docs/book-i-topos-wedge-product/)
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L115-L115)
- Source range: L115-L115
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval (cat_coproduct ⟨fun n => n % 2 == 0⟩ ⟨fun n => n % 3 == 0⟩).support 5  -- false
```
