---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_slug": "book-v-fluid-macro-phase-transitions",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/PhaseTransitions.lean",
  "sha256": "963a1003c31e2f96ddfca615ead7018f0529404d7daf3b8b56ab3d136430bf24",
  "imports": [
    "TauLib.BookV.FluidMacro.TauAlfven"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.ClassicalIllusion"
  ],
  "registry_ids": [
    "V.D113",
    "V.D114",
    "V.D115",
    "V.D116",
    "V.D336",
    "V.P190",
    "V.P54",
    "V.P55",
    "V.R157",
    "V.R158",
    "V.R159",
    "V.R160",
    "V.R471",
    "V.T76",
    "V.T77"
  ],
  "declaration_counts": {
    "inductive": 3,
    "structure": 7,
    "theorem": 9,
    "def": 10,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "PhaseType",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/phase-type/",
      "source_line_start": 71,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauOrderParameter",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-order-parameter/",
      "source_line_start": 81,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": [
        "V.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "order_parameter_determines",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/order-parameter-determines/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P54"
      ]
    },
    {
      "kind": "theorem",
      "name": "nonzero_means_ordered",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/nonzero-means-ordered/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "TransitionOrder",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/transition-order/",
      "source_line_start": 106,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauPhaseTransition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-phase-transition/",
      "source_line_start": 117,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": [
        "V.D114"
      ]
    },
    {
      "kind": "def",
      "name": "symmetry_breaking_remark",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-remark/",
      "source_line_start": 140,
      "source_line_end": 142,
      "formal_status": "defined",
      "registry_ids": [
        "V.R157"
      ]
    },
    {
      "kind": "theorem",
      "name": "symmetry_breaking_holds",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-holds/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CriticalExponentSet",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/critical-exponent-set/",
      "source_line_start": 155,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": [
        "V.D115"
      ]
    },
    {
      "kind": "structure",
      "name": "UniversalityClass",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-class/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "registry_ids": [
        "V.D116"
      ]
    },
    {
      "kind": "def",
      "name": "mean_field_class",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-class/",
      "source_line_start": 205,
      "source_line_end": 217,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ising_3d_class",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ising-3d-class/",
      "source_line_start": 220,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "universality_from_renormalization",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-from-renormalization/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T76"
      ]
    },
    {
      "kind": "structure",
      "name": "HiggsOmegaCrossing",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing/",
      "source_line_start": 261,
      "source_line_end": 270,
      "formal_status": "defined",
      "registry_ids": [
        "V.P55"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_omega_crossing",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing-l273/",
      "source_line_start": 273,
      "source_line_end": 275,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_fine_tuning",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning/",
      "source_line_start": 285,
      "source_line_end": 287,
      "formal_status": "defined",
      "registry_ids": [
        "V.R159"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_fine_tuning_holds",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning-holds/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CosmologicalPhaseTransition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-phase-transition/",
      "source_line_start": 306,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": [
        "V.T77"
      ]
    },
    {
      "kind": "theorem",
      "name": "phase_transition_completeness",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/phase-transition-completeness/",
      "source_line_start": 318,
      "source_line_end": 323,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CosmologicalTransitionRemark",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-transition-remark/",
      "source_line_start": 335,
      "source_line_end": 342,
      "formal_status": "defined",
      "registry_ids": [
        "V.R160"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_transition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/qcd-transition/",
      "source_line_start": 345,
      "source_line_end": 348,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ew_transition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ew-transition/",
      "source_line_start": 351,
      "source_line_end": 354,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mean_field_scaling",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-scaling/",
      "source_line_start": 362,
      "source_line_end": 374,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "disordered_op",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/disordered-op/",
      "source_line_start": 390,
      "source_line_end": 393,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ordered_op",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ordered-op/",
      "source_line_start": 396,
      "source_line_end": 399,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "water_boiling",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/water-boiling/",
      "source_line_start": 402,
      "source_line_end": 405,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l407/",
      "source_line_start": 407,
      "source_line_end": 407,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l411/",
      "source_line_start": 411,
      "source_line_end": 411,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l412/",
      "source_line_start": 412,
      "source_line_end": 412,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NSCrustCoreTransition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/nscrust-core-transition/",
      "source_line_start": 422,
      "source_line_end": 430,
      "formal_status": "defined",
      "registry_ids": [
        "V.D336"
      ]
    },
    {
      "kind": "def",
      "name": "crust_fraction_permille",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/crust-fraction-permille/",
      "source_line_start": 435,
      "source_line_end": 435,
      "formal_status": "defined",
      "registry_ids": [
        "V.P190"
      ]
    },
    {
      "kind": "theorem",
      "name": "transition_positive",
      "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/transition-positive/",
      "source_line_start": 438,
      "source_line_end": 445,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R471"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/PhaseTransitions.lean`
- SHA-256: `963a1003c31e2f96ddfca615ead7018f0529404d7daf3b8b56ab3d136430bf24`

## Registry Links

- `V.D113` — Macro tau-crystal
- `V.D114` — Macro tau-glass
- `V.D115` — First-order macro transition
- `V.D116` — Second-order macro transition
- `V.D336` — Neutron Star Crust-Core Transition Density
- `V.P190` — Crust Fraction from Defect-Tuple Crossing
- `V.P54` — Crossing preservation
- `V.P55` — Neutron star phase sequence
- `V.R157` — The glass transition is not a phase transition
- `V.R158` — Gaia and crystallization
- `V.R159` — DDT and turbulence
- `V.R160` — Universality is structural, not accidental
- `V.R471` — Condensed Matter Bridge Status (OQ-C6)
- `V.T76` — Critical surface is codimension 1
- `V.T77` — Phase-transition universality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.TauAlfven`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.ClassicalIllusion`

## Declaration Counts

- `def`: 10
- `eval`: 6
- `inductive`: 3
- `structure`: 7
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [PhaseType](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/phase-type/) | L71-L76 | defined | — |
| `structure` | [TauOrderParameter](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-order-parameter/) | L81-L89 | defined | `V.D113` |
| `theorem` | [order_parameter_determines](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/order-parameter-determines/) | L92-L94 | formalized | `V.P54` |
| `theorem` | [nonzero_means_ordered](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/nonzero-means-ordered/) | L97-L99 | formalized | — |
| `inductive` | [TransitionOrder](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/transition-order/) | L106-L113 | defined | — |
| `structure` | [TauPhaseTransition](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/tau-phase-transition/) | L117-L128 | defined | `V.D114` |
| `def` | [symmetry_breaking_remark](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-remark/) | L140-L142 | defined | `V.R157` |
| `theorem` | [symmetry_breaking_holds](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-holds/) | L144-L144 | formalized | — |
| `structure` | [CriticalExponentSet](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/critical-exponent-set/) | L155-L182 | defined | `V.D115` |
| `structure` | [UniversalityClass](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-class/) | L193-L202 | defined | `V.D116` |
| `def` | [mean_field_class](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-class/) | L205-L217 | defined | — |
| `def` | [ising_3d_class](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ising-3d-class/) | L220-L233 | defined | — |
| `theorem` | [universality_from_renormalization](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-from-renormalization/) | L246-L249 | formalized | `V.T76` |
| `structure` | [HiggsOmegaCrossing](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing/) | L261-L270 | defined | `V.P55` |
| `theorem` | [higgs_omega_crossing](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing-l273/) | L273-L275 | formalized | — |
| `def` | [no_fine_tuning](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning/) | L285-L287 | defined | `V.R159` |
| `theorem` | [no_fine_tuning_holds](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning-holds/) | L289-L289 | formalized | — |
| `inductive` | [CosmologicalPhaseTransition](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-phase-transition/) | L306-L315 | defined | `V.T77` |
| `theorem` | [phase_transition_completeness](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/phase-transition-completeness/) | L318-L323 | formalized | — |
| `structure` | [CosmologicalTransitionRemark](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-transition-remark/) | L335-L342 | defined | `V.R160` |
| `def` | [qcd_transition](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/qcd-transition/) | L345-L348 | defined | — |
| `def` | [ew_transition](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ew-transition/) | L351-L354 | defined | — |
| `theorem` | [mean_field_scaling](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-scaling/) | L362-L374 | formalized | — |
| `def` | [disordered_op](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/disordered-op/) | L390-L393 | defined | — |
| `def` | [ordered_op](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ordered-op/) | L396-L399 | defined | — |
| `def` | [water_boiling](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/water-boiling/) | L402-L405 | defined | — |
| `eval` | [#eval L407](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l407/) | L407-L407 | computed | — |
| `eval` | [#eval L408](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l408/) | L408-L408 | computed | — |
| `eval` | [#eval L409](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l409/) | L409-L409 | computed | — |
| `eval` | [#eval L410](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l410/) | L410-L410 | computed | — |
| `eval` | [#eval L411](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l411/) | L411-L411 | computed | — |
| `eval` | [#eval L412](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l412/) | L412-L412 | computed | — |
| `structure` | [NSCrustCoreTransition](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/nscrust-core-transition/) | L422-L430 | defined | `V.D336` |
| `def` | [crust_fraction_permille](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/crust-fraction-permille/) | L435-L435 | defined | `V.P190` |
| `theorem` | [transition_positive](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/transition-positive/) | L438-L445 | formalized | `V.R471` |
