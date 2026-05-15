---
{
  "projection_kind": "taulib_declaration",
  "title": "denotational_lt_trans",
  "permalink": "/corpus/taulib/docs/book-i-denotation-order/denotational-lt-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::denotational_lt_trans",
  "declaration_slug": "denotational-lt-trans",
  "kind": "theorem",
  "name": "denotational_lt_trans",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/corpus/taulib/docs/book-i-denotation-order/",
  "source_line_start": 60,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L60-L71",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L60-L71",
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
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L60-L71)
- Source range: L60-L71
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Transitivity. -/
```

## Source Excerpt

```lean
theorem denotational_lt_trans {x y z : TauObj}
    (h1 : denotational_lt x y) (h2 : denotational_lt y z) :
    denotational_lt x z := by
  cases h1 with
  | inl h1 =>
    cases h2 with
    | inl h2 => exact Or.inl (Nat.lt_trans h1 h2)
    | inr h2 => exact Or.inl (h2.1 ▸ h1)
  | inr h1 =>
    cases h2 with
    | inl h2 => exact Or.inl (h1.1 ▸ h2)
    | inr h2 => exact Or.inr ⟨h1.1.trans h2.1, Nat.lt_trans h1.2 h2.2⟩
```
