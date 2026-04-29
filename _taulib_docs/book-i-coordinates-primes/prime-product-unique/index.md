---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_product_unique",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/prime-product-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::prime_product_unique",
  "declaration_slug": "prime-product-unique",
  "kind": "theorem",
  "name": "prime_product_unique",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 359,
  "source_line_end": 407,
  "registry_ids": [
    "I.T09"
  ],
  "related_registry_items": [
    {
      "id": "I.T09",
      "title": "FTA on tau-Idx",
      "url": "/registry/object/I.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L359-L407",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Primes",
        "url": "/verify/taulib/docs/book-i-coordinates-primes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L359-L407",
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

- Module: [TauLib.BookI.Coordinates.Primes](/verify/taulib/docs/book-i-coordinates-primes/)
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L359-L407)
- Source range: L359-L407
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T09` — FTA on tau-Idx

## Immediate Comment / Docstring

```lean
/-- [I.T09] FTA uniqueness: two sorted non-decreasing prime lists
    with the same product are identical. -/
```

## Source Excerpt

```lean
theorem prime_product_unique (ps qs : List TauIdx)
    (hps : ∀ p ∈ ps, idx_prime p) (hqs : ∀ q ∈ qs, idx_prime q)
    (hps_sorted : sorted_nd ps) (hqs_sorted : sorted_nd qs)
    (heq : list_prod ps = list_prod qs) : ps = qs := by
  induction ps generalizing qs with
  | nil =>
    exact (prod_one_implies_nil qs hqs (by simp [list_prod] at heq; exact heq.symm)).symm
  | cons p rest₁ ih =>
    rcases qs with _ | ⟨q, rest₂⟩
    · -- qs empty, ps nonempty: contradiction
      exfalso
      simp only [list_prod] at heq
      have hp : p ≥ 2 := (hps p (by simp)).1
      have hr : list_prod rest₁ ≥ 1 :=
        list_prod_pos_of_primes rest₁ (fun q hq => hps q (List.mem_cons_of_mem p hq))
      have := Nat.mul_le_mul hp hr
      simp only [TauIdx] at *; omega
    · -- Both nonempty: show p = q, then recurse
      have hp_prime : idx_prime p := hps p (by simp)
      have hq_prime : idx_prime q := hqs q (by simp)
      -- p ∈ qs (since p | product of qs)
      have hp_in_qs : p ∈ q :: rest₂ :=
        prime_mem_of_dvd_prod hp_prime hqs (heq ▸ ⟨list_prod rest₁, rfl⟩)
      -- q ∈ ps (since q | product of ps)
      have hq_in_ps : q ∈ p :: rest₁ :=
        prime_mem_of_dvd_prod hq_prime hps (heq ▸ ⟨list_prod rest₂, rfl⟩)
      -- p ≥ q (p ∈ sorted qs, q is head)
      have hp_ge_q : p ≥ q := by
        rcases List.mem_cons.mp hp_in_qs with rfl | hr
        · simp only [TauIdx] at *; omega
        · exact mem_ge_of_all_ge hqs_sorted.1 hr
      -- q ≥ p (q ∈ sorted ps, p is head)
      have hq_ge_p : q ≥ p := by
        rcases List.mem_cons.mp hq_in_ps with rfl | hr
        · simp only [TauIdx] at *; omega
        · exact mem_ge_of_all_ge hps_sorted.1 hr
      -- Therefore p = q
      have hpq : p = q := by simp only [TauIdx] at *; omega
      subst hpq
      -- Cancel p: list_prod rest₁ = list_prod rest₂
      simp only [list_prod] at heq
      have hp_pos : p > 0 := by have := hp_prime.1; simp only [TauIdx] at *; omega
      have h_rest : list_prod rest₁ = list_prod rest₂ := nat_mul_cancel_left hp_pos heq
      -- Inductive step
      have hps_rest : ∀ r ∈ rest₁, idx_prime r :=
        fun r hr => hps r (List.mem_cons_of_mem p hr)
      have hqs_rest : ∀ r ∈ rest₂, idx_prime r :=
        fun r hr => hqs r (List.mem_cons_of_mem p hr)
      exact congrArg (p :: ·) (ih rest₂ hps_rest hqs_rest hps_sorted.2 hqs_sorted.2 h_rest)
```
