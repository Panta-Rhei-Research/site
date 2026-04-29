---
{
  "projection_kind": "taulib_declaration",
  "title": "ArrowOfTime",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::ArrowOfTime",
  "declaration_slug": "arrow-of-time",
  "kind": "structure",
  "name": "ArrowOfTime",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 192,
  "source_line_end": 198,
  "registry_ids": [
    "IV.T32"
  ],
  "related_registry_items": [
    {
      "id": "IV.T32",
      "title": "Structural Arrow of Time",
      "url": "/registry/object/IV.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L192-L198",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L192-L198",
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

- Module: [TauLib.BookIV.QuantumMechanics.EnergyEntropy](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/)
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L192-L198)
- Source range: L192-L198
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T32` — Structural Arrow of Time

## Immediate Comment / Docstring

```lean
/-- [IV.T32] Arrow of time = direction of increasing refinement + entropy. -/
```

## Source Excerpt

```lean
structure ArrowOfTime where
  direction : TemporalDirection
  entropy_witness : EntropyMonotonicity
  depth_consistent :
    direction.depth_before = entropy_witness.s_before.depth ∧
    direction.depth_after = entropy_witness.s_after.depth
  deriving Repr
```
