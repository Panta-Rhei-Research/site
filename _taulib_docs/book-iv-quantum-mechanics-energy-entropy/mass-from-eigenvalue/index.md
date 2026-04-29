---
{
  "projection_kind": "taulib_declaration",
  "title": "MassFromEigenvalue",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/mass-from-eigenvalue/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::MassFromEigenvalue",
  "declaration_slug": "mass-from-eigenvalue",
  "kind": "structure",
  "name": "MassFromEigenvalue",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 85,
  "source_line_end": 90,
  "registry_ids": [
    "IV.D78"
  ],
  "related_registry_items": [
    {
      "id": "IV.D78",
      "title": "Mass as Fiber Stiffness",
      "url": "/registry/object/IV.D78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L85-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L85-L90",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L85-L90)
- Source range: L85-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D78` — Mass as Fiber Stiffness

## Immediate Comment / Docstring

```lean
/-- [IV.D78] Mass from H_∞ eigenvalue via fiber curvature: m_k = λ_k / c²_τ. -/
```

## Source Excerpt

```lean
structure MassFromEigenvalue where
  mode_index : Nat
  mass_numer : Nat
  mass_denom : Nat
  denom_pos : mass_denom > 0
  deriving Repr
```
