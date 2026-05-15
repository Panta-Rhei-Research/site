---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.CosmicAPI",
  "permalink": "/corpus/taulib/docs/book-v-temporal-cosmic-api/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.CosmicAPI`.",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_slug": "book-v-temporal-cosmic-api",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/CosmicAPI.lean",
  "sha256": "c79074e5d465528fef3d94ec25e0de02061484fddde73fb7faaeea7bc9b991c5",
  "imports": [
    "TauLib.BookV.Temporal.BoundaryData"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.FrameHolonomy"
  ],
  "registry_ids": [
    "V.D40",
    "V.R52"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 2,
    "def": 2,
    "theorem": 8,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "APIScope",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/apiscope/",
      "source_line_start": 56,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "APIItem",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/apiitem/",
      "source_line_start": 66,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cosmic_stack_api",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api/",
      "source_line_start": 91,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.D40"
      ]
    },
    {
      "kind": "structure",
      "name": "CosmicStackAPI",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api-l126/",
      "source_line_start": 126,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D40"
      ]
    },
    {
      "kind": "def",
      "name": "cosmic_stack_summary",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-summary/",
      "source_line_start": 138,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "api_item_count",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/api-item-count/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.D40"
      ]
    },
    {
      "kind": "theorem",
      "name": "api_scope_distribution",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/api-scope-distribution/",
      "source_line_start": 152,
      "source_line_end": 155,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R52"
      ]
    },
    {
      "kind": "theorem",
      "name": "api_complete",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/api-complete/",
      "source_line_start": 158,
      "source_line_end": 162,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "summary_matches_list",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/summary-matches-list/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_items_have_ids",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/all-items-have-ids/",
      "source_line_start": 169,
      "source_line_end": 170,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_items_have_names",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/all-items-have-names/",
      "source_line_start": 173,
      "source_line_end": 174,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "conjectural_items_identified",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/conjectural-items-identified/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "minimum_id_length",
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/minimum-id-length/",
      "source_line_start": 182,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l193/",
      "source_line_start": 193,
      "source_line_end": 193,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 197,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l198/",
      "source_line_start": 198,
      "source_line_end": 198,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l199/",
      "source_line_start": 199,
      "source_line_end": 199,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l202/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l203/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    }
  ],
  "right_rail": {
    "related": [
      {
        "title": "TauLib Overview",
        "url": "/verify/taulib/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Module",
      "source": "Corpus projection",
      "commit": "cb5e8301"
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
  "type": "TauLib Module"
}
---

## Corpus TauLib Projection

This page is generated directly from the pinned TauLib Lean source snapshot in `corpus/taulib-sources/project`. It is a Corpus-native module view designed for cross-linking Registry, Construction Spine, Results, and Verify surfaces.

## Source Provenance

- Source repository: `Panta-Rhei-Research/taulib`
- Source commit: [`cb5e8301`](https://github.com/Panta-Rhei-Research/taulib/commit/cb5e83015b54dd72eba560953fe2461820078757)
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/CosmicAPI.lean`
- SHA-256: `c79074e5d465528fef3d94ec25e0de02061484fddde73fb7faaeea7bc9b991c5`

## Registry Links

- `V.D40` — Cosmic Stack API
- `V.R52` — Scope census

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.BoundaryData`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.FrameHolonomy`

## Declaration Counts

- `def`: 2
- `eval`: 8
- `inductive`: 1
- `structure`: 2
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [APIScope](/corpus/taulib/docs/book-v-temporal-cosmic-api/apiscope/) | L56-L59 | type/data schema | type/data schema | — |
| `structure` | [APIItem](/corpus/taulib/docs/book-v-temporal-cosmic-api/apiitem/) | L66-L73 | type/data schema | type/data schema | — |
| `def` | [cosmic_stack_api](/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api/) | L91-L118 | data/computed value | data/computed value | `V.D40` |
| `structure` | [CosmicStackAPI](/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api-l126/) | L126-L135 | type/data schema | type/data schema | `V.D40` |
| `def` | [cosmic_stack_summary](/corpus/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-summary/) | L138-L142 | definition | definition | — |
| `theorem` | [api_item_count](/corpus/taulib/docs/book-v-temporal-cosmic-api/api-item-count/) | L149-L149 | proof obligation | formal proof obligation checked | `V.D40` |
| `theorem` | [api_scope_distribution](/corpus/taulib/docs/book-v-temporal-cosmic-api/api-scope-distribution/) | L152-L155 | proof obligation | formal proof obligation checked | `V.R52` |
| `theorem` | [api_complete](/corpus/taulib/docs/book-v-temporal-cosmic-api/api-complete/) | L158-L162 | proof obligation | formal proof obligation checked | — |
| `theorem` | [summary_matches_list](/corpus/taulib/docs/book-v-temporal-cosmic-api/summary-matches-list/) | L165-L166 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_items_have_ids](/corpus/taulib/docs/book-v-temporal-cosmic-api/all-items-have-ids/) | L169-L170 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_items_have_names](/corpus/taulib/docs/book-v-temporal-cosmic-api/all-items-have-names/) | L173-L174 | proof obligation | formal proof obligation checked | — |
| `theorem` | [conjectural_items_identified](/corpus/taulib/docs/book-v-temporal-cosmic-api/conjectural-items-identified/) | L177-L179 | proof obligation | formal proof obligation checked | — |
| `theorem` | [minimum_id_length](/corpus/taulib/docs/book-v-temporal-cosmic-api/minimum-id-length/) | L182-L183 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L190](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l190/) | L190-L190 | computed check | computed check | — |
| `eval` | [#eval L193](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l193/) | L193-L193 | computed check | computed check | — |
| `eval` | [#eval L194](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l194/) | L194-L194 | computed check | computed check | — |
| `eval` | [#eval L197](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l197/) | L197-L197 | computed check | computed check | — |
| `eval` | [#eval L198](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l198/) | L198-L198 | computed check | computed check | — |
| `eval` | [#eval L199](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l199/) | L199-L199 | computed check | computed check | — |
| `eval` | [#eval L202](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l202/) | L202-L202 | computed check | computed check | — |
| `eval` | [#eval L203](/corpus/taulib/docs/book-v-temporal-cosmic-api/eval-l203/) | L203-L205 | computed check | computed check | — |
