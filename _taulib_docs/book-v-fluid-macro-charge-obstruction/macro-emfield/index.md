---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroEMField",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-emfield/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::MacroEMField",
  "declaration_slug": "macro-emfield",
  "kind": "structure",
  "name": "MacroEMField",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 170,
  "source_line_end": 177,
  "registry_ids": [
    "V.D102"
  ],
  "related_registry_items": [
    {
      "id": "V.D102",
      "title": "Macro EM field",
      "url": "/registry/object/V.D102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L170-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
        "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L170-L177",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L170-L177)
- Source range: L170-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D102` — Macro EM field

## Immediate Comment / Docstring

```lean
/-- [V.D102] Macro EM field: the chart-level readout of the B-sector
    defect components integrated over the base τ¹.

    F_μν^macro(x) = R_μ(∫_{τ¹} D_B(t, x) dt)

    Provides the macroscopic electromagnetic field tensor. -/
```

## Source Excerpt

```lean
structure MacroEMField where
  /-- Number of nonzero field components. -/
  nonzero_components : Nat
  /-- Whether the field satisfies Maxwell equations. -/
  satisfies_maxwell : Bool := true
  /-- Whether the field is sourceless globally. -/
  globally_sourceless : Bool := true
  deriving Repr
```
