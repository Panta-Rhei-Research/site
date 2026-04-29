---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_product_exists",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/prime-product-exists/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::prime_product_exists",
  "declaration_slug": "prime-product-exists",
  "kind": "theorem",
  "name": "prime_product_exists",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 243,
  "source_line_end": 273,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L243-L273",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L243-L273",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L243-L273)
- Source range: L243-L273
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every n ≥ 2 is a product of primes. -/
```

## Source Excerpt

```lean
theorem prime_product_exists (n : TauIdx) (hn : n ≥ 2) :
    ∃ ps : List TauIdx, (∀ p ∈ ps, idx_prime p) ∧ list_prod ps = n := by
  induction n using Nat.strongRecOn with
  | _ n ih =>
    obtain ⟨p, hp, hpn⟩ := exists_prime_divisor n hn
    obtain ⟨m, hm⟩ := hpn
    by_cases hm1 : m = 1
    · -- n = p * 1 = p
      refine ⟨[n], fun q hq => ?_, by simp [list_prod]⟩
      simp at hq; rw [hq, hm, hm1, Nat.mul_one]; exact hp
    · -- m ≥ 2
      have hm0 : m ≠ 0 := by
        intro heq; subst heq
        simp only [Nat.mul_zero] at hm
        simp only [TauIdx] at hn hm; omega
      have hm_ge2 : m ≥ 2 := by
        rcases m with _ | _ | m
        · exact absurd rfl hm0
        · exact absurd rfl hm1
        · exact Nat.le_add_left 2 m
      have hm_lt : m < n := by
        rw [hm]
        have hp2 := hp.1
        have : 2 * m ≤ p * m := Nat.mul_le_mul_right m hp2
        simp only [TauIdx] at *; omega
      obtain ⟨ps, hps, hprod⟩ := ih m hm_lt hm_ge2
      exact ⟨p :: ps, fun q hq => by
        simp at hq; rcases hq with rfl | hq
        · exact hp
        · exact hps q hq,
        by simp [list_prod, hprod, hm]⟩
```
