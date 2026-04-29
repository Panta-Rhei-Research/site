---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.equiv_iff_int_cross",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-int-cross/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::TauRat.equiv_iff_int_cross",
  "declaration_slug": "equiv-iff-int-cross",
  "kind": "theorem",
  "name": "TauRat.equiv_iff_int_cross",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 102,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L102-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatField",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L102-L112",
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

- Module: [TauLib.BookI.Boundary.TauRatField](/verify/taulib/docs/book-i-boundary-tau-rat-field/)
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L102-L112)
- Source range: L102-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Convert TauRat.equiv to a clean cross-multiplication identity in ℤ.
    This is the workhorse lemma. -/
```

## Source Excerpt

```lean
theorem TauRat.equiv_iff_int_cross (a b : TauRat) :
    TauRat.equiv a b ↔
    a.num.toInt * (b.den : Int) = b.num.toInt * (a.den : Int) := by
  constructor
  · intro h
    have := (equiv_iff_toInt_eq _ _).mp h
    simpa [toInt_mul, toInt_fromNat] using this
  · intro h
    simp only [TauRat.equiv]
    rw [equiv_iff_toInt_eq, toInt_mul, toInt_mul, toInt_fromNat, toInt_fromNat]
    exact h
```
