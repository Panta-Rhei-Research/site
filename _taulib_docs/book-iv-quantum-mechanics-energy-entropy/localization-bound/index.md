---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalizationBound",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::LocalizationBound",
  "declaration_slug": "localization-bound",
  "kind": "structure",
  "name": "LocalizationBound",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 68,
  "source_line_end": 75,
  "registry_ids": [
    "IV.P29"
  ],
  "related_registry_items": [
    {
      "id": "IV.P29",
      "title": "Energy-Localization Bound",
      "url": "/registry/object/IV.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L68-L75",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L68-L75",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L68-L75)
- Source range: L68-L75
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P29` — Energy-Localization Bound

## Immediate Comment / Docstring

```lean
/-- [IV.P29] E[ψ] ≥ E_vac + ℏ_τ²/(2(Δx)²): localization costs energy. -/
```

## Source Excerpt

```lean
structure LocalizationBound where
  e_vac_numer : Nat
  e_vac_denom : Nat
  hbar_sq_numer : Nat
  hbar_sq_denom : Nat
  vac_denom_pos : e_vac_denom > 0
  hbar_denom_pos : hbar_sq_denom > 0
  deriving Repr
```
