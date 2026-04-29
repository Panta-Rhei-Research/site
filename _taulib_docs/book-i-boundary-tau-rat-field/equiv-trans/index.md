---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.equiv_trans",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-field/equiv-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::TauRat.equiv_trans",
  "declaration_slug": "equiv-trans",
  "kind": "theorem",
  "name": "TauRat.equiv_trans",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 59,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L59-L76",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L59-L76",
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
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L59-L76)
- Source range: L59-L76
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauRat equivalence is transitive.  This was missing from NumberTower.lean
    where only `equiv_refl` and `equiv_symm` were proved.

    Strategy: convert all three TauInt-equivs to integer equalities via
    `equiv_iff_toInt_eq`, then use the cross-multiplication identity
    via `linear_combination`. -/
```

## Source Excerpt

```lean
theorem TauRat.equiv_trans {a b c : TauRat}
    (hab : TauRat.equiv a b) (hbc : TauRat.equiv b c) :
    TauRat.equiv a c := by
  -- Unfold and convert to Int equalities
  simp only [TauRat.equiv] at *
  rw [equiv_iff_toInt_eq] at *
  simp only [toInt_mul, toInt_fromNat] at *
  -- Now: hab: a.num.toInt * b.den = b.num.toInt * a.den
  --      hbc: b.num.toInt * c.den = c.num.toInt * b.den
  -- Goal: a.num.toInt * c.den = c.num.toInt * a.den
  -- Cancel b.den (which is positive).
  have hb_pos : (b.den : Int) > 0 := by exact_mod_cast b.den_pos
  have hb_ne : (b.den : Int) ≠ 0 := ne_of_gt hb_pos
  have key :
      (a.num.toInt * (c.den : Int)) * (b.den : Int) =
      (c.num.toInt * (a.den : Int)) * (b.den : Int) := by
    linear_combination (c.den : Int) * hab + (a.den : Int) * hbc
  exact mul_right_cancel₀ hb_ne key
```
