---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroColorConfinement",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-color-confinement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::MacroColorConfinement",
  "declaration_slug": "macro-color-confinement",
  "kind": "structure",
  "name": "MacroColorConfinement",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 204,
  "source_line_end": 211,
  "registry_ids": [
    "V.C12"
  ],
  "related_registry_items": [
    {
      "id": "V.C12",
      "title": "Macro color confinement",
      "url": "/registry/object/V.C12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L204-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L204-L211",
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
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L204-L211)
- Source range: L204-L211
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.C12` — Macro color confinement

## Immediate Comment / Docstring

```lean
/-- [V.C12] Macro color confinement: no macroscopic configuration carries
    a net color charge. Every hadron, nucleus, and astrophysical body is
    a color singlet.

    The C-sector contributes to the macro defect tuple only through
    confined composites (mesons, baryons) and cross-couplings κ(A,C)
    and κ(C,D). -/
```

## Source Excerpt

```lean
structure MacroColorConfinement where
  /-- Confinement level. -/
  level : ConfinementLevel
  /-- Net color charge is zero. -/
  net_color_zero : Bool := true
  /-- Only singlet composites are observable. -/
  singlet_only : Bool := true
  deriving Repr
```
