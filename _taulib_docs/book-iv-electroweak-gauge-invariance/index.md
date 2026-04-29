---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_slug": "book-iv-electroweak-gauge-invariance",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/GaugeInvariance.lean",
  "sha256": "66ed3e45b8b8d664f7063a753866a540b15ed42c44275cb78324648ff42bd1db",
  "imports": [
    "TauLib.BookIV.Electroweak.PhotonMode"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.GaugeInvariance2"
  ],
  "registry_ids": [
    "IV.D85",
    "IV.D86",
    "IV.D87",
    "IV.D88",
    "IV.D89",
    "IV.D90",
    "IV.D91",
    "IV.D92",
    "IV.D93",
    "IV.D94",
    "IV.D95",
    "IV.P37",
    "IV.P38",
    "IV.P39",
    "IV.T37",
    "IV.T38"
  ],
  "declaration_counts": {
    "structure": 14,
    "def": 8,
    "theorem": 6,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "EMPrincipalBundle",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emprincipal-bundle/",
      "source_line_start": 63,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D85"
      ]
    },
    {
      "kind": "def",
      "name": "em_bundle",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/em-bundle/",
      "source_line_start": 79,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LocalTrivialization",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/local-trivialization/",
      "source_line_start": 95,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D86"
      ]
    },
    {
      "kind": "structure",
      "name": "TransitionFunction",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transition-function/",
      "source_line_start": 109,
      "source_line_end": 118,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D87"
      ]
    },
    {
      "kind": "def",
      "name": "TransitionFunction.compose",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/compose/",
      "source_line_start": 121,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BundleSection",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/bundle-section/",
      "source_line_start": 133,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D88"
      ]
    },
    {
      "kind": "theorem",
      "name": "global_section_chern",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/global-section-chern/",
      "source_line_start": 141,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EMConnection",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emconnection/",
      "source_line_start": 152,
      "source_line_end": 158,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D89"
      ]
    },
    {
      "kind": "def",
      "name": "em_connection",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/em-connection/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CovariantDerivative",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/covariant-derivative/",
      "source_line_start": 171,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D90"
      ]
    },
    {
      "kind": "structure",
      "name": "ParallelTransport",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/parallel-transport/",
      "source_line_start": 185,
      "source_line_end": 192,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D91"
      ]
    },
    {
      "kind": "def",
      "name": "ParallelTransport.compose",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/compose-l195/",
      "source_line_start": 195,
      "source_line_end": 199,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FieldStrengthTensor",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-tensor/",
      "source_line_start": 208,
      "source_line_end": 217,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D92"
      ]
    },
    {
      "kind": "def",
      "name": "field_strength",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength/",
      "source_line_start": 220,
      "source_line_end": 224,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AharonovBohmPhase",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/aharonov-bohm-phase/",
      "source_line_start": 233,
      "source_line_end": 241,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D93"
      ]
    },
    {
      "kind": "structure",
      "name": "EMLoopSpace",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emloop-space/",
      "source_line_start": 250,
      "source_line_end": 256,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D94"
      ]
    },
    {
      "kind": "structure",
      "name": "SigmaEquivariant",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/sigma-equivariant/",
      "source_line_start": 265,
      "source_line_end": 271,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D95"
      ]
    },
    {
      "kind": "theorem",
      "name": "gauge_invariance",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/gauge-invariance/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T37"
      ]
    },
    {
      "kind": "theorem",
      "name": "field_strength_invariant",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-invariant/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T38"
      ]
    },
    {
      "kind": "structure",
      "name": "ChernClassifier",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/chern-classifier/",
      "source_line_start": 297,
      "source_line_end": 302,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P37"
      ]
    },
    {
      "kind": "theorem",
      "name": "chern_class_classifier",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/chern-class-classifier/",
      "source_line_start": 304,
      "source_line_end": 306,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TransportCovariance",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transport-covariance/",
      "source_line_start": 315,
      "source_line_end": 320,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P38"
      ]
    },
    {
      "kind": "theorem",
      "name": "parallel_transport_covariance",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/parallel-transport-covariance/",
      "source_line_start": 322,
      "source_line_end": 324,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FFromCommutator",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/ffrom-commutator/",
      "source_line_start": 332,
      "source_line_end": 337,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P39"
      ]
    },
    {
      "kind": "theorem",
      "name": "f_from_commutator",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/f-from-commutator/",
      "source_line_start": 339,
      "source_line_end": 341,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_triv",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-triv/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_transport",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-transport/",
      "source_line_start": 355,
      "source_line_end": 356,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_ab",
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-ab/",
      "source_line_start": 358,
      "source_line_end": 359,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l360/",
      "source_line_start": 360,
      "source_line_end": 362,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/GaugeInvariance.lean`
- SHA-256: `66ed3e45b8b8d664f7063a753866a540b15ed42c44275cb78324648ff42bd1db`

## Registry Links

- `IV.D85` — EM Principal Bundle
- `IV.D86` — Local Trivialization
- `IV.D87` — Transition Function
- `IV.D88` — Section of the EM Bundle
- `IV.D89` — Gauge Connection
- `IV.D90` — Covariant Derivative
- `IV.D91` — Parallel Transport
- `IV.D92` — Electromagnetic Field Strength
- `IV.D93` — Aharonov-Bohm Phase
- `IV.D94` — EM Loop Space
- `IV.D95` — Sigma-Equivariance
- `IV.P37` — EM Bundle Topology
- `IV.P38` — Parallel Transport is Gauge-Covariant
- `IV.P39` — Explicit Form of F_mu_nu
- `IV.T37` — Gauge Invariance Kernel Theorem
- `IV.T38` — Gauge Invariance of F_mu_nu

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.PhotonMode`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.GaugeInvariance2`

## Declaration Counts

- `def`: 8
- `eval`: 9
- `structure`: 14
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [EMPrincipalBundle](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emprincipal-bundle/) | L63-L76 | defined | `IV.D85` |
| `def` | [em_bundle](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/em-bundle/) | L79-L87 | defined | — |
| `structure` | [LocalTrivialization](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/local-trivialization/) | L95-L100 | defined | `IV.D86` |
| `structure` | [TransitionFunction](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transition-function/) | L109-L118 | defined | `IV.D87` |
| `def` | [TransitionFunction.compose](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/compose/) | L121-L125 | defined | — |
| `structure` | [BundleSection](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/bundle-section/) | L133-L138 | defined | `IV.D88` |
| `theorem` | [global_section_chern](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/global-section-chern/) | L141-L143 | formalized | — |
| `structure` | [EMConnection](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emconnection/) | L152-L158 | defined | `IV.D89` |
| `def` | [em_connection](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/em-connection/) | L161-L163 | defined | — |
| `structure` | [CovariantDerivative](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/covariant-derivative/) | L171-L177 | defined | `IV.D90` |
| `structure` | [ParallelTransport](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/parallel-transport/) | L185-L192 | defined | `IV.D91` |
| `def` | [ParallelTransport.compose](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/compose-l195/) | L195-L199 | defined | — |
| `structure` | [FieldStrengthTensor](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-tensor/) | L208-L217 | defined | `IV.D92` |
| `def` | [field_strength](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength/) | L220-L224 | defined | — |
| `structure` | [AharonovBohmPhase](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/aharonov-bohm-phase/) | L233-L241 | defined | `IV.D93` |
| `structure` | [EMLoopSpace](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emloop-space/) | L250-L256 | defined | `IV.D94` |
| `structure` | [SigmaEquivariant](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/sigma-equivariant/) | L265-L271 | defined | `IV.D95` |
| `theorem` | [gauge_invariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/gauge-invariance/) | L280-L281 | formalized | `IV.T37` |
| `theorem` | [field_strength_invariant](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-invariant/) | L289-L289 | formalized | `IV.T38` |
| `structure` | [ChernClassifier](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/chern-classifier/) | L297-L302 | defined | `IV.P37` |
| `theorem` | [chern_class_classifier](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/chern-class-classifier/) | L304-L306 | formalized | — |
| `structure` | [TransportCovariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transport-covariance/) | L315-L320 | defined | `IV.P38` |
| `theorem` | [parallel_transport_covariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/parallel-transport-covariance/) | L322-L324 | formalized | — |
| `structure` | [FFromCommutator](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/ffrom-commutator/) | L332-L337 | defined | `IV.P39` |
| `theorem` | [f_from_commutator](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/f-from-commutator/) | L339-L341 | formalized | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l350/) | L350-L350 | computed | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l352/) | L352-L352 | computed | — |
| `def` | [example_triv](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-triv/) | L353-L353 | defined | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l354/) | L354-L354 | computed | — |
| `def` | [example_transport](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-transport/) | L355-L356 | defined | — |
| `eval` | [#eval L357](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l357/) | L357-L357 | computed | — |
| `def` | [example_ab](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/example-ab/) | L358-L359 | defined | — |
| `eval` | [#eval L360](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/eval-l360/) | L360-L362 | computed | — |
