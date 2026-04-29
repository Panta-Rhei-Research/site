---
{
  "projection_kind": "taulib_declaration",
  "title": "not_dvd_succ_of_ge_two",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/not-dvd-succ-of-ge-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::not_dvd_succ_of_ge_two",
  "declaration_slug": "not-dvd-succ-of-ge-two",
  "kind": "theorem",
  "name": "not_dvd_succ_of_ge_two",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 207,
  "source_line_end": 223,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L207-L223",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L207-L223",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L207-L223)
- Source range: L207-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If g ≥ 2 divides both a and a+1, contradiction. -/
```

## Source Excerpt

```lean
private theorem not_dvd_succ_of_ge_two {g a : Nat} (hg : g ≥ 2)
    (h1 : g ∣ a) (h2 : g ∣ a + 1) : False := by
  obtain ⟨j, rfl⟩ := h1      -- a = g * j
  obtain ⟨k, hk⟩ := h2        -- g * j + 1 = g * k
  -- k > j (else g*k ≤ g*j < g*j+1)
  suffices hgt : k > j by
    -- k ≤ j (else g*(j+1) ≤ g*k but g*(j+1) = g*j+g > g*j+1 = g*k)
    suffices hle : k ≤ j from absurd hgt (by omega)
    suffices ¬(j + 1 ≤ k) by omega
    intro hjk
    have h_mul : g * (j + 1) ≤ g * k := Nat.mul_le_mul_left g hjk
    have h_succ : g * (j + 1) = g * j + g := Nat.mul_succ g j
    omega
  suffices ¬(k ≤ j) by omega
  intro hkj
  have : g * k ≤ g * j := Nat.mul_le_mul_left g hkj
  omega
```
