---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "permalink": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_slug": "book-v-thermodynamics-vacuum-no-void",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean",
  "sha256": "2768b03763a811c4f7df734bcebe42f8847f789973767b851cb24343e6bfebdc",
  "imports": [
    "TauLib.BookV.Thermodynamics.HeatEM"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Thermodynamics.DarkEnergyArtifact"
  ],
  "registry_ids": [
    "V.C08",
    "V.D94",
    "V.P38",
    "V.P39",
    "V.R130",
    "V.R131",
    "V.R132",
    "V.T65",
    "V.T66",
    "V.T67"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 5,
    "theorem": 8,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauVacuum",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/tau-vacuum/",
      "source_line_start": 70,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D94"
      ]
    },
    {
      "kind": "def",
      "name": "TauVacuum.energyFloat",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/energy-float/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_holomorphic",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-holomorphic/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_energy_is_boundary",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-energy-is-boundary/",
      "source_line_start": 105,
      "source_line_end": 107,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T65"
      ]
    },
    {
      "kind": "structure",
      "name": "QFTVacuumAsRefinement",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qftvacuum-as-refinement/",
      "source_line_start": 118,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P38"
      ]
    },
    {
      "kind": "def",
      "name": "qft_vacuum_planck",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qft-vacuum-planck/",
      "source_line_start": 130,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qft_discrepancy_120",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qft-discrepancy-120/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_catastrophe_category_error",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-catastrophe-category-error/",
      "source_line_start": 148,
      "source_line_end": 150,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T66"
      ]
    },
    {
      "kind": "theorem",
      "name": "vacuum_source_finite",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-source-finite/",
      "source_line_start": 162,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C08"
      ]
    },
    {
      "kind": "theorem",
      "name": "normal_ordering_comparison",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/normal-ordering-comparison/",
      "source_line_start": 174,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R131"
      ]
    },
    {
      "kind": "structure",
      "name": "GroundStateUniqueness",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/ground-state-uniqueness/",
      "source_line_start": 189,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T67"
      ]
    },
    {
      "kind": "theorem",
      "name": "ground_state_unique",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/ground-state-unique/",
      "source_line_start": 199,
      "source_line_end": 201,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CasimirFromBoundary",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-from-boundary/",
      "source_line_start": 214,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P39"
      ]
    },
    {
      "kind": "theorem",
      "name": "casimir_no_mode_sum",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-no-mode-sum/",
      "source_line_start": 228,
      "source_line_end": 230,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_vacuum",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/example-vacuum/",
      "source_line_start": 248,
      "source_line_end": 251,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l253/",
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
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l255/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "planck_cutoff",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/planck-cutoff/",
      "source_line_start": 259,
      "source_line_end": 261,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "casimir_example",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-example/",
      "source_line_start": 267,
      "source_line_end": 270,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l272/",
      "source_line_start": 272,
      "source_line_end": 272,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l273/",
      "source_line_start": 273,
      "source_line_end": 275,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`
- SHA-256: `2768b03763a811c4f7df734bcebe42f8847f789973767b851cb24343e6bfebdc`

## Registry Links

- `V.C08` — Vacuum source term is finite
- `V.D94` — The tau-vacuum
- `V.P38` — QFT vacuum = refinement sum
- `V.P39` — Casimir effect from boundary modes
- `V.R130` — Why no divergence
- `V.R131` — Comparison with normal ordering
- `V.R132` — Casimir does not prove mode summation
- `V.T65` — Vacuum energy is boundary energy
- `V.T66` — The vacuum catastrophe is a category error
- `V.T67` — H_partial[omega

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Thermodynamics.HeatEM`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`

## Declaration Counts

- `def`: 5
- `eval`: 8
- `structure`: 4
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauVacuum](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/tau-vacuum/) | L70-L85 | type/data schema | type/data schema | `V.D94` |
| `def` | [TauVacuum.energyFloat](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/energy-float/) | L88-L89 | data/computed value | data/computed value | — |
| `theorem` | [vacuum_holomorphic](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-holomorphic/) | L92-L93 | proof obligation | formal proof obligation checked | — |
| `theorem` | [vacuum_energy_is_boundary](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-energy-is-boundary/) | L105-L107 | proof obligation | formal proof obligation checked | `V.T65` |
| `structure` | [QFTVacuumAsRefinement](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qftvacuum-as-refinement/) | L118-L127 | type/data schema | type/data schema | `V.P38` |
| `def` | [qft_vacuum_planck](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qft-vacuum-planck/) | L130-L132 | definition | definition | — |
| `theorem` | [qft_discrepancy_120](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/qft-discrepancy-120/) | L134-L135 | proof obligation | formal proof obligation checked | — |
| `theorem` | [vacuum_catastrophe_category_error](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-catastrophe-category-error/) | L148-L150 | proof obligation | formal proof obligation checked | `V.T66` |
| `theorem` | [vacuum_source_finite](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-source-finite/) | L162-L164 | proof obligation | formal proof obligation checked | `V.C08` |
| `theorem` | [normal_ordering_comparison](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/normal-ordering-comparison/) | L174-L176 | proof obligation | formal proof obligation checked | `V.R131` |
| `structure` | [GroundStateUniqueness](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/ground-state-uniqueness/) | L189-L196 | type/data schema | type/data schema | `V.T67` |
| `theorem` | [ground_state_unique](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/ground-state-unique/) | L199-L201 | proof obligation | formal proof obligation checked | — |
| `structure` | [CasimirFromBoundary](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-from-boundary/) | L214-L225 | type/data schema | type/data schema | `V.P39` |
| `theorem` | [casimir_no_mode_sum](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-no-mode-sum/) | L228-L230 | proof obligation | formal proof obligation checked | — |
| `def` | [example_vacuum](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/example-vacuum/) | L248-L251 | definition | definition | — |
| `eval` | [#eval L253](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l253/) | L253-L253 | computed check | computed check | — |
| `eval` | [#eval L254](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l254/) | L254-L254 | computed check | computed check | — |
| `eval` | [#eval L255](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l255/) | L255-L255 | computed check | computed check | — |
| `eval` | [#eval L256](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l256/) | L256-L256 | computed check | computed check | — |
| `def` | [planck_cutoff](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/planck-cutoff/) | L259-L261 | definition | definition | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l264/) | L264-L264 | computed check | computed check | — |
| `def` | [casimir_example](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-example/) | L267-L270 | definition | definition | — |
| `eval` | [#eval L272](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l272/) | L272-L272 | computed check | computed check | — |
| `eval` | [#eval L273](/corpus/taulib/docs/book-v-thermodynamics-vacuum-no-void/eval-l273/) | L273-L275 | computed check | computed check | — |
