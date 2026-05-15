---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_proj1",
  "permalink": "/corpus/taulib/docs/book-i-topos-cartesian-product/cat-proj1/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CartesianProduct`.",
  "declaration_id": "TauLib.BookI.Topos.CartesianProduct::cat_proj1",
  "declaration_slug": "cat-proj1",
  "kind": "theorem",
  "name": "cat_proj1",
  "module_name": "TauLib.BookI.Topos.CartesianProduct",
  "module_url": "/corpus/taulib/docs/book-i-topos-cartesian-product/",
  "source_line_start": 36,
  "source_line_end": 38,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L36-L38",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CartesianProduct",
        "url": "/corpus/taulib/docs/book-i-topos-cartesian-product/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L36-L38",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Topos.CartesianProduct](/corpus/taulib/docs/book-i-topos-cartesian-product/)
- Source path: [`TauLib/BookI/Topos/CartesianProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CartesianProduct.lean#L36-L38)
- Source range: L36-L38
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- First projection: product → first factor. -/
```

## Source Excerpt

```lean
theorem cat_proj1 (P Q : Presheaf) (x : TauIdx)
    (h : (cat_product P Q).support x = true) : P.support x = true := by
  simp [cat_product, presheaf_product] at h; exact h.1
```
