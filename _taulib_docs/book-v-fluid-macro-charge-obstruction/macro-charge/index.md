---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroCharge",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-charge/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::MacroCharge",
  "declaration_slug": "macro-charge",
  "kind": "structure",
  "name": "MacroCharge",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 72,
  "source_line_end": 79,
  "registry_ids": [
    "V.D101"
  ],
  "related_registry_items": [
    {
      "id": "V.D101",
      "title": "Macro charge",
      "url": "/registry/object/V.D101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L72-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L72-L79",
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
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L72-L79)
- Source range: L72-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D101` — Macro charge

## Immediate Comment / Docstring

```lean
/-- [V.D101] Macro charge: Q^macro = ∫_{τ¹} Hol_B(d|_{t × T²}) dt,
    the base-integrated B-sector holonomy obstruction.

    The macroscopic charge is the total boundary obstruction accumulated
    over the temporal circle. -/
```

## Source Excerpt

```lean
structure MacroCharge where
  /-- Charge value (integer in natural units). -/
  value : Int
  /-- Which sector. -/
  sector : ChargeSector := .BSector
  /-- Whether this is a local charge (within a region). -/
  is_local : Bool
  deriving Repr, DecidableEq, BEq
```
