---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_hyp_5",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/crt-hyp-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::crt_hyp_5",
  "declaration_slug": "crt-hyp-5",
  "kind": "theorem",
  "name": "crt_hyp_5",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 209,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L209-L221",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L209-L221",
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
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L209-L221)
- Source range: L209-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem crt_hyp_5 : CRTHyp 5 where
  all_prime := all_primes_lt_5
  pairwise_coprime := by
    intro i j hi hj hij
    have hne : nth_prime (i + 1) ≠ nth_prime (j + 1) := by
      have hi5 : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 ∨ i = 4 := by
        simp only [TauIdx] at *; omega
      have hj5 : j = 0 ∨ j = 1 ∨ j = 2 ∨ j = 3 ∨ j = 4 := by
        simp only [TauIdx] at *; omega
      rcases hi5 with rfl | rfl | rfl | rfl | rfl <;>
        rcases hj5 with rfl | rfl | rfl | rfl | rfl <;>
        first | exact absurd rfl hij | native_decide
    exact distinct_primes_coprime (all_primes_lt_5 i hi) (all_primes_lt_5 j hj) hne
```
