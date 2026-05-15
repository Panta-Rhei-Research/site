---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.MacroReadout",
  "permalink": "/corpus/taulib/docs/book-v-temporal-macro-readout/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.MacroReadout`.",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_slug": "book-v-temporal-macro-readout",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/MacroReadout.lean",
  "sha256": "d145fe8e6f6ef693781ec1750fb379cc0c863e5acdef691bd70072f4c072ee65",
  "imports": [
    "TauLib.BookV.Temporal.HighEnergy",
    "TauLib.BookIV.Sectors.SectorParameters",
    "TauLib.BookIV.Physics.QuantityFramework"
  ],
  "imported_by": [
    "TauLib.BookV"
  ],
  "registry_ids": [
    "V.D27",
    "V.D28",
    "V.D29",
    "V.D30",
    "V.D31",
    "V.P06",
    "V.T14",
    "V.T15",
    "V.T16"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 5,
    "theorem": 8,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "NullIntertwiner",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/null-intertwiner/",
      "source_line_start": 39,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D27"
      ]
    },
    {
      "kind": "def",
      "name": "photon_null",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/photon-null/",
      "source_line_start": 55,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "boundary_supports_null",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/boundary-supports-null/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T14"
      ]
    },
    {
      "kind": "theorem",
      "name": "null_selects_em",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/null-selects-em/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P06"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_unique_null",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/em-unique-null/",
      "source_line_start": 86,
      "source_line_end": 91,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OperationalDistance",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/operational-distance/",
      "source_line_start": 100,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D28"
      ]
    },
    {
      "kind": "def",
      "name": "OperationalDistance.toFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/to-float/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distance_time_dual",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/distance-time-dual/",
      "source_line_start": 121,
      "source_line_end": 125,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T15"
      ]
    },
    {
      "kind": "structure",
      "name": "RefinementDrift",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/refinement-drift/",
      "source_line_start": 135,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D29"
      ]
    },
    {
      "kind": "def",
      "name": "RefinementDrift.depth_diff",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/depth-diff/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "drift_formula_positive",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/drift-formula-positive/",
      "source_line_start": 154,
      "source_line_end": 157,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T16"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutExpansion",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/readout-expansion/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D30"
      ]
    },
    {
      "kind": "def",
      "name": "ReadoutExpansion.toFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/to-float-l175/",
      "source_line_start": 175,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HubbleReadout",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/hubble-readout/",
      "source_line_start": 185,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D31"
      ]
    },
    {
      "kind": "def",
      "name": "HubbleReadout.toFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/to-float-l194/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "null_structural",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/null-structural/",
      "source_line_start": 202,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "null_transport_scale",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/null-transport-scale/",
      "source_line_start": 207,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "redshift_requires_earlier",
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/redshift-requires-earlier/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l222/",
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
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l230/",
      "source_line_start": 230,
      "source_line_end": 233,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean",
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
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/MacroReadout.lean`
- SHA-256: `d145fe8e6f6ef693781ec1750fb379cc0c863e5acdef691bd70072f4c072ee65`

## Registry Links

- `V.D27` — Null Intertwiner (Photon)
- `V.D28` — Operational Distance
- `V.D29` — Refinement Drift (Redshift)
- `V.D30` — Readout Expansion
- `V.D31` — Hubble Readout Parameter
- `V.P06` — Null Character Uniqueness
- `V.T14` — Photon Existence Theorem
- `V.T15` — Distance-Duration Duality
- `V.T16` — Redshift-Depth Relation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.HighEnergy`
- `TauLib.BookIV.Sectors.SectorParameters`
- `TauLib.BookIV.Physics.QuantityFramework`

## Imported By

- `TauLib.BookV`

## Declaration Counts

- `def`: 5
- `eval`: 6
- `structure`: 5
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [NullIntertwiner](/corpus/taulib/docs/book-v-temporal-macro-readout/null-intertwiner/) | L39-L52 | type/data schema | type/data schema | `V.D27` |
| `def` | [photon_null](/corpus/taulib/docs/book-v-temporal-macro-readout/photon-null/) | L55-L61 | definition | definition | — |
| `theorem` | [boundary_supports_null](/corpus/taulib/docs/book-v-temporal-macro-readout/boundary-supports-null/) | L69-L73 | proof obligation | formal proof obligation checked | `V.T14` |
| `theorem` | [null_selects_em](/corpus/taulib/docs/book-v-temporal-macro-readout/null-selects-em/) | L82-L83 | proof obligation | formal proof obligation checked | `V.P06` |
| `theorem` | [em_unique_null](/corpus/taulib/docs/book-v-temporal-macro-readout/em-unique-null/) | L86-L91 | proof obligation | formal proof obligation checked | — |
| `structure` | [OperationalDistance](/corpus/taulib/docs/book-v-temporal-macro-readout/operational-distance/) | L100-L108 | type/data schema | type/data schema | `V.D28` |
| `def` | [OperationalDistance.toFloat](/corpus/taulib/docs/book-v-temporal-macro-readout/to-float/) | L111-L112 | data/computed value | data/computed value | — |
| `theorem` | [distance_time_dual](/corpus/taulib/docs/book-v-temporal-macro-readout/distance-time-dual/) | L121-L125 | proof obligation | formal proof obligation checked | `V.T15` |
| `structure` | [RefinementDrift](/corpus/taulib/docs/book-v-temporal-macro-readout/refinement-drift/) | L135-L142 | type/data schema | type/data schema | `V.D29` |
| `def` | [RefinementDrift.depth_diff](/corpus/taulib/docs/book-v-temporal-macro-readout/depth-diff/) | L145-L146 | data/computed value | data/computed value | — |
| `theorem` | [drift_formula_positive](/corpus/taulib/docs/book-v-temporal-macro-readout/drift-formula-positive/) | L154-L157 | proof obligation | formal proof obligation checked | `V.T16` |
| `structure` | [ReadoutExpansion](/corpus/taulib/docs/book-v-temporal-macro-readout/readout-expansion/) | L166-L172 | type/data schema | type/data schema | `V.D30` |
| `def` | [ReadoutExpansion.toFloat](/corpus/taulib/docs/book-v-temporal-macro-readout/to-float-l175/) | L175-L176 | data/computed value | data/computed value | — |
| `structure` | [HubbleReadout](/corpus/taulib/docs/book-v-temporal-macro-readout/hubble-readout/) | L185-L191 | type/data schema | type/data schema | `V.D31` |
| `def` | [HubbleReadout.toFloat](/corpus/taulib/docs/book-v-temporal-macro-readout/to-float-l194/) | L194-L195 | data/computed value | data/computed value | — |
| `theorem` | [null_structural](/corpus/taulib/docs/book-v-temporal-macro-readout/null-structural/) | L202-L204 | proof obligation | formal proof obligation checked | — |
| `theorem` | [null_transport_scale](/corpus/taulib/docs/book-v-temporal-macro-readout/null-transport-scale/) | L207-L210 | proof obligation | formal proof obligation checked | — |
| `theorem` | [redshift_requires_earlier](/corpus/taulib/docs/book-v-temporal-macro-readout/redshift-requires-earlier/) | L213-L214 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L220](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l220/) | L220-L220 | computed check | computed check | — |
| `eval` | [#eval L221](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l221/) | L221-L221 | computed check | computed check | — |
| `eval` | [#eval L222](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l222/) | L222-L222 | computed check | computed check | — |
| `eval` | [#eval L223](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l223/) | L223-L223 | computed check | computed check | — |
| `eval` | [#eval L226](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l226/) | L226-L226 | computed check | computed check | — |
| `eval` | [#eval L230](/corpus/taulib/docs/book-v-temporal-macro-readout/eval-l230/) | L230-L233 | computed check | computed check | — |
