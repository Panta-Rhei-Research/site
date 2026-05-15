---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_fuel_ok",
  "permalink": "/corpus/taulib/docs/book-i-polarity-nth-prime/nth-prime-fuel-ok/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::nth_prime_fuel_ok",
  "declaration_slug": "nth-prime-fuel-ok",
  "kind": "def",
  "name": "nth_prime_fuel_ok",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/corpus/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 121,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L121-L122",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L121-L122",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L121-L122)
- Source range: L121-L122
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Boolean fuel-sufficiency check for nth_prime. -/
```

## Source Excerpt

```lean
def nth_prime_fuel_ok (k : Nat) : Bool :=
  k == 0 || decide (count_primes_in 1 (1 + (k * k * 10 + 10)) ≥ k)
```
