---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.DistanceLadder",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.DistanceLadder`.",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_slug": "book-v-temporal-distance-ladder",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/DistanceLadder.lean",
  "sha256": "e4bcd96b36feb6d51832af0213864c15fd9788d1245e7c44e7009341dc52df74",
  "imports": [
    "TauLib.BookV.Gravity.Schwarzschild"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Temporal.BoundaryData"
  ],
  "registry_ids": [
    "V.D32",
    "V.D33",
    "V.D34",
    "V.D35",
    "V.R40",
    "V.R41",
    "V.R44",
    "V.T17",
    "V.T18",
    "V.T19"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 2,
    "inductive": 1,
    "theorem": 8,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "DistanceReadout",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-readout/",
      "source_line_start": 78,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": [
        "V.D32"
      ]
    },
    {
      "kind": "def",
      "name": "DistanceReadout.toFloat",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/to-float/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "DistanceLadderRung",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-ladder-rung/",
      "source_line_start": 109,
      "source_line_end": 120,
      "formal_status": "defined",
      "registry_ids": [
        "V.T17"
      ]
    },
    {
      "kind": "def",
      "name": "DistanceLadderRung.log10_parsec",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/log10-parsec/",
      "source_line_start": 123,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CepheidCalibrator",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/cepheid-calibrator/",
      "source_line_start": 139,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": [
        "V.D33"
      ]
    },
    {
      "kind": "structure",
      "name": "BAOStandardRuler",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/baostandard-ruler/",
      "source_line_start": 164,
      "source_line_end": 175,
      "formal_status": "defined",
      "registry_ids": [
        "V.D34"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutCurvature",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/readout-curvature/",
      "source_line_start": 188,
      "source_line_end": 201,
      "formal_status": "defined",
      "registry_ids": [
        "V.D35"
      ]
    },
    {
      "kind": "theorem",
      "name": "ladder_rung_count",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/ladder-rung-count/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T17"
      ]
    },
    {
      "kind": "theorem",
      "name": "distance_is_operational",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-is-operational/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R40"
      ]
    },
    {
      "kind": "theorem",
      "name": "gaia_calibrates_nearby",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/gaia-calibrates-nearby/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R41"
      ]
    },
    {
      "kind": "theorem",
      "name": "H0_tension_structural",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/h0-tension-structural/",
      "source_line_start": 228,
      "source_line_end": 230,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T18"
      ]
    },
    {
      "kind": "theorem",
      "name": "dark_energy_artifact",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-artifact/",
      "source_line_start": 237,
      "source_line_end": 238,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T19"
      ]
    },
    {
      "kind": "theorem",
      "name": "dark_energy_scope",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-scope/",
      "source_line_start": 242,
      "source_line_end": 243,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R44"
      ]
    },
    {
      "kind": "theorem",
      "name": "scale_ordering",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/scale-ordering/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bao_snia_same_scale",
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/bao-snia-same-scale/",
      "source_line_start": 252,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l267/",
      "source_line_start": 267,
      "source_line_end": 270,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean",
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/DistanceLadder.lean`
- SHA-256: `e4bcd96b36feb6d51832af0213864c15fd9788d1245e7c44e7009341dc52df74`

## Registry Links

- `V.D32` — Distance readout functor
- `V.D33` — Cepheid readout calibrator
- `V.D34` — BAO standard ruler
- `V.D35` — Readout curvature
- `V.R40` — Distance is operational
- `V.R41` — Gaia and the tau-readout
- `V.R44` — Scope and deferral
- `V.T17` — Distance Ladder Translation
- `V.T18` — Hubble Tension Resolution
- `V.T19` — Dark Energy Artifact --- First Pass

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Gravity.Schwarzschild`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Temporal.BoundaryData`

## Declaration Counts

- `def`: 2
- `eval`: 6
- `inductive`: 1
- `structure`: 4
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [DistanceReadout](/verify/taulib/docs/book-v-temporal-distance-ladder/distance-readout/) | L78-L91 | defined | `V.D32` |
| `def` | [DistanceReadout.toFloat](/verify/taulib/docs/book-v-temporal-distance-ladder/to-float/) | L94-L95 | defined | — |
| `inductive` | [DistanceLadderRung](/verify/taulib/docs/book-v-temporal-distance-ladder/distance-ladder-rung/) | L109-L120 | defined | `V.T17` |
| `def` | [DistanceLadderRung.log10_parsec](/verify/taulib/docs/book-v-temporal-distance-ladder/log10-parsec/) | L123-L128 | defined | — |
| `structure` | [CepheidCalibrator](/verify/taulib/docs/book-v-temporal-distance-ladder/cepheid-calibrator/) | L139-L151 | defined | `V.D33` |
| `structure` | [BAOStandardRuler](/verify/taulib/docs/book-v-temporal-distance-ladder/baostandard-ruler/) | L164-L175 | defined | `V.D34` |
| `structure` | [ReadoutCurvature](/verify/taulib/docs/book-v-temporal-distance-ladder/readout-curvature/) | L188-L201 | defined | `V.D35` |
| `theorem` | [ladder_rung_count](/verify/taulib/docs/book-v-temporal-distance-ladder/ladder-rung-count/) | L208-L210 | formalized | `V.T17` |
| `theorem` | [distance_is_operational](/verify/taulib/docs/book-v-temporal-distance-ladder/distance-is-operational/) | L215-L216 | formalized | `V.R40` |
| `theorem` | [gaia_calibrates_nearby](/verify/taulib/docs/book-v-temporal-distance-ladder/gaia-calibrates-nearby/) | L220-L221 | formalized | `V.R41` |
| `theorem` | [H0_tension_structural](/verify/taulib/docs/book-v-temporal-distance-ladder/h0-tension-structural/) | L228-L230 | formalized | `V.T18` |
| `theorem` | [dark_energy_artifact](/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-artifact/) | L237-L238 | formalized | `V.T19` |
| `theorem` | [dark_energy_scope](/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-scope/) | L242-L243 | formalized | `V.R44` |
| `theorem` | [scale_ordering](/verify/taulib/docs/book-v-temporal-distance-ladder/scale-ordering/) | L246-L249 | formalized | — |
| `theorem` | [bao_snia_same_scale](/verify/taulib/docs/book-v-temporal-distance-ladder/bao-snia-same-scale/) | L252-L253 | formalized | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L261](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l261/) | L261-L261 | computed | — |
| `eval` | [#eval L262](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l262/) | L262-L262 | computed | — |
| `eval` | [#eval L263](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l263/) | L263-L263 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L267](/verify/taulib/docs/book-v-temporal-distance-ladder/eval-l267/) | L267-L270 | computed | — |
