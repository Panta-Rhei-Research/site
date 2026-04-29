---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_go_is_prime",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/nth-prime-go-is-prime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::nth_prime_go_is_prime",
  "declaration_slug": "nth-prime-go-is-prime",
  "kind": "theorem",
  "name": "nth_prime_go_is_prime",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 73,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L73-L114",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.NthPrime",
        "url": "/verify/taulib/docs/book-i-polarity-nth-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L73-L114",
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

- Module: [TauLib.BookI.Polarity.NthPrime](/verify/taulib/docs/book-i-polarity-nth-prime/)
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L73-L114)
- Source range: L73-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If fuel contains enough primes, nth_prime_go returns a value that
    passes is_prime_bool.

    Invariant: count = target → is_prime_bool cur = true.
    This propagates cleanly:
    - When count < target and next is prime: count+1 = target → is_prime_bool next (trivially true)
    - When count < target and next is NOT prime: count = target → ... (vacuously true since count < target)
    - When count = target: function returns cur, and invariant gives primality. -/
```

## Source Excerpt

```lean
theorem nth_prime_go_is_prime
    (target count cur fuel : Nat)
    (h_target : target ≥ 1)
    (h_le : count ≤ target)
    (h_inv : count = target → is_prime_bool cur = true)
    (h_fuel : count_primes_in cur (cur + fuel) ≥ target - count) :
    is_prime_bool (nth_prime_go target count cur fuel) = true := by
  induction fuel generalizing count cur with
  | zero =>
    -- fuel = 0: count_primes_in cur cur = 0 ≥ target - count forces count = target
    rw [Nat.add_zero] at h_fuel
    rw [count_primes_in_empty] at h_fuel
    have hcount_eq : count = target := by omega
    unfold nth_prime_go; simp
    exact h_inv hcount_eq
  | succ n ih =>
    unfold nth_prime_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · -- count == target: return cur
      rename_i hbeq
      exact h_inv (beq_iff_eq.mp hbeq)
    · -- count ≠ target
      rename_i hbeq
      have hne : count ≠ target := fun heq => hbeq (beq_iff_eq.mpr heq)
      have hlt : count < target := by omega
      have hcur_lt : cur < cur + (n + 1) := by omega
      have hshift : cur + (n + 1) = cur + 1 + n := by omega
      split
      · -- is_prime_bool (cur + 1) = true
        rename_i hp
        have hstep := count_primes_in_step_prime cur (cur + (n + 1)) hcur_lt hp
        rw [hshift] at hstep h_fuel
        -- ih : ∀ (count cur : Nat), count ≤ target → (count = target → ...) → fuel_hyp → ...
        exact ih (count + 1) (cur + 1) (by omega) (fun _ => hp) (by omega)
      · -- is_prime_bool (cur + 1) = false
        rename_i hp
        have hnp : is_prime_bool (cur + 1) = false := by
          revert hp; cases is_prime_bool (cur + 1) <;> simp
        have hstep := count_primes_in_step_not cur (cur + (n + 1)) hcur_lt hnp
        rw [hshift] at hstep h_fuel
        exact ih count (cur + 1) h_le (fun heq => absurd heq hne) (by omega)
```
