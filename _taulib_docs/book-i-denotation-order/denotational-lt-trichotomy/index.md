---
{
  "projection_kind": "taulib_declaration",
  "title": "denotational_lt_trichotomy",
  "permalink": "/verify/taulib/docs/book-i-denotation-order/denotational-lt-trichotomy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::denotational_lt_trichotomy",
  "declaration_slug": "denotational-lt-trichotomy",
  "kind": "theorem",
  "name": "denotational_lt_trichotomy",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/verify/taulib/docs/book-i-denotation-order/",
  "source_line_start": 74,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L74-L93",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Order",
        "url": "/verify/taulib/docs/book-i-denotation-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L74-L93",
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

- Module: [TauLib.BookI.Denotation.Order](/verify/taulib/docs/book-i-denotation-order/)
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L74-L93)
- Source range: L74-L93
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Trichotomy: for any two TauObj, exactly one of <, =, > holds. -/
```

## Source Excerpt

```lean
theorem denotational_lt_trichotomy (x y : TauObj) :
    denotational_lt x y ∨ x = y ∨ denotational_lt y x := by
  cases x with | mk sx dx =>
  cases y with | mk sy dy =>
  simp only [denotational_lt]
  by_cases h_seed : sx.toNat < sy.toNat
  · exact Or.inl (Or.inl h_seed)
  · by_cases h_seed_eq : sx = sy
    · subst h_seed_eq
      by_cases h_depth : dx < dy
      · exact Or.inl (Or.inr ⟨rfl, h_depth⟩)
      · by_cases h_depth_eq : dx = dy
        · subst h_depth_eq; exact Or.inr (Or.inl rfl)
        · have : dy < dx := by omega
          exact Or.inr (Or.inr (Or.inr ⟨rfl, this⟩))
    · by_cases h_seed2 : sy.toNat < sx.toNat
      · exact Or.inr (Or.inr (Or.inl h_seed2))
      · exfalso
        have : sx.toNat = sy.toNat := by omega
        exact h_seed_eq (Generator.toNat_injective sx sy this)
```
