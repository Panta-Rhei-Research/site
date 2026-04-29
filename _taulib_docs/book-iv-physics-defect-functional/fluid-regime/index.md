---
{
  "projection_kind": "taulib_declaration",
  "title": "FluidRegime",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/fluid-regime/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::FluidRegime",
  "declaration_slug": "fluid-regime",
  "kind": "inductive",
  "name": "FluidRegime",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 103,
  "source_line_end": 128,
  "registry_ids": [
    "IV.D18"
  ],
  "related_registry_items": [
    {
      "id": "IV.D18",
      "title": "Fluid Regime",
      "url": "/registry/object/IV.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L103-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.DefectFunctional",
        "url": "/verify/taulib/docs/book-iv-physics-defect-functional/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L103-L128",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Physics.DefectFunctional](/verify/taulib/docs/book-iv-physics-defect-functional/)
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L103-L128)
- Source range: L103-L128
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D18` — Fluid Regime

## Immediate Comment / Docstring

```lean
/-- [IV.D18] The 8 canonical fluid regimes, classified by
    defect-tuple inequality patterns.

    Each regime is a τ-native formulation of a classical fluid type,
    defined WITHOUT importing the reals. -/
```

## Source Excerpt

```lean
inductive FluidRegime where
  /-- Periodic NF-code + arrested transport.
      Physical: crystalline solid with periodic lattice. -/
  | Crystal
  /-- Aperiodic NF-code + mobility below glass threshold k_glass.
      Physical: amorphous solid (thermal aging). -/
  | Glass
  /-- Kelvin-invariant + defect-budget preserved (inviscid).
      Physical: ideal fluid with circulation conservation. -/
  | Euler
  /-- Viscous shear-defect dominant + dissipation normalizer.
      Physical: viscous fluid with energy dissipation. -/
  | NavierStokes
  /-- Coupled fluid + EM holonomy with frozen-flux axiom.
      Physical: magnetohydrodynamic flow (Alfvén modes). -/
  | MHD
  /-- EM-active fluid with boundary-obstruction transport.
      Physical: ionized gas with Debye screening. -/
  | Plasma
  /-- Quantized circulation constraint (hard lattice on plaquettes).
      Physical: superfluid with protected vortex defects. -/
  | Superfluid
  /-- EM-superfluid with quantized flux Φ_τ.
      Physical: superconductor (Meissner effect, Abrikosov vortices). -/
  | Superconductor
  deriving Repr, DecidableEq, BEq, Inhabited
```
