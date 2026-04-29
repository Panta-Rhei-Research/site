---
{
  "projection_kind": "taulib_declaration",
  "title": "EntanglementClass",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-class/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::EntanglementClass",
  "declaration_slug": "entanglement-class",
  "kind": "inductive",
  "name": "EntanglementClass",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 286,
  "source_line_end": 291,
  "registry_ids": [
    "IV.D64"
  ],
  "related_registry_items": [
    {
      "id": "IV.D64",
      "title": "Entanglement",
      "url": "/registry/object/IV.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L286-L291",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L286-L291",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L286-L291)
- Source range: L286-L291
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D64` — Entanglement

## Immediate Comment / Docstring

```lean
/-- [IV.D64] Entanglement classification: a state is entangled if
    it cannot be written as a tensor product of subsystem states. -/
```

## Source Excerpt

```lean
inductive EntanglementClass where
  /-- psi = psi_A tensor psi_B (factorizable). -/
  | Separable
  /-- psi is not factorizable (entangled). -/
  | Entangled
  deriving Repr, DecidableEq, BEq
```
