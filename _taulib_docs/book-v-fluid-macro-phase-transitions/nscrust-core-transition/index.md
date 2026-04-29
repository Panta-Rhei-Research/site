---
{
  "projection_kind": "taulib_declaration",
  "title": "NSCrustCoreTransition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/nscrust-core-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::NSCrustCoreTransition",
  "declaration_slug": "nscrust-core-transition",
  "kind": "structure",
  "name": "NSCrustCoreTransition",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 422,
  "source_line_end": 430,
  "registry_ids": [
    "V.D336"
  ],
  "related_registry_items": [
    {
      "id": "V.D336",
      "title": "Neutron Star Crust-Core Transition Density",
      "url": "/registry/object/V.D336/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L422-L430",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L422-L430",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L422-L430)
- Source range: L422-L430
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D336` — Neutron Star Crust-Core Transition Density

## Immediate Comment / Docstring

```lean
/-- [V.D336] Neutron star crust-core transition density.
    The transition occurs at ρ_cc = ρ₀(1 − κ_D) ≈ 0.5ρ₀
    where the mobility-compressibility inequality reverses.
    Scope: conjectural (crust fraction overshoots without metric corrections). -/
```

## Source Excerpt

```lean
structure NSCrustCoreTransition where
  /-- Nuclear saturation density in 10¹⁴ g/cm³ (≈ 2.8). -/
  rho_0_unit : Nat := 28  -- in units of 10¹³ g/cm³
  /-- κ_D = 1 − ι_τ ≈ 0.659 (in permille: 659). -/
  kappa_D_permille : Nat := 659
  /-- Transition fraction: 1 − κ_D ≈ 0.341 ≈ ι_τ. -/
  transition_fraction_permille : Nat := 341
  /-- Transition is at ≈ 0.5ρ₀ (rounded). -/
  transition_half : transition_fraction_permille < 500 := by omega
```
