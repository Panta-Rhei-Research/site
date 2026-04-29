---
{
  "projection_kind": "taulib_declaration",
  "title": "NullIntertwiner",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/null-intertwiner/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::NullIntertwiner",
  "declaration_slug": "null-intertwiner",
  "kind": "structure",
  "name": "NullIntertwiner",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 39,
  "source_line_end": 52,
  "registry_ids": [
    "V.D27"
  ],
  "related_registry_items": [
    {
      "id": "V.D27",
      "title": "Null Intertwiner (Photon)",
      "url": "/registry/object/V.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L39-L52",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L39-L52",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L39-L52)
- Source range: L39-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D27` — Null Intertwiner (Photon)

## Immediate Comment / Docstring

```lean
/-- [V.D27] Null intertwiner: massless morphism in boundary holonomy.
    Null transport moves along base τ¹ at c_τ. Sector B (EM) is
    uniquely selected by the null (zero fiber stiffness) condition. -/
```

## Source Excerpt

```lean
structure NullIntertwiner where
  /-- The sector supporting this null intertwiner. -/
  sector : Sector
  /-- Null selects EM. -/
  null_is_em : sector = .B
  /-- The carrier type (always Base for null transport). -/
  carrier : CarrierType
  /-- Null transport is base-only. -/
  carrier_is_base : carrier = .Base
  /-- Massless flag. -/
  massless : Bool
  /-- Must be massless. -/
  massless_true : massless = true
  deriving Repr
```
