---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_earned_from_rho",
  "permalink": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/sieve-earned-from-rho/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::sieve_earned_from_rho",
  "declaration_slug": "sieve-earned-from-rho",
  "kind": "theorem",
  "name": "sieve_earned_from_rho",
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 136,
  "source_line_end": 142,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L136-L142",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L136-L142",
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/verify/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L136-L142)
- Source range: L136-L142
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Earned Sieve Principle: the prime enumeration is computable
    using only the earned predicate is_prime_bool, which chains through
    the fold hierarchy: is_prime_bool → idx_divides → idx_mul →
    idx_add → iter_rho → ρ.
    Ground truth: chunk_0060 (UR-ITER). -/
```

## Source Excerpt

```lean
theorem sieve_earned_from_rho :
    (∀ k, ∃ p, p = nthPrime k) ∧
    (∀ n, ∃ c, c = prime_count n) ∧
    (∀ p, ∃ k, k = prime_index p) :=
  ⟨fun k => ⟨nthPrime k, rfl⟩,
   fun n => ⟨prime_count n, rfl⟩,
   fun p => ⟨prime_index p, rfl⟩⟩
```
