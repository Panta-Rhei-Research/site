---
{
  "projection_kind": "taulib_declaration",
  "title": "product_distributes_right",
  "permalink": "/verify/taulib/docs/book-i-topos-wedge-product/product-distributes-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::product_distributes_right",
  "declaration_slug": "product-distributes-right",
  "kind": "theorem",
  "name": "product_distributes_right",
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 73,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L73-L78",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L73-L78",
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

- Module: [TauLib.BookI.Topos.WedgeProduct](/verify/taulib/docs/book-i-topos-wedge-product/)
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L73-L78)
- Source range: L73-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Right distributivity: (P ∨ Q) × R = (P × R) ∨ (Q × R). -/
```

## Source Excerpt

```lean
theorem product_distributes_right (P Q R : Presheaf) :
    (cat_product (cat_coproduct P Q) R).support =
    (cat_coproduct (cat_product P R) (cat_product Q R)).support := by
  ext x
  simp [cat_product, cat_coproduct, presheaf_product, presheaf_coproduct]
  cases P.support x <;> cases Q.support x <;> cases R.support x <;> simp
```
