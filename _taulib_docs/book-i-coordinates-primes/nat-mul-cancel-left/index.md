---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_mul_cancel_left",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/nat-mul-cancel-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::nat_mul_cancel_left",
  "declaration_slug": "nat-mul-cancel-left",
  "kind": "theorem",
  "name": "nat_mul_cancel_left",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 323,
  "source_line_end": 334,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L323-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L323-L334",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L323-L334)
- Source range: L323-L334
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Nat multiplication left cancellation. -/
```

## Source Excerpt

```lean
private theorem nat_mul_cancel_left {a b c : Nat} (ha : a > 0)
    (h : a * b = a * c) : b = c := by
  rcases Nat.lt_or_ge b c with hbc | hbc
  · -- b < c: a*(b+1) ≤ a*c, but a*(b+1) = a*b + a > a*b = a*c
    have h1 := Nat.mul_le_mul_left a hbc
    have h2 : a * Nat.succ b = a * b + a := Nat.mul_succ a b
    omega
  · rcases Nat.lt_or_ge c b with hcb | hcb
    · have h1 := Nat.mul_le_mul_left a hcb
      have h2 : a * Nat.succ c = a * c + a := Nat.mul_succ a c
      omega
    · omega
```
