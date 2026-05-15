---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.BaseCircle",
  "permalink": "/corpus/taulib/docs/book-v-temporal-base-circle/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.BaseCircle`.",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_slug": "book-v-temporal-base-circle",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/BaseCircle.lean",
  "sha256": "cf6bcb8470c9bff6d12bc3e7820df930f5a1beb292e31542702755bee0a99cbd",
  "imports": [
    "TauLib.BookIV.Arena.RefinementTower",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Temporal.TemporalIgnition"
  ],
  "registry_ids": [
    "V.D15",
    "V.D16",
    "V.D17",
    "V.D18",
    "V.D19",
    "V.P03",
    "V.T08",
    "V.T09",
    "V.T10"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 4,
    "theorem": 8,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BaseCircle",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/base-circle/",
      "source_line_start": 74,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D15"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_base_circle",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/canonical-base-circle/",
      "source_line_start": 85,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlphaTick",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick/",
      "source_line_start": 102,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D16"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_tick_at",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick-at/",
      "source_line_start": 112,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tick_causal",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick-causal/",
      "source_line_start": 118,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ProperTimeSeries",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/proper-time-series/",
      "source_line_start": 135,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D17"
      ]
    },
    {
      "kind": "def",
      "name": "ProperTimeSeries.toFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/to-float/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "physical_time_derived",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/physical-time-derived/",
      "source_line_start": 168,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T08"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_direction",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/temporal-direction/",
      "source_line_start": 188,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P03"
      ]
    },
    {
      "kind": "theorem",
      "name": "causal_ordering_enforced",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/causal-ordering-enforced/",
      "source_line_start": 209,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T09"
      ]
    },
    {
      "kind": "theorem",
      "name": "causal_transitive",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/causal-transitive/",
      "source_line_start": 214,
      "source_line_end": 216,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "causal_irreflexive",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/causal-irreflexive/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeodesicDuration",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/geodesic-duration/",
      "source_line_start": 232,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D19"
      ]
    },
    {
      "kind": "def",
      "name": "GeodesicDuration.tick_count",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/tick-count/",
      "source_line_start": 242,
      "source_line_end": 243,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geodesic_positive",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/geodesic-positive/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "total_proper_time_bounded",
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/total-proper-time-bounded/",
      "source_line_start": 265,
      "source_line_end": 272,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T10"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l281/",
      "source_line_start": 281,
      "source_line_end": 281,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l282/",
      "source_line_start": 282,
      "source_line_end": 282,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-base-circle/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 289,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean",
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
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/BaseCircle.lean`
- SHA-256: `cf6bcb8470c9bff6d12bc3e7820df930f5a1beb292e31542702755bee0a99cbd`

## Registry Links

- `V.D15` — Base Circle tau^1 (Macroscopic)
- `V.D16` — Alpha-Tick
- `V.D17` — Proper Time (Arc Length)
- `V.D18` — Causal Ordering Relation
- `V.D19` — Geodesic Duration
- `V.P03` — Arrow of Time = Orbit Direction
- `V.T08` — Time Derivation Theorem
- `V.T09` — Causal Ordering Theorem
- `V.T10` — Bounded Time Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.RefinementTower`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Temporal.TemporalIgnition`

## Declaration Counts

- `def`: 4
- `eval`: 7
- `structure`: 4
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BaseCircle](/corpus/taulib/docs/book-v-temporal-base-circle/base-circle/) | L74-L82 | type/data schema | type/data schema | `V.D15` |
| `def` | [canonical_base_circle](/corpus/taulib/docs/book-v-temporal-base-circle/canonical-base-circle/) | L85-L89 | definition | definition | — |
| `structure` | [AlphaTick](/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick/) | L102-L109 | type/data schema | type/data schema | `V.D16` |
| `def` | [alpha_tick_at](/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick-at/) | L112-L115 | data/computed value | data/computed value | — |
| `theorem` | [alpha_tick_causal](/corpus/taulib/docs/book-v-temporal-base-circle/alpha-tick-causal/) | L118-L120 | proof obligation | formal proof obligation checked | — |
| `structure` | [ProperTimeSeries](/corpus/taulib/docs/book-v-temporal-base-circle/proper-time-series/) | L135-L146 | type/data schema | type/data schema | `V.D17` |
| `def` | [ProperTimeSeries.toFloat](/corpus/taulib/docs/book-v-temporal-base-circle/to-float/) | L149-L150 | data/computed value | data/computed value | — |
| `theorem` | [physical_time_derived](/corpus/taulib/docs/book-v-temporal-base-circle/physical-time-derived/) | L168-L175 | proof obligation | formal proof obligation checked | `V.T08` |
| `theorem` | [temporal_direction](/corpus/taulib/docs/book-v-temporal-base-circle/temporal-direction/) | L188-L191 | proof obligation | formal proof obligation checked | `V.P03` |
| `theorem` | [causal_ordering_enforced](/corpus/taulib/docs/book-v-temporal-base-circle/causal-ordering-enforced/) | L209-L211 | proof obligation | formal proof obligation checked | `V.T09` |
| `theorem` | [causal_transitive](/corpus/taulib/docs/book-v-temporal-base-circle/causal-transitive/) | L214-L216 | proof obligation | formal proof obligation checked | — |
| `theorem` | [causal_irreflexive](/corpus/taulib/docs/book-v-temporal-base-circle/causal-irreflexive/) | L219-L220 | proof obligation | formal proof obligation checked | — |
| `structure` | [GeodesicDuration](/corpus/taulib/docs/book-v-temporal-base-circle/geodesic-duration/) | L232-L239 | type/data schema | type/data schema | `V.D19` |
| `def` | [GeodesicDuration.tick_count](/corpus/taulib/docs/book-v-temporal-base-circle/tick-count/) | L242-L243 | data/computed value | data/computed value | — |
| `theorem` | [geodesic_positive](/corpus/taulib/docs/book-v-temporal-base-circle/geodesic-positive/) | L246-L249 | proof obligation | formal proof obligation checked | — |
| `theorem` | [total_proper_time_bounded](/corpus/taulib/docs/book-v-temporal-base-circle/total-proper-time-bounded/) | L265-L272 | proof obligation | formal proof obligation checked | `V.T10` |
| `eval` | [#eval L278](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l279/) | L279-L279 | computed check | computed check | — |
| `eval` | [#eval L280](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l280/) | L280-L280 | computed check | computed check | — |
| `eval` | [#eval L281](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l281/) | L281-L281 | computed check | computed check | — |
| `eval` | [#eval L282](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l282/) | L282-L282 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-v-temporal-base-circle/eval-l287/) | L287-L289 | computed check | computed check | — |
