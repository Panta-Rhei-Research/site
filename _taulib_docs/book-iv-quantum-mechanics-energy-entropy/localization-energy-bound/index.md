---
{
  "projection_kind": "taulib_declaration",
  "title": "localization_energy_bound",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-energy-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::localization_energy_bound",
  "declaration_slug": "localization-energy-bound",
  "kind": "theorem",
  "name": "localization_energy_bound",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 77,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L77-L78",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L77-L78",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L77-L78)
- Source range: L77-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem localization_energy_bound (b : LocalizationBound) :
    b.e_vac_numer ≥ 0 := Nat.zero_le b.e_vac_numer
```
