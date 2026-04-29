---
{
  "projection_kind": "taulib_declaration",
  "title": "HolomorphicTension",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/holomorphic-tension/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::HolomorphicTension",
  "declaration_slug": "holomorphic-tension",
  "kind": "structure",
  "name": "HolomorphicTension",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 39,
  "source_line_end": 43,
  "registry_ids": [
    "IV.D76"
  ],
  "related_registry_items": [
    {
      "id": "IV.D76",
      "title": "Energy as CR-Tension",
      "url": "/registry/object/IV.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L39-L43",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L39-L43",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L39-L43)
- Source range: L39-L43
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D76` — Energy as CR-Tension

## Immediate Comment / Docstring

```lean
/-- [IV.D76] Energy E[f] = holomorphic tension integral on T². -/
```

## Source Excerpt

```lean
structure HolomorphicTension where
  energy_numer : Nat
  energy_denom : Nat
  denom_pos : energy_denom > 0
  deriving Repr
```
