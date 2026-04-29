---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_prime_of_fuel",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/nth-prime-prime-of-fuel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::nth_prime_prime_of_fuel",
  "declaration_slug": "nth-prime-prime-of-fuel",
  "kind": "theorem",
  "name": "nth_prime_prime_of_fuel",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 125,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L125-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L125-L134",
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
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L125-L134)
- Source range: L125-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- When fuel suffices, nth_prime k is prime. -/
```

## Source Excerpt

```lean
theorem nth_prime_prime_of_fuel {k : TauIdx} (hk : k ≥ 1)
    (hfuel : count_primes_in 1 (1 + (k * k * 10 + 10)) ≥ k) :
    idx_prime (nth_prime k) := by
  have hk0 : k ≠ 0 := by simp only [TauIdx] at *; omega
  unfold nth_prime; rw [if_neg hk0]
  have h := nth_prime_go_is_prime k 0 1 (k * k * 10 + 10)
    hk (Nat.zero_le k)
    (fun h => absurd h (by simp only [TauIdx] at *; omega))
    hfuel
  exact (is_prime_bool_iff _).mp h
```
