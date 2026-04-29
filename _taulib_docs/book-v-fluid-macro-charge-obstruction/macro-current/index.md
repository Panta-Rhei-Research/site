---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroCurrent",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-current/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::MacroCurrent",
  "declaration_slug": "macro-current",
  "kind": "structure",
  "name": "MacroCurrent",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 226,
  "source_line_end": 233,
  "registry_ids": [
    "V.D103"
  ],
  "related_registry_items": [
    {
      "id": "V.D103",
      "title": "Macro current",
      "url": "/registry/object/V.D103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L226-L233",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L226-L233",
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
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L226-L233)
- Source range: L226-L233
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D103` — Macro current

## Immediate Comment / Docstring

```lean
/-- [V.D103] Macro current density: J^macro(x) = R_μ(q μ_B(x) v̂_B(x)),
    the readout of the B-sector mobility flow, where q is the local
    charge, μ_B is the B-sector mobility, and v̂_B is the unit velocity
    direction. -/
```

## Source Excerpt

```lean
structure MacroCurrent where
  /-- Local charge quantum number. -/
  charge : ChargeQuantum
  /-- B-sector mobility (scaled). -/
  mobility_scaled : Nat
  /-- Whether the current is conserved (∂_μ J^μ = 0). -/
  is_conserved : Bool := true
  deriving Repr
```
