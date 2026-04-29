---
{
  "projection_kind": "taulib_declaration",
  "title": "ThreePolarityTerms",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/three-polarity-terms/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::ThreePolarityTerms",
  "declaration_slug": "three-polarity-terms",
  "kind": "structure",
  "name": "ThreePolarityTerms",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 55,
  "source_line_end": 58,
  "registry_ids": [
    "VI.D03"
  ],
  "related_registry_items": [
    {
      "id": "VI.D03",
      "title": "Three Polarity Terms",
      "url": "/registry/object/VI.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L55-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.ParityBridge",
        "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L55-L58",
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

- Module: [TauLib.BookVI.LifeCore.ParityBridge](/verify/taulib/docs/book-vi-life-core-parity-bridge/)
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L55-L58)
- Source range: L55-L58
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D03` — Three Polarity Terms

## Immediate Comment / Docstring

```lean
/-- [VI.D03] Three polarity terms: source, basin, stabilizer. -/
```

## Source Excerpt

```lean
structure ThreePolarityTerms where
  term_count : Nat
  count_eq : term_count = 3
  deriving Repr
```
