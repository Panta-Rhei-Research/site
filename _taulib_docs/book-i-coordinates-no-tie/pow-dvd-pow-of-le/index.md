---
{
  "projection_kind": "taulib_declaration",
  "title": "pow_dvd_pow_of_le",
  "permalink": "/verify/taulib/docs/book-i-coordinates-no-tie/pow-dvd-pow-of-le/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::pow_dvd_pow_of_le",
  "declaration_slug": "pow-dvd-pow-of-le",
  "kind": "theorem",
  "name": "pow_dvd_pow_of_le",
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/verify/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 53,
  "source_line_end": 54,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L53-L54",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NoTie",
        "url": "/verify/taulib/docs/book-i-coordinates-no-tie/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L53-L54",
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

- Module: [TauLib.BookI.Coordinates.NoTie](/verify/taulib/docs/book-i-coordinates-no-tie/)
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L53-L54)
- Source range: L53-L54
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- a^m divides a^n when m ≤ n. -/
```

## Source Excerpt

```lean
theorem pow_dvd_pow_of_le (a : Nat) {m n : Nat} (h : m ≤ n) : a ^ m ∣ a ^ n := by
  exact ⟨a ^ (n - m), by rw [← Nat.pow_add a m (n - m), Nat.add_sub_cancel' h]⟩
```
