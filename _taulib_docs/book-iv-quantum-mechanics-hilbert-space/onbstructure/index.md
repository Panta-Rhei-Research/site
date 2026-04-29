---
{
  "projection_kind": "taulib_declaration",
  "title": "ONBStructure",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onbstructure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::ONBStructure",
  "declaration_slug": "onbstructure",
  "kind": "structure",
  "name": "ONBStructure",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 221,
  "source_line_end": 234,
  "registry_ids": [
    "IV.T19"
  ],
  "related_registry_items": [
    {
      "id": "IV.T19",
      "title": "Orthonormal Basis",
      "url": "/registry/object/IV.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L221-L234",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L221-L234",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L221-L234)
- Source range: L221-L234
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T19` — Orthonormal Basis

## Immediate Comment / Docstring

```lean
/-- [IV.T19] The CR-admissible characters {chi_{m,n} : (m,n) in Lambda_CR}
    form an orthonormal basis (ONB) for H_tau.
    The basis is indexed by the admissible sublattice. -/
```

## Source Excerpt

```lean
structure ONBStructure where
  /-- Basis is indexed by admissible lattice points. -/
  index_type : String
  index_is_admissible : index_type = "Lambda_CR"
  /-- Basis elements are orthogonal. -/
  is_orthogonal : Bool
  orth_true : is_orthogonal = true
  /-- Basis elements are normalized. -/
  is_normalized : Bool
  norm_true : is_normalized = true
  /-- Basis is complete (spans H_tau). -/
  is_complete : Bool
  comp_true : is_complete = true
  deriving Repr
```
