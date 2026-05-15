---
{
  "projection_kind": "taulib_declaration",
  "title": "OperationalDistance",
  "permalink": "/corpus/taulib/docs/book-v-temporal-macro-readout/operational-distance/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::OperationalDistance",
  "declaration_slug": "operational-distance",
  "kind": "structure",
  "name": "OperationalDistance",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/corpus/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 100,
  "source_line_end": 108,
  "registry_ids": [
    "V.D28"
  ],
  "related_registry_items": [
    {
      "id": "V.D28",
      "title": "Operational Distance",
      "url": "/registry/object/V.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L100-L108",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L100-L108",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/corpus/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L100-L108)
- Source range: L100-L108
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D28` — Operational Distance

## Immediate Comment / Docstring

```lean
/-- [V.D28] Operational distance: tick count of the null intertwiner
    connecting two events at depth n₀. The τ-native spatial distance
    is NOT a primitive metric but a counting readout of null transport. -/
```

## Source Excerpt

```lean
structure OperationalDistance where
  /-- Reference depth for the measurement. -/
  ref_depth : Nat
  ref_depth_pos : ref_depth > 0
  /-- Distance numerator (tick count * scale). -/
  dist_numer : Nat
  dist_denom : Nat
  denom_pos : dist_denom > 0
  deriving Repr
```
