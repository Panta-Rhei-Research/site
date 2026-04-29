---
{
  "projection_kind": "taulib_declaration",
  "title": "api_scope_distribution",
  "permalink": "/verify/taulib/docs/book-v-temporal-cosmic-api/api-scope-distribution/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::api_scope_distribution",
  "declaration_slug": "api-scope-distribution",
  "kind": "theorem",
  "name": "api_scope_distribution",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/verify/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 152,
  "source_line_end": 155,
  "registry_ids": [
    "V.R52"
  ],
  "related_registry_items": [
    {
      "id": "V.R52",
      "title": "Scope census",
      "url": "/registry/object/V.R52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L152-L155",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L152-L155",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L152-L155)
- Source range: L152-L155
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R52` — Scope census

## Immediate Comment / Docstring

```lean
/-- [V.R52] Scope distribution: 19 τ-effective, 2 conjectural. -/
```

## Source Excerpt

```lean
theorem api_scope_distribution :
    (cosmic_stack_api.filter (·.scope == .TauEffective)).length = 19 ∧
    (cosmic_stack_api.filter (·.scope == .Conjectural)).length = 2 := by
  native_decide
```
