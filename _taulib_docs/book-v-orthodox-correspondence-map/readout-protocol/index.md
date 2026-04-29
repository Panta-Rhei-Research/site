---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutProtocol",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/readout-protocol/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::ReadoutProtocol",
  "declaration_slug": "readout-protocol",
  "kind": "structure",
  "name": "ReadoutProtocol",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 180,
  "source_line_end": 191,
  "registry_ids": [
    "V.D187"
  ],
  "related_registry_items": [
    {
      "id": "V.D187",
      "title": "Readout interpretation protocol",
      "url": "/registry/object/V.D187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L180-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L180-L191",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L180-L191)
- Source range: L180-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D187` — Readout interpretation protocol

## Immediate Comment / Docstring

```lean
/-- [V.D187] Readout interpretation protocol: given an orthodox
    result R_orth, identify its ontic source and classify it.

    The protocol has three steps:
    1. Identify the boundary character(s) involved
    2. Trace through the chart projection
    3. Classify as faithful, partial, or artifact -/
```

## Source Excerpt

```lean
structure ReadoutProtocol where
  /-- Number of protocol steps. -/
  step_count : Nat
  /-- Always 3 steps. -/
  step_eq : step_count = 3
  /-- Step 1: identify boundary character. -/
  identify_source : Bool := true
  /-- Step 2: trace chart projection. -/
  trace_projection : Bool := true
  /-- Step 3: classify result. -/
  classify_result : Bool := true
  deriving Repr
```
