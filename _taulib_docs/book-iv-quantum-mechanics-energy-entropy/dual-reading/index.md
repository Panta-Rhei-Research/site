---
{
  "projection_kind": "taulib_declaration",
  "title": "DualReading",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::DualReading",
  "declaration_slug": "dual-reading",
  "kind": "structure",
  "name": "DualReading",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 107,
  "source_line_end": 113,
  "registry_ids": [
    "IV.T29"
  ],
  "related_registry_items": [
    {
      "id": "IV.T29",
      "title": "Energy Duality",
      "url": "/registry/object/IV.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L107-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L107-L113",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L107-L113)
- Source range: L107-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T29` — Energy Duality

## Immediate Comment / Docstring

```lean
/-- [IV.T29] E_k = m_k c²_τ = ℏ_τ ω_k: one eigenvalue, two readings.
    Mass (fiber) and frequency (base) are the SAME eigenvalue read
    through different functors, not equated by postulate. -/
```

## Source Excerpt

```lean
structure DualReading where
  mode_index : Nat
  mass : MassFromEigenvalue
  freq : FrequencyFromEigenvalue
  same_mode : mass.mode_index = freq.mode_index
  index_match : mass.mode_index = mode_index
  deriving Repr
```
