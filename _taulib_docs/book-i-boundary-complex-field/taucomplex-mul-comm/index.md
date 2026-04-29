---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_mul_comm",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_mul_comm",
  "declaration_slug": "taucomplex-mul-comm",
  "kind": "theorem",
  "name": "taucomplex_mul_comm",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 157,
  "source_line_end": 175,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L157-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L157-L175",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L157-L175)
- Source range: L157-L175
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Multiplication is commutative.
    Re: ac - bd = ca - db. Im: ad + bc = cb + da. -/
```

## Source Excerpt

```lean
theorem taucomplex_mul_comm (a b : TauComplex) :
    TauComplex.equiv (TauComplex.mul a b) (TauComplex.mul b a) := by
  constructor
  · -- Real part: sub(mul(a.re, b.re), mul(a.im, b.im)) ≡ sub(mul(b.re, a.re), mul(b.im, a.im))
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauReal.sub, TauReal.add, TauReal.mul, TauReal.negate]
    simp only [TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat]
    push_cast; try ring
  · -- Imaginary part: add(mul(a.re, b.im), mul(a.im, b.re)) ≡ add(mul(b.re, a.im), mul(b.im, a.re))
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauReal.add, TauReal.mul]
    simp only [TauRat.equiv, TauRat.add, TauRat.mul]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_fromNat]
    push_cast; try ring
```
