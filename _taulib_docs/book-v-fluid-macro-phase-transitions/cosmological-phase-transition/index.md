---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmologicalPhaseTransition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-phase-transition/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::CosmologicalPhaseTransition",
  "declaration_slug": "cosmological-phase-transition",
  "kind": "inductive",
  "name": "CosmologicalPhaseTransition",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 306,
  "source_line_end": 315,
  "registry_ids": [
    "V.T77"
  ],
  "related_registry_items": [
    {
      "id": "V.T77",
      "title": "Phase-transition universality",
      "url": "/registry/object/V.T77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L306-L315",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L306-L315",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L306-L315)
- Source range: L306-L315
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.T77` — Phase-transition universality

## Immediate Comment / Docstring

```lean
/-- [V.T77] Phase transition completeness: every phase transition in
    the physical universe corresponds to a defect-budget crossing in
    the τ-framework.

    The four physical phase transitions:
    1. QCD confinement (C-sector, T ~ 170 MeV)
    2. EW symmetry breaking (ω-sector, T ~ 160 GeV)
    3. Superfluid/superconductor (quantized circulation)
    4. Classical liquid-gas (mobility crossing)

    All four are readout-level events of the same τ-structural mechanism. -/
```

## Source Excerpt

```lean
inductive CosmologicalPhaseTransition where
  /-- QCD confinement: C-sector phase transition. -/
  | QCDConfinement
  /-- Electroweak symmetry breaking: ω-sector crossing. -/
  | EWSymmetryBreaking
  /-- Superfluid transition: quantized circulation onset. -/
  | SuperfluidTransition
  /-- Classical liquid-gas: mobility crossing. -/
  | LiquidGas
  deriving Repr, DecidableEq, BEq
```
