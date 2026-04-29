---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalQuantization",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/topological-quantization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::TopologicalQuantization",
  "declaration_slug": "topological-quantization",
  "kind": "structure",
  "name": "TopologicalQuantization",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 122,
  "source_line_end": 135,
  "registry_ids": [
    "IV.T20"
  ],
  "related_registry_items": [
    {
      "id": "IV.T20",
      "title": "Topological Quantization",
      "url": "/registry/object/IV.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L122-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Quantization",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L122-L135",
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L122-L135)
- Source range: L122-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T20` — Topological Quantization

## Immediate Comment / Docstring

```lean
/-- [IV.T20] Topological quantization: the compactness of T^2 forces
    the dual lattice Z^2 to be discrete, which forces the spectrum of
    every quantum operator to be discrete.

    Chain: compact T^2 → discrete Z^2 → Lambda_CR → discrete spectra.

    The essential point: the compactness of the fiber is why physics
    has discrete quantum numbers. -/
```

## Source Excerpt

```lean
structure TopologicalQuantization where
  /-- T^2 is compact. -/
  fiber_compact : Bool
  compact_true : fiber_compact = true
  /-- Dual lattice is discrete (Z^2). -/
  dual_discrete : Bool
  discrete_true : dual_discrete = true
  /-- Spectrum is discrete. -/
  spectrum_discrete : Bool
  spec_true : spectrum_discrete = true
  /-- Compactness chain: compact → discrete dual → discrete spectrum. -/
  chain_length : Nat
  chain_eq : chain_length = 3
  deriving Repr
```
