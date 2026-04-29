---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.HolonomyCorrection",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_slug": "book-iv-physics-holonomy-correction",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/HolonomyCorrection.lean",
  "sha256": "bff21d8cf6788ccd3d66cde9c3f26c627ae53946e0c5d06b257617b5029f498d",
  "imports": [
    "TauLib.BookIV.Sectors.FineStructure"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.DimensionlessAlpha",
    "TauLib.BookIV.MassDerivation.HolonomyDetail",
    "TauLib.BookV.GravityField.ExponentDerivation"
  ],
  "registry_ids": [
    "IV.D44",
    "IV.D45",
    "IV.R12",
    "IV.T12"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 7,
    "theorem": 13,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TripleHolonomy",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/triple-holonomy/",
      "source_line_start": 77,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D44"
      ]
    },
    {
      "kind": "def",
      "name": "triple_holonomy",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/triple-holonomy-l91/",
      "source_line_start": 91,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_circles",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/three-circles/",
      "source_line_start": 99,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pi_cubed_exponent",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-exponent/",
      "source_line_start": 102,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pi_cubed_numer",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-numer/",
      "source_line_start": 113,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pi_cubed_denom",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-denom/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pi_cubed_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-denom-pos/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pi_cubed_float",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-float/",
      "source_line_start": 121,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pi_cubed_in_range",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-in-range/",
      "source_line_start": 125,
      "source_line_end": 128,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_sq_numer",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-numer/",
      "source_line_start": 141,
      "source_line_end": 142,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_sq_denom",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-denom/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_sq_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-denom-pos/",
      "source_line_start": 148,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyCorrectionData",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-correction-data/",
      "source_line_start": 161,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D45"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_correction",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-correction/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction_lt_2_per_mille",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-lt-2-per-mille/",
      "source_line_start": 188,
      "source_line_end": 193,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T12"
      ]
    },
    {
      "kind": "theorem",
      "name": "correction_gt_1_per_mille",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-gt-1-per-mille/",
      "source_line_start": 196,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "perturbative_hierarchy",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/perturbative-hierarchy/",
      "source_line_start": 211,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChargConjugation",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/charg-conjugation/",
      "source_line_start": 239,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R12"
      ]
    },
    {
      "kind": "theorem",
      "name": "holonomy_from_top_cohomology",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-from-top-cohomology/",
      "source_line_start": 261,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D44"
      ]
    },
    {
      "kind": "theorem",
      "name": "charge_conjugation_kills_odd",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/charge-conjugation-kills-odd/",
      "source_line_start": 279,
      "source_line_end": 283,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction_coefficient_unique",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-coefficient-unique/",
      "source_line_start": 294,
      "source_line_end": 298,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s4_from_weight_and_dimension",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/s4-from-weight-and-dimension/",
      "source_line_start": 314,
      "source_line_end": 318,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s4_uniqueness_from_exponent",
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/s4-uniqueness-from-exponent/",
      "source_line_start": 327,
      "source_line_end": 328,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 348,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean",
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
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/HolonomyCorrection.lean`
- SHA-256: `bff21d8cf6788ccd3d66cde9c3f26c627ae53946e0c5d06b257617b5029f498d`

## Registry Links

- `IV.D44` — Triple Holonomy
- `IV.D45` — Holonomy Correction
- `IV.R12` — Charge Conjugation
- `IV.T12` — Correction Smallness

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.FineStructure`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.DimensionlessAlpha`
- `TauLib.BookIV.MassDerivation.HolonomyDetail`
- `TauLib.BookV.GravityField.ExponentDerivation`

## Declaration Counts

- `def`: 7
- `eval`: 5
- `structure`: 3
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TripleHolonomy](/verify/taulib/docs/book-iv-physics-holonomy-correction/triple-holonomy/) | L77-L88 | defined | `IV.D44` |
| `def` | [triple_holonomy](/verify/taulib/docs/book-iv-physics-holonomy-correction/triple-holonomy-l91/) | L91-L96 | defined | — |
| `theorem` | [three_circles](/verify/taulib/docs/book-iv-physics-holonomy-correction/three-circles/) | L99-L99 | formalized | — |
| `theorem` | [pi_cubed_exponent](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-exponent/) | L102-L102 | formalized | — |
| `def` | [pi_cubed_numer](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-numer/) | L113-L113 | defined | — |
| `def` | [pi_cubed_denom](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-denom/) | L114-L114 | defined | — |
| `theorem` | [pi_cubed_denom_pos](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-denom-pos/) | L117-L118 | formalized | — |
| `def` | [pi_cubed_float](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-float/) | L121-L122 | defined | — |
| `theorem` | [pi_cubed_in_range](/verify/taulib/docs/book-iv-physics-holonomy-correction/pi-cubed-in-range/) | L125-L128 | formalized | — |
| `def` | [alpha_sq_numer](/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-numer/) | L141-L142 | defined | — |
| `def` | [alpha_sq_denom](/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-denom/) | L144-L145 | defined | — |
| `theorem` | [alpha_sq_denom_pos](/verify/taulib/docs/book-iv-physics-holonomy-correction/alpha-sq-denom-pos/) | L148-L149 | formalized | — |
| `structure` | [HolonomyCorrectionData](/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-correction-data/) | L161-L170 | defined | `IV.D45` |
| `def` | [holonomy_correction](/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-correction/) | L173-L176 | defined | — |
| `theorem` | [correction_lt_2_per_mille](/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-lt-2-per-mille/) | L188-L193 | formalized | `IV.T12` |
| `theorem` | [correction_gt_1_per_mille](/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-gt-1-per-mille/) | L196-L201 | formalized | — |
| `theorem` | [perturbative_hierarchy](/verify/taulib/docs/book-iv-physics-holonomy-correction/perturbative-hierarchy/) | L211-L222 | formalized | — |
| `structure` | [ChargConjugation](/verify/taulib/docs/book-iv-physics-holonomy-correction/charg-conjugation/) | L239-L246 | defined | `IV.R12` |
| `theorem` | [holonomy_from_top_cohomology](/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-from-top-cohomology/) | L261-L269 | formalized | `IV.D44` |
| `theorem` | [charge_conjugation_kills_odd](/verify/taulib/docs/book-iv-physics-holonomy-correction/charge-conjugation-kills-odd/) | L279-L283 | formalized | — |
| `theorem` | [correction_coefficient_unique](/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-coefficient-unique/) | L294-L298 | formalized | — |
| `theorem` | [s4_from_weight_and_dimension](/verify/taulib/docs/book-iv-physics-holonomy-correction/s4-from-weight-and-dimension/) | L314-L318 | formalized | — |
| `theorem` | [s4_uniqueness_from_exponent](/verify/taulib/docs/book-iv-physics-holonomy-correction/s4-uniqueness-from-exponent/) | L327-L328 | formalized | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L339](/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l339/) | L339-L339 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-iv-physics-holonomy-correction/eval-l345/) | L345-L348 | computed | — |
