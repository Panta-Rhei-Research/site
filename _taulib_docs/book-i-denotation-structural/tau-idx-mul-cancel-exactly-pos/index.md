---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_mul_cancel_exactly_pos",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-mul-cancel-exactly-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_mul_cancel_exactly_pos",
  "declaration_slug": "tau-idx-mul-cancel-exactly-pos",
  "kind": "theorem",
  "name": "tauIdx_mul_cancel_exactly_pos",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 203,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L203-L230",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L203-L230",
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
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L203-L230)
- Source range: L203-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The characterization theorem**: multiplicative cancellation holds for n
    if and only if n > 0.  This makes the single zero-sensitive locus maximally explicit.

    Read as: "zero is the unique obstruction to multiplicative cancellation in τ-Idx." -/
```

## Source Excerpt

```lean
theorem tauIdx_mul_cancel_exactly_pos (n : TauIdx) :
    (∀ a b, idx_mul n a = idx_mul n b → a = b) ↔ n > 0 := by
  constructor
  · -- Forward: if n cancels universally, then n > 0
    intro h
    cases Nat.eq_zero_or_pos n with
    | inr hn => exact hn
    | inl hn =>
      -- n = 0: derive contradiction from 0*1 = 0*2 but 1 ≠ 2
      subst hn
      exact absurd (h 1 2 (by simp [idx_mul_eq_nat_mul])) (by decide)
  · -- Backward: if n > 0, then n cancels (from idx_mul_injective)
    intro hn a b hab
    exact idx_mul_injective n hn hab

-- ============================================================
-- SECTION 5: OMEGA AS DYNAMICAL ABSORBER
-- ============================================================

/-! ## Section 5: Omega as Dynamical Absorber

Omega (ω) is the *one-point compactification* of the positive naturals N⁺.
It absorbs the dynamical iterator ρ (fixed point by K2), but it does NOT
absorb algebraic operations (multiplication).  This is the τ-analog of
∞ in N⁺ ∪ {∞}: omega is a topological/dynamical limit, not an algebraic zero.

Key contrast with standard Nat: Nat has 0 as algebraic absorber (0 × n = 0).
τ has ω as dynamical absorber (ρ(ω) = ω).  These are structurally orthogonal. -/
```
