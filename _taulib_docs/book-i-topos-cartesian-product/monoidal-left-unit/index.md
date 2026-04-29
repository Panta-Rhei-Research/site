---
{
  "projection_kind": "taulib_declaration",
  "title": "monoidal_left_unit",
  "permalink": "/verify/taulib/docs/book-i-topos-cartesian-product/monoidal-left-unit/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CartesianProduct`.",
  "declaration_id": "TauLib.BookI.Topos.CartesianProduct::monoidal_left_unit",
  "declaration_slug": "monoidal-left-unit",
  "kind": "theorem",
  "name": "monoidal_left_unit",
  "module_name": "TauLib.BookI.Topos.CartesianProduct",
  "module_url": "/verify/taulib/docs/book-i-topos-cartesian-product/",
  "source_line_start": 91,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L91-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L91-L93",
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
- Source path: [`TauLib/BookI/Topos/CartesianProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L91-L93)
- Source range: L91-L93
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Left unit law. -/
```

## Source Excerpt

```lean
theorem monoidal_left_unit (P : Presheaf) :
    (cat_product ⟨fun _ => true⟩ P).support = P.support := by
  ext x; simp [cat_product, presheaf_product, Bool.true_and]
```
