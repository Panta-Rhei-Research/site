---
{
  "projection_kind": "taulib_declaration",
  "title": "HubbleReadout",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/hubble-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::HubbleReadout",
  "declaration_slug": "hubble-readout",
  "kind": "structure",
  "name": "HubbleReadout",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 185,
  "source_line_end": 191,
  "registry_ids": [
    "V.D31"
  ],
  "related_registry_items": [
    {
      "id": "V.D31",
      "title": "Hubble Readout Parameter",
      "url": "/registry/object/V.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L185-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L185-L191",
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
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L185-L191)
- Source range: L185-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D31` — Hubble Readout Parameter

## Immediate Comment / Docstring

```lean
/-- [V.D31] Hubble readout H(n) := Δa/a per tick. NOT constant: decays
    with depth. Early (opening) H is large (inflation), late H is small.
    H(n) ~ 1 − ι_τ to leading order. -/
```

## Source Excerpt

```lean
structure HubbleReadout where
  depth : Nat
  depth_pos : depth > 0
  hubble_numer : Nat
  hubble_denom : Nat
  denom_pos : hubble_denom > 0
  deriving Repr
```
