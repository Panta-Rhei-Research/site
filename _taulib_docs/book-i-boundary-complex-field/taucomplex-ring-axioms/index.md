---
{
  "projection_kind": "taulib_declaration",
  "title": "taucomplex_ring_axioms",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-ring-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::taucomplex_ring_axioms",
  "declaration_slug": "taucomplex-ring-axioms",
  "kind": "theorem",
  "name": "taucomplex_ring_axioms",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 249,
  "source_line_end": 260,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L249-L260",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L249-L260",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L249-L260)
- Source range: L249-L260
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full TauComplex ring axiom collection. -/
```

## Source Excerpt

```lean
theorem taucomplex_ring_axioms :
    (∀ (a b : TauComplex), TauComplex.equiv (a.add b) (b.add a)) ∧
    (∀ (a b c : TauComplex), TauComplex.equiv ((a.add b).add c) (a.add (b.add c))) ∧
    (∀ (a : TauComplex), TauComplex.equiv (a.add TauComplex.zero) a) ∧
    (∀ (a : TauComplex), TauComplex.equiv (a.add a.negate) TauComplex.zero) ∧
    (∀ (a b : TauComplex), TauComplex.equiv (a.mul b) (b.mul a)) ∧
    (∀ (a b c : TauComplex), TauComplex.equiv ((a.mul b).mul c) (a.mul (b.mul c))) ∧
    (∀ (a : TauComplex), TauComplex.equiv (a.mul TauComplex.one) a) ∧
    (∀ (a b c : TauComplex), TauComplex.equiv (a.mul (b.add c)) ((a.mul b).add (a.mul c))) :=
  ⟨taucomplex_add_comm, taucomplex_add_assoc, taucomplex_add_zero, taucomplex_add_negate,
   taucomplex_mul_comm, taucomplex_mul_assoc, taucomplex_mul_one,
   taucomplex_left_distrib⟩
```
