---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_left_distrib",
  "permalink": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-left-distrib/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_left_distrib",
  "declaration_slug": "taucomplex-left-distrib",
  "kind": "theorem",
  "name": "taucomplex_left_distrib",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 225,
  "source_line_end": 246,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L225-L246",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L225-L246",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L225-L246)
- Source range: L225-L246
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Left distributivity: a * (b + c) = a*b + a*c. -/
```

## Source Excerpt

```lean
theorem taucomplex_left_distrib (a b c : TauComplex) :
    TauComplex.equiv (TauComplex.mul a (TauComplex.add b c))
                     (TauComplex.add (TauComplex.mul a b) (TauComplex.mul a c)) := by
  constructor
  · -- Real part
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.add, TauReal.sub, TauReal.add, TauReal.mul,
               TauReal.negate]
    simp only [TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat]
    push_cast; try ring
  · -- Imaginary part
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.mul, TauComplex.add, TauReal.sub, TauReal.add, TauReal.mul,
               TauReal.negate]
    simp only [TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat]
    push_cast; try ring
```
