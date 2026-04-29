---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroThreeConditions",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-conditions/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::MacroThreeConditions",
  "declaration_slug": "macro-three-conditions",
  "kind": "structure",
  "name": "MacroThreeConditions",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 162,
  "source_line_end": 169,
  "registry_ids": [
    "V.T70"
  ],
  "related_registry_items": [
    {
      "id": "V.T70",
      "title": "Macro three-condition sufficiency",
      "url": "/registry/object/V.T70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L162-L169",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L162-L169",
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
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L162-L169)
- Source range: L162-L169
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T70` — Macro three-condition sufficiency

## Immediate Comment / Docstring

```lean
/-- [V.T70] Macro three-condition sufficiency: the macro defect-transport
    equation satisfies conditions (C1), (C2), (C3) of III.T25 at
    the macroscopic scale. -/
```

## Source Excerpt

```lean
structure MacroThreeConditions where
  /-- C1 holds. -/
  c1_clopen_locality : Bool := true
  /-- C2 holds. -/
  c2_bounded_extraction : Bool := true
  /-- C3 holds. -/
  c3_defect_contractivity : Bool := true
  deriving Repr
```
