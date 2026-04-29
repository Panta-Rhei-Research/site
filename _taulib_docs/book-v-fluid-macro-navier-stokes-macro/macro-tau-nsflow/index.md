---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroTauNSFlow",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-nsflow/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::MacroTauNSFlow",
  "declaration_slug": "macro-tau-nsflow",
  "kind": "structure",
  "name": "MacroTauNSFlow",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 98,
  "source_line_end": 107,
  "registry_ids": [
    "V.D97"
  ],
  "related_registry_items": [
    {
      "id": "V.D97",
      "title": "Macro tau-Navier--Stokes flow",
      "url": "/registry/object/V.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L98-L107",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L98-L107",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L98-L107)
- Source range: L98-L107
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D97` — Macro tau-Navier--Stokes flow

## Immediate Comment / Docstring

```lean
/-- [V.D97] Macro tau-NS flow: a sequence of τ-admissible configurations
    satisfying base-sector (D and A) dominance and macro viscous decay.

    The macro viscous decay condition:
    B^macro_{n+1} - B^macro_n ∝ viscosity correction. -/
```

## Source Excerpt

```lean
structure MacroTauNSFlow where
  /-- Initial defect transport state. -/
  initial : MacroDefectTransport
  /-- Whether base-sector (D and A) dominance holds. -/
  base_sector_dominant : Bool := true
  /-- Whether viscous decay condition is satisfied. -/
  viscous_decay : Bool := true
  /-- Number of evolution steps. -/
  steps : Nat
  deriving Repr
```
