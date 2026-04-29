---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_slug": "book-v-thermodynamics-defect-exhaustion",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/DefectExhaustion.lean",
  "sha256": "843aebd1e6a68c2bcc3d5be522157a40bef12144248b579f164e111cdfc8a36e",
  "imports": [
    "TauLib.BookV.Thermodynamics.EntropySplitting"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Thermodynamics.HeatEM"
  ],
  "registry_ids": [
    "V.C07",
    "V.D88",
    "V.D89",
    "V.D90",
    "V.L03",
    "V.P30",
    "V.P31",
    "V.P32",
    "V.P33",
    "V.R123",
    "V.R124",
    "V.R125",
    "V.R126",
    "V.R127",
    "V.T60",
    "V.T61",
    "V.T62"
  ],
  "declaration_counts": {
    "structure": 9,
    "def": 5,
    "theorem": 7,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "FiniteInitialDefectCount",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-initial-defect-count/",
      "source_line_start": 71,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": [
        "V.P30"
      ]
    },
    {
      "kind": "structure",
      "name": "GlobalDefectBudget",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-budget/",
      "source_line_start": 89,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": [
        "V.D88"
      ]
    },
    {
      "kind": "def",
      "name": "GlobalDefectBudget.boundFloat",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/bound-float/",
      "source_line_start": 104,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "finite_defect_budget",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-defect-budget/",
      "source_line_start": 119,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T60"
      ]
    },
    {
      "kind": "structure",
      "name": "IntegerThreshold",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/integer-threshold/",
      "source_line_start": 133,
      "source_line_end": 140,
      "formal_status": "defined",
      "registry_ids": [
        "V.L03"
      ]
    },
    {
      "kind": "def",
      "name": "threshold_example",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/threshold-example/",
      "source_line_start": 145,
      "source_line_end": 148,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GlobalDefectExhaustionThm",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-exhaustion-thm/",
      "source_line_start": 160,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "V.T61"
      ]
    },
    {
      "kind": "structure",
      "name": "RefinedCoherenceHorizon",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/refined-coherence-horizon/",
      "source_line_start": 182,
      "source_line_end": 193,
      "formal_status": "defined",
      "registry_ids": [
        "V.D89"
      ]
    },
    {
      "kind": "structure",
      "name": "MasterExhaustion",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/master-exhaustion/",
      "source_line_start": 205,
      "source_line_end": 218,
      "formal_status": "defined",
      "registry_ids": [
        "V.T62"
      ]
    },
    {
      "kind": "theorem",
      "name": "master_exhaustion_controlled_by_iota",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/master-exhaustion-controlled-by-iota/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectHalfLife",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/defect-half-life/",
      "source_line_start": 235,
      "source_line_end": 244,
      "formal_status": "defined",
      "registry_ids": [
        "V.D90"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_half_life",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/canonical-half-life/",
      "source_line_start": 247,
      "source_line_end": 250,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "DefectHalfLife.toFloat",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/to-float/",
      "source_line_start": 253,
      "source_line_end": 254,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "finite_irreversibility",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-irreversibility/",
      "source_line_start": 265,
      "source_line_end": 267,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C07"
      ]
    },
    {
      "kind": "structure",
      "name": "VacuumCirculation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/vacuum-circulation/",
      "source_line_start": 279,
      "source_line_end": 290,
      "formal_status": "defined",
      "registry_ids": [
        "V.P31"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_poincare_conflict",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/no-poincare-conflict/",
      "source_line_start": 300,
      "source_line_end": 302,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P32"
      ]
    },
    {
      "kind": "theorem",
      "name": "arrow_has_endpoint",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/arrow-has-endpoint/",
      "source_line_start": 315,
      "source_line_end": 317,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P33"
      ]
    },
    {
      "kind": "theorem",
      "name": "contrast_with_qft",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/contrast-with-qft/",
      "source_line_start": 326,
      "source_line_end": 328,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R123"
      ]
    },
    {
      "kind": "structure",
      "name": "OrbitStepsNotYears",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/orbit-steps-not-years/",
      "source_line_start": 331,
      "source_line_end": 336,
      "formal_status": "defined",
      "registry_ids": [
        "V.R124"
      ]
    },
    {
      "kind": "theorem",
      "name": "universal_half_life",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/universal-half-life/",
      "source_line_start": 343,
      "source_line_end": 344,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R125",
        "V.R126"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": [
        "V.R127"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_budget",
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/example-budget/",
      "source_line_start": 358,
      "source_line_end": 363,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l365/",
      "source_line_start": 365,
      "source_line_end": 367,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/DefectExhaustion.lean`
- SHA-256: `843aebd1e6a68c2bcc3d5be522157a40bef12144248b579f164e111cdfc8a36e`

## Registry Links

- `V.C07` — Finite irreversibility
- `V.D88` — Global defect budget
- `V.D89` — Coherence horizon---refined
- `V.D90` — Defect half-life
- `V.L03` — Integer threshold
- `V.P30` — Finite initial defect count
- `V.P31` — Vacuum circulation is periodic
- `V.P32` — No Poincar'e recurrence conflict
- `V.P33` — The arrow has an endpoint
- `V.R123` — Contrast with QFT
- `V.R124` — Orbit steps are not years
- `V.R125` — Contrast with heat death
- `V.R126` — Universal half-life
- `V.R127` — Time continues; the arrow does not
- `V.T60` — Finite defect budget
- `V.T61` — Global Defect Exhaustion
- `V.T62` — Master exhaustion inequality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Thermodynamics.EntropySplitting`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Thermodynamics.HeatEM`

## Declaration Counts

- `def`: 5
- `eval`: 4
- `structure`: 9
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [FiniteInitialDefectCount](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-initial-defect-count/) | L71-L78 | defined | `V.P30` |
| `structure` | [GlobalDefectBudget](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-budget/) | L89-L101 | defined | `V.D88` |
| `def` | [GlobalDefectBudget.boundFloat](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/bound-float/) | L104-L105 | defined | — |
| `theorem` | [finite_defect_budget](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-defect-budget/) | L119-L120 | formalized | `V.T60` |
| `structure` | [IntegerThreshold](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/integer-threshold/) | L133-L140 | defined | `V.L03` |
| `def` | [threshold_example](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/threshold-example/) | L145-L148 | defined | — |
| `structure` | [GlobalDefectExhaustionThm](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-exhaustion-thm/) | L160-L169 | defined | `V.T61` |
| `structure` | [RefinedCoherenceHorizon](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/refined-coherence-horizon/) | L182-L193 | defined | `V.D89` |
| `structure` | [MasterExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/master-exhaustion/) | L205-L218 | defined | `V.T62` |
| `theorem` | [master_exhaustion_controlled_by_iota](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/master-exhaustion-controlled-by-iota/) | L221-L222 | formalized | — |
| `structure` | [DefectHalfLife](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/defect-half-life/) | L235-L244 | defined | `V.D90` |
| `def` | [canonical_half_life](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/canonical-half-life/) | L247-L250 | defined | — |
| `def` | [DefectHalfLife.toFloat](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/to-float/) | L253-L254 | defined | — |
| `theorem` | [finite_irreversibility](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-irreversibility/) | L265-L267 | formalized | `V.C07` |
| `structure` | [VacuumCirculation](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/vacuum-circulation/) | L279-L290 | defined | `V.P31` |
| `theorem` | [no_poincare_conflict](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/no-poincare-conflict/) | L300-L302 | formalized | `V.P32` |
| `theorem` | [arrow_has_endpoint](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/arrow-has-endpoint/) | L315-L317 | formalized | `V.P33` |
| `theorem` | [contrast_with_qft](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/contrast-with-qft/) | L326-L328 | formalized | `V.R123` |
| `structure` | [OrbitStepsNotYears](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/orbit-steps-not-years/) | L331-L336 | defined | `V.R124` |
| `theorem` | [universal_half_life](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/universal-half-life/) | L343-L344 | formalized | `V.R125`, `V.R126` |
| `eval` | [#eval L352](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l352/) | L352-L352 | computed | `V.R127` |
| `eval` | [#eval L354](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l354/) | L354-L354 | computed | — |
| `eval` | [#eval L355](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l355/) | L355-L355 | computed | — |
| `def` | [example_budget](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/example-budget/) | L358-L363 | defined | — |
| `eval` | [#eval L365](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/eval-l365/) | L365-L367 | computed | — |
