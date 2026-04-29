---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_slug": "book-v-thermodynamics-dark-energy-artifact",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean",
  "sha256": "ee9041fe52eb9680093747192c1ddeb0b6104c8144616ff8ee4c9c0bb326efa5",
  "imports": [
    "TauLib.BookV.Thermodynamics.VacuumNoVoid"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.Tour.GuidedTour.BookV"
  ],
  "registry_ids": [
    "V.D293",
    "V.D294",
    "V.D95",
    "V.P159",
    "V.P40",
    "V.P41",
    "V.R133",
    "V.R134",
    "V.R135",
    "V.R136",
    "V.R418",
    "V.T234",
    "V.T68",
    "V.T69"
  ],
  "declaration_counts": {
    "structure": 6,
    "theorem": 13,
    "inductive": 2,
    "def": 10,
    "eval": 12
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CapacitySurplus",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/capacity-surplus/",
      "source_line_start": 74,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": [
        "V.D95"
      ]
    },
    {
      "kind": "theorem",
      "name": "surplus_nonneg",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/surplus-nonneg/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "EoSRegime",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eo-sregime/",
      "source_line_start": 96,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectDrivenAcceleration",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-driven-acceleration/",
      "source_line_start": 113,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": [
        "V.T68"
      ]
    },
    {
      "kind": "def",
      "name": "DefectDrivenAcceleration.determineRegime",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/determine-regime/",
      "source_line_start": 133,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_lambda",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/no-lambda/",
      "source_line_start": 150,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P40"
      ]
    },
    {
      "kind": "theorem",
      "name": "dark_energy_artifact",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-artifact/",
      "source_line_start": 164,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T69"
      ]
    },
    {
      "kind": "theorem",
      "name": "the_68_percent",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/the-68-percent/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P41"
      ]
    },
    {
      "kind": "theorem",
      "name": "data_vs_interpretation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/data-vs-interpretation/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R133"
      ]
    },
    {
      "kind": "theorem",
      "name": "two_faces",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/two-faces/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R134"
      ]
    },
    {
      "kind": "theorem",
      "name": "where_68_goes",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/where-68-goes/",
      "source_line_start": 217,
      "source_line_end": 219,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R135"
      ]
    },
    {
      "kind": "structure",
      "name": "DarkEnergyTestability",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-testability/",
      "source_line_start": 233,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": [
        "V.R136"
      ]
    },
    {
      "kind": "def",
      "name": "dark_energy_testability",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-testability-l249/",
      "source_line_start": 249,
      "source_line_end": 250,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "w_varies_prediction",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/w-varies-prediction/",
      "source_line_start": 253,
      "source_line_end": 254,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CosmicComponent",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-component/",
      "source_line_start": 261,
      "source_line_end": 266,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cosmic_budget",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-budget/",
      "source_line_start": 269,
      "source_line_end": 270,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cosmic_budget_two_components",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-budget-two-components/",
      "source_line_start": 273,
      "source_line_end": 274,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "early_universe",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/early-universe/",
      "source_line_start": 281,
      "source_line_end": 285,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "present_epoch",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/present-epoch/",
      "source_line_start": 288,
      "source_line_end": 292,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l294/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l297/",
      "source_line_start": 297,
      "source_line_end": 297,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "surplus_example",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/surplus-example/",
      "source_line_start": 300,
      "source_line_end": 305,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "testability",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/testability/",
      "source_line_start": 312,
      "source_line_end": 312,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OmegaLambdaStandalone",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-standalone/",
      "source_line_start": 327,
      "source_line_end": 340,
      "formal_status": "defined",
      "registry_ids": [
        "V.T234"
      ]
    },
    {
      "kind": "def",
      "name": "omega_lambda_canonical",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-canonical/",
      "source_line_start": 343,
      "source_line_end": 348,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_lambda_deviation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-deviation/",
      "source_line_start": 351,
      "source_line_end": 352,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_lambda_tau_effective",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-tau-effective/",
      "source_line_start": 355,
      "source_line_end": 356,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectFractionEoS",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-fraction-eo-s/",
      "source_line_start": 369,
      "source_line_end": 379,
      "formal_status": "defined",
      "registry_ids": [
        "V.D293",
        "V.P159"
      ]
    },
    {
      "kind": "def",
      "name": "defect_eos_canonical",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-eos-canonical/",
      "source_line_start": 382,
      "source_line_end": 385,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "w0_quintessence",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/w0-quintessence/",
      "source_line_start": 388,
      "source_line_end": 389,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TransitionRedshift",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/transition-redshift/",
      "source_line_start": 399,
      "source_line_end": 408,
      "formal_status": "defined",
      "registry_ids": [
        "V.D294",
        "V.R418"
      ]
    },
    {
      "kind": "def",
      "name": "z_acc_canonical",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/z-acc-canonical/",
      "source_line_start": 411,
      "source_line_end": 413,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "z_acc_within_1sigma",
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/z-acc-within-1sigma/",
      "source_line_start": 416,
      "source_line_end": 418,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l420/",
      "source_line_start": 420,
      "source_line_end": 420,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l421/",
      "source_line_start": 421,
      "source_line_end": 421,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l422/",
      "source_line_start": 422,
      "source_line_end": 422,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 425,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`
- SHA-256: `ee9041fe52eb9680093747192c1ddeb0b6104c8144616ff8ee4c9c0bb326efa5`

## Registry Links

- `V.D293` — Defect Fraction Function
- `V.D294` — Transition Redshift z_acc
- `V.D95` — Capacity surplus
- `V.P159` — w₀ from Defect Dynamics
- `V.P40` — No Lambda in the tau-Einstein equation
- `V.P41` — The 68% is refinement entropy
- `V.R133` — Data versus interpretation
- `V.R134` — Two faces of the same problem
- `V.R135` — Where does the 68% go?
- `V.R136` — Testability
- `V.R418` — Transition Redshift Comparison
- `V.T234` — Ω_Λ Structural Theorem
- `V.T68` — Defect-driven acceleration
- `V.T69` — Dark energy is a readout artifact

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Thermodynamics.VacuumNoVoid`

## Imported By

- `TauLib.BookV`
- `TauLib.Tour.GuidedTour.BookV`

## Declaration Counts

- `def`: 10
- `eval`: 12
- `inductive`: 2
- `structure`: 6
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [CapacitySurplus](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/capacity-surplus/) | L74-L85 | defined | `V.D95` |
| `theorem` | [surplus_nonneg](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/surplus-nonneg/) | L88-L89 | formalized | — |
| `inductive` | [EoSRegime](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eo-sregime/) | L96-L103 | defined | — |
| `structure` | [DefectDrivenAcceleration](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-driven-acceleration/) | L113-L130 | defined | `V.T68` |
| `def` | [DefectDrivenAcceleration.determineRegime](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/determine-regime/) | L133-L138 | defined | — |
| `theorem` | [no_lambda](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/no-lambda/) | L150-L152 | formalized | `V.P40` |
| `theorem` | [dark_energy_artifact](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-artifact/) | L164-L166 | formalized | `V.T69` |
| `theorem` | [the_68_percent](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/the-68-percent/) | L177-L179 | formalized | `V.P41` |
| `theorem` | [data_vs_interpretation](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/data-vs-interpretation/) | L189-L191 | formalized | `V.R133` |
| `theorem` | [two_faces](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/two-faces/) | L203-L205 | formalized | `V.R134` |
| `theorem` | [where_68_goes](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/where-68-goes/) | L217-L219 | formalized | `V.R135` |
| `structure` | [DarkEnergyTestability](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-testability/) | L233-L246 | defined | `V.R136` |
| `def` | [dark_energy_testability](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-testability-l249/) | L249-L250 | defined | — |
| `theorem` | [w_varies_prediction](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/w-varies-prediction/) | L253-L254 | formalized | — |
| `inductive` | [CosmicComponent](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-component/) | L261-L266 | defined | — |
| `def` | [cosmic_budget](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-budget/) | L269-L270 | defined | — |
| `theorem` | [cosmic_budget_two_components](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/cosmic-budget-two-components/) | L273-L274 | formalized | — |
| `def` | [early_universe](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/early-universe/) | L281-L285 | defined | — |
| `def` | [present_epoch](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/present-epoch/) | L288-L292 | defined | — |
| `eval` | [#eval L294](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l294/) | L294-L294 | computed | — |
| `eval` | [#eval L295](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l295/) | L295-L295 | computed | — |
| `eval` | [#eval L296](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l296/) | L296-L296 | computed | — |
| `eval` | [#eval L297](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l297/) | L297-L297 | computed | — |
| `def` | [surplus_example](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/surplus-example/) | L300-L305 | defined | — |
| `eval` | [#eval L307](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l307/) | L307-L307 | computed | — |
| `eval` | [#eval L309](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l309/) | L309-L309 | computed | — |
| `def` | [testability](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/testability/) | L312-L312 | defined | — |
| `eval` | [#eval L314](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l314/) | L314-L314 | computed | — |
| `eval` | [#eval L315](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l315/) | L315-L315 | computed | — |
| `structure` | [OmegaLambdaStandalone](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-standalone/) | L327-L340 | defined | `V.T234` |
| `def` | [omega_lambda_canonical](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-canonical/) | L343-L348 | defined | — |
| `theorem` | [omega_lambda_deviation](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-deviation/) | L351-L352 | formalized | — |
| `theorem` | [omega_lambda_tau_effective](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/omega-lambda-tau-effective/) | L355-L356 | formalized | — |
| `structure` | [DefectFractionEoS](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-fraction-eo-s/) | L369-L379 | defined | `V.D293`, `V.P159` |
| `def` | [defect_eos_canonical](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/defect-eos-canonical/) | L382-L385 | defined | — |
| `theorem` | [w0_quintessence](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/w0-quintessence/) | L388-L389 | formalized | — |
| `structure` | [TransitionRedshift](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/transition-redshift/) | L399-L408 | defined | `V.D294`, `V.R418` |
| `def` | [z_acc_canonical](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/z-acc-canonical/) | L411-L413 | defined | — |
| `theorem` | [z_acc_within_1sigma](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/z-acc-within-1sigma/) | L416-L418 | formalized | — |
| `eval` | [#eval L420](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l420/) | L420-L420 | computed | — |
| `eval` | [#eval L421](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l421/) | L421-L421 | computed | — |
| `eval` | [#eval L422](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l422/) | L422-L422 | computed | — |
| `eval` | [#eval L423](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/eval-l423/) | L423-L425 | computed | — |
