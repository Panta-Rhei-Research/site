---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_conj_involution",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-involution/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_conj_involution",
  "declaration_slug": "taucomplex-conj-involution",
  "kind": "theorem",
  "name": "taucomplex_conj_involution",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 308,
  "source_line_end": 319,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L308-L319",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L308-L319",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L308-L319)
- Source range: L308-L319
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Conjugation is an involution: conj(conj(z)) ≡ z. -/
```

## Source Excerpt

```lean
theorem taucomplex_conj_involution (a : TauComplex) :
    TauComplex.equiv (TauComplex.conj (TauComplex.conj a)) a := by
  constructor
  · exact TauReal.equiv_refl a.re
  · -- negate(negate(a.im)) ≡ a.im
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.conj, TauReal.negate]
    simp only [TauRat.equiv, TauRat.negate]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_negate, toInt_mul, toInt_fromNat]
    push_cast; try ring
```
