---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_dvd_factorial",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/prime-dvd-factorial/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::prime_dvd_factorial",
  "declaration_slug": "prime-dvd-factorial",
  "kind": "theorem",
  "name": "prime_dvd_factorial",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 190,
  "source_line_end": 204,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L190-L204",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L190-L204",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L190-L204)
- Source range: L190-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every prime p ≤ n divides n!. -/
```

## Source Excerpt

```lean
theorem prime_dvd_factorial {p n : TauIdx} (hp : idx_prime p) (hpn : p ≤ n) :
    p ∣ idx_factorial n := by
  induction n with
  | zero =>
    have h2 : p ≥ 2 := hp.1
    have h0 : p ≤ 0 := hpn
    exact absurd (Nat.le_antisymm h0 (Nat.zero_le p))
      (by intro heq; subst heq; exact Nat.not_succ_le_zero 1 h2)
  | succ n ih =>
    simp only [idx_factorial]
    rcases Nat.eq_or_lt_of_le hpn with h | h
    · -- p = n + 1
      subst h; exact nat_dvd_mul_right (n + 1) (idx_factorial n)
    · -- p < n + 1, so p ≤ n
      exact nat_dvd_mul_of_dvd (ih (Nat.lt_succ_iff.mp h)) (n + 1)
```
