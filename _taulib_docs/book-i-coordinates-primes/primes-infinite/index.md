---
{
  "projection_kind": "taulib_declaration",
  "title": "primes_infinite",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/primes-infinite/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::primes_infinite",
  "declaration_slug": "primes-infinite",
  "kind": "theorem",
  "name": "primes_infinite",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 226,
  "source_line_end": 232,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L226-L232",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L226-L232",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L226-L232)
- Source range: L226-L232
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For every n, there exists a prime p > n. -/
```

## Source Excerpt

```lean
theorem primes_infinite (n : TauIdx) : ∃ p, idx_prime p ∧ p > n := by
  have hm2 : idx_factorial n + 1 ≥ 2 := Nat.succ_le_succ (idx_factorial_pos n)
  obtain ⟨p, hp, hpdvd⟩ := exists_prime_divisor (idx_factorial n + 1) hm2
  refine ⟨p, hp, ?_⟩
  suffices ¬(p ≤ n) by simp only [TauIdx] at *; omega
  intro hle
  exact not_dvd_succ_of_ge_two hp.1 (prime_dvd_factorial hp hle) hpdvd
```
