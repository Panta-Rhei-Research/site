---
{
  "projection_kind": "taulib_declaration",
  "title": "APIScope",
  "permalink": "/corpus/taulib/docs/book-v-temporal-cosmic-api/apiscope/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::APIScope",
  "declaration_slug": "apiscope",
  "kind": "inductive",
  "name": "APIScope",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 56,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L56-L59",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.CosmicAPI",
        "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L56-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Temporal.CosmicAPI](/corpus/taulib/docs/book-v-temporal-cosmic-api/)
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L56-L59)
- Source range: L56-L59
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Scope of an API item (simplified for Part I). -/
```

## Source Excerpt

```lean
inductive APIScope where
  | TauEffective
  | Conjectural
  deriving Repr, DecidableEq, BEq
```
