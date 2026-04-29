---
{
  "projection_kind": "taulib_declaration",
  "title": "EnergyConservation",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::EnergyConservation",
  "declaration_slug": "energy-conservation",
  "kind": "structure",
  "name": "EnergyConservation",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 123,
  "source_line_end": 130,
  "registry_ids": [
    "IV.T30"
  ],
  "related_registry_items": [
    {
      "id": "IV.T30",
      "title": "Energy Conservation",
      "url": "/registry/object/IV.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L123-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L123-L130",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L123-L130)
- Source range: L123-L130
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T30` — Energy Conservation

## Immediate Comment / Docstring

```lean
/-- [IV.T30] Total energy conserved under α-orbit evolution. -/
```

## Source Excerpt

```lean
structure EnergyConservation where
  e_initial_numer : Nat
  e_initial_denom : Nat
  e_final_numer : Nat
  e_final_denom : Nat
  conserved : e_initial_numer * e_final_denom =
              e_final_numer * e_initial_denom
  deriving Repr
```
