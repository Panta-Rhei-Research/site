---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.abs_equiv_zero_iff_equiv_zero",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/abs-equiv-zero-iff-equiv-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::TauRat.abs_equiv_zero_iff_equiv_zero",
  "declaration_slug": "abs-equiv-zero-iff-equiv-zero",
  "kind": "theorem",
  "name": "TauRat.abs_equiv_zero_iff_equiv_zero",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 133,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L133-L144",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatAbs",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L133-L144",
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

- Module: [TauLib.BookI.Boundary.TauRatAbs](/verify/taulib/docs/book-i-boundary-tau-rat-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L133-L144)
- Source range: L133-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `abs q` is equiv to zero iff `q` is equiv to zero. -/
```

## Source Excerpt

```lean
theorem TauRat.abs_equiv_zero_iff_equiv_zero (q : TauRat) :
    TauRat.equiv q.abs TauRat.zero ↔ TauRat.equiv q TauRat.zero := by
  rw [equiv_iff_toRat_eq, equiv_iff_toRat_eq, toRat_zero]
  by_cases h : 0 ≤ q.toRat
  · rw [toRat_abs_of_nonneg h]
  · push_neg at h
    rw [toRat_abs_of_neg h]
    constructor
    · intro h_neg_zero
      linarith
    · intro h_zero
      rw [h_zero, neg_zero]
```
