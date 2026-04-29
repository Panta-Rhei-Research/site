---
{
  "projection_kind": "taulib_declaration",
  "title": "equiv_iff_toRat_eq",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-to-rat-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::equiv_iff_toRat_eq",
  "declaration_slug": "equiv-iff-to-rat-eq",
  "kind": "theorem",
  "name": "equiv_iff_toRat_eq",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 115,
  "source_line_end": 133,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L115-L133",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L115-L133",
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
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L115-L133)
- Source range: L115-L133
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauRat.equiv is equivalent to Rat equality of toRat values. -/
```

## Source Excerpt

```lean
theorem equiv_iff_toRat_eq (a b : TauRat) :
    TauRat.equiv a b ↔ a.toRat = b.toRat := by
  rw [TauRat.equiv_iff_int_cross]
  constructor
  · intro h
    simp only [TauRat.toRat]
    have ha_ne : (a.den : Rat) ≠ 0 := a.den_ne_zero_rat
    have hb_ne : (b.den : Rat) ≠ 0 := b.den_ne_zero_rat
    rw [div_eq_div_iff ha_ne hb_ne]
    have h_rat : (a.num.toInt : Rat) * (b.den : Rat) =
                 (b.num.toInt : Rat) * (a.den : Rat) := by
      exact_mod_cast h
    linear_combination h_rat
  · intro h
    simp only [TauRat.toRat] at h
    have ha_ne : (a.den : Rat) ≠ 0 := a.den_ne_zero_rat
    have hb_ne : (b.den : Rat) ≠ 0 := b.den_ne_zero_rat
    rw [div_eq_div_iff ha_ne hb_ne] at h
    exact_mod_cast h
```
