---
{
  "projection_kind": "taulib_declaration",
  "title": "sc_ring_axioms",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/sc-ring-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::sc_ring_axioms",
  "declaration_slug": "sc-ring-axioms",
  "kind": "theorem",
  "name": "sc_ring_axioms",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 89,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L89-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/verify/taulib/docs/book-i-boundary-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L89-L108",
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

- Module: [TauLib.BookI.Boundary.SplitComplex](/verify/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L89-L108)
- Source range: L89-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full SplitComplex ring axiom collection. -/
```

## Source Excerpt

```lean
theorem sc_ring_axioms :
    (∀ (a b : SplitComplex), SplitComplex.add a b = SplitComplex.add b a) ∧
    (∀ (a b c : SplitComplex), SplitComplex.add (SplitComplex.add a b) c =
      SplitComplex.add a (SplitComplex.add b c)) ∧
    (∀ (a : SplitComplex), SplitComplex.add a SplitComplex.zero = a) ∧
    (∀ (a : SplitComplex), SplitComplex.add a (SplitComplex.neg a) = SplitComplex.zero) ∧
    (∀ (a b : SplitComplex), SplitComplex.mul a b = SplitComplex.mul b a) ∧
    (∀ (a b c : SplitComplex), SplitComplex.mul (SplitComplex.mul a b) c =
      SplitComplex.mul a (SplitComplex.mul b c)) ∧
    (∀ (a : SplitComplex), SplitComplex.mul a SplitComplex.one = a) ∧
    (∀ (a b c : SplitComplex), SplitComplex.mul a (SplitComplex.add b c) =
      SplitComplex.add (SplitComplex.mul a b) (SplitComplex.mul a c)) :=
  ⟨sc_add_comm, sc_add_assoc, sc_add_zero, sc_add_neg,
   sc_mul_comm, sc_mul_assoc, sc_mul_one, sc_left_distrib⟩

-- ============================================================
-- SECTORPAIR EXTENSIONALITY
-- ============================================================

@[ext]
```
