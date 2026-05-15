---
{
  "projection_kind": "taulib_declaration",
  "title": "count_primes_in_unfold",
  "permalink": "/corpus/taulib/docs/book-i-polarity-nth-prime/count-primes-in-unfold/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::count_primes_in_unfold",
  "declaration_slug": "count-primes-in-unfold",
  "kind": "theorem",
  "name": "count_primes_in_unfold",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/corpus/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 36,
  "source_line_end": 40,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L36-L40",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.NthPrime",
        "url": "/corpus/taulib/docs/book-i-polarity-nth-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L36-L40",
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

- Module: [TauLib.BookI.Polarity.NthPrime](/corpus/taulib/docs/book-i-polarity-nth-prime/)
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L36-L40)
- Source range: L36-L40
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
private theorem count_primes_in_unfold (lo hi : Nat) :
    count_primes_in lo hi =
    if lo ≥ hi then 0
    else (if is_prime_bool (lo + 1) then 1 else 0) + count_primes_in (lo + 1) hi :=
  count_primes_in.eq_1 lo hi
```
