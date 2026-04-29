---
{
  "projection_kind": "taulib_declaration",
  "title": "TauPhaseTransition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-phase-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::TauPhaseTransition",
  "declaration_slug": "tau-phase-transition",
  "kind": "structure",
  "name": "TauPhaseTransition",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 117,
  "source_line_end": 128,
  "registry_ids": [
    "V.D114"
  ],
  "related_registry_items": [
    {
      "id": "V.D114",
      "title": "Macro tau-glass",
      "url": "/registry/object/V.D114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L117-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L117-L128",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L117-L128)
- Source range: L117-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D114` — Macro tau-glass

## Immediate Comment / Docstring

```lean
/-- [V.D114] τ-phase transition: a change of phase at a critical
    temperature/coupling determined by the defect-budget crossing. -/
```

## Source Excerpt

```lean
structure TauPhaseTransition where
  /-- Transition order. -/
  order : TransitionOrder
  /-- Critical temperature index (scaled). -/
  critical_temp : Nat
  /-- High-temperature phase. -/
  high_temp_phase : PhaseType := .Disordered
  /-- Low-temperature phase. -/
  low_temp_phase : PhaseType := .Ordered
  /-- Whether the phases differ. -/
  phases_differ : high_temp_phase ≠ low_temp_phase
  deriving Repr
```
