---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_i_squared",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-i-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_i_squared",
  "declaration_slug": "taucomplex-i-squared",
  "kind": "theorem",
  "name": "taucomplex_i_squared",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 107,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L107-L128",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ComplexField",
        "url": "/verify/taulib/docs/book-i-boundary-complex-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L107-L128",
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

- Module: [TauLib.BookI.Boundary.ComplexField](/verify/taulib/docs/book-i-boundary-complex-field/)
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L107-L128)
- Source range: L107-L128
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The defining relation of the complex field: i² = -1.
    mul(0,1)(0,1) = (0*0 - 1*1, 0*1 + 1*0) = (-1, 0) = negate(1, 0). -/
```

## Source Excerpt

```lean
theorem taucomplex_i_squared :
    TauComplex.equiv (TauComplex.mul TauComplex.i_unit TauComplex.i_unit)
                     (TauComplex.negate TauComplex.one) := by
  constructor
  · -- Real part: sub(mul(0,0), mul(1,1)) ≡ negate(1) i.e. 0*0 - 1*1 ≡ -1
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.i_unit, TauComplex.negate, TauComplex.one,
               TauReal.sub, TauReal.add, TauReal.mul, TauReal.negate, TauReal.zero, TauReal.one]
    simp only [TauRat.equiv, TauRat.add, TauRat.mul, TauRat.negate, TauRat.zero, TauRat.one]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat, toInt_zero, toInt_one]
    push_cast; try ring
  · -- Imaginary part: add(mul(0,1), mul(1,0)) ≡ negate(0) i.e. 0*1 + 1*0 ≡ 0
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.i_unit, TauComplex.negate, TauComplex.one,
               TauReal.add, TauReal.mul, TauReal.negate, TauReal.zero, TauReal.one]
    simp only [TauRat.equiv, TauRat.add, TauRat.mul, TauRat.negate, TauRat.zero, TauRat.one]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat, toInt_zero, toInt_one]
    push_cast; try ring
```
