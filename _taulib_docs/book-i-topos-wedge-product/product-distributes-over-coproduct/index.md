---
{
  "projection_kind": "taulib_declaration",
  "title": "product_distributes_over_coproduct",
  "permalink": "/verify/taulib/docs/book-i-topos-wedge-product/product-distributes-over-coproduct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::product_distributes_over_coproduct",
  "declaration_slug": "product-distributes-over-coproduct",
  "kind": "theorem",
  "name": "product_distributes_over_coproduct",
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 65,
  "source_line_end": 70,
  "registry_ids": [
    "I.T27"
  ],
  "related_registry_items": [
    {
      "id": "I.T27",
      "title": "Distributivity",
      "url": "/registry/object/I.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L65-L70",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L65-L70",
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
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L65-L70)
- Source range: L65-L70
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T27` — Distributivity

## Immediate Comment / Docstring

```lean
/-- [I.T27] Product distributes over coproduct:
    P × (Q ∨ R) = (P × Q) ∨ (P × R). -/
```

## Source Excerpt

```lean
theorem product_distributes_over_coproduct (P Q R : Presheaf) :
    (cat_product P (cat_coproduct Q R)).support =
    (cat_coproduct (cat_product P Q) (cat_product P R)).support := by
  ext x
  simp [cat_product, cat_coproduct, presheaf_product, presheaf_coproduct,
        Bool.and_or_distrib_left]
```
