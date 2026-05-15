---
{
  "projection_kind": "taulib_declaration",
  "title": "BiMonoidal",
  "permalink": "/corpus/taulib/docs/book-i-topos-wedge-product/bi-monoidal/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::BiMonoidal",
  "declaration_slug": "bi-monoidal",
  "kind": "structure",
  "name": "BiMonoidal",
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/corpus/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 86,
  "source_line_end": 94,
  "registry_ids": [
    "I.D63"
  ],
  "related_registry_items": [
    {
      "id": "I.D63",
      "title": "Bi-Monoidal Structure",
      "url": "/registry/object/I.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L86-L94",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.WedgeProduct",
        "url": "/corpus/taulib/docs/book-i-topos-wedge-product/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L86-L94",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Topos.WedgeProduct](/corpus/taulib/docs/book-i-topos-wedge-product/)
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L86-L94)
- Source range: L86-L94
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.D63` — Bi-Monoidal Structure

## Immediate Comment / Docstring

```lean
/-- [I.D63] The bi-monoidal structure on E_τ:
    product (×) and coproduct (∨) with distributivity. -/
```

## Source Excerpt

```lean
structure BiMonoidal where
  -- Multiplicative tensor
  times : Presheaf → Presheaf → Presheaf := cat_product
  -- Additive tensor
  wedge : Presheaf → Presheaf → Presheaf := cat_coproduct
  -- Multiplicative unit
  one : Presheaf := ⟨fun _ => true⟩
  -- Additive unit
  zero : Presheaf := ⟨fun _ => false⟩
```
