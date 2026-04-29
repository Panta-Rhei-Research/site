---
{
  "projection_kind": "taulib_declaration",
  "title": "taureal_ring_axioms",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/taureal-ring-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::taureal_ring_axioms",
  "declaration_slug": "taureal-ring-axioms",
  "kind": "theorem",
  "name": "taureal_ring_axioms",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 347,
  "source_line_end": 357,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L347-L357",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L347-L357",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L347-L357)
- Source range: L347-L357
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full TauReal ring axiom collection. -/
```

## Source Excerpt

```lean
theorem taureal_ring_axioms :
    (∀ (a b : TauReal), TauReal.equiv (a.add b) (b.add a)) ∧
    (∀ (a b c : TauReal), TauReal.equiv ((a.add b).add c) (a.add (b.add c))) ∧
    (∀ (a : TauReal), TauReal.equiv (a.add TauReal.zero) a) ∧
    (∀ (a : TauReal), TauReal.equiv (a.add a.negate) TauReal.zero) ∧
    (∀ (a b : TauReal), TauReal.equiv (a.mul b) (b.mul a)) ∧
    (∀ (a b c : TauReal), TauReal.equiv ((a.mul b).mul c) (a.mul (b.mul c))) ∧
    (∀ (a : TauReal), TauReal.equiv (a.mul TauReal.one) a) ∧
    (∀ (a b c : TauReal), TauReal.equiv (a.mul (b.add c)) ((a.mul b).add (a.mul c))) :=
  ⟨taureal_add_comm, taureal_add_assoc, taureal_add_zero, taureal_add_negate,
   taureal_mul_comm, taureal_mul_assoc, taureal_mul_one, taureal_left_distrib⟩
```
