---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_slug": "book-v-astrophysics-bullet-cluster-lss",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/BulletClusterLSS.lean",
  "sha256": "a7ad6d71b2f8b7394465abd48f882320cf68d1a0e71489f7555bc3007bb961a8",
  "imports": [
    "TauLib.BookV.Astrophysics.EHTReread"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.SectorExhaustion"
  ],
  "registry_ids": [
    "V.D140",
    "V.D141",
    "V.D142",
    "V.D143",
    "V.D291",
    "V.D292",
    "V.D300",
    "V.P157",
    "V.P165",
    "V.P84",
    "V.P85",
    "V.R200",
    "V.R201",
    "V.R423",
    "V.T233",
    "V.T240",
    "V.T97",
    "V.T98"
  ],
  "declaration_counts": {
    "structure": 8,
    "theorem": 9,
    "inductive": 1,
    "def": 6,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BulletClusterAnalysis",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bullet-cluster-analysis/",
      "source_line_start": 68,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D140"
      ]
    },
    {
      "kind": "theorem",
      "name": "lensing_gas_offset",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lensing-gas-offset/",
      "source_line_start": 101,
      "source_line_end": 103,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T97"
      ]
    },
    {
      "kind": "theorem",
      "name": "collisionless_stellar",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/collisionless-stellar/",
      "source_line_start": 117,
      "source_line_end": 119,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P84"
      ]
    },
    {
      "kind": "structure",
      "name": "LSSData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lssdata/",
      "source_line_start": 127,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D141"
      ]
    },
    {
      "kind": "inductive",
      "name": "CosmicWebType",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/cosmic-web-type/",
      "source_line_start": 146,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D142"
      ]
    },
    {
      "kind": "theorem",
      "name": "cosmic_web_complete",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/cosmic-web-complete/",
      "source_line_start": 158,
      "source_line_end": 161,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bao_scale",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-scale/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bao_from_boundary",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-from-boundary/",
      "source_line_start": 180,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T98"
      ]
    },
    {
      "kind": "structure",
      "name": "PowerSpectrumData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/power-spectrum-data/",
      "source_line_start": 189,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D143"
      ]
    },
    {
      "kind": "def",
      "name": "planck_power_spectrum",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/planck-power-spectrum/",
      "source_line_start": 201,
      "source_line_end": 205,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "lss_from_boundary_growth",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lss-from-boundary-growth/",
      "source_line_start": 218,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P85"
      ]
    },
    {
      "kind": "def",
      "name": "bullet_cluster",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bullet-cluster/",
      "source_line_start": 243,
      "source_line_end": 250,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WilsonLoopFlux",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/wilson-loop-flux/",
      "source_line_start": 263,
      "source_line_end": 272,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D291"
      ]
    },
    {
      "kind": "structure",
      "name": "FilamentBFieldAlignment",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-alignment/",
      "source_line_start": 276,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D292"
      ]
    },
    {
      "kind": "theorem",
      "name": "filament_bfield_theorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-theorem/",
      "source_line_start": 290,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T233"
      ]
    },
    {
      "kind": "theorem",
      "name": "topo_exceeds_dynamo",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/topo-exceeds-dynamo/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IGMFPrediction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/igmfprediction/",
      "source_line_start": 298,
      "source_line_end": 305,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P157"
      ]
    },
    {
      "kind": "def",
      "name": "vernstrom_detection",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/vernstrom-detection/",
      "source_line_start": 308,
      "source_line_end": 309,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vernstrom_in_tau_range",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/vernstrom-in-tau-range/",
      "source_line_start": 312,
      "source_line_end": 315,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauTransferFunction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/tau-transfer-function/",
      "source_line_start": 329,
      "source_line_end": 338,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D300"
      ]
    },
    {
      "kind": "structure",
      "name": "MatterPowerSpectrum",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/matter-power-spectrum/",
      "source_line_start": 343,
      "source_line_end": 354,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T240"
      ]
    },
    {
      "kind": "def",
      "name": "tau_transfer_canonical",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/tau-transfer-canonical/",
      "source_line_start": 357,
      "source_line_end": 361,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "power_spectrum_canonical",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/power-spectrum-canonical/",
      "source_line_start": 364,
      "source_line_end": 368,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bao_scale_consistent",
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-scale-consistent/",
      "source_line_start": 371,
      "source_line_end": 373,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P165"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l377/",
      "source_line_start": 377,
      "source_line_end": 377,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R423"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l378/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 382,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/BulletClusterLSS.lean`
- SHA-256: `a7ad6d71b2f8b7394465abd48f882320cf68d1a0e71489f7555bc3007bb961a8`

## Registry Links

- `V.D140` — Boundary-Mass Offset (tau)
- `V.D141` — Handle-Scale Event
- `V.D142` — Wilson Skeleton (Cosmic Web)
- `V.D143` — Topological Lensing Signature
- `V.D291` — Wilson Loop Magnetic Flux
- `V.D292` — Filament B-Field Alignment
- `V.D300` — τ-Native Transfer Function
- `V.P157` — IGMF Magnitude
- `V.P165` — BAO Scale Prediction
- `V.P84` — Lensing-Gas Offset Bound
- `V.P85` — Filament Scaling Relation
- `V.R200` — Bullet Cluster Orthodox Argument
- `V.R201` — BAO and Holonomy Periodicity
- `V.R423` — BOSS Data Comparison
- `V.T233` — Filament Magnetic Field Theorem
- `V.T240` — Power Spectrum Consistency
- `V.T97` — Bullet Cluster Without Dark Matter
- `V.T98` — Cosmic Web from Holonomy Loops

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.EHTReread`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.SectorExhaustion`

## Declaration Counts

- `def`: 6
- `eval`: 9
- `inductive`: 1
- `structure`: 8
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BulletClusterAnalysis](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bullet-cluster-analysis/) | L68-L85 | type/data schema | type/data schema | `V.D140` |
| `theorem` | [lensing_gas_offset](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lensing-gas-offset/) | L101-L103 | proof obligation | formal proof obligation checked | `V.T97` |
| `theorem` | [collisionless_stellar](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/collisionless-stellar/) | L117-L119 | proof obligation | formal proof obligation checked | `V.P84` |
| `structure` | [LSSData](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lssdata/) | L127-L138 | type/data schema | type/data schema | `V.D141` |
| `inductive` | [CosmicWebType](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/cosmic-web-type/) | L146-L155 | type/data schema | type/data schema | `V.D142` |
| `theorem` | [cosmic_web_complete](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/cosmic-web-complete/) | L158-L161 | proof obligation | formal proof obligation checked | — |
| `def` | [bao_scale](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-scale/) | L168-L168 | data/computed value | data/computed value | — |
| `theorem` | [bao_from_boundary](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-from-boundary/) | L180-L181 | proof obligation | formal proof obligation checked | `V.T98` |
| `structure` | [PowerSpectrumData](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/power-spectrum-data/) | L189-L198 | type/data schema | type/data schema | `V.D143` |
| `def` | [planck_power_spectrum](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/planck-power-spectrum/) | L201-L205 | definition | definition | — |
| `theorem` | [lss_from_boundary_growth](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/lss-from-boundary-growth/) | L218-L220 | proof obligation | formal proof obligation checked | `V.P85` |
| `def` | [bullet_cluster](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bullet-cluster/) | L243-L250 | definition | definition | — |
| `eval` | [#eval L252](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l252/) | L252-L252 | computed check | computed check | — |
| `eval` | [#eval L253](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l253/) | L253-L253 | computed check | computed check | — |
| `eval` | [#eval L254](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l254/) | L254-L254 | computed check | computed check | — |
| `structure` | [WilsonLoopFlux](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/wilson-loop-flux/) | L263-L272 | type/data schema | type/data schema | `V.D291` |
| `structure` | [FilamentBFieldAlignment](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-alignment/) | L276-L285 | type/data schema | type/data schema | `V.D292` |
| `theorem` | [filament_bfield_theorem](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/filament-bfield-theorem/) | L290-L292 | proof obligation | formal proof obligation checked | `V.T233` |
| `theorem` | [topo_exceeds_dynamo](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/topo-exceeds-dynamo/) | L295-L295 | proof obligation | formal proof obligation checked | — |
| `structure` | [IGMFPrediction](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/igmfprediction/) | L298-L305 | type/data schema | type/data schema | `V.P157` |
| `def` | [vernstrom_detection](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/vernstrom-detection/) | L308-L309 | definition | definition | — |
| `theorem` | [vernstrom_in_tau_range](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/vernstrom-in-tau-range/) | L312-L315 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L317](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l317/) | L317-L317 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l318/) | L318-L318 | computed check | computed check | — |
| `structure` | [TauTransferFunction](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/tau-transfer-function/) | L329-L338 | type/data schema | type/data schema | `V.D300` |
| `structure` | [MatterPowerSpectrum](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/matter-power-spectrum/) | L343-L354 | type/data schema | type/data schema | `V.T240` |
| `def` | [tau_transfer_canonical](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/tau-transfer-canonical/) | L357-L361 | definition | definition | — |
| `def` | [power_spectrum_canonical](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/power-spectrum-canonical/) | L364-L368 | definition | definition | — |
| `theorem` | [bao_scale_consistent](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-scale-consistent/) | L371-L373 | proof obligation | formal proof obligation checked | `V.P165` |
| `eval` | [#eval L377](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l377/) | L377-L377 | computed check | computed check | `V.R423` |
| `eval` | [#eval L378](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l378/) | L378-L378 | computed check | computed check | — |
| `eval` | [#eval L379](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l379/) | L379-L379 | computed check | computed check | — |
| `eval` | [#eval L380](/corpus/taulib/docs/book-v-astrophysics-bullet-cluster-lss/eval-l380/) | L380-L382 | computed check | computed check | — |
