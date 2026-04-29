---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.Thermodynamics",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.Thermodynamics`.",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_slug": "book-iv-physics-thermodynamics",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/Thermodynamics.lean",
  "sha256": "edc84896174c2102582a607dd612b5c11b232a1b8fe18cd3309532a59e9f3b4a",
  "imports": [
    "TauLib.BookIV.Physics.DefectFunctional",
    "TauLib.BookIV.Sectors.CouplingFormulas"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.RunningRegime",
    "TauLib.BookIV.QuantumMechanics.EnergyEntropy"
  ],
  "registry_ids": [
    "IV.D24",
    "IV.D25",
    "IV.P04",
    "IV.R05",
    "IV.R06",
    "IV.T04"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 9,
    "theorem": 5,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "EntropySplitting",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/entropy-splitting/",
      "source_line_start": 76,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D24"
      ]
    },
    {
      "kind": "def",
      "name": "EntropySplitting.totalFloat",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/total-float/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EntropySplitting.sDefFloat",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/s-def-float/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EntropySplitting.sRefFloat",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/s-ref-float/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectBudget",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/defect-budget/",
      "source_line_start": 116,
      "source_line_end": 124,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D25"
      ]
    },
    {
      "kind": "structure",
      "name": "NoRunningPrinciple",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-principle/",
      "source_line_start": 140,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P04"
      ]
    },
    {
      "kind": "def",
      "name": "no_running_em",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-em/",
      "source_line_start": 158,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_running_weak",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-weak/",
      "source_line_start": 165,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_running_strong",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-strong/",
      "source_line_start": 172,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_running_gravity",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-gravity/",
      "source_line_start": 179,
      "source_line_end": 183,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_running_higgs",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-higgs/",
      "source_line_start": 186,
      "source_line_end": 190,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_no_running",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/all-no-running/",
      "source_line_start": 193,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_budget_conserved",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/euler-budget-conserved/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T04"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_running_all_sectors",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-all-sectors/",
      "source_line_start": 208,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_regime_independent",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/all-regime-independent/",
      "source_line_start": 211,
      "source_line_end": 214,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s_def_zero_at_horizon",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/s-def-zero-at-horizon/",
      "source_line_start": 218,
      "source_line_end": 219,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.R05"
      ]
    },
    {
      "kind": "theorem",
      "name": "budget_nonneg",
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/budget-nonneg/",
      "source_line_start": 222,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l230/",
      "source_line_start": 230,
      "source_line_end": 230,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 239,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean",
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
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/Thermodynamics.lean`
- SHA-256: `edc84896174c2102582a607dd612b5c11b232a1b8fe18cd3309532a59e9f3b4a`

## Registry Links

- `IV.D24` — Entropy Splitting
- `IV.D25` — Defect Budget
- `IV.P04` — No-Running Principle
- `IV.T04` — Euler Budget Conservation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.DefectFunctional`
- `TauLib.BookIV.Sectors.CouplingFormulas`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.RunningRegime`
- `TauLib.BookIV.QuantumMechanics.EnergyEntropy`

## Declaration Counts

- `def`: 9
- `eval`: 3
- `structure`: 3
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [EntropySplitting](/verify/taulib/docs/book-iv-physics-thermodynamics/entropy-splitting/) | L76-L89 | defined | `IV.D24` |
| `def` | [EntropySplitting.totalFloat](/verify/taulib/docs/book-iv-physics-thermodynamics/total-float/) | L92-L94 | defined | — |
| `def` | [EntropySplitting.sDefFloat](/verify/taulib/docs/book-iv-physics-thermodynamics/s-def-float/) | L97-L98 | defined | — |
| `def` | [EntropySplitting.sRefFloat](/verify/taulib/docs/book-iv-physics-thermodynamics/s-ref-float/) | L101-L102 | defined | — |
| `structure` | [DefectBudget](/verify/taulib/docs/book-iv-physics-thermodynamics/defect-budget/) | L116-L124 | defined | `IV.D25` |
| `structure` | [NoRunningPrinciple](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-principle/) | L140-L151 | defined | `IV.P04` |
| `def` | [no_running_em](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-em/) | L158-L162 | defined | — |
| `def` | [no_running_weak](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-weak/) | L165-L169 | defined | — |
| `def` | [no_running_strong](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-strong/) | L172-L176 | defined | — |
| `def` | [no_running_gravity](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-gravity/) | L179-L183 | defined | — |
| `def` | [no_running_higgs](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-higgs/) | L186-L190 | defined | — |
| `def` | [all_no_running](/verify/taulib/docs/book-iv-physics-thermodynamics/all-no-running/) | L193-L195 | defined | — |
| `theorem` | [euler_budget_conserved](/verify/taulib/docs/book-iv-physics-thermodynamics/euler-budget-conserved/) | L203-L205 | formalized | `IV.T04` |
| `theorem` | [no_running_all_sectors](/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-all-sectors/) | L208-L208 | formalized | — |
| `theorem` | [all_regime_independent](/verify/taulib/docs/book-iv-physics-thermodynamics/all-regime-independent/) | L211-L214 | formalized | — |
| `theorem` | [s_def_zero_at_horizon](/verify/taulib/docs/book-iv-physics-thermodynamics/s-def-zero-at-horizon/) | L218-L219 | formalized | `IV.R05` |
| `theorem` | [budget_nonneg](/verify/taulib/docs/book-iv-physics-thermodynamics/budget-nonneg/) | L222-L223 | formalized | — |
| `eval` | [#eval L230](/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l230/) | L230-L230 | computed | — |
| `eval` | [#eval L234](/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l234/) | L234-L234 | computed | — |
| `eval` | [#eval L237](/verify/taulib/docs/book-iv-physics-thermodynamics/eval-l237/) | L237-L239 | computed | — |
