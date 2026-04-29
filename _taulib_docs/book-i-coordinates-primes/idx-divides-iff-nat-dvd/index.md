---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_divides_iff_nat_dvd",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-iff-nat-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::idx_divides_iff_nat_dvd",
  "declaration_slug": "idx-divides-iff-nat-dvd",
  "kind": "theorem",
  "name": "idx_divides_iff_nat_dvd",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 46,
  "source_line_end": 52,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L46-L52",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L46-L52",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L46-L52)
- Source range: L46-L52
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bridge: idx_divides ↔ Nat.dvd. -/
```

## Source Excerpt

```lean
theorem idx_divides_iff_nat_dvd (a b : TauIdx) : idx_divides a b ↔ a ∣ b := by
  constructor
  · rintro ⟨k, hk⟩; exact ⟨k, by rw [idx_mul_eq_nat_mul] at hk; exact hk⟩
  · rintro ⟨k, hk⟩; exact ⟨k, by rw [idx_mul_eq_nat_mul]; exact hk⟩

instance instDecidableIdxDivides (a b : TauIdx) : Decidable (idx_divides a b) :=
  decidable_of_iff (a ∣ b) (idx_divides_iff_nat_dvd a b).symm
```
