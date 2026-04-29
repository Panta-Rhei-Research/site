---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_partial_one_toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-partial-one-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauRat.pi_partial_one_toRat",
  "declaration_slug": "pi-partial-one-to-rat",
  "kind": "theorem",
  "name": "TauRat.pi_partial_one_toRat",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 102,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L102-L111",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L102-L111",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L102-L111)
- Source range: L102-L111
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `pi_partial 1 = 8/3` at the `toRat` level. -/
```

## Source Excerpt

```lean
theorem TauRat.pi_partial_one_toRat :
    (TauRat.pi_partial 1).toRat = 8 / 3 := by
  show (TauRat.sum TauRat.pi_pair_term 1).toRat = 8 / 3
  -- sum f 1 = sum f 0 + f 0 = 0 + f 0
  rw [TauRat.sum_succ, toRat_add, TauRat.sum_zero, toRat_zero]
  -- goal: 0 + (pi_pair_term 0).toRat = 8/3
  rw [TauRat.pi_pair_term_toRat]
  -- 0 + 8 / (((4*0+1)*(4*0+3) : Nat) : Rat) = 8/3
  push_cast
  norm_num
```
