---
{
  "projection_kind": "taulib_declaration",
  "title": "EntanglementGenericity",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-genericity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::EntanglementGenericity",
  "declaration_slug": "entanglement-genericity",
  "kind": "structure",
  "name": "EntanglementGenericity",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 300,
  "source_line_end": 307,
  "registry_ids": [
    "IV.P21"
  ],
  "related_registry_items": [
    {
      "id": "IV.P21",
      "title": "Generic Entanglement",
      "url": "/registry/object/IV.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L300-L307",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L300-L307",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L300-L307)
- Source range: L300-L307
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P21` — Generic Entanglement

## Immediate Comment / Docstring

```lean
/-- [IV.P21] Separable states are measure zero; entangled states are
    generic (dense, open, and full-measure in the state space).
    Formalized structurally: separable is the exception, not the rule. -/
```

## Source Excerpt

```lean
structure EntanglementGenericity where
  /-- Separable states have measure zero. -/
  separable_measure_zero : Bool
  sep_true : separable_measure_zero = true
  /-- Entangled states are dense. -/
  entangled_dense : Bool
  ent_true : entangled_dense = true
  deriving Repr
```
