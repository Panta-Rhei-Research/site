---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_pairwise_coprime",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/nth-prime-pairwise-coprime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::nth_prime_pairwise_coprime",
  "declaration_slug": "nth-prime-pairwise-coprime",
  "kind": "theorem",
  "name": "nth_prime_pairwise_coprime",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 188,
  "source_line_end": 194,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L188-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L188-L194",
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
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L188-L194)
- Source range: L188-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pairwise coprimality from primality and distinctness. -/
```

## Source Excerpt

```lean
theorem nth_prime_pairwise_coprime {k : TauIdx}
    (hprimes : ∀ i, i < k → idx_prime (nth_prime (i + 1)))
    (hdistinct : ∀ i j, i < k → j < k → i ≠ j → nth_prime (i + 1) ≠ nth_prime (j + 1)) :
    ∀ i j, i < k → j < k → i ≠ j →
    Nat.Coprime (nth_prime (i + 1)) (nth_prime (j + 1)) :=
  fun i j hi hj hij =>
    distinct_primes_coprime (hprimes i hi) (hprimes j hj) (hdistinct i j hi hj hij)
```
