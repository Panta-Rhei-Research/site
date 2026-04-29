---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.RunningRegime",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.RunningRegime`.",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_slug": "book-iv-calibration-running-regime",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/RunningRegime.lean",
  "sha256": "eae3dcb6782f5202c876b449d2b183a861f01d74ae4ab51805cc6ed739c3826c",
  "imports": [
    "TauLib.BookIV.Calibration.ConstantsLedger",
    "TauLib.BookIV.Physics.Thermodynamics"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D299",
    "IV.D300",
    "IV.D301",
    "IV.D302",
    "IV.D303",
    "IV.D304",
    "IV.P168",
    "IV.P169",
    "IV.P170",
    "IV.R279",
    "IV.R280",
    "IV.R282",
    "IV.T113"
  ],
  "declaration_counts": {
    "structure": 6,
    "theorem": 4,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BetaFunction",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/beta-function/",
      "source_line_start": 42,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D299"
      ]
    },
    {
      "kind": "structure",
      "name": "ObservableLedger",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/observable-ledger/",
      "source_line_start": 59,
      "source_line_end": 66,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D300"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutFunctor",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-functor/",
      "source_line_start": 75,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D301"
      ]
    },
    {
      "kind": "theorem",
      "name": "readout_properties",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-properties/",
      "source_line_start": 88,
      "source_line_end": 90,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P168"
      ]
    },
    {
      "kind": "theorem",
      "name": "beta_as_derivative",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/beta-as-derivative/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P169"
      ]
    },
    {
      "kind": "structure",
      "name": "EntropyAtScale",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/entropy-at-scale/",
      "source_line_start": 112,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D302"
      ]
    },
    {
      "kind": "theorem",
      "name": "entropy_invariance",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/entropy-invariance/",
      "source_line_start": 126,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P170"
      ]
    },
    {
      "kind": "structure",
      "name": "RegimeTransition",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/regime-transition/",
      "source_line_start": 137,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D303"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutLandscape",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-landscape/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D304"
      ]
    },
    {
      "kind": "theorem",
      "name": "readout_landscape_unique",
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-landscape-unique/",
      "source_line_start": 173,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T113"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/eval-l180/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/eval-l181/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-running-regime/eval-l182/",
      "source_line_start": 182,
      "source_line_end": 184,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean",
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
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/RunningRegime.lean`
- SHA-256: `eae3dcb6782f5202c876b449d2b183a861f01d74ae4ab51805cc6ed739c3826c`

## Registry Links

- `IV.D299` — Beta function
- `IV.D300` — Coupling Ledger and Observable Ledger
- `IV.D301` — Readout Functor
- `IV.D302` — Entropy splitting
- `IV.D303` — Regime transition
- `IV.D304` — Readout landscape
- `IV.P168` — Readout Properties
- `IV.P169` — Beta Function as Readout Derivative
- `IV.P170` — Total Entropy Invariance
- `IV.R279` — Asymptotic freedom revisited
- `IV.R280` — Scheme dependence resolved
- `IV.R282` — Lean formalization
- `IV.T113` — Readout Landscape Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Calibration.ConstantsLedger`
- `TauLib.BookIV.Physics.Thermodynamics`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `eval`: 3
- `structure`: 6
- `theorem`: 4

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [BetaFunction](/verify/taulib/docs/book-iv-calibration-running-regime/beta-function/) | L42-L50 | defined | `IV.D299` |
| `structure` | [ObservableLedger](/verify/taulib/docs/book-iv-calibration-running-regime/observable-ledger/) | L59-L66 | defined | `IV.D300` |
| `structure` | [ReadoutFunctor](/verify/taulib/docs/book-iv-calibration-running-regime/readout-functor/) | L75-L85 | defined | `IV.D301` |
| `theorem` | [readout_properties](/verify/taulib/docs/book-iv-calibration-running-regime/readout-properties/) | L88-L90 | formalized | `IV.P168` |
| `theorem` | [beta_as_derivative](/verify/taulib/docs/book-iv-calibration-running-regime/beta-as-derivative/) | L95-L97 | formalized | `IV.P169` |
| `structure` | [EntropyAtScale](/verify/taulib/docs/book-iv-calibration-running-regime/entropy-at-scale/) | L112-L122 | defined | `IV.D302` |
| `theorem` | [entropy_invariance](/verify/taulib/docs/book-iv-calibration-running-regime/entropy-invariance/) | L126-L129 | formalized | `IV.P170` |
| `structure` | [RegimeTransition](/verify/taulib/docs/book-iv-calibration-running-regime/regime-transition/) | L137-L145 | defined | `IV.D303` |
| `structure` | [ReadoutLandscape](/verify/taulib/docs/book-iv-calibration-running-regime/readout-landscape/) | L157-L164 | defined | `IV.D304` |
| `theorem` | [readout_landscape_unique](/verify/taulib/docs/book-iv-calibration-running-regime/readout-landscape-unique/) | L173-L174 | formalized | `IV.T113` |
| `eval` | [#eval L180](/verify/taulib/docs/book-iv-calibration-running-regime/eval-l180/) | L180-L180 | computed | — |
| `eval` | [#eval L181](/verify/taulib/docs/book-iv-calibration-running-regime/eval-l181/) | L181-L181 | computed | — |
| `eval` | [#eval L182](/verify/taulib/docs/book-iv-calibration-running-regime/eval-l182/) | L182-L184 | computed | — |
