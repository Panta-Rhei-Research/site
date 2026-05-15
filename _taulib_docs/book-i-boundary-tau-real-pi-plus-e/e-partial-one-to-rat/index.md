---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.e_partial_one_toRat",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/e-partial-one-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauRat.e_partial_one_toRat",
  "declaration_slug": "e-partial-one-to-rat",
  "kind": "theorem",
  "name": "TauRat.e_partial_one_toRat",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 114,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L114-L120",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L114-L120",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L114-L120)
- Source range: L114-L120
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `e_partial 1 = 1` at the `toRat` level. -/
```

## Source Excerpt

```lean
theorem TauRat.e_partial_one_toRat :
    (TauRat.e_partial 1).toRat = 1 := by
  show (TauRat.sum TauRat.e_term 1).toRat = 1
  rw [TauRat.sum_succ, toRat_add, TauRat.sum_zero, toRat_zero]
  rw [TauRat.e_term_toRat]
  -- goal: 0 + 1 / (Nat.factorial 0 : Rat) = 1
  simp [Nat.factorial]
```
