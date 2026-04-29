---
{
  "projection_kind": "taulib_declaration",
  "title": "EWPrediction",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/ewprediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::EWPrediction",
  "declaration_slug": "ewprediction",
  "kind": "structure",
  "name": "EWPrediction",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 254,
  "source_line_end": 263,
  "registry_ids": [
    "IV.P65"
  ],
  "related_registry_items": [
    {
      "id": "IV.P65",
      "title": "Electroweak Coupling Summary",
      "url": "/registry/object/IV.P65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L254-L263",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L254-L263",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L254-L263)
- Source range: L254-L263
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P65` — Electroweak Coupling Summary

## Immediate Comment / Docstring

```lean
/-- [IV.P65] Electroweak prediction summary table: key observables
    and their tau-framework status. -/
```

## Source Excerpt

```lean
structure EWPrediction where
  /-- Observable name. -/
  name : String
  /-- Predicted value (scaled Nat). -/
  predicted : Nat
  /-- Observed value (scaled Nat). -/
  observed : Nat
  /-- Scale factor description. -/
  scale : String
  deriving Repr
```
