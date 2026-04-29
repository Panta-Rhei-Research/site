---
{
  "projection_kind": "taulib_declaration",
  "title": "DarkEnergyTestability",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-testability/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::DarkEnergyTestability",
  "declaration_slug": "dark-energy-testability",
  "kind": "structure",
  "name": "DarkEnergyTestability",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 233,
  "source_line_end": 246,
  "registry_ids": [
    "V.R136"
  ],
  "related_registry_items": [
    {
      "id": "V.R136",
      "title": "Testability",
      "url": "/registry/object/V.R136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L233-L246",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L233-L246",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L233-L246)
- Source range: L233-L246
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R136` — Testability

## Immediate Comment / Docstring

```lean
/-- [V.R136] Testability: w_eff(z) should vary with redshift.
    - w > -1/3 at high z (defect-dominated epoch)
    - w ~ -1 at low z (refinement-dominated)
    - Transition at z_acc ~ 0.7

    Distinguishing prediction: w_eff is NOT exactly -1 but varies.
    Future measurements of w(z) can test the defect-transition model
    against a true cosmological constant (w = -1 exactly). -/
```

## Source Excerpt

```lean
structure DarkEnergyTestability where
  /-- Prediction: w varies with redshift. -/
  w_varies : Bool := true
  /-- w > -1/3 at high z. -/
  high_z_decelerating : Bool := true
  /-- w ~ -1 at low z. -/
  low_z_near_minus_one : Bool := true
  /-- Transition redshift z_acc (numer/denom). -/
  z_acc_numer : Nat := 7
  /-- Transition redshift denominator. -/
  z_acc_denom : Nat := 10
  /-- Denominator positive. -/
  denom_pos : z_acc_denom > 0 := by omega
  deriving Repr
```
