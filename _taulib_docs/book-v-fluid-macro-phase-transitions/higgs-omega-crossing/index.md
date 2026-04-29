---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsOmegaCrossing",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::HiggsOmegaCrossing",
  "declaration_slug": "higgs-omega-crossing",
  "kind": "structure",
  "name": "HiggsOmegaCrossing",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 261,
  "source_line_end": 270,
  "registry_ids": [
    "V.P55"
  ],
  "related_registry_items": [
    {
      "id": "V.P55",
      "title": "Neutron star phase sequence",
      "url": "/registry/object/V.P55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L261-L270",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L261-L270",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L261-L270)
- Source range: L261-L270
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P55` — Neutron star phase sequence

## Immediate Comment / Docstring

```lean
/-- [V.P55] Higgs as ω-sector crossing: the Higgs mechanism is the
    cosmological phase transition at the ω-sector (lobe crossing)
    where the order parameter (Higgs field) acquires a VEV.

    This is the τ-native description of spontaneous EW symmetry breaking.
    The ω-sector is the crossing point of the lemniscate L = S¹ ∨ S¹. -/
```

## Source Excerpt

```lean
structure HiggsOmegaCrossing where
  /-- The phase transition. -/
  transition : TauPhaseTransition
  /-- The order parameter is the Higgs VEV. -/
  is_higgs_vev : Bool := true
  /-- This is the ω-sector (B ∩ C crossing). -/
  is_omega_sector : Bool := true
  /-- EW symmetry is broken in the low-temperature phase. -/
  ew_broken_below : Bool := true
  deriving Repr
```
