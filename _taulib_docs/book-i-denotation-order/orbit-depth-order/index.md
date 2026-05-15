---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_depth_order",
  "permalink": "/corpus/taulib/docs/book-i-denotation-order/orbit-depth-order/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::orbit_depth_order",
  "declaration_slug": "orbit-depth-order",
  "kind": "theorem",
  "name": "orbit_depth_order",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/corpus/taulib/docs/book-i-denotation-order/",
  "source_line_start": 116,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L116-L118",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Order",
        "url": "/corpus/taulib/docs/book-i-denotation-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L116-L118",
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

- Module: [TauLib.BookI.Denotation.Order](/corpus/taulib/docs/book-i-denotation-order/)
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L116-L118)
- Source range: L116-L118
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Within each orbit ray, depth gives a total order. -/
```

## Source Excerpt

```lean
theorem orbit_depth_order (g : Generator) (n m : Nat) (h : n < m) :
    denotational_lt ⟨g, n⟩ ⟨g, m⟩ :=
  Or.inr ⟨rfl, h⟩
```
