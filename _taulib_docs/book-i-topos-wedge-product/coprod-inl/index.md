---
{
  "projection_kind": "taulib_declaration",
  "title": "coprod_inl",
  "permalink": "/corpus/taulib/docs/book-i-topos-wedge-product/coprod-inl/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.WedgeProduct`.",
  "declaration_id": "TauLib.BookI.Topos.WedgeProduct::coprod_inl",
  "declaration_slug": "coprod-inl",
  "kind": "theorem",
  "name": "coprod_inl",
  "module_name": "TauLib.BookI.Topos.WedgeProduct",
  "module_url": "/corpus/taulib/docs/book-i-topos-wedge-product/",
  "source_line_start": 34,
  "source_line_end": 36,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L34-L36",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L34-L36",
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

- Module: [TauLib.BookI.Topos.WedgeProduct](/corpus/taulib/docs/book-i-topos-wedge-product/)
- Source path: [`TauLib/BookI/Topos/WedgeProduct.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/WedgeProduct.lean#L34-L36)
- Source range: L34-L36
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Left injection: P → P ∨ Q. -/
```

## Source Excerpt

```lean
theorem coprod_inl (P Q : Presheaf) (x : TauIdx) :
    P.support x = true → (cat_coproduct P Q).support x = true := by
  intro h; simp [cat_coproduct, presheaf_coproduct, h]
```
