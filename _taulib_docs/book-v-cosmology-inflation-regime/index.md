---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.InflationRegime",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.InflationRegime`.",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_slug": "book-v-cosmology-inflation-regime",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/InflationRegime.lean",
  "sha256": "4de6eacd7c7009238a31930da30293b09c6ef0ce62257a73c87d743c80458a9f",
  "imports": [
    "TauLib.BookV.Cosmology.BigBangRegime"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.ThresholdLadder"
  ],
  "registry_ids": [
    "V.C17",
    "V.D155",
    "V.D156",
    "V.D157",
    "V.P91",
    "V.R214",
    "V.R215",
    "V.R216",
    "V.R217",
    "V.T105",
    "V.T106"
  ],
  "declaration_counts": {
    "structure": 6,
    "theorem": 9,
    "def": 4,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "RegimeInvariance",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/regime-invariance/",
      "source_line_start": 72,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D155"
      ]
    },
    {
      "kind": "theorem",
      "name": "regime_invariance_theorem",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/regime-invariance-theorem/",
      "source_line_start": 94,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T105"
      ]
    },
    {
      "kind": "structure",
      "name": "InflatonNoGo",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflaton-no-go/",
      "source_line_start": 109,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.C17"
      ]
    },
    {
      "kind": "theorem",
      "name": "inflaton_nogo",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflaton-nogo/",
      "source_line_start": 121,
      "source_line_end": 121,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InflationaryRegime",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflationary-regime/",
      "source_line_start": 134,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D156"
      ]
    },
    {
      "kind": "structure",
      "name": "EFoldReadout",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/efold-readout/",
      "source_line_start": 161,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D157"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_efolds",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/canonical-efolds/",
      "source_line_start": 169,
      "source_line_end": 171,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "efolds_sufficient",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/efolds-sufficient/",
      "source_line_start": 174,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "flatness_from_compactness",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/flatness-from-compactness/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T106"
      ]
    },
    {
      "kind": "theorem",
      "name": "horizon_resolution",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/horizon-resolution/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P91"
      ]
    },
    {
      "kind": "def",
      "name": "slow_roll_unnecessary",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/slow-roll-unnecessary/",
      "source_line_start": 215,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R215"
      ]
    },
    {
      "kind": "theorem",
      "name": "slow_roll_holds",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/slow-roll-holds/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TensorToScalarPrediction",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/tensor-to-scalar-prediction/",
      "source_line_start": 232,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R217"
      ]
    },
    {
      "kind": "def",
      "name": "tau_r_prediction",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/tau-r-prediction/",
      "source_line_start": 242,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FiberDimensionalSuppression",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/fiber-dimensional-suppression/",
      "source_line_start": 260,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "fiber_suppression",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/fiber-suppression/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r_exponent_decomposition",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/r-exponent-decomposition/",
      "source_line_start": 286,
      "source_line_end": 291,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r_not_slow_roll",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/r-not-slow-roll/",
      "source_line_start": 295,
      "source_line_end": 296,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pt_exponent_decomp",
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/pt-exponent-decomp/",
      "source_line_start": 299,
      "source_line_end": 301,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R214",
        "V.R216"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 329,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean",
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
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/InflationRegime.lean`
- SHA-256: `4de6eacd7c7009238a31930da30293b09c6ef0ce62257a73c87d743c80458a9f`

## Registry Links

- `V.C17` — Inflaton No-Go Corollary
- `V.D155` — Regime Invariance
- `V.D156` — Inflationary Regime
- `V.D157` — e-Fold Readout
- `V.P91` — Horizon Resolution
- `V.R214` — Contrast with running couplings
- `V.R215` — Slow Roll Unnecessary
- `V.R216` — Compactness vs. inflation
- `V.R217` — A falsifiable prediction
- `V.T105` — Regime Invariance Theorem
- `V.T106` — Flatness from Compactness

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.BigBangRegime`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.ThresholdLadder`

## Declaration Counts

- `def`: 4
- `eval`: 6
- `structure`: 6
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [RegimeInvariance](/corpus/taulib/docs/book-v-cosmology-inflation-regime/regime-invariance/) | L72-L83 | type/data schema | type/data schema | `V.D155` |
| `theorem` | [regime_invariance_theorem](/corpus/taulib/docs/book-v-cosmology-inflation-regime/regime-invariance-theorem/) | L94-L96 | proof obligation | formal proof obligation checked | `V.T105` |
| `structure` | [InflatonNoGo](/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflaton-no-go/) | L109-L118 | type/data schema | type/data schema | `V.C17` |
| `theorem` | [inflaton_nogo](/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflaton-nogo/) | L121-L121 | proof obligation | formal proof obligation checked | — |
| `structure` | [InflationaryRegime](/corpus/taulib/docs/book-v-cosmology-inflation-regime/inflationary-regime/) | L134-L147 | type/data schema | type/data schema | `V.D156` |
| `structure` | [EFoldReadout](/corpus/taulib/docs/book-v-cosmology-inflation-regime/efold-readout/) | L161-L166 | type/data schema | type/data schema | `V.D157` |
| `def` | [canonical_efolds](/corpus/taulib/docs/book-v-cosmology-inflation-regime/canonical-efolds/) | L169-L171 | definition | definition | — |
| `theorem` | [efolds_sufficient](/corpus/taulib/docs/book-v-cosmology-inflation-regime/efolds-sufficient/) | L174-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [flatness_from_compactness](/corpus/taulib/docs/book-v-cosmology-inflation-regime/flatness-from-compactness/) | L189-L191 | proof obligation | formal proof obligation checked | `V.T106` |
| `theorem` | [horizon_resolution](/corpus/taulib/docs/book-v-cosmology-inflation-regime/horizon-resolution/) | L203-L205 | proof obligation | formal proof obligation checked | `V.P91` |
| `def` | [slow_roll_unnecessary](/corpus/taulib/docs/book-v-cosmology-inflation-regime/slow-roll-unnecessary/) | L215-L217 | definition | definition | `V.R215` |
| `theorem` | [slow_roll_holds](/corpus/taulib/docs/book-v-cosmology-inflation-regime/slow-roll-holds/) | L219-L219 | proof obligation | formal proof obligation checked | — |
| `structure` | [TensorToScalarPrediction](/corpus/taulib/docs/book-v-cosmology-inflation-regime/tensor-to-scalar-prediction/) | L232-L239 | type/data schema | type/data schema | `V.R217` |
| `def` | [tau_r_prediction](/corpus/taulib/docs/book-v-cosmology-inflation-regime/tau-r-prediction/) | L242-L245 | definition | definition | — |
| `structure` | [FiberDimensionalSuppression](/corpus/taulib/docs/book-v-cosmology-inflation-regime/fiber-dimensional-suppression/) | L260-L281 | type/data schema | type/data schema | — |
| `def` | [fiber_suppression](/corpus/taulib/docs/book-v-cosmology-inflation-regime/fiber-suppression/) | L283-L283 | definition | definition | — |
| `theorem` | [r_exponent_decomposition](/corpus/taulib/docs/book-v-cosmology-inflation-regime/r-exponent-decomposition/) | L286-L291 | proof obligation | formal proof obligation checked | — |
| `theorem` | [r_not_slow_roll](/corpus/taulib/docs/book-v-cosmology-inflation-regime/r-not-slow-roll/) | L295-L296 | proof obligation | formal proof obligation checked | — |
| `theorem` | [pt_exponent_decomp](/corpus/taulib/docs/book-v-cosmology-inflation-regime/pt-exponent-decomp/) | L299-L301 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L322](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l322/) | L322-L322 | computed check | computed check | `V.R214`, `V.R216` |
| `eval` | [#eval L323](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l323/) | L323-L323 | computed check | computed check | — |
| `eval` | [#eval L324](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l324/) | L324-L324 | computed check | computed check | — |
| `eval` | [#eval L325](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l325/) | L325-L325 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-v-cosmology-inflation-regime/eval-l327/) | L327-L329 | computed check | computed check | — |
