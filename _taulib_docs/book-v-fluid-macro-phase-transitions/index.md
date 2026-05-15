---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/",
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
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/phase-type/",
      "source_line_start": 71,
      "source_line_end": 76,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauOrderParameter",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/tau-order-parameter/",
      "source_line_start": 81,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "order_parameter_determines",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/order-parameter-determines/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P54"
      ]
    },
    {
      "kind": "theorem",
      "name": "nonzero_means_ordered",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/nonzero-means-ordered/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "TransitionOrder",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/transition-order/",
      "source_line_start": 106,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauPhaseTransition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/tau-phase-transition/",
      "source_line_start": 117,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D114"
      ]
    },
    {
      "kind": "def",
      "name": "symmetry_breaking_remark",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-remark/",
      "source_line_start": 140,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R157"
      ]
    },
    {
      "kind": "theorem",
      "name": "symmetry_breaking_holds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-holds/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CriticalExponentSet",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/critical-exponent-set/",
      "source_line_start": 155,
      "source_line_end": 182,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D115"
      ]
    },
    {
      "kind": "structure",
      "name": "UniversalityClass",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/universality-class/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D116"
      ]
    },
    {
      "kind": "def",
      "name": "mean_field_class",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-class/",
      "source_line_start": 205,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ising_3d_class",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ising-3d-class/",
      "source_line_start": 220,
      "source_line_end": 233,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "universality_from_renormalization",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/universality-from-renormalization/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T76"
      ]
    },
    {
      "kind": "structure",
      "name": "HiggsOmegaCrossing",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing/",
      "source_line_start": 261,
      "source_line_end": 270,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P55"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_omega_crossing",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing-l273/",
      "source_line_start": 273,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_fine_tuning",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning/",
      "source_line_start": 285,
      "source_line_end": 287,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R159"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_fine_tuning_holds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning-holds/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CosmologicalPhaseTransition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-phase-transition/",
      "source_line_start": 306,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T77"
      ]
    },
    {
      "kind": "theorem",
      "name": "phase_transition_completeness",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/phase-transition-completeness/",
      "source_line_start": 318,
      "source_line_end": 323,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CosmologicalTransitionRemark",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-transition-remark/",
      "source_line_start": 335,
      "source_line_end": 342,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R160"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_transition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/qcd-transition/",
      "source_line_start": 345,
      "source_line_end": 348,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ew_transition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ew-transition/",
      "source_line_start": 351,
      "source_line_end": 354,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mean_field_scaling",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-scaling/",
      "source_line_start": 362,
      "source_line_end": 374,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "disordered_op",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/disordered-op/",
      "source_line_start": 390,
      "source_line_end": 393,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ordered_op",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ordered-op/",
      "source_line_start": 396,
      "source_line_end": 399,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "water_boiling",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/water-boiling/",
      "source_line_start": 402,
      "source_line_end": 405,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l407/",
      "source_line_start": 407,
      "source_line_end": 407,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l411/",
      "source_line_start": 411,
      "source_line_end": 411,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l412/",
      "source_line_start": 412,
      "source_line_end": 412,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NSCrustCoreTransition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/nscrust-core-transition/",
      "source_line_start": 422,
      "source_line_end": 430,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D336"
      ]
    },
    {
      "kind": "def",
      "name": "crust_fraction_permille",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/crust-fraction-permille/",
      "source_line_start": 435,
      "source_line_end": 435,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.P190"
      ]
    },
    {
      "kind": "theorem",
      "name": "transition_positive",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/transition-positive/",
      "source_line_start": 438,
      "source_line_end": 445,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [PhaseType](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/phase-type/) | L71-L76 | type/data schema | type/data schema | — |
| `structure` | [TauOrderParameter](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/tau-order-parameter/) | L81-L89 | type/data schema | type/data schema | `V.D113` |
| `theorem` | [order_parameter_determines](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/order-parameter-determines/) | L92-L94 | proof obligation | formal proof obligation checked | `V.P54` |
| `theorem` | [nonzero_means_ordered](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/nonzero-means-ordered/) | L97-L99 | proof obligation | formal proof obligation checked | — |
| `inductive` | [TransitionOrder](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/transition-order/) | L106-L113 | type/data schema | type/data schema | — |
| `structure` | [TauPhaseTransition](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/tau-phase-transition/) | L117-L128 | type/data schema | type/data schema | `V.D114` |
| `def` | [symmetry_breaking_remark](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-remark/) | L140-L142 | definition | definition | `V.R157` |
| `theorem` | [symmetry_breaking_holds](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/symmetry-breaking-holds/) | L144-L144 | proof obligation | formal proof obligation checked | — |
| `structure` | [CriticalExponentSet](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/critical-exponent-set/) | L155-L182 | type/data schema | type/data schema | `V.D115` |
| `structure` | [UniversalityClass](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/universality-class/) | L193-L202 | type/data schema | type/data schema | `V.D116` |
| `def` | [mean_field_class](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-class/) | L205-L217 | definition | definition | — |
| `def` | [ising_3d_class](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ising-3d-class/) | L220-L233 | definition | definition | — |
| `theorem` | [universality_from_renormalization](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/universality-from-renormalization/) | L246-L249 | proof obligation | formal proof obligation checked | `V.T76` |
| `structure` | [HiggsOmegaCrossing](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing/) | L261-L270 | type/data schema | type/data schema | `V.P55` |
| `theorem` | [higgs_omega_crossing](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/higgs-omega-crossing-l273/) | L273-L275 | proof obligation | formal proof obligation checked | — |
| `def` | [no_fine_tuning](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning/) | L285-L287 | definition | definition | `V.R159` |
| `theorem` | [no_fine_tuning_holds](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/no-fine-tuning-holds/) | L289-L289 | proof obligation | formal proof obligation checked | — |
| `inductive` | [CosmologicalPhaseTransition](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-phase-transition/) | L306-L315 | type/data schema | type/data schema | `V.T77` |
| `theorem` | [phase_transition_completeness](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/phase-transition-completeness/) | L318-L323 | proof obligation | formal proof obligation checked | — |
| `structure` | [CosmologicalTransitionRemark](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/cosmological-transition-remark/) | L335-L342 | type/data schema | type/data schema | `V.R160` |
| `def` | [qcd_transition](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/qcd-transition/) | L345-L348 | definition | definition | — |
| `def` | [ew_transition](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ew-transition/) | L351-L354 | definition | definition | — |
| `theorem` | [mean_field_scaling](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-scaling/) | L362-L374 | proof obligation | formal proof obligation checked | — |
| `def` | [disordered_op](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/disordered-op/) | L390-L393 | definition | definition | — |
| `def` | [ordered_op](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/ordered-op/) | L396-L399 | definition | definition | — |
| `def` | [water_boiling](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/water-boiling/) | L402-L405 | definition | definition | — |
| `eval` | [#eval L407](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l407/) | L407-L407 | computed check | computed check | — |
| `eval` | [#eval L408](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l408/) | L408-L408 | computed check | computed check | — |
| `eval` | [#eval L409](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l409/) | L409-L409 | computed check | computed check | — |
| `eval` | [#eval L410](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l410/) | L410-L410 | computed check | computed check | — |
| `eval` | [#eval L411](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l411/) | L411-L411 | computed check | computed check | — |
| `eval` | [#eval L412](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/eval-l412/) | L412-L412 | computed check | computed check | — |
| `structure` | [NSCrustCoreTransition](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/nscrust-core-transition/) | L422-L430 | type/data schema | type/data schema | `V.D336` |
| `def` | [crust_fraction_permille](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/crust-fraction-permille/) | L435-L435 | data/computed value | data/computed value | `V.P190` |
| `theorem` | [transition_positive](/corpus/taulib/docs/book-v-fluid-macro-phase-transitions/transition-positive/) | L438-L445 | proof obligation | formal proof obligation checked | `V.R471` |
