---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L202",
  "permalink": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l202/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::#eval:202",
  "declaration_slug": "eval-l202",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 202,
  "source_line_end": 202,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L202-L202",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L202-L202",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "role": "computed check",
      "status": "computed check"
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
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L202-L202)
- Source range: L202-L202
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- First and last API items
```

## Source Excerpt

```lean
#eval (cosmic_stack_api.head?).map (·.name)   -- "Base circle τ¹"
```
