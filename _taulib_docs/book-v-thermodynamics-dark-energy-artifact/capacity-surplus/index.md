---
{
  "projection_kind": "taulib_declaration",
  "title": "CapacitySurplus",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/capacity-surplus/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::CapacitySurplus",
  "declaration_slug": "capacity-surplus",
  "kind": "structure",
  "name": "CapacitySurplus",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 74,
  "source_line_end": 85,
  "registry_ids": [
    "V.D95"
  ],
  "related_registry_items": [
    {
      "id": "V.D95",
      "title": "Capacity surplus",
      "url": "/registry/object/V.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L74-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
        "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L74-L85",
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

- Module: [TauLib.BookV.Thermodynamics.DarkEnergyArtifact](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/)
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L74-L85)
- Source range: L74-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D95` — Capacity surplus

## Immediate Comment / Docstring

```lean
/-- [V.D95] Capacity surplus: the difference between total absorption
    capacity of the lemniscate boundary L and the current defect count.

    C_surplus(n) = C_total - |D_n|

    Unused boundary capacity manifests as negative effective pressure
    in the readout functor's projection. As defects are absorbed,
    C_surplus increases, driving the transition to acceleration. -/
```

## Source Excerpt

```lean
structure CapacitySurplus where
  /-- Total absorption capacity of L. -/
  c_total : Nat
  /-- Current defect count |D_n|. -/
  d_n : Nat
  /-- Surplus = total - defect count. -/
  surplus : Nat
  /-- Surplus equals capacity minus defects. -/
  surplus_eq : surplus = c_total - d_n
  /-- Capacity exceeds defect count (surplus non-negative). -/
  capacity_exceeds : d_n ≤ c_total
  deriving Repr
```
