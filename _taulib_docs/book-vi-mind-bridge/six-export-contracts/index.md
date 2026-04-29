---
{
  "projection_kind": "taulib_declaration",
  "title": "SixExportContracts",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/six-export-contracts/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::SixExportContracts",
  "declaration_slug": "six-export-contracts",
  "kind": "structure",
  "name": "SixExportContracts",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 144,
  "source_line_end": 151,
  "registry_ids": [
    "VI.T40"
  ],
  "related_registry_items": [
    {
      "id": "VI.T40",
      "title": "Six Export Contracts to Book VII",
      "url": "/registry/object/VI.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L144-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L144-L151",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L144-L151)
- Source range: L144-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T40` — Six Export Contracts to Book VII

## Immediate Comment / Docstring

```lean
/-- [VI.T40] Six Export Contracts to Book VII.
    Book VI delivers exactly 6 results to Book VII:
    (1) Life = Distinction AND SelfDesc (VI.T01)
    (2) 4+1 sector classification (VI.T07)
    (3) Consumer = mixed sector (VI.D46)
    (4) Consciousness = mixed-sector self-modeling (VI.T38)
    (5) Language = shared code (VI.T39)
    (6) ω-germ code as identity criterion (VI.D53)
    All 6 are delivered (established). -/
```

## Source Excerpt

```lean
structure SixExportContracts where
  /-- Number of export contracts. -/
  export_count : Nat
  /-- Exactly 6 contracts. -/
  count_eq : export_count = 6
  /-- All contracts delivered. -/
  all_delivered : Bool := true
  deriving Repr
```
