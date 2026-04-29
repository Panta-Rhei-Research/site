---
{
  "projection_kind": "taulib_declaration",
  "title": "CartesianMonoidal",
  "permalink": "/verify/taulib/docs/book-i-topos-cartesian-product/cartesian-monoidal/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.CartesianProduct`.",
  "declaration_id": "TauLib.BookI.Topos.CartesianProduct::CartesianMonoidal",
  "declaration_slug": "cartesian-monoidal",
  "kind": "structure",
  "name": "CartesianMonoidal",
  "module_name": "TauLib.BookI.Topos.CartesianProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-cartesian-product/",
  "source_line_start": 81,
  "source_line_end": 85,
  "registry_ids": [
    "I.D61"
  ],
  "related_registry_items": [
    {
      "id": "I.D61",
      "title": "Cartesian Monoidal Structure",
      "url": "/registry/object/I.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L81-L85",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L81-L85",
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

- Module: [TauLib.BookI.Topos.CartesianProduct](/verify/taulib/docs/book-i-topos-cartesian-product/)
- Source path: [`TauLib/BookI/Topos/CartesianProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L81-L85)
- Source range: L81-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D61` — Cartesian Monoidal Structure

## Immediate Comment / Docstring

```lean
/-- [I.D61] The cartesian monoidal structure on E_τ.
    Unit: terminal presheaf. Tensor: pointwise product. -/
```

## Source Excerpt

```lean
structure CartesianMonoidal where
  -- Monoidal unit
  unit : Presheaf := ⟨fun _ => true⟩
  -- Tensor product
  tensor : Presheaf → Presheaf → Presheaf := cat_product
```
