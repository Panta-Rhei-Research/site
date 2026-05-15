---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.ClosingIdentity",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.ClosingIdentity`.",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_slug": "book-v-gravity-field-closing-identity",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/ClosingIdentity.lean",
  "sha256": "919feea70997369f6cdf4a6d802fcee0fa0cb81e9018609b91513a730c938151",
  "imports": [
    "TauLib.BookV.GravityField.CalibrationTriangle",
    "TauLib.BookV.Gravity.CoRotorCoupling"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.NavierStokesMacro",
    "TauLib.BookV.GravityField.ExponentDerivation",
    "TauLib.BookV.Orthodox.CorrespondenceMap",
    "TauLib.BookV.Thermodynamics.Inversion"
  ],
  "registry_ids": [
    "V.D81",
    "V.D82",
    "V.R104",
    "V.R105",
    "V.R106",
    "V.R107",
    "V.R108",
    "V.R109",
    "V.R110",
    "V.T51",
    "V.T52",
    "V.T53",
    "V.T54"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 3,
    "theorem": 7,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "ClosingIdentityData",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-data/",
      "source_line_start": 95,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D81"
      ]
    },
    {
      "kind": "def",
      "name": "closing_identity_canonical",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-canonical/",
      "source_line_start": 118,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CorrectedCoRotor",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/corrected-co-rotor/",
      "source_line_start": 141,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D82"
      ]
    },
    {
      "kind": "def",
      "name": "corrected_corotor",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/corrected-corotor/",
      "source_line_start": 159,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_spectral_distance",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/sqrt3-spectral-distance/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T51"
      ]
    },
    {
      "kind": "theorem",
      "name": "g_predicted_3ppm",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/g-predicted-3ppm/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T52"
      ]
    },
    {
      "kind": "theorem",
      "name": "r_independent_of_kn",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/r-independent-of-kn/",
      "source_line_start": 205,
      "source_line_end": 207,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T53"
      ]
    },
    {
      "kind": "theorem",
      "name": "ten_link_chain_complete",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/ten-link-chain-complete/",
      "source_line_start": 215,
      "source_line_end": 219,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T54"
      ]
    },
    {
      "kind": "theorem",
      "name": "closing_exponent_18",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-exponent-18/",
      "source_line_start": 222,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "closing_deficit_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-deficit-positive/",
      "source_line_start": 227,
      "source_line_end": 229,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "closing_c1_range",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-c1-range/",
      "source_line_start": 232,
      "source_line_end": 234,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TwoPredictions",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/two-predictions/",
      "source_line_start": 266,
      "source_line_end": 273,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "two_predictions",
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/two-predictions-l276/",
      "source_line_start": 276,
      "source_line_end": 278,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l289/",
      "source_line_start": 289,
      "source_line_end": 290,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l297/",
      "source_line_start": 297,
      "source_line_end": 299,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean",
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
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/ClosingIdentity.lean`
- SHA-256: `919feea70997369f6cdf4a6d802fcee0fa0cb81e9018609b91513a730c938151`

## Registry Links

- `V.D81` — Gravitational Closing Identity --- V.D11
- `V.D82` — Corrected Co-Rotor Coupling --- V.D10
- `V.R104` — Scope: c_1 = 3/pi is conjectural
- `V.R105` — G is the least precise fundamental constant
- `V.R106` — The hierarchy ``problem'' dissolved
- `V.R107` — Two independent predictions
- `V.R108` — The closing identity completes the Hermetic Principle
- `V.R109` — Open problem: c_1 from first principles
- `V.R110` — The 7times amplification in R
- `V.T51` — Spectral Distance --- IV.T11
- `V.T52` — G Prediction --- V.T04, V.T05
- `V.T53` — R Formula Independence --- V.R03
- `V.T54` — 10-Link Derivation Chain

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.CalibrationTriangle`
- `TauLib.BookV.Gravity.CoRotorCoupling`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.NavierStokesMacro`
- `TauLib.BookV.GravityField.ExponentDerivation`
- `TauLib.BookV.Orthodox.CorrespondenceMap`
- `TauLib.BookV.Thermodynamics.Inversion`

## Declaration Counts

- `def`: 3
- `eval`: 8
- `structure`: 3
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [ClosingIdentityData](/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-data/) | L95-L115 | type/data schema | type/data schema | `V.D81` |
| `def` | [closing_identity_canonical](/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-canonical/) | L118-L126 | definition | definition | — |
| `structure` | [CorrectedCoRotor](/corpus/taulib/docs/book-v-gravity-field-closing-identity/corrected-co-rotor/) | L141-L156 | type/data schema | type/data schema | `V.D82` |
| `def` | [corrected_corotor](/corpus/taulib/docs/book-v-gravity-field-closing-identity/corrected-corotor/) | L159-L166 | definition | definition | — |
| `theorem` | [sqrt3_spectral_distance](/corpus/taulib/docs/book-v-gravity-field-closing-identity/sqrt3-spectral-distance/) | L177-L179 | proof obligation | formal proof obligation checked | `V.T51` |
| `theorem` | [g_predicted_3ppm](/corpus/taulib/docs/book-v-gravity-field-closing-identity/g-predicted-3ppm/) | L191-L193 | proof obligation | formal proof obligation checked | `V.T52` |
| `theorem` | [r_independent_of_kn](/corpus/taulib/docs/book-v-gravity-field-closing-identity/r-independent-of-kn/) | L205-L207 | proof obligation | formal proof obligation checked | `V.T53` |
| `theorem` | [ten_link_chain_complete](/corpus/taulib/docs/book-v-gravity-field-closing-identity/ten-link-chain-complete/) | L215-L219 | proof obligation | formal proof obligation checked | `V.T54` |
| `theorem` | [closing_exponent_18](/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-exponent-18/) | L222-L224 | proof obligation | formal proof obligation checked | — |
| `theorem` | [closing_deficit_positive](/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-deficit-positive/) | L227-L229 | proof obligation | formal proof obligation checked | — |
| `theorem` | [closing_c1_range](/corpus/taulib/docs/book-v-gravity-field-closing-identity/closing-c1-range/) | L232-L234 | proof obligation | formal proof obligation checked | — |
| `structure` | [TwoPredictions](/corpus/taulib/docs/book-v-gravity-field-closing-identity/two-predictions/) | L266-L273 | type/data schema | type/data schema | — |
| `def` | [two_predictions](/corpus/taulib/docs/book-v-gravity-field-closing-identity/two-predictions-l276/) | L276-L278 | definition | definition | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l285/) | L285-L286 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l288/) | L288-L288 | computed check | computed check | — |
| `eval` | [#eval L289](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l289/) | L289-L290 | computed check | computed check | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l292/) | L292-L293 | computed check | computed check | — |
| `eval` | [#eval L295](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l295/) | L295-L295 | computed check | computed check | — |
| `eval` | [#eval L296](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l296/) | L296-L296 | computed check | computed check | — |
| `eval` | [#eval L297](/corpus/taulib/docs/book-v-gravity-field-closing-identity/eval-l297/) | L297-L299 | computed check | computed check | — |
