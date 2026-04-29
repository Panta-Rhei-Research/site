---
{
  "projection_kind": "taulib_declaration",
  "title": "FrequencyFromEigenvalue",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/frequency-from-eigenvalue/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::FrequencyFromEigenvalue",
  "declaration_slug": "frequency-from-eigenvalue",
  "kind": "structure",
  "name": "FrequencyFromEigenvalue",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 93,
  "source_line_end": 98,
  "registry_ids": [
    "IV.D79"
  ],
  "related_registry_items": [
    {
      "id": "IV.D79",
      "title": "Frequency as Base Circulation",
      "url": "/registry/object/IV.D79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L93-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L93-L98",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L93-L98)
- Source range: L93-L98
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D79` — Frequency as Base Circulation

## Immediate Comment / Docstring

```lean
/-- [IV.D79] Frequency from H_∞ eigenvalue via base evolution: ω_k = λ_k / ℏ_τ. -/
```

## Source Excerpt

```lean
structure FrequencyFromEigenvalue where
  mode_index : Nat
  freq_numer : Nat
  freq_denom : Nat
  denom_pos : freq_denom > 0
  deriving Repr
```
