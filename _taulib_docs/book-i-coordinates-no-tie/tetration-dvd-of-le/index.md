---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_dvd_of_le",
  "permalink": "/verify/taulib/docs/book-i-coordinates-no-tie/tetration-dvd-of-le/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::tetration_dvd_of_le",
  "declaration_slug": "tetration-dvd-of-le",
  "kind": "theorem",
  "name": "tetration_dvd_of_le",
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/verify/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 57,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L57-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L57-L61",
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
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L57-L61)
- Source range: L57-L61
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Higher tetrations divide lower tetrations (for c ≥ 1, both are powers of A). -/
```

## Source Excerpt

```lean
theorem tetration_dvd_of_le (a : Nat) (ha : a ≥ 2) {c1 c2 : Nat}
    (hc1 : c1 ≥ 1) (hc2 : c2 ≥ 1) (h : c1 ≤ c2) :
    tetration a c1 ∣ tetration a c2 := by
  rw [tetration_as_pow a c1 hc1, tetration_as_pow a c2 hc2]
  exact pow_dvd_pow_of_le a (tetration_mono a ha (Nat.sub_le_sub_right h 1))
```
