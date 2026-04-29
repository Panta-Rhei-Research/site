---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmologicalTransitionRemark",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-transition-remark/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::CosmologicalTransitionRemark",
  "declaration_slug": "cosmological-transition-remark",
  "kind": "structure",
  "name": "CosmologicalTransitionRemark",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 335,
  "source_line_end": 342,
  "registry_ids": [
    "V.R160"
  ],
  "related_registry_items": [
    {
      "id": "V.R160",
      "title": "Universality is structural, not accidental",
      "url": "/registry/object/V.R160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L335-L342",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L335-L342",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L335-L342)
- Source range: L335-L342
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R160` — Universality is structural, not accidental

## Immediate Comment / Docstring

```lean
/-- [V.R160] Cosmological phase transitions: the early universe underwent
    at least two phase transitions (QCD, EW), both of which are τ-native.

    The EW transition may be first-order (enabling baryogenesis) or
    crossover (standard model prediction) — the distinction depends on
    the Higgs self-coupling at the ω-sector. -/
```

## Source Excerpt

```lean
structure CosmologicalTransitionRemark where
  /-- Which transition. -/
  transition : CosmologicalPhaseTransition
  /-- Temperature scale (MeV, scaled). -/
  temp_mev : Nat
  /-- Whether first-order or crossover. -/
  order : TransitionOrder
  deriving Repr
```
