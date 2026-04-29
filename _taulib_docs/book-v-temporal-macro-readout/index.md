---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.MacroReadout",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/",
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
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/null-intertwiner/",
      "source_line_start": 39,
      "source_line_end": 52,
      "formal_status": "defined",
      "registry_ids": [
        "V.D27"
      ]
    },
    {
      "kind": "def",
      "name": "photon_null",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/photon-null/",
      "source_line_start": 55,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "boundary_supports_null",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/boundary-supports-null/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T14"
      ]
    },
    {
      "kind": "theorem",
      "name": "null_selects_em",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/null-selects-em/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P06"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_unique_null",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/em-unique-null/",
      "source_line_start": 86,
      "source_line_end": 91,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OperationalDistance",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/operational-distance/",
      "source_line_start": 100,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": [
        "V.D28"
      ]
    },
    {
      "kind": "def",
      "name": "OperationalDistance.toFloat",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/to-float/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distance_time_dual",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/distance-time-dual/",
      "source_line_start": 121,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T15"
      ]
    },
    {
      "kind": "structure",
      "name": "RefinementDrift",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/refinement-drift/",
      "source_line_start": 135,
      "source_line_end": 142,
      "formal_status": "defined",
      "registry_ids": [
        "V.D29"
      ]
    },
    {
      "kind": "def",
      "name": "RefinementDrift.depth_diff",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/depth-diff/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "drift_formula_positive",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/drift-formula-positive/",
      "source_line_start": 154,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T16"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutExpansion",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/readout-expansion/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": [
        "V.D30"
      ]
    },
    {
      "kind": "def",
      "name": "ReadoutExpansion.toFloat",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/to-float-l175/",
      "source_line_start": 175,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HubbleReadout",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/hubble-readout/",
      "source_line_start": 185,
      "source_line_end": 191,
      "formal_status": "defined",
      "registry_ids": [
        "V.D31"
      ]
    },
    {
      "kind": "def",
      "name": "HubbleReadout.toFloat",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/to-float-l194/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "null_structural",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/null-structural/",
      "source_line_start": 202,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "null_transport_scale",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/null-transport-scale/",
      "source_line_start": 207,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "redshift_requires_earlier",
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/redshift-requires-earlier/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-macro-readout/eval-l230/",
      "source_line_start": 230,
      "source_line_end": 233,
      "formal_status": "computed",
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [NullIntertwiner](/verify/taulib/docs/book-v-temporal-macro-readout/null-intertwiner/) | L39-L52 | defined | `V.D27` |
| `def` | [photon_null](/verify/taulib/docs/book-v-temporal-macro-readout/photon-null/) | L55-L61 | defined | — |
| `theorem` | [boundary_supports_null](/verify/taulib/docs/book-v-temporal-macro-readout/boundary-supports-null/) | L69-L73 | formalized | `V.T14` |
| `theorem` | [null_selects_em](/verify/taulib/docs/book-v-temporal-macro-readout/null-selects-em/) | L82-L83 | formalized | `V.P06` |
| `theorem` | [em_unique_null](/verify/taulib/docs/book-v-temporal-macro-readout/em-unique-null/) | L86-L91 | formalized | — |
| `structure` | [OperationalDistance](/verify/taulib/docs/book-v-temporal-macro-readout/operational-distance/) | L100-L108 | defined | `V.D28` |
| `def` | [OperationalDistance.toFloat](/verify/taulib/docs/book-v-temporal-macro-readout/to-float/) | L111-L112 | defined | — |
| `theorem` | [distance_time_dual](/verify/taulib/docs/book-v-temporal-macro-readout/distance-time-dual/) | L121-L125 | formalized | `V.T15` |
| `structure` | [RefinementDrift](/verify/taulib/docs/book-v-temporal-macro-readout/refinement-drift/) | L135-L142 | defined | `V.D29` |
| `def` | [RefinementDrift.depth_diff](/verify/taulib/docs/book-v-temporal-macro-readout/depth-diff/) | L145-L146 | defined | — |
| `theorem` | [drift_formula_positive](/verify/taulib/docs/book-v-temporal-macro-readout/drift-formula-positive/) | L154-L157 | formalized | `V.T16` |
| `structure` | [ReadoutExpansion](/verify/taulib/docs/book-v-temporal-macro-readout/readout-expansion/) | L166-L172 | defined | `V.D30` |
| `def` | [ReadoutExpansion.toFloat](/verify/taulib/docs/book-v-temporal-macro-readout/to-float-l175/) | L175-L176 | defined | — |
| `structure` | [HubbleReadout](/verify/taulib/docs/book-v-temporal-macro-readout/hubble-readout/) | L185-L191 | defined | `V.D31` |
| `def` | [HubbleReadout.toFloat](/verify/taulib/docs/book-v-temporal-macro-readout/to-float-l194/) | L194-L195 | defined | — |
| `theorem` | [null_structural](/verify/taulib/docs/book-v-temporal-macro-readout/null-structural/) | L202-L204 | formalized | — |
| `theorem` | [null_transport_scale](/verify/taulib/docs/book-v-temporal-macro-readout/null-transport-scale/) | L207-L210 | formalized | — |
| `theorem` | [redshift_requires_earlier](/verify/taulib/docs/book-v-temporal-macro-readout/redshift-requires-earlier/) | L213-L214 | formalized | — |
| `eval` | [#eval L220](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l220/) | L220-L220 | computed | — |
| `eval` | [#eval L221](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l221/) | L221-L221 | computed | — |
| `eval` | [#eval L222](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l222/) | L222-L222 | computed | — |
| `eval` | [#eval L223](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l223/) | L223-L223 | computed | — |
| `eval` | [#eval L226](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l226/) | L226-L226 | computed | — |
| `eval` | [#eval L230](/verify/taulib/docs/book-v-temporal-macro-readout/eval-l230/) | L230-L233 | computed | — |
