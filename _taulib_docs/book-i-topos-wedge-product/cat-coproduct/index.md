---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_coproduct",
  "permalink": "/verify/taulib/docs/book-i-topos-wedge-product/cat-coproduct/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::cat_coproduct",
  "declaration_slug": "cat-coproduct",
  "kind": "def",
  "name": "cat_coproduct",
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 30,
  "source_line_end": 31,
  "registry_ids": [
    "I.D62"
  ],
  "related_registry_items": [
    {
      "id": "I.D62",
      "title": "Categorical Coproduct",
      "url": "/registry/object/I.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L30-L31",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L30-L31",
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

- Module: [TauLib.BookI.Topos.WedgeProduct](/verify/taulib/docs/book-i-topos-wedge-product/)
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L30-L31)
- Source range: L30-L31
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D62` — Categorical Coproduct

## Immediate Comment / Docstring

```lean
/-- [I.D62] The categorical coproduct of two presheaves:
    pointwise disjunction of support predicates. -/
```

## Source Excerpt

```lean
def cat_coproduct (P Q : Presheaf) : Presheaf :=
  presheaf_coproduct P Q
```
