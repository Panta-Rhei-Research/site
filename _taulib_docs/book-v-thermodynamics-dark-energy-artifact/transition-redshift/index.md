---
{
  "projection_kind": "taulib_declaration",
  "title": "TransitionRedshift",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/transition-redshift/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::TransitionRedshift",
  "declaration_slug": "transition-redshift",
  "kind": "structure",
  "name": "TransitionRedshift",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 399,
  "source_line_end": 408,
  "registry_ids": [
    "V.D294",
    "V.R418"
  ],
  "related_registry_items": [
    {
      "id": "V.D294",
      "title": "Transition Redshift z_acc",
      "url": "/registry/object/V.D294/"
    },
    {
      "id": "V.R418",
      "title": "Transition Redshift Comparison",
      "url": "/registry/object/V.R418/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L399-L408",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L399-L408",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L399-L408)
- Source range: L399-L408
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D294` — Transition Redshift z_acc
- `V.R418` — Transition Redshift Comparison

## Immediate Comment / Docstring

```lean
/-- [V.D294] Transition redshift z_acc = (2Ω_Λ/Ω_m)^(1/3) − 1 ≈ 0.632.
    Observed: 0.64 ± 0.05 (SN Ia). Deviation: −1.3%.

    [V.R418] Comparison: τ-prediction within observational uncertainty. -/
```

## Source Excerpt

```lean
structure TransitionRedshift where
  /-- z_acc (scaled ×1000): 0.632 → 632. -/
  z_acc_x1000 : Nat
  /-- Observed central value (scaled ×1000): 0.64 → 640. -/
  observed_x1000 : Nat := 640
  /-- Observed uncertainty (scaled ×1000): 0.05 → 50. -/
  uncertainty_x1000 : Nat := 50
  /-- Deviation from observed (ppm, negative = τ below). -/
  deviation_ppm : Int
  deriving Repr
```
