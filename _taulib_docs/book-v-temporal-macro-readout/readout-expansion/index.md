---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutExpansion",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/readout-expansion/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::ReadoutExpansion",
  "declaration_slug": "readout-expansion",
  "kind": "structure",
  "name": "ReadoutExpansion",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 166,
  "source_line_end": 172,
  "registry_ids": [
    "V.D30"
  ],
  "related_registry_items": [
    {
      "id": "V.D30",
      "title": "Readout Expansion",
      "url": "/registry/object/V.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L166-L172",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L166-L172",
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
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L166-L172)
- Source range: L166-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D30` — Readout Expansion

## Immediate Comment / Docstring

```lean
/-- [V.D30] Readout expansion a(n) ~ ι_τ^(-n): cumulative proper-time
    scaling. The universe "expands" because the tower deepens and
    proper-time increments shrink — not because space stretches. -/
```

## Source Excerpt

```lean
structure ReadoutExpansion where
  depth : Nat
  depth_pos : depth > 0
  expansion_numer : Nat
  expansion_denom : Nat
  denom_pos : expansion_denom > 0
  deriving Repr
```
