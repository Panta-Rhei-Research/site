---
{
  "projection_kind": "taulib_declaration",
  "title": "product_universal",
  "permalink": "/verify/taulib/docs/book-i-topos-cartesian-product/product-universal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CartesianProduct`.",
  "declaration_id": "TauLib.BookI.Topos.CartesianProduct::product_universal",
  "declaration_slug": "product-universal",
  "kind": "theorem",
  "name": "product_universal",
  "module_name": "TauLib.BookI.Topos.CartesianProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-cartesian-product/",
  "source_line_start": 51,
  "source_line_end": 57,
  "registry_ids": [
    "I.T26"
  ],
  "related_registry_items": [
    {
      "id": "I.T26",
      "title": "Product Universal Property",
      "url": "/registry/object/I.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L51-L57",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CartesianProduct",
        "url": "/verify/taulib/docs/book-i-topos-cartesian-product/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L51-L57",
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

- Module: [TauLib.BookI.Topos.CartesianProduct](/verify/taulib/docs/book-i-topos-cartesian-product/)
- Source path: [`TauLib/BookI/Topos/CartesianProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L51-L57)
- Source range: L51-L57
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T26` — Product Universal Property

## Immediate Comment / Docstring

```lean
/-- [I.T26] Product universal property: if R maps to both P and Q pointwise,
    then R maps to P × Q. -/
```

## Source Excerpt

```lean
theorem product_universal (P Q R : Presheaf)
    (hP : ∀ x, R.support x = true → P.support x = true)
    (hQ : ∀ x, R.support x = true → Q.support x = true) :
    ∀ x, R.support x = true → (cat_product P Q).support x = true := by
  intro x hr
  simp [cat_product, presheaf_product]
  exact ⟨hP x hr, hQ x hr⟩
```
