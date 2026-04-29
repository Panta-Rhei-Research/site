---
{
  "projection_kind": "taulib_declaration",
  "title": "APIItem",
  "permalink": "/verify/taulib/docs/book-v-temporal-cosmic-api/apiitem/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::APIItem",
  "declaration_slug": "apiitem",
  "kind": "structure",
  "name": "APIItem",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/verify/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 66,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L66-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.CosmicAPI",
        "url": "/verify/taulib/docs/book-v-temporal-cosmic-api/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L66-L73",
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

- Module: [TauLib.BookV.Temporal.CosmicAPI](/verify/taulib/docs/book-v-temporal-cosmic-api/)
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L66-L73)
- Source range: L66-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A single item in the Cosmic Stack API. -/
```

## Source Excerpt

```lean
structure APIItem where
  /-- Registry ID (e.g., "V.D15"). -/
  id : String
  /-- Display name. -/
  name : String
  /-- Scope label. -/
  scope : APIScope
  deriving Repr
```
