---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.FineStructure",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-fine-structure/",
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
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-numer/",
      "source_line_start": 85,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_fourth_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-denom/",
      "source_line_start": 88,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_spectral_numer",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-numer/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D08"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_spectral_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom/",
      "source_line_start": 94,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D08"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_spectral_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom-pos/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_spectral_float",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-float/",
      "source_line_start": 105,
      "source_line_end": 106,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_inverse_float",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-float/",
      "source_line_start": 109,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_in_range",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-in-range/",
      "source_line_start": 119,
      "source_line_end": 124,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P02"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_inverse_in_range",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-in-range/",
      "source_line_start": 127,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.R02"
      ]
    },
    {
      "kind": "def",
      "name": "wrong_alpha_numer",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-numer/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "wrong_alpha_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-denom/",
      "source_line_start": 152,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wrong_formula_refutation",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-formula-refutation/",
      "source_line_start": 158,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correct_vs_wrong_ratio",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/correct-vs-wrong-ratio/",
      "source_line_start": 168,
      "source_line_end": 174,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_from_em_coupling",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-from-em-coupling/",
      "source_line_start": 186,
      "source_line_end": 195,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_numer",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-numer/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom/",
      "source_line_start": 207,
      "source_line_end": 207,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom-pos/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_float",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-float/",
      "source_line_start": 214,
      "source_line_end": 215,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tower_inverse_float",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-float/",
      "source_line_start": 218,
      "source_line_end": 219,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_in_range",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-in-range/",
      "source_line_start": 224,
      "source_line_end": 229,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_tower_inverse_tight",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-tight/",
      "source_line_start": 233,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_refines_spectral",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/tower-refines-spectral/",
      "source_line_start": 244,
      "source_line_end": 250,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_correction_is_s5",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/tower-correction-is-s5/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_solenoidal_numerator",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-numerator/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_solenoidal_form",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-form/",
      "source_line_start": 274,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyFormula",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/holonomy-formula/",
      "source_line_start": 298,
      "source_line_end": 306,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R01"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_alpha",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/holonomy-alpha/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_is_fourth_power",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-is-fourth-power/",
      "source_line_start": 319,
      "source_line_end": 322,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_exp_inverse_scaled",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-exp-inverse-scaled/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_inverse_correct_ballpark",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-correct-ballpark/",
      "source_line_start": 335,
      "source_line_end": 340,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_factor_decomposition",
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/primorial-factor-decomposition/",
      "source_line_start": 350,
      "source_line_end": 351,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 358,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l359/",
      "source_line_start": 359,
      "source_line_end": 359,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l362/",
      "source_line_start": 362,
      "source_line_end": 362,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l369/",
      "source_line_start": 369,
      "source_line_end": 369,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l370/",
      "source_line_start": 370,
      "source_line_end": 370,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 374,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l375/",
      "source_line_start": 375,
      "source_line_end": 375,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 382,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [iota_fourth_numer](/corpus/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-numer/) | L85-L85 | data/computed value | data/computed value | — |
| `def` | [iota_fourth_denom](/corpus/taulib/docs/book-iv-sectors-fine-structure/iota-fourth-denom/) | L88-L88 | data/computed value | data/computed value | — |
| `def` | [alpha_spectral_numer](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-numer/) | L91-L91 | data/computed value | data/computed value | `IV.D08` |
| `def` | [alpha_spectral_denom](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom/) | L94-L94 | data/computed value | data/computed value | `IV.D08` |
| `theorem` | [alpha_spectral_denom_pos](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom-pos/) | L97-L98 | proof obligation | formal proof obligation checked | — |
| `def` | [alpha_spectral_float](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-float/) | L105-L106 | data/computed value | data/computed value | — |
| `def` | [alpha_inverse_float](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-float/) | L109-L110 | data/computed value | data/computed value | — |
| `theorem` | [alpha_in_range](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-in-range/) | L119-L124 | proof obligation | formal proof obligation checked | `IV.P02` |
| `theorem` | [alpha_inverse_in_range](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-in-range/) | L127-L146 | proof obligation | formal proof obligation checked | `IV.R02` |
| `def` | [wrong_alpha_numer](/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-numer/) | L149-L149 | data/computed value | data/computed value | — |
| `def` | [wrong_alpha_denom](/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-alpha-denom/) | L152-L152 | data/computed value | data/computed value | — |
| `theorem` | [wrong_formula_refutation](/corpus/taulib/docs/book-iv-sectors-fine-structure/wrong-formula-refutation/) | L158-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correct_vs_wrong_ratio](/corpus/taulib/docs/book-iv-sectors-fine-structure/correct-vs-wrong-ratio/) | L168-L174 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_from_em_coupling](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-from-em-coupling/) | L186-L195 | proof obligation | formal proof obligation checked | — |
| `def` | [alpha_tower_numer](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-numer/) | L203-L203 | data/computed value | data/computed value | — |
| `def` | [alpha_tower_denom](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom/) | L207-L207 | data/computed value | data/computed value | — |
| `theorem` | [alpha_tower_denom_pos](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-denom-pos/) | L210-L211 | proof obligation | formal proof obligation checked | — |
| `def` | [alpha_tower_float](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-float/) | L214-L215 | data/computed value | data/computed value | — |
| `def` | [alpha_tower_inverse_float](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-float/) | L218-L219 | data/computed value | data/computed value | — |
| `theorem` | [alpha_tower_in_range](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-in-range/) | L224-L229 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_tower_inverse_tight](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-tight/) | L233-L238 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tower_refines_spectral](/corpus/taulib/docs/book-iv-sectors-fine-structure/tower-refines-spectral/) | L244-L250 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tower_correction_is_s5](/corpus/taulib/docs/book-iv-sectors-fine-structure/tower-correction-is-s5/) | L254-L255 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_solenoidal_numerator](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-numerator/) | L268-L269 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_solenoidal_form](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-solenoidal-form/) | L274-L277 | proof obligation | formal proof obligation checked | — |
| `structure` | [HolonomyFormula](/corpus/taulib/docs/book-iv-sectors-fine-structure/holonomy-formula/) | L298-L306 | type/data schema | type/data schema | `IV.R01` |
| `def` | [holonomy_alpha](/corpus/taulib/docs/book-iv-sectors-fine-structure/holonomy-alpha/) | L309-L309 | definition | definition | — |
| `theorem` | [alpha_is_fourth_power](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-is-fourth-power/) | L319-L322 | proof obligation | formal proof obligation checked | — |
| `def` | [alpha_exp_inverse_scaled](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-exp-inverse-scaled/) | L331-L331 | data/computed value | data/computed value | — |
| `theorem` | [alpha_inverse_correct_ballpark](/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-correct-ballpark/) | L335-L340 | proof obligation | formal proof obligation checked | — |
| `theorem` | [primorial_factor_decomposition](/corpus/taulib/docs/book-iv-sectors-fine-structure/primorial-factor-decomposition/) | L350-L351 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L358](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l358/) | L358-L358 | computed check | computed check | — |
| `eval` | [#eval L359](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l359/) | L359-L359 | computed check | computed check | — |
| `eval` | [#eval L362](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l362/) | L362-L362 | computed check | computed check | — |
| `eval` | [#eval L366](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l366/) | L366-L366 | computed check | computed check | — |
| `eval` | [#eval L369](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l369/) | L369-L369 | computed check | computed check | — |
| `eval` | [#eval L370](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l370/) | L370-L370 | computed check | computed check | — |
| `eval` | [#eval L374](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l374/) | L374-L374 | computed check | computed check | — |
| `eval` | [#eval L375](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l375/) | L375-L375 | computed check | computed check | — |
| `eval` | [#eval L379](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l379/) | L379-L379 | computed check | computed check | — |
| `eval` | [#eval L380](/corpus/taulib/docs/book-iv-sectors-fine-structure/eval-l380/) | L380-L382 | computed check | computed check | — |
