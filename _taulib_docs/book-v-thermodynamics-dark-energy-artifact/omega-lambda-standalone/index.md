---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaLambdaStandalone",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-standalone/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::OmegaLambdaStandalone",
  "declaration_slug": "omega-lambda-standalone",
  "kind": "structure",
  "name": "OmegaLambdaStandalone",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 327,
  "source_line_end": 340,
  "registry_ids": [
    "V.T234"
  ],
  "related_registry_items": [
    {
      "id": "V.T234",
      "title": "Ω_Λ Structural Theorem",
      "url": "/registry/object/V.T234/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L327-L340",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L327-L340",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L327-L340)
- Source range: L327-L340
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T234` — Ω_Λ Structural Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T234] Standalone Ω_Λ structural theorem:
    Ω_Λ = κ_D · (1 + ι_τ³) = (1 − ι_τ)(1 + ι_τ³) ≈ 0.6849.
    Zero-parameter prediction from master constant ι_τ.

    κ_D = D-sector coupling (gravity), ι_τ³ = fiber volume correction.
    Planck 2018: 0.6847 ± 0.0073. Deviation: +269 ppm (+0.03σ). -/
```

## Source Excerpt

```lean
structure OmegaLambdaStandalone where
  /-- κ_D numerator (scaled ×10000): (1 − ι_τ) ≈ 0.6587 → 6587. -/
  kappa_D_x10000 : Nat
  /-- ι_τ³ numerator (scaled ×100000): ι_τ³ ≈ 0.03979 → 3979. -/
  iota_tau_cubed_x100000 : Nat
  /-- Ω_Λ (scaled ×10000): ≈ 0.6849 → 6849. -/
  omega_lambda_x10000 : Nat
  /-- Planck 2018 value (scaled ×10000): 0.6847 → 6847. -/
  planck_x10000 : Nat := 6847
  /-- Deviation in ppm (positive = τ exceeds Planck). -/
  deviation_ppm : Int
  /-- τ-effective scope: derived from κ_D and ι_τ only. -/
  scope_tau_effective : Bool := true
  deriving Repr
```
