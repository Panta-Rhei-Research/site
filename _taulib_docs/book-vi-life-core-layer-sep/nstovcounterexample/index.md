---
{
  "projection_kind": "taulib_declaration",
  "title": "NSTOVCounterexample",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/nstovcounterexample/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::NSTOVCounterexample",
  "declaration_slug": "nstovcounterexample",
  "kind": "structure",
  "name": "NSTOVCounterexample",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 24,
  "source_line_end": 29,
  "registry_ids": [
    "VI.L02"
  ],
  "related_registry_items": [
    {
      "id": "VI.L02",
      "title": "NS-TOV Counterexample",
      "url": "/registry/object/VI.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L24-L29",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.LayerSep",
        "url": "/verify/taulib/docs/book-vi-life-core-layer-sep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L24-L29",
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

- Module: [TauLib.BookVI.LifeCore.LayerSep](/verify/taulib/docs/book-vi-life-core-layer-sep/)
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L24-L29)
- Source range: L24-L29
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L02` — NS-TOV Counterexample

## Immediate Comment / Docstring

```lean
/-- [VI.L02] NS-TOV counterexample: passes all 5 distinction conditions,
    fails SelfDesc due to oscillatory boundary instability. -/
```

## Source Excerpt

```lean
structure NSTOVCounterexample where
  distinction_passed : Nat
  all_five : distinction_passed = 5
  selfdesc_fails : Bool := true
  failure_reason : String := "oscillatory-boundary-instability"
  deriving Repr
```
