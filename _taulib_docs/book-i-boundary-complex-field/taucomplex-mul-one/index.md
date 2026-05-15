---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_mul_one",
  "permalink": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_mul_one",
  "declaration_slug": "taucomplex-mul-one",
  "kind": "theorem",
  "name": "taucomplex_mul_one",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 201,
  "source_line_end": 222,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L201-L222",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ComplexField",
        "url": "/corpus/taulib/docs/book-i-boundary-complex-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L201-L222",
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

- Module: [TauLib.BookI.Boundary.ComplexField](/corpus/taulib/docs/book-i-boundary-complex-field/)
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L201-L222)
- Source range: L201-L222
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- One is a right identity for multiplication: z * 1 = z. -/
```

## Source Excerpt

```lean
theorem taucomplex_mul_one (a : TauComplex) :
    TauComplex.equiv (TauComplex.mul a TauComplex.one) a := by
  constructor
  · -- Real part: a.re * 1 - a.im * 0 ≡ a.re
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.one, TauReal.sub, TauReal.add, TauReal.mul,
               TauReal.negate, TauReal.one, TauReal.zero]
    simp only [TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate,
               TauRat.one, TauRat.zero]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat, toInt_zero, toInt_one]
    push_cast; try ring
  · -- Imaginary part: a.re * 0 + a.im * 1 ≡ a.im
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.one, TauReal.add, TauReal.mul,
               TauReal.one, TauReal.zero]
    simp only [TauRat.equiv, TauRat.add, TauRat.mul, TauRat.one, TauRat.zero]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_fromNat, toInt_zero, toInt_one]
    push_cast; try ring
```
