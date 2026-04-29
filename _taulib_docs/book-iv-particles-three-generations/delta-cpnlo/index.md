---
{
  "projection_kind": "taulib_declaration",
  "title": "DeltaCPNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/delta-cpnlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::DeltaCPNLO",
  "declaration_slug": "delta-cpnlo",
  "kind": "structure",
  "name": "DeltaCPNLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 3060,
  "source_line_end": 3073,
  "registry_ids": [
    "IV.T207"
  ],
  "related_registry_items": [
    {
      "id": "IV.T207",
      "title": "δ_CP NLO from Fiber Correction",
      "url": "/registry/object/IV.T207/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3060-L3073",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3060-L3073",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3060-L3073)
- Source range: L3060-L3073
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T207` — δ_CP NLO from Fiber Correction

## Immediate Comment / Docstring

```lean
/-- [IV.T207] δ_CP NLO from fiber correction.
    δ_CP = π + arctan(ι_τ·(1−ι_τ³)) = 198.11°
    Fiber correction (1−ι_τ³) = confinement screening at ι_τ^dim(τ³).
    Same correction as CKM Jarlskog NLO (IV.T198).
    PDG: 197° ± 25°. Deviation: +5645 ppm (was +9365), 40% improvement. -/
```

## Source Excerpt

```lean
structure DeltaCPNLO where
  /-- τ-prediction in degrees × 100. -/
  tau_deg_x100 : Nat := 19811
  /-- PDG central value × 100. -/
  pdg_deg_x100 : Nat := 19700
  /-- Fiber correction exponent (dim(τ³)). -/
  fiber_exp : Nat := 3
  /-- LO deviation ppm. -/
  lo_ppm : Nat := 9365
  /-- NLO deviation ppm. -/
  nlo_ppm : Nat := 5645
  /-- Improvement percentage. -/
  improvement_pct : Nat := 40
  deriving Repr
```
