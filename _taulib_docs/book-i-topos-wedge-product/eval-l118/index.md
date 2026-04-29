---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L118",
  "permalink": "/verify/taulib/docs/book-i-topos-wedge-product/eval-l118/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::#eval:118",
  "declaration_slug": "eval-l118",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 118,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L118-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L118-L121",
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
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L118-L121)
- Source range: L118-L121
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Distributivity witness
```

## Source Excerpt

```lean
#eval (cat_product ⟨fun _ => true⟩ (cat_coproduct ⟨fun _ => false⟩ ⟨fun _ => true⟩)).support 0
-- true = (true && (false || true))

end Tau.Topos
```
