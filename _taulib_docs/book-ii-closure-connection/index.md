---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Closure.Connection",
  "permalink": "/corpus/taulib/docs/book-ii-closure-connection/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Closure.Connection`.",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_slug": "book-ii-closure-connection",
  "book": "BookII",
  "family": "Closure",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Closure/Connection.lean",
  "sha256": "595ad786ee28a2c3df215b47e23b6bd6da7efe6700378819742b395cce217f88",
  "imports": [
    "TauLib.BookII.Closure.TauManifold"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Closure.Curvature"
  ],
  "registry_ids": [
    "II.D78",
    "II.D79",
    "II.P16",
    "II.T50"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 9,
    "theorem": 6,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauConnection",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/tau-connection/",
      "source_line_start": 54,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D78"
      ]
    },
    {
      "kind": "def",
      "name": "flat_connection",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D78"
      ]
    },
    {
      "kind": "def",
      "name": "connection_tower_check",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/connection-tower-check/",
      "source_line_start": 64,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D78"
      ]
    },
    {
      "kind": "def",
      "name": "connection_check",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/connection-check/",
      "source_line_start": 82,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D78"
      ]
    },
    {
      "kind": "def",
      "name": "parallel_transport",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/parallel-transport/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D79"
      ]
    },
    {
      "kind": "def",
      "name": "transport_in_range",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/transport-in-range/",
      "source_line_start": 103,
      "source_line_end": 106,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D79"
      ]
    },
    {
      "kind": "def",
      "name": "flatness_check_loop",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flatness-check-loop/",
      "source_line_start": 114,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T50"
      ]
    },
    {
      "kind": "def",
      "name": "flat_connection_check_stage",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection-check-stage/",
      "source_line_start": 121,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T50"
      ]
    },
    {
      "kind": "def",
      "name": "flat_connection_check",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection-check/",
      "source_line_start": 142,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T50"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_trivial_check",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-check/",
      "source_line_start": 158,
      "source_line_end": 178,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P16"
      ]
    },
    {
      "kind": "theorem",
      "name": "flat_connection_compatible_2",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection-compatible-2/",
      "source_line_start": 185,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D78"
      ]
    },
    {
      "kind": "theorem",
      "name": "flat_connection_flat_2",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection-flat-2/",
      "source_line_start": 189,
      "source_line_end": 190,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T50"
      ]
    },
    {
      "kind": "theorem",
      "name": "holonomy_trivial_1",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-1/",
      "source_line_start": 193,
      "source_line_end": 194,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.P16"
      ]
    },
    {
      "kind": "theorem",
      "name": "holonomy_trivial_2",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-2/",
      "source_line_start": 197,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.P16"
      ]
    },
    {
      "kind": "theorem",
      "name": "transport_zero",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/transport-zero/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "transport_empty",
      "url": "/corpus/taulib/docs/book-ii-closure-connection/transport-empty/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-connection/eval-l229/",
      "source_line_start": 229,
      "source_line_end": 231,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Closure/Connection.lean`
- SHA-256: `595ad786ee28a2c3df215b47e23b6bd6da7efe6700378819742b395cce217f88`

## Registry Links

- `II.D78` — τ-Connection
- `II.D79` — Parallel Transport
- `II.P16` — Holonomy Triviality
- `II.T50` — Flat Connection Existence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Closure.TauManifold`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Closure.Curvature`

## Declaration Counts

- `def`: 9
- `eval`: 7
- `structure`: 1
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauConnection](/corpus/taulib/docs/book-ii-closure-connection/tau-connection/) | L54-L55 | type/data schema | type/data schema | `II.D78` |
| `def` | [flat_connection](/corpus/taulib/docs/book-ii-closure-connection/flat-connection/) | L58-L59 | definition | definition | `II.D78` |
| `def` | [connection_tower_check](/corpus/taulib/docs/book-ii-closure-connection/connection-tower-check/) | L64-L79 | data/computed value | data/computed value | `II.D78` |
| `def` | [connection_check](/corpus/taulib/docs/book-ii-closure-connection/connection-check/) | L82-L89 | data/computed value | data/computed value | `II.D78` |
| `def` | [parallel_transport](/corpus/taulib/docs/book-ii-closure-connection/parallel-transport/) | L97-L99 | data/computed value | data/computed value | `II.D79` |
| `def` | [transport_in_range](/corpus/taulib/docs/book-ii-closure-connection/transport-in-range/) | L103-L106 | data/computed value | data/computed value | `II.D79` |
| `def` | [flatness_check_loop](/corpus/taulib/docs/book-ii-closure-connection/flatness-check-loop/) | L114-L117 | data/computed value | data/computed value | `II.T50` |
| `def` | [flat_connection_check_stage](/corpus/taulib/docs/book-ii-closure-connection/flat-connection-check-stage/) | L121-L139 | data/computed value | data/computed value | `II.T50` |
| `def` | [flat_connection_check](/corpus/taulib/docs/book-ii-closure-connection/flat-connection-check/) | L142-L149 | data/computed value | data/computed value | `II.T50` |
| `def` | [holonomy_trivial_check](/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-check/) | L158-L178 | data/computed value | data/computed value | `II.P16` |
| `theorem` | [flat_connection_compatible_2](/corpus/taulib/docs/book-ii-closure-connection/flat-connection-compatible-2/) | L185-L186 | proof obligation | formal proof obligation checked | `II.D78` |
| `theorem` | [flat_connection_flat_2](/corpus/taulib/docs/book-ii-closure-connection/flat-connection-flat-2/) | L189-L190 | proof obligation | formal proof obligation checked | `II.T50` |
| `theorem` | [holonomy_trivial_1](/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-1/) | L193-L194 | proof obligation | formal proof obligation checked | `II.P16` |
| `theorem` | [holonomy_trivial_2](/corpus/taulib/docs/book-ii-closure-connection/holonomy-trivial-2/) | L197-L198 | proof obligation | formal proof obligation checked | `II.P16` |
| `theorem` | [transport_zero](/corpus/taulib/docs/book-ii-closure-connection/transport-zero/) | L201-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [transport_empty](/corpus/taulib/docs/book-ii-closure-connection/transport-empty/) | L206-L208 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L215](/corpus/taulib/docs/book-ii-closure-connection/eval-l215/) | L215-L215 | computed check | computed check | — |
| `eval` | [#eval L216](/corpus/taulib/docs/book-ii-closure-connection/eval-l216/) | L216-L216 | computed check | computed check | — |
| `eval` | [#eval L219](/corpus/taulib/docs/book-ii-closure-connection/eval-l219/) | L219-L219 | computed check | computed check | — |
| `eval` | [#eval L222](/corpus/taulib/docs/book-ii-closure-connection/eval-l222/) | L222-L222 | computed check | computed check | — |
| `eval` | [#eval L225](/corpus/taulib/docs/book-ii-closure-connection/eval-l225/) | L225-L225 | computed check | computed check | — |
| `eval` | [#eval L228](/corpus/taulib/docs/book-ii-closure-connection/eval-l228/) | L228-L228 | computed check | computed check | — |
| `eval` | [#eval L229](/corpus/taulib/docs/book-ii-closure-connection/eval-l229/) | L229-L231 | computed check | computed check | — |
