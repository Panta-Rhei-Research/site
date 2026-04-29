---
{
  "projection_kind": "taulib_declaration",
  "title": "PhaseTransportWitness",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-witness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::PhaseTransportWitness",
  "declaration_slug": "phase-transport-witness",
  "kind": "structure",
  "name": "PhaseTransportWitness",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 96,
  "source_line_end": 105,
  "registry_ids": [
    "IV.D70"
  ],
  "related_registry_items": [
    {
      "id": "IV.D70",
      "title": "Phase Transport Witness",
      "url": "/registry/object/IV.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L96-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L96-L105",
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L96-L105)
- Source range: L96-L105
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D70` — Phase Transport Witness

## Immediate Comment / Docstring

```lean
/-- [IV.D70] Phase transport witness W_omega(f): the minimal phase
    transport needed to move a state f to a clopenly localized
    configuration. Records the structural cost of localization. -/
```

## Source Excerpt

```lean
structure PhaseTransportWitness where
  /-- Transport cost numerator (scaled). -/
  cost_numer : Nat
  /-- Transport cost denominator. -/
  cost_denom : Nat
  /-- Denominator positive. -/
  denom_pos : cost_denom > 0
  /-- Cost is non-negative. -/
  cost_nonneg : True  -- numer : Nat is always >= 0
  deriving Repr
```
