---
{
  "projection_kind": "taulib_declaration",
  "title": "ConsumerBridgeE3",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/consumer-bridge-e3/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::ConsumerBridgeE3",
  "declaration_slug": "consumer-bridge-e3",
  "kind": "structure",
  "name": "ConsumerBridgeE3",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 69,
  "source_line_end": 72,
  "registry_ids": [
    "VI.L07"
  ],
  "related_registry_items": [
    {
      "id": "VI.L07",
      "title": "Consumer as Bridge-Head to E₃",
      "url": "/registry/object/VI.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L69-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Absence",
        "url": "/verify/taulib/docs/book-vi-sectors-absence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L69-L72",
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

- Module: [TauLib.BookVI.Sectors.Absence](/verify/taulib/docs/book-vi-sectors-absence/)
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L69-L72)
- Source range: L69-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L07` — Consumer as Bridge-Head to E₃

## Immediate Comment / Docstring

```lean
/-- [VI.L07] Consumer sector is unique bridge-head to E₃. -/
```

## Source Excerpt

```lean
structure ConsumerBridgeE3 where
  has_eval_squared : Bool := true
  consumer_only : Bool := true
  deriving Repr
```
