---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.FineStructure",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.FineStructure`.",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_slug": "book-iv-sectors-fine-structure",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/FineStructure.lean",
  "sha256": "b08ad690bf2fe8d2872629aa4aad59842c84430a5cc9b3d53af7a7bd6f0e19c9",
  "imports": [
    "TauLib.BookIV.Sectors.CouplingFormulas"
  ],
  "imported_by": [
    "TauLib.BookIII.Spectral.ModularForms",
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.DimensionlessAlpha",
    "TauLib.BookIV.Calibration.DimensionlessNearMatch",
    "TauLib.BookIV.Calibration.EpsteinZeta",
    "TauLib.BookIV.Calibration.MassRatioFormula",
    "TauLib.BookIV.Physics.HolonomyCorrection",
    "TauLib.BookIV.Physics.NucleonMassSplitting",
    "TauLib.Tour.GuidedTour.BookIV"
  ],
  "registry_ids": [
    "IV.D08",
    "IV.P02",
    "IV.R01",
    "IV.R02"
  ],
  "declaration_counts": {
    "def": 14,
    "theorem": 16,
    "structure": 1,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "iota_fourth_numer",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-numer/",
      "source_line_start": 85,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_fourth_denom",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-denom/",
      "source_line_start": 88,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_spectral_numer",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-numer/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D08"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_spectral_denom",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom/",
      "source_line_start": 94,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D08"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_spectral_denom_pos",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom-pos/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_spectral_float",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-float/",
      "source_line_start": 105,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_inverse_float",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-float/",
      "source_line_start": 109,
      "source_line_end": 110,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_in_range",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-in-range/",
      "source_line_start": 119,
      "source_line_end": 124,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P02"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_inverse_in_range",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-in-range/",
      "source_line_start": 127,
      "source_line_end": 146,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.R02"
      ]
    },
    {
      "kind": "def",
      "name": "wrong_alpha_numer",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-numer/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "wrong_alpha_denom",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-denom/",
      "source_line_start": 152,
      "source_line_end": 152,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wrong_formula_refutation",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-formula-refutation/",
      "source_line_start": 158,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correct_vs_wrong_ratio",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/correct-vs-wrong-ratio/",
      "source_line_start": 168,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_from_em_coupling",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-from-em-coupling/",
      "source_line_start": 186,
      "source_line_end": 195,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_numer",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-numer/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_denom",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom/",
      "source_line_start": 207,
      "source_line_end": 207,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_denom_pos",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom-pos/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_float",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-float/",
      "source_line_start": 214,
      "source_line_end": 215,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_inverse_float",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-float/",
      "source_line_start": 218,
      "source_line_end": 219,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_in_range",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-in-range/",
      "source_line_start": 224,
      "source_line_end": 229,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_inverse_tight",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-tight/",
      "source_line_start": 233,
      "source_line_end": 238,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_refines_spectral",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/tower-refines-spectral/",
      "source_line_start": 244,
      "source_line_end": 250,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_correction_is_s5",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/tower-correction-is-s5/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_solenoidal_numerator",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-numerator/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_solenoidal_form",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-form/",
      "source_line_start": 274,
      "source_line_end": 277,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyFormula",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/holonomy-formula/",
      "source_line_start": 298,
      "source_line_end": 306,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R01"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_alpha",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/holonomy-alpha/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_is_fourth_power",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-is-fourth-power/",
      "source_line_start": 319,
      "source_line_end": 322,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_exp_inverse_scaled",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-exp-inverse-scaled/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_inverse_correct_ballpark",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-correct-ballpark/",
      "source_line_start": 335,
      "source_line_end": 340,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_factor_decomposition",
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/primorial-factor-decomposition/",
      "source_line_start": 350,
      "source_line_end": 351,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 358,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l359/",
      "source_line_start": 359,
      "source_line_end": 359,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l362/",
      "source_line_start": 362,
      "source_line_end": 362,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l369/",
      "source_line_start": 369,
      "source_line_end": 369,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l370/",
      "source_line_start": 370,
      "source_line_end": 370,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 374,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l375/",
      "source_line_start": 375,
      "source_line_end": 375,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 382,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean",
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
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/FineStructure.lean`
- SHA-256: `b08ad690bf2fe8d2872629aa4aad59842c84430a5cc9b3d53af7a7bd6f0e19c9`

## Registry Links

- `IV.D08` — Spectral Fine Structure
- `IV.P02` — α Numerical Range
- `IV.R01` — Holonomy vs Spectral
- `IV.R02` — Wrong Formula Correction

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.CouplingFormulas`

## Imported By

- `TauLib.BookIII.Spectral.ModularForms`
- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.DimensionlessAlpha`
- `TauLib.BookIV.Calibration.DimensionlessNearMatch`
- `TauLib.BookIV.Calibration.EpsteinZeta`
- `TauLib.BookIV.Calibration.MassRatioFormula`
- `TauLib.BookIV.Physics.HolonomyCorrection`
- `TauLib.BookIV.Physics.NucleonMassSplitting`
- `TauLib.Tour.GuidedTour.BookIV`

## Declaration Counts

- `def`: 14
- `eval`: 10
- `structure`: 1
- `theorem`: 16

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [iota_fourth_numer](/verify/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-numer/) | L85-L85 | defined | — |
| `def` | [iota_fourth_denom](/verify/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-denom/) | L88-L88 | defined | — |
| `def` | [alpha_spectral_numer](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-numer/) | L91-L91 | defined | `IV.D08` |
| `def` | [alpha_spectral_denom](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom/) | L94-L94 | defined | `IV.D08` |
| `theorem` | [alpha_spectral_denom_pos](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom-pos/) | L97-L98 | formalized | — |
| `def` | [alpha_spectral_float](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-float/) | L105-L106 | defined | — |
| `def` | [alpha_inverse_float](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-float/) | L109-L110 | defined | — |
| `theorem` | [alpha_in_range](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-in-range/) | L119-L124 | formalized | `IV.P02` |
| `theorem` | [alpha_inverse_in_range](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-in-range/) | L127-L146 | formalized | `IV.R02` |
| `def` | [wrong_alpha_numer](/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-numer/) | L149-L149 | defined | — |
| `def` | [wrong_alpha_denom](/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-denom/) | L152-L152 | defined | — |
| `theorem` | [wrong_formula_refutation](/verify/taulib/docs/book-iv-sectors-fine-structure/wrong-formula-refutation/) | L158-L163 | formalized | — |
| `theorem` | [correct_vs_wrong_ratio](/verify/taulib/docs/book-iv-sectors-fine-structure/correct-vs-wrong-ratio/) | L168-L174 | formalized | — |
| `theorem` | [alpha_from_em_coupling](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-from-em-coupling/) | L186-L195 | formalized | — |
| `def` | [alpha_tower_numer](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-numer/) | L203-L203 | defined | — |
| `def` | [alpha_tower_denom](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom/) | L207-L207 | defined | — |
| `theorem` | [alpha_tower_denom_pos](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom-pos/) | L210-L211 | formalized | — |
| `def` | [alpha_tower_float](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-float/) | L214-L215 | defined | — |
| `def` | [alpha_tower_inverse_float](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-float/) | L218-L219 | defined | — |
| `theorem` | [alpha_tower_in_range](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-in-range/) | L224-L229 | formalized | — |
| `theorem` | [alpha_tower_inverse_tight](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-tight/) | L233-L238 | formalized | — |
| `theorem` | [tower_refines_spectral](/verify/taulib/docs/book-iv-sectors-fine-structure/tower-refines-spectral/) | L244-L250 | formalized | — |
| `theorem` | [tower_correction_is_s5](/verify/taulib/docs/book-iv-sectors-fine-structure/tower-correction-is-s5/) | L254-L255 | formalized | — |
| `theorem` | [alpha_solenoidal_numerator](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-numerator/) | L268-L269 | formalized | — |
| `theorem` | [alpha_solenoidal_form](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-form/) | L274-L277 | formalized | — |
| `structure` | [HolonomyFormula](/verify/taulib/docs/book-iv-sectors-fine-structure/holonomy-formula/) | L298-L306 | defined | `IV.R01` |
| `def` | [holonomy_alpha](/verify/taulib/docs/book-iv-sectors-fine-structure/holonomy-alpha/) | L309-L309 | defined | — |
| `theorem` | [alpha_is_fourth_power](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-is-fourth-power/) | L319-L322 | formalized | — |
| `def` | [alpha_exp_inverse_scaled](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-exp-inverse-scaled/) | L331-L331 | defined | — |
| `theorem` | [alpha_inverse_correct_ballpark](/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-correct-ballpark/) | L335-L340 | formalized | — |
| `theorem` | [primorial_factor_decomposition](/verify/taulib/docs/book-iv-sectors-fine-structure/primorial-factor-decomposition/) | L350-L351 | formalized | — |
| `eval` | [#eval L358](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l358/) | L358-L358 | computed | — |
| `eval` | [#eval L359](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l359/) | L359-L359 | computed | — |
| `eval` | [#eval L362](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l362/) | L362-L362 | computed | — |
| `eval` | [#eval L366](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l366/) | L366-L366 | computed | — |
| `eval` | [#eval L369](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l369/) | L369-L369 | computed | — |
| `eval` | [#eval L370](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l370/) | L370-L370 | computed | — |
| `eval` | [#eval L374](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l374/) | L374-L374 | computed | — |
| `eval` | [#eval L375](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l375/) | L375-L375 | computed | — |
| `eval` | [#eval L379](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l379/) | L379-L379 | computed | — |
| `eval` | [#eval L380](/verify/taulib/docs/book-iv-sectors-fine-structure/eval-l380/) | L380-L382 | computed | — |
