---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectDrivenAcceleration",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-driven-acceleration/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::DefectDrivenAcceleration",
  "declaration_slug": "defect-driven-acceleration",
  "kind": "structure",
  "name": "DefectDrivenAcceleration",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 113,
  "source_line_end": 130,
  "registry_ids": [
    "V.T68"
  ],
  "related_registry_items": [
    {
      "id": "V.T68",
      "title": "Defect-driven acceleration",
      "url": "/registry/object/V.T68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L113-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L113-L130",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L113-L130)
- Source range: L113-L130
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T68` — Defect-driven acceleration

## Immediate Comment / Docstring

```lean
/-- [V.T68] Defect-driven acceleration: as S_def decreases,
    the effective w shifts from w > -1/3 to w < -1/3.

    The transition occurs when the defect-to-refinement ratio
    crosses a critical threshold determined by iota_tau.

    Transition redshift z_acc ~ 0.7 corresponds to
    S_def/S_ref crossing the critical ratio. -/
```

## Source Excerpt

```lean
structure DefectDrivenAcceleration where
  /-- Current regime. -/
  regime : EoSRegime
  /-- Defect-to-refinement ratio numerator (S_def). -/
  ratio_def_numer : Nat
  /-- Defect-to-refinement ratio denominator (S_ref). -/
  ratio_ref_denom : Nat
  /-- Denominator positive. -/
  denom_pos : ratio_ref_denom > 0
  /-- The critical ratio threshold (scaled, ~ 1/3). -/
  critical_threshold_numer : Nat := 1
  /-- Critical threshold denominator. -/
  critical_threshold_denom : Nat := 3
  /-- Transition redshift (z_acc ~ 0.7, stored as 7/10). -/
  z_acc_numer : Nat := 7
  /-- Transition redshift denominator. -/
  z_acc_denom : Nat := 10
  deriving Repr
```
