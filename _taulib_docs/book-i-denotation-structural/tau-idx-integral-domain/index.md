---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_integral_domain",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-integral-domain/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_integral_domain",
  "declaration_slug": "tau-idx-integral-domain",
  "kind": "theorem",
  "name": "tauIdx_integral_domain",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 132,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L132-L150",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L132-L150",
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

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L132-L150)
- Source range: L132-L150
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Integral domain property**: the product of two τ-Idx values is zero
    iff at least one factor is zero.  Equivalently: positive × positive = positive.
    There is no "annihilation" except through the vacuous zero. -/
```

## Source Excerpt

```lean
theorem tauIdx_integral_domain (n m : TauIdx) :
    idx_mul n m = 0 ↔ n = 0 ∨ m = 0 := by
  simp only [idx_mul_eq_nat_mul]
  constructor
  · intro h
    -- Forward: n * m = 0 → n = 0 ∨ m = 0 (contrapositive via Nat.mul_pos)
    cases Nat.eq_zero_or_pos n with
    | inl hn => exact Or.inl hn
    | inr hn =>
      cases Nat.eq_zero_or_pos m with
      | inl hm => exact Or.inr hm
      | inr hm =>
        have hpos := Nat.mul_pos hn hm
        rw [h] at hpos
        exact absurd hpos (Nat.lt_irrefl 0)
  · intro h
    cases h with
    | inl h => subst h; simp
    | inr h => subst h; simp
```
