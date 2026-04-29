---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.EWSynthesis",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_slug": "book-iv-electroweak-ewsynthesis",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/EWSynthesis.lean",
  "sha256": "a49121b1844a8b9ac5c0269cc01f365c5f3001212af3d76c209123a5b6701a5f",
  "imports": [
    "TauLib.BookIV.Electroweak.TauHiggs2"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Strong.StrongVacuum",
    "TauLib.Tour.GuidedTour.BookIV",
    "TauLib.Tour.OneConstant",
    "TauLib.Tour.Physics",
    "TauLib.Tour.VerifyItYourself"
  ],
  "registry_ids": [
    "IV.D143",
    "IV.P175",
    "IV.P78",
    "IV.P79",
    "IV.R37",
    "IV.R38",
    "IV.R39",
    "IV.R40",
    "IV.T124",
    "IV.T66",
    "IV.T67"
  ],
  "declaration_counts": {
    "structure": 6,
    "def": 19,
    "theorem": 7,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "YukawaCouplingFull",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-coupling-full/",
      "source_line_start": 65,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D143"
      ]
    },
    {
      "kind": "def",
      "name": "YukawaCouplingFull.toFloat",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/to-float/",
      "source_line_start": 81,
      "source_line_end": 82,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_full_top",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-top/",
      "source_line_start": 85,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_full_bottom",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-bottom/",
      "source_line_start": 93,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_full_charm",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-charm/",
      "source_line_start": 101,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_full_electron",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-electron/",
      "source_line_start": 109,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EWSynthesisPrediction",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ewsynthesis-prediction/",
      "source_line_start": 121,
      "source_line_end": 134,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EWSynthesisPrediction.tauFloat",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/tau-float/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EWSynthesisPrediction.expFloat",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/exp-float/",
      "source_line_start": 141,
      "source_line_end": 142,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ew_prediction_table",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-prediction-table/",
      "source_line_start": 145,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T66"
      ]
    },
    {
      "kind": "theorem",
      "name": "nine_ew_quantities",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/nine-ew-quantities/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EWAxiomTrace",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ewaxiom-trace/",
      "source_line_start": 171,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T67"
      ]
    },
    {
      "kind": "def",
      "name": "ew_traces_to_axioms",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-traces-to-axioms/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ew_two_inputs",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-two-inputs/",
      "source_line_start": 184,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Sqrt3Triad",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad/",
      "source_line_start": 202,
      "source_line_end": 213,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T124"
      ]
    },
    {
      "kind": "def",
      "name": "sqrt3_triad",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_triad_count",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad-count/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "yukawa_ordering",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-ordering/",
      "source_line_start": 230,
      "source_line_end": 237,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P78"
      ]
    },
    {
      "kind": "structure",
      "name": "ZeroVsNineteen",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/zero-vs-nineteen/",
      "source_line_start": 251,
      "source_line_end": 258,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P79"
      ]
    },
    {
      "kind": "def",
      "name": "zero_vs_nineteen",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/zero-vs-nineteen-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_zero_params",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/tau-zero-params/",
      "source_line_start": 262,
      "source_line_end": 263,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sm_nineteen_params",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sm-nineteen-params/",
      "source_line_start": 265,
      "source_line_end": 266,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LemniscateSupport",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/lemniscate-support/",
      "source_line_start": 279,
      "source_line_end": 286,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P175"
      ]
    },
    {
      "kind": "def",
      "name": "support_B_lobe",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-b-lobe/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "support_C_lobe",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-c-lobe/",
      "source_line_start": 293,
      "source_line_end": 296,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "support_crossing",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-crossing/",
      "source_line_start": 298,
      "source_line_end": 301,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "three_lemniscate_supports",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/three-lemniscate-supports/",
      "source_line_start": 304,
      "source_line_end": 305,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_supports_count",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/three-supports-count/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_ew_complete",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-ew-complete/",
      "source_line_start": 316,
      "source_line_end": 317,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R37"
      ]
    },
    {
      "kind": "def",
      "name": "remark_no_bsm",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-no-bsm/",
      "source_line_start": 322,
      "source_line_end": 323,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R38"
      ]
    },
    {
      "kind": "def",
      "name": "remark_test_program",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-test-program/",
      "source_line_start": 331,
      "source_line_end": 332,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R39"
      ]
    },
    {
      "kind": "def",
      "name": "remark_book_v_connection",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-book-v-connection/",
      "source_line_start": 338,
      "source_line_end": 339,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R40"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 360,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/EWSynthesis.lean`
- SHA-256: `a49121b1844a8b9ac5c0269cc01f365c5f3001212af3d76c209123a5b6701a5f`

## Registry Links

- `IV.D143` — τ-Yukawa Coupling (Overlap Integral)
- `IV.P175` — Three-Fold Structure of~mathbbL
- `IV.P78` — τ-Yukawa Hierarchy
- `IV.P79` — Framework Comparison
- `IV.R37` — Explicit Overlap Integrals
- `IV.R38` — Precision Gap Lesson
- `IV.R39` — √3 as Category τ Signature
- `IV.R40` — Honesty About Precision
- `IV.T124` — The sqrt3
- `IV.T66` — Electroweak Prediction Table
- `IV.T67` — Zero Free Parameters in Electroweak Sector

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.TauHiggs2`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Strong.StrongVacuum`
- `TauLib.Tour.GuidedTour.BookIV`
- `TauLib.Tour.OneConstant`
- `TauLib.Tour.Physics`
- `TauLib.Tour.VerifyItYourself`

## Declaration Counts

- `def`: 19
- `eval`: 14
- `structure`: 6
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [YukawaCouplingFull](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-coupling-full/) | L65-L78 | defined | `IV.D143` |
| `def` | [YukawaCouplingFull.toFloat](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/to-float/) | L81-L82 | defined | — |
| `def` | [yukawa_full_top](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-top/) | L85-L90 | defined | — |
| `def` | [yukawa_full_bottom](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-bottom/) | L93-L98 | defined | — |
| `def` | [yukawa_full_charm](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-charm/) | L101-L106 | defined | — |
| `def` | [yukawa_full_electron](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-electron/) | L109-L114 | defined | — |
| `structure` | [EWSynthesisPrediction](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ewsynthesis-prediction/) | L121-L134 | defined | — |
| `def` | [EWSynthesisPrediction.tauFloat](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/tau-float/) | L137-L138 | defined | — |
| `def` | [EWSynthesisPrediction.expFloat](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/exp-float/) | L141-L142 | defined | — |
| `def` | [ew_prediction_table](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-prediction-table/) | L145-L155 | defined | `IV.T66` |
| `theorem` | [nine_ew_quantities](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/nine-ew-quantities/) | L158-L158 | formalized | — |
| `structure` | [EWAxiomTrace](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ewaxiom-trace/) | L171-L180 | defined | `IV.T67` |
| `def` | [ew_traces_to_axioms](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-traces-to-axioms/) | L182-L182 | defined | — |
| `theorem` | [ew_two_inputs](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-two-inputs/) | L184-L185 | formalized | — |
| `structure` | [Sqrt3Triad](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad/) | L202-L213 | defined | `IV.T124` |
| `def` | [sqrt3_triad](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad-l215/) | L215-L215 | defined | — |
| `theorem` | [sqrt3_triad_count](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad-count/) | L217-L218 | formalized | — |
| `theorem` | [yukawa_ordering](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-ordering/) | L230-L237 | formalized | `IV.P78` |
| `structure` | [ZeroVsNineteen](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/zero-vs-nineteen/) | L251-L258 | defined | `IV.P79` |
| `def` | [zero_vs_nineteen](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/zero-vs-nineteen-l260/) | L260-L260 | defined | — |
| `theorem` | [tau_zero_params](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/tau-zero-params/) | L262-L263 | formalized | — |
| `theorem` | [sm_nineteen_params](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sm-nineteen-params/) | L265-L266 | formalized | — |
| `structure` | [LemniscateSupport](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/lemniscate-support/) | L279-L286 | defined | `IV.P175` |
| `def` | [support_B_lobe](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-b-lobe/) | L288-L291 | defined | — |
| `def` | [support_C_lobe](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-c-lobe/) | L293-L296 | defined | — |
| `def` | [support_crossing](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/support-crossing/) | L298-L301 | defined | — |
| `def` | [three_lemniscate_supports](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/three-lemniscate-supports/) | L304-L305 | defined | — |
| `theorem` | [three_supports_count](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/three-supports-count/) | L307-L308 | formalized | — |
| `def` | [remark_ew_complete](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-ew-complete/) | L316-L317 | defined | `IV.R37` |
| `def` | [remark_no_bsm](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-no-bsm/) | L322-L323 | defined | `IV.R38` |
| `def` | [remark_test_program](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-test-program/) | L331-L332 | defined | `IV.R39` |
| `def` | [remark_book_v_connection](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-book-v-connection/) | L338-L339 | defined | `IV.R40` |
| `eval` | [#eval L345](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l350/) | L350-L350 | computed | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l354/) | L354-L354 | computed | — |
| `eval` | [#eval L355](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l355/) | L355-L355 | computed | — |
| `eval` | [#eval L356](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l356/) | L356-L356 | computed | — |
| `eval` | [#eval L357](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l357/) | L357-L357 | computed | — |
| `eval` | [#eval L358](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/eval-l358/) | L358-L360 | computed | — |
