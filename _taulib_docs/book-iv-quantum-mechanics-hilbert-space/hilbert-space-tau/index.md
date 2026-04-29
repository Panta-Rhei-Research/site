---
{
  "projection_kind": "taulib_declaration",
  "title": "HilbertSpaceTau",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/hilbert-space-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::HilbertSpaceTau",
  "declaration_slug": "hilbert-space-tau",
  "kind": "structure",
  "name": "HilbertSpaceTau",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 153,
  "source_line_end": 163,
  "registry_ids": [
    "IV.D62"
  ],
  "related_registry_items": [
    {
      "id": "IV.D62",
      "title": "Holomorphic Hilbert Space",
      "url": "/registry/object/IV.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L153-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L153-L163",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L153-L163)
- Source range: L153-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D62` — Holomorphic Hilbert Space

## Immediate Comment / Docstring

```lean
/-- [IV.D62] H_tau = L^2-completion of CR(tau^3): the Hilbert space
    of quantum states. Equipped with the canonical inner product. -/
```

## Source Excerpt

```lean
structure HilbertSpaceTau where
  /-- Complete (Cauchy sequences converge). -/
  is_complete : Bool
  complete_true : is_complete = true
  /-- Separable (countable dense subset). -/
  is_separable : Bool
  separable_true : is_separable = true
  /-- Infinite-dimensional. -/
  is_infinite_dim : Bool
  inf_true : is_infinite_dim = true
  deriving Repr
```
