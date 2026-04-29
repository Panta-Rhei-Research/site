---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_slug": "book-iv-electroweak-gauge-invariance2",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/GaugeInvariance2.lean",
  "sha256": "86023f7119f581898bc093f7c7c677ee019e5d41c619d8c4d27593b54af4878a",
  "imports": [
    "TauLib.BookIV.Electroweak.GaugeInvariance"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.TauMaxwell"
  ],
  "registry_ids": [
    "IV.D96",
    "IV.D97",
    "IV.P173",
    "IV.P40",
    "IV.P41",
    "IV.P42",
    "IV.P43",
    "IV.R25",
    "IV.R359",
    "IV.R360",
    "IV.R362",
    "IV.T121",
    "IV.T39",
    "IV.T40",
    "IV.T41"
  ],
  "declaration_counts": {
    "structure": 9,
    "def": 13,
    "theorem": 9,
    "inductive": 1,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "WilsonLoop",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/wilson-loop/",
      "source_line_start": 64,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D96"
      ]
    },
    {
      "kind": "def",
      "name": "wilson_u1",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/wilson-u1/",
      "source_line_start": 76,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "WilsonLoop.compose",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/compose/",
      "source_line_start": 83,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NonAbelianGauge",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/non-abelian-gauge/",
      "source_line_start": 96,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D97"
      ]
    },
    {
      "kind": "def",
      "name": "gauge_u1",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-u1/",
      "source_line_start": 107,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gauge_su2",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-su2/",
      "source_line_start": 114,
      "source_line_end": 118,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gauge_su3",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-su3/",
      "source_line_start": 121,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ABPhaseUniqueness",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abphase-uniqueness/",
      "source_line_start": 134,
      "source_line_end": 140,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T39"
      ]
    },
    {
      "kind": "theorem",
      "name": "ab_phase_unique",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-phase-unique/",
      "source_line_start": 142,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ABRootOfUnity",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abroot-of-unity/",
      "source_line_start": 152,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T40"
      ]
    },
    {
      "kind": "def",
      "name": "ab_root_example",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-root-example/",
      "source_line_start": 161,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ab_root_of_unity",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-root-of-unity/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyFromCurvature",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-from-curvature/",
      "source_line_start": 175,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T41"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_curvature_example",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-curvature-example/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "holonomy_from_curvature",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-from-curvature-l184/",
      "source_line_start": 184,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GaugeTransformationLaw",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transformation-law/",
      "source_line_start": 194,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T121"
      ]
    },
    {
      "kind": "def",
      "name": "gauge_transform_u1",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transform-u1/",
      "source_line_start": 206,
      "source_line_end": 211,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gauge_transformation_law",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transformation-law-l213/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ObservableLevel",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/observable-level/",
      "source_line_start": 223,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P40"
      ]
    },
    {
      "kind": "def",
      "name": "ObservableLevel.toNat",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/to-nat/",
      "source_line_start": 230,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "observable_hierarchy",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/observable-hierarchy/",
      "source_line_start": 235,
      "source_line_end": 238,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nonabelian_self_interaction",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/nonabelian-self-interaction/",
      "source_line_start": 247,
      "source_line_end": 251,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P41"
      ]
    },
    {
      "kind": "structure",
      "name": "PathOrderedExp",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-exp/",
      "source_line_start": 260,
      "source_line_end": 266,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P42"
      ]
    },
    {
      "kind": "def",
      "name": "path_ordered_u1",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-u1/",
      "source_line_start": 269,
      "source_line_end": 272,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "path_ordered_exp",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-exp-l274/",
      "source_line_start": 274,
      "source_line_end": 275,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SevenStepChain",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain/",
      "source_line_start": 284,
      "source_line_end": 292,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P43"
      ]
    },
    {
      "kind": "def",
      "name": "seven_step_chain",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain-l294/",
      "source_line_start": 294,
      "source_line_end": 296,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "seven_step_chain_valid",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain-valid/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ABInterference",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abinterference/",
      "source_line_start": 307,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P173"
      ]
    },
    {
      "kind": "def",
      "name": "example_ab_interf",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/example-ab-interf/",
      "source_line_start": 317,
      "source_line_end": 319,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ab_interference",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-interference/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_wilson",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/example-wilson/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R25",
        "IV.R359",
        "IV.R360",
        "IV.R362"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 352,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/GaugeInvariance2.lean`
- SHA-256: `86023f7119f581898bc093f7c7c677ee019e5d41c619d8c4d27593b54af4878a`

## Registry Links

- `IV.D96` — Wilson Loop
- `IV.D97` — Non-Abelian Gauge Field
- `IV.P173` — AB interference shift
- `IV.P40` — Observable Hierarchy
- `IV.P41` — Self-Interaction from Non-Commutativity
- `IV.P42` — Non-Abelian Holonomy
- `IV.P43` — Categorical Derivation of Gauge Structure
- `IV.R25` — Gauge Invariance Is Geometric Not Dynamic
- `IV.R359` — Physical content lives in the curvature
- `IV.R360` — Experimental confirmation
- `IV.R362` — The AB effect as an observable
- `IV.T121` — Gauge covariance of D_mu
- `IV.T39` — tau-AB Kernel Theorem
- `IV.T40` — AB Phase Quantization
- `IV.T41` — Ambrose-Singer Reconstruction

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.GaugeInvariance`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.TauMaxwell`

## Declaration Counts

- `def`: 13
- `eval`: 10
- `inductive`: 1
- `structure`: 9
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [WilsonLoop](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/wilson-loop/) | L64-L73 | defined | `IV.D96` |
| `def` | [wilson_u1](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/wilson-u1/) | L76-L80 | defined | — |
| `def` | [WilsonLoop.compose](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/compose/) | L83-L87 | defined | — |
| `structure` | [NonAbelianGauge](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/non-abelian-gauge/) | L96-L104 | defined | `IV.D97` |
| `def` | [gauge_u1](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-u1/) | L107-L111 | defined | — |
| `def` | [gauge_su2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-su2/) | L114-L118 | defined | — |
| `def` | [gauge_su3](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-su3/) | L121-L125 | defined | — |
| `structure` | [ABPhaseUniqueness](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abphase-uniqueness/) | L134-L140 | defined | `IV.T39` |
| `theorem` | [ab_phase_unique](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-phase-unique/) | L142-L143 | formalized | — |
| `structure` | [ABRootOfUnity](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abroot-of-unity/) | L152-L159 | defined | `IV.T40` |
| `def` | [ab_root_example](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-root-example/) | L161-L164 | defined | — |
| `theorem` | [ab_root_of_unity](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-root-of-unity/) | L166-L166 | formalized | — |
| `structure` | [HolonomyFromCurvature](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-from-curvature/) | L175-L180 | defined | `IV.T41` |
| `def` | [holonomy_curvature_example](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-curvature-example/) | L182-L182 | defined | — |
| `theorem` | [holonomy_from_curvature](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/holonomy-from-curvature-l184/) | L184-L185 | formalized | — |
| `structure` | [GaugeTransformationLaw](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transformation-law/) | L194-L203 | defined | `IV.T121` |
| `def` | [gauge_transform_u1](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transform-u1/) | L206-L211 | defined | — |
| `theorem` | [gauge_transformation_law](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transformation-law-l213/) | L213-L214 | formalized | — |
| `inductive` | [ObservableLevel](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/observable-level/) | L223-L227 | defined | `IV.P40` |
| `def` | [ObservableLevel.toNat](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/to-nat/) | L230-L233 | defined | — |
| `theorem` | [observable_hierarchy](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/observable-hierarchy/) | L235-L238 | formalized | — |
| `theorem` | [nonabelian_self_interaction](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/nonabelian-self-interaction/) | L247-L251 | formalized | `IV.P41` |
| `structure` | [PathOrderedExp](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-exp/) | L260-L266 | defined | `IV.P42` |
| `def` | [path_ordered_u1](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-u1/) | L269-L272 | defined | — |
| `theorem` | [path_ordered_exp](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-exp-l274/) | L274-L275 | formalized | — |
| `structure` | [SevenStepChain](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain/) | L284-L292 | defined | `IV.P43` |
| `def` | [seven_step_chain](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain-l294/) | L294-L296 | defined | — |
| `theorem` | [seven_step_chain_valid](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain-valid/) | L298-L298 | formalized | — |
| `structure` | [ABInterference](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abinterference/) | L307-L315 | defined | `IV.P173` |
| `def` | [example_ab_interf](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/example-ab-interf/) | L317-L319 | defined | — |
| `theorem` | [ab_interference](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/ab-interference/) | L321-L321 | formalized | — |
| `def` | [example_wilson](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/example-wilson/) | L340-L340 | defined | `IV.R25`, `IV.R359`, `IV.R360`, `IV.R362` |
| `eval` | [#eval L341](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l343/) | L343-L343 | computed | — |
| `eval` | [#eval L344](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/eval-l350/) | L350-L352 | computed | — |
