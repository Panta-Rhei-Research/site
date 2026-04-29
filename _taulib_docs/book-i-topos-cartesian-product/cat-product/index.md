---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_product",
  "permalink": "/verify/taulib/docs/book-i-topos-cartesian-product/cat-product/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.CartesianProduct`.",
  "declaration_id": "TauLib.BookI.Topos.CartesianProduct::cat_product",
  "declaration_slug": "cat-product",
  "kind": "def",
  "name": "cat_product",
  "module_name": "TauLib.BookI.Topos.CartesianProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-cartesian-product/",
  "source_line_start": 32,
  "source_line_end": 33,
  "registry_ids": [
    "I.D60"
  ],
  "related_registry_items": [
    {
      "id": "I.D60",
      "title": "Categorical Product",
      "url": "/registry/object/I.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L32-L33",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L32-L33",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/Topos/CartesianProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L32-L33)
- Source range: L32-L33
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D60` — Categorical Product

## Immediate Comment / Docstring

```lean
/-- [I.D60] The categorical product of two presheaves:
    pointwise conjunction of support predicates. -/
```

## Source Excerpt

```lean
def cat_product (P Q : Presheaf) : Presheaf :=
  presheaf_product P Q
```
