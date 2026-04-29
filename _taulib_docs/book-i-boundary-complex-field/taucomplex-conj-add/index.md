---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_conj_add",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-add/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_conj_add",
  "declaration_slug": "taucomplex-conj-add",
  "kind": "theorem",
  "name": "taucomplex_conj_add",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 322,
  "source_line_end": 362,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L322-L362",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L322-L362",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L322-L362)
- Source range: L322-L362
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Conjugation distributes over addition: conj(a + b) ≡ conj(a) + conj(b). -/
```

## Source Excerpt

```lean
theorem taucomplex_conj_add (a b : TauComplex) :
    TauComplex.equiv (TauComplex.conj (TauComplex.add a b))
                     (TauComplex.add (TauComplex.conj a) (TauComplex.conj b)) := by
  constructor
  · exact TauReal.equiv_refl _
  · -- negate(add(a.im, b.im)) ≡ add(negate(a.im), negate(b.im))
    apply TauReal.equiv_of_pointwise
    intro n
    simp only [TauComplex.conj, TauComplex.add, TauReal.negate, TauReal.add]
    simp only [TauRat.equiv, TauRat.negate, TauRat.add]
    rw [equiv_iff_toInt_eq]
    simp only [toInt_add, toInt_negate, toInt_mul, toInt_fromNat]
    push_cast; try ring

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Type checks
#check TauComplex
#check TauComplex.equiv
#check TauComplex.i_unit
#check TauComplex.mul
#check TauComplex.conj

-- Theorem checks
#check taucomplex_i_squared
#check taucomplex_add_comm
#check taucomplex_add_assoc
#check taucomplex_add_zero
#check taucomplex_add_negate
#check taucomplex_mul_comm
#check taucomplex_mul_assoc
#check taucomplex_mul_one
#check taucomplex_left_distrib
#check taucomplex_ring_axioms
#check elliptic_hyperbolic_dichotomy
#check taucomplex_conj_involution
#check taucomplex_conj_add

end Tau.Boundary
```
