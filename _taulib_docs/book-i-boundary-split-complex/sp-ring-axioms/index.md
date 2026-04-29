---
{
  "projection_kind": "taulib_declaration",
  "title": "sp_ring_axioms",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/sp-ring-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::sp_ring_axioms",
  "declaration_slug": "sp-ring-axioms",
  "kind": "theorem",
  "name": "sp_ring_axioms",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 172,
  "source_line_end": 185,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L172-L185",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L172-L185",
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
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L172-L185)
- Source range: L172-L185
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full SectorPair ring axiom collection. -/
```

## Source Excerpt

```lean
theorem sp_ring_axioms :
    (∀ (a b : SectorPair), SectorPair.add a b = SectorPair.add b a) ∧
    (∀ (a b c : SectorPair), SectorPair.add (SectorPair.add a b) c =
      SectorPair.add a (SectorPair.add b c)) ∧
    (∀ (a : SectorPair), SectorPair.add a SectorPair.zero = a) ∧
    (∀ (a : SectorPair), SectorPair.add a (SectorPair.neg a) = SectorPair.zero) ∧
    (∀ (a b : SectorPair), SectorPair.mul a b = SectorPair.mul b a) ∧
    (∀ (a b c : SectorPair), SectorPair.mul (SectorPair.mul a b) c =
      SectorPair.mul a (SectorPair.mul b c)) ∧
    (∀ (a : SectorPair), SectorPair.mul a SectorPair.one = a) ∧
    (∀ (a b c : SectorPair), SectorPair.mul a (SectorPair.add b c) =
      SectorPair.add (SectorPair.mul a b) (SectorPair.mul a c)) :=
  ⟨sp_add_comm, sp_add_assoc, sp_add_zero, sp_add_neg,
   sp_mul_comm, sp_mul_assoc, sp_mul_one, sp_left_distrib⟩
```
