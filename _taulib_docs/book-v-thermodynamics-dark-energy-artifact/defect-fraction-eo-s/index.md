---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectFractionEoS",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-fraction-eo-s/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::DefectFractionEoS",
  "declaration_slug": "defect-fraction-eo-s",
  "kind": "structure",
  "name": "DefectFractionEoS",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 369,
  "source_line_end": 379,
  "registry_ids": [
    "V.D293",
    "V.P159"
  ],
  "related_registry_items": [
    {
      "id": "V.D293",
      "title": "Defect Fraction Function",
      "url": "/registry/object/V.D293/"
    },
    {
      "id": "V.P159",
      "title": "w₀ from Defect Dynamics",
      "url": "/registry/object/V.P159/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L369-L379",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L369-L379",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L369-L379)
- Source range: L369-L379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D293` — Defect Fraction Function
- `V.P159` — w₀ from Defect Dynamics

## Immediate Comment / Docstring

```lean
/-- [V.D293] Defect fraction function:
    f_def(z) = S_def(z) / (S_def(z) + S_ref(z)).
    At z → ∞: f_def → 1. At z = 0: f_def → ι_τ³ ≈ 0.040.

    [V.P159] Effective equation of state:
    w(z) = −1 + (2/3) · f_def(z)/(1 − f_def(z)).
    At z = 0: w₀ = ι_τ³ − 1 ≈ −0.960 (quintessence-like). -/
```

## Source Excerpt

```lean
structure DefectFractionEoS where
  /-- Present defect fraction f_def(0) (scaled ×10000): ι_τ³ ≈ 0.0398 → 398. -/
  f_def_present_x10000 : Nat
  /-- w₀ (scaled ×1000, offset from −1): ι_τ³ ≈ 0.040 → 40 means w₀ = −0.960. -/
  w0_offset_x1000 : Nat
  /-- w₀ > −1 (quintessence-like, no phantom). -/
  w0_gt_minus_one : Bool := true
  /-- Transition value: w = −1/3 at z_acc. -/
  transition_w_numer : Int := -1
  transition_w_denom : Nat := 3
  deriving Repr
```
