---
{
  "projection_kind": "taulib_declaration",
  "title": "TauOrderParameter",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-order-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::TauOrderParameter",
  "declaration_slug": "tau-order-parameter",
  "kind": "structure",
  "name": "TauOrderParameter",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 81,
  "source_line_end": 89,
  "registry_ids": [
    "V.D113"
  ],
  "related_registry_items": [
    {
      "id": "V.D113",
      "title": "Macro tau-crystal",
      "url": "/registry/object/V.D113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L81-L89",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L81-L89",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L81-L89)
- Source range: L81-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D113` — Macro tau-crystal

## Immediate Comment / Docstring

```lean
/-- [V.D113] τ-order parameter: a boundary character projection that
    distinguishes phases. The order parameter is zero in the disordered
    phase and nonzero in the ordered phase. -/
```

## Source Excerpt

```lean
structure TauOrderParameter where
  /-- Order parameter value (scaled, 0 = zero). -/
  value : Nat
  /-- Phase classification. -/
  phase : PhaseType
  /-- Classification is consistent with value. -/
  consistent : (value = 0 → phase = .Disordered) ∧
               (value > 0 → phase = .Ordered)
  deriving Repr
```
