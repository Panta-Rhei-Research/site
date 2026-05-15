---
{
  "projection_kind": "taulib_declaration",
  "title": "AlfvenDampingMechanism",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-mechanism/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::AlfvenDampingMechanism",
  "declaration_slug": "alfven-damping-mechanism",
  "kind": "inductive",
  "name": "AlfvenDampingMechanism",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 183,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L183-L192",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L183-L192",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L183-L192)
- Source range: L183-L192
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Damping mechanism for Alfven waves. -/
```

## Source Excerpt

```lean
inductive AlfvenDampingMechanism where
  /-- Ion-neutral friction (partially ionized plasmas). -/
  | IonNeutralFriction
  /-- Viscous dissipation. -/
  | Viscous
  /-- Resistive dissipation (finite conductivity). -/
  | Resistive
  /-- Phase mixing in inhomogeneous medium. -/
  | PhaseMixing
  deriving Repr, DecidableEq, BEq
```
