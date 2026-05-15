---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_dvd_mul_of_dvd",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-primes/nat-dvd-mul-of-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::nat_dvd_mul_of_dvd",
  "declaration_slug": "nat-dvd-mul-of-dvd",
  "kind": "theorem",
  "name": "nat_dvd_mul_of_dvd",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 34,
  "source_line_end": 36,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L34-L36",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Primes",
        "url": "/corpus/taulib/docs/book-i-coordinates-primes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L34-L36",
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

- Module: [TauLib.BookI.Coordinates.Primes](/corpus/taulib/docs/book-i-coordinates-primes/)
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L34-L36)
- Source range: L34-L36
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
private theorem nat_dvd_mul_of_dvd {a b : Nat} (h : a ∣ b) (c : Nat) : a ∣ c * b := by
  obtain ⟨k, rfl⟩ := h
  exact ⟨c * k, by rw [← Nat.mul_assoc, Nat.mul_comm c a, Nat.mul_assoc]⟩
```
