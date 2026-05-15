---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.EHTReread",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.EHTReread`.",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_slug": "book-v-astrophysics-ehtreread",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/EHTReread.lean",
  "sha256": "c805ae9b57b8ed73e26fcfc14162d4ce4862699de00bb005a1deceefb1f0c2c6",
  "imports": [
    "TauLib.BookV.Astrophysics.BinaryMergersGW"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.BulletClusterLSS"
  ],
  "registry_ids": [
    "V.D137",
    "V.D138",
    "V.D139",
    "V.D241",
    "V.D284",
    "V.D287",
    "V.D288",
    "V.P82",
    "V.P83",
    "V.R196",
    "V.R197",
    "V.R198",
    "V.R199",
    "V.R412",
    "V.T184",
    "V.T227",
    "V.T229",
    "V.T230",
    "V.T95",
    "V.T96"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 15,
    "def": 21,
    "theorem": 23,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "HorizonType",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/horizon-type/",
      "source_line_start": 67,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauHorizonDef",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/tau-horizon-def/",
      "source_line_start": 84,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D137"
      ]
    },
    {
      "kind": "def",
      "name": "m87_shadow_uas",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-shadow-uas/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_shadow_uas",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-shadow-uas/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shadow_size_prediction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-size-prediction/",
      "source_line_start": 121,
      "source_line_end": 123,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T95"
      ]
    },
    {
      "kind": "theorem",
      "name": "photon_ring_holonomy",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/photon-ring-holonomy/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P82"
      ]
    },
    {
      "kind": "structure",
      "name": "EHTObservableData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/ehtobservable-data/",
      "source_line_start": 146,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D138"
      ]
    },
    {
      "kind": "def",
      "name": "m87_eht",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-eht/",
      "source_line_start": 160,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_eht",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-eht/",
      "source_line_start": 167,
      "source_line_end": 171,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shadow_circularity",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-circularity/",
      "source_line_start": 181,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P83"
      ]
    },
    {
      "kind": "structure",
      "name": "HorizonComparison",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/horizon-comparison/",
      "source_line_start": 191,
      "source_line_end": 204,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D139"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_comparison",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/canonical-comparison/",
      "source_line_start": 207,
      "source_line_end": 207,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_information_loss",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/no-information-loss/",
      "source_line_start": 223,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T96"
      ]
    },
    {
      "kind": "def",
      "name": "iota_float",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/iota-float/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.R196",
        "V.R197",
        "V.R198",
        "V.R199"
      ]
    },
    {
      "kind": "def",
      "name": "t2_shadow_correction_factor",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction-factor/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.D241"
      ]
    },
    {
      "kind": "structure",
      "name": "T2ShadowCorrection",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction/",
      "source_line_start": 263,
      "source_line_end": 275,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D241"
      ]
    },
    {
      "kind": "theorem",
      "name": "t2_shadow_correction_conjunction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction-conjunction/",
      "source_line_start": 278,
      "source_line_end": 283,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shadow_denominator_is_ell_sq",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-denominator-is-ell-sq/",
      "source_line_start": 286,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l290/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "eht_shadow_t2_pct_over_gr",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-pct-over-gr/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.T184"
      ]
    },
    {
      "kind": "structure",
      "name": "EHTShadowT2",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/ehtshadow-t2/",
      "source_line_start": 298,
      "source_line_end": 310,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T184"
      ]
    },
    {
      "kind": "theorem",
      "name": "eht_shadow_t2_conjunction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-conjunction/",
      "source_line_start": 313,
      "source_line_end": 318,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shadow_correction_gt_one",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-correction-gt-one/",
      "source_line_start": 321,
      "source_line_end": 323,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l325/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BiRotationalDynamics",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/bi-rotational-dynamics/",
      "source_line_start": 344,
      "source_line_end": 348,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SynchrotronFrequencyPair",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/synchrotron-frequency-pair/",
      "source_line_start": 351,
      "source_line_end": 356,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "birotational_synchrotron_ratio_x1000",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/birotational-synchrotron-ratio-x1000/",
      "source_line_start": 359,
      "source_line_end": 359,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_synchrotron",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-synchrotron/",
      "source_line_start": 362,
      "source_line_end": 363,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_synchrotron",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-synchrotron/",
      "source_line_start": 366,
      "source_line_end": 367,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "synchrotron_ratio_universal",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/synchrotron-ratio-universal/",
      "source_line_start": 370,
      "source_line_end": 372,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BrightnessHarmonicMode",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-harmonic-mode/",
      "source_line_start": 379,
      "source_line_end": 383,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "brightness_modes",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-modes/",
      "source_line_start": 386,
      "source_line_end": 393,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "harmonic_frequency_ratio_x1000",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/harmonic-frequency-ratio-x1000/",
      "source_line_start": 397,
      "source_line_end": 397,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SgrAVariability",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgr-avariability/",
      "source_line_start": 401,
      "source_line_end": 405,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_variability",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-variability/",
      "source_line_start": 407,
      "source_line_end": 407,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "M87Variability",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-variability/",
      "source_line_start": 411,
      "source_line_end": 414,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_variability",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-variability-l416/",
      "source_line_start": 416,
      "source_line_end": 416,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "variability_ratio_matches_synchrotron",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/variability-ratio-matches-synchrotron/",
      "source_line_start": 419,
      "source_line_end": 421,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "brightness_eigenvalue_eq_qnm",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-eigenvalue-eq-qnm/",
      "source_line_start": 437,
      "source_line_end": 439,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "brightness_ratio_is_iota_inv_x1000",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-ratio-is-iota-inv-x1000/",
      "source_line_start": 445,
      "source_line_end": 446,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "birotation_ratio_eq_qnm_ratio",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/birotation-ratio-eq-qnm-ratio/",
      "source_line_start": 456,
      "source_line_end": 457,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_ratios_unified",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/all-ratios-unified/",
      "source_line_start": 461,
      "source_line_end": 465,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SMBHPrediction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/smbhprediction/",
      "source_line_start": 472,
      "source_line_end": 479,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_prediction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-prediction/",
      "source_line_start": 482,
      "source_line_end": 483,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_prediction",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-prediction/",
      "source_line_start": 486,
      "source_line_end": 487,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "smbh_universal_t2",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/smbh-universal-t2/",
      "source_line_start": 490,
      "source_line_end": 493,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "m87_shadow_in_eht_range",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-shadow-in-eht-range/",
      "source_line_start": 496,
      "source_line_end": 499,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sgra_shadow_in_eht_2sigma",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-shadow-in-eht-2sigma/",
      "source_line_start": 502,
      "source_line_end": 505,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "eht_comparison_remark",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-comparison-remark/",
      "source_line_start": 508,
      "source_line_end": 510,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ToroidalBFieldConfig",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/toroidal-bfield-config/",
      "source_line_start": 519,
      "source_line_end": 531,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D284"
      ]
    },
    {
      "kind": "theorem",
      "name": "rm_winding_theorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/rm-winding-theorem/",
      "source_line_start": 536,
      "source_line_end": 538,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T227"
      ]
    },
    {
      "kind": "theorem",
      "name": "rm_winding_t2_is_double_s2",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/rm-winding-t2-is-double-s2/",
      "source_line_start": 541,
      "source_line_end": 541,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "StokesParameterSuite",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/stokes-parameter-suite/",
      "source_line_start": 550,
      "source_line_end": 566,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D287"
      ]
    },
    {
      "kind": "theorem",
      "name": "circular_winding_theorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/circular-winding-theorem/",
      "source_line_start": 569,
      "source_line_end": 571,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T229"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_windings_equal",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/all-windings-equal/",
      "source_line_start": 574,
      "source_line_end": 577,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NearHorizonBField",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/near-horizon-bfield/",
      "source_line_start": 585,
      "source_line_end": 596,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D288"
      ]
    },
    {
      "kind": "theorem",
      "name": "magnetic_ratio_is_iota_inv",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-ratio-is-iota-inv/",
      "source_line_start": 599,
      "source_line_end": 601,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T230"
      ]
    },
    {
      "kind": "structure",
      "name": "MagneticPredictionSuite",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-prediction-suite/",
      "source_line_start": 605,
      "source_line_end": 626,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R412"
      ]
    },
    {
      "kind": "theorem",
      "name": "magnetic_suite_winding_consistency",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-suite-winding-consistency/",
      "source_line_start": 629,
      "source_line_end": 632,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_bfield",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-bfield/",
      "source_line_start": 635,
      "source_line_end": 636,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sgra_bfield",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-bfield/",
      "source_line_start": 639,
      "source_line_end": 640,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_stokes",
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-stokes/",
      "source_line_start": 643,
      "source_line_end": 644,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l646/",
      "source_line_start": 646,
      "source_line_end": 646,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l647/",
      "source_line_start": 647,
      "source_line_end": 647,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l648/",
      "source_line_start": 648,
      "source_line_end": 650,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/EHTReread.lean`
- SHA-256: `c805ae9b57b8ed73e26fcfc14162d4ce4862699de00bb005a1deceefb1f0c2c6`

## Registry Links

- `V.D137` — Toroidal Shadow (T^2 Readout)
- `V.D138` — Photon Ring Winding Number
- `V.D139` — Polarization Handedness Signature
- `V.D241` — T² Quadrupole Shadow Correction Factor: f = 1 + ι_τ²/4
- `V.D284` — Toroidal B-Field Configuration
- `V.D287` — Stokes Parameter Decomposition on T²
- `V.D288` — Near-Horizon B-Field
- `V.P82` — Inner Shadow Ellipticity
- `V.P83` — Photon Subring Spacing
- `V.R196` — Observational accessibility
- `V.R197` — M87* Shadow Re-Read
- `V.R198` — Sgr A* Shadow Re-Read
- `V.R199` — The strongest single test
- `V.R412` — Complete Magnetic Table
- `V.T184` — EHT Shadow T² Correction: f = 1 + ι_τ²/4 at 2.91% over GR
- `V.T227` — RM Winding Theorem
- `V.T229` — Circular Polarization Winding
- `V.T230` — Magnetic Field Ratio Theorem
- `V.T95` — Shadow Shape Theorem (T^2 vs S^2)
- `V.T96` — Polarization Winding Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.BinaryMergersGW`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.BulletClusterLSS`

## Declaration Counts

- `def`: 21
- `eval`: 11
- `inductive`: 1
- `structure`: 15
- `theorem`: 23

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [HorizonType](/corpus/taulib/docs/book-v-astrophysics-ehtreread/horizon-type/) | L67-L74 | type/data schema | type/data schema | — |
| `structure` | [TauHorizonDef](/corpus/taulib/docs/book-v-astrophysics-ehtreread/tau-horizon-def/) | L84-L97 | type/data schema | type/data schema | `V.D137` |
| `def` | [m87_shadow_uas](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-shadow-uas/) | L104-L104 | data/computed value | data/computed value | — |
| `def` | [sgra_shadow_uas](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-shadow-uas/) | L105-L105 | data/computed value | data/computed value | — |
| `theorem` | [shadow_size_prediction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-size-prediction/) | L121-L123 | proof obligation | formal proof obligation checked | `V.T95` |
| `theorem` | [photon_ring_holonomy](/corpus/taulib/docs/book-v-astrophysics-ehtreread/photon-ring-holonomy/) | L136-L138 | proof obligation | formal proof obligation checked | `V.P82` |
| `structure` | [EHTObservableData](/corpus/taulib/docs/book-v-astrophysics-ehtreread/ehtobservable-data/) | L146-L157 | type/data schema | type/data schema | `V.D138` |
| `def` | [m87_eht](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-eht/) | L160-L164 | definition | definition | — |
| `def` | [sgra_eht](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-eht/) | L167-L171 | definition | definition | — |
| `theorem` | [shadow_circularity](/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-circularity/) | L181-L183 | proof obligation | formal proof obligation checked | `V.P83` |
| `structure` | [HorizonComparison](/corpus/taulib/docs/book-v-astrophysics-ehtreread/horizon-comparison/) | L191-L204 | type/data schema | type/data schema | `V.D139` |
| `def` | [canonical_comparison](/corpus/taulib/docs/book-v-astrophysics-ehtreread/canonical-comparison/) | L207-L207 | definition | definition | — |
| `theorem` | [no_information_loss](/corpus/taulib/docs/book-v-astrophysics-ehtreread/no-information-loss/) | L223-L225 | proof obligation | formal proof obligation checked | `V.T96` |
| `def` | [iota_float](/corpus/taulib/docs/book-v-astrophysics-ehtreread/iota-float/) | L255-L255 | data/computed value | data/computed value | `V.R196`, `V.R197`, `V.R198`, `V.R199` |
| `def` | [t2_shadow_correction_factor](/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction-factor/) | L259-L259 | data/computed value | data/computed value | `V.D241` |
| `structure` | [T2ShadowCorrection](/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction/) | L263-L275 | type/data schema | type/data schema | `V.D241` |
| `theorem` | [t2_shadow_correction_conjunction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction-conjunction/) | L278-L283 | proof obligation | formal proof obligation checked | — |
| `theorem` | [shadow_denominator_is_ell_sq](/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-denominator-is-ell-sq/) | L286-L288 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L290](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l290/) | L290-L290 | computed check | computed check | — |
| `def` | [eht_shadow_t2_pct_over_gr](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-pct-over-gr/) | L294-L294 | data/computed value | data/computed value | `V.T184` |
| `structure` | [EHTShadowT2](/corpus/taulib/docs/book-v-astrophysics-ehtreread/ehtshadow-t2/) | L298-L310 | type/data schema | type/data schema | `V.T184` |
| `theorem` | [eht_shadow_t2_conjunction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-conjunction/) | L313-L318 | proof obligation | formal proof obligation checked | — |
| `theorem` | [shadow_correction_gt_one](/corpus/taulib/docs/book-v-astrophysics-ehtreread/shadow-correction-gt-one/) | L321-L323 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L325](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l325/) | L325-L325 | computed check | computed check | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l331/) | L331-L331 | computed check | computed check | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l332/) | L332-L332 | computed check | computed check | — |
| `eval` | [#eval L333](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l334/) | L334-L334 | computed check | computed check | — |
| `eval` | [#eval L335](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l335/) | L335-L335 | computed check | computed check | — |
| `eval` | [#eval L336](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l336/) | L336-L336 | computed check | computed check | — |
| `structure` | [BiRotationalDynamics](/corpus/taulib/docs/book-v-astrophysics-ehtreread/bi-rotational-dynamics/) | L344-L348 | type/data schema | type/data schema | — |
| `structure` | [SynchrotronFrequencyPair](/corpus/taulib/docs/book-v-astrophysics-ehtreread/synchrotron-frequency-pair/) | L351-L356 | type/data schema | type/data schema | — |
| `def` | [birotational_synchrotron_ratio_x1000](/corpus/taulib/docs/book-v-astrophysics-ehtreread/birotational-synchrotron-ratio-x1000/) | L359-L359 | data/computed value | data/computed value | — |
| `def` | [m87_synchrotron](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-synchrotron/) | L362-L363 | definition | definition | — |
| `def` | [sgra_synchrotron](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-synchrotron/) | L366-L367 | definition | definition | — |
| `theorem` | [synchrotron_ratio_universal](/corpus/taulib/docs/book-v-astrophysics-ehtreread/synchrotron-ratio-universal/) | L370-L372 | proof obligation | formal proof obligation checked | — |
| `structure` | [BrightnessHarmonicMode](/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-harmonic-mode/) | L379-L383 | type/data schema | type/data schema | — |
| `def` | [brightness_modes](/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-modes/) | L386-L393 | data/computed value | data/computed value | — |
| `def` | [harmonic_frequency_ratio_x1000](/corpus/taulib/docs/book-v-astrophysics-ehtreread/harmonic-frequency-ratio-x1000/) | L397-L397 | data/computed value | data/computed value | — |
| `structure` | [SgrAVariability](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgr-avariability/) | L401-L405 | type/data schema | type/data schema | — |
| `def` | [sgra_variability](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-variability/) | L407-L407 | definition | definition | — |
| `structure` | [M87Variability](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-variability/) | L411-L414 | type/data schema | type/data schema | — |
| `def` | [m87_variability](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-variability-l416/) | L416-L416 | definition | definition | — |
| `theorem` | [variability_ratio_matches_synchrotron](/corpus/taulib/docs/book-v-astrophysics-ehtreread/variability-ratio-matches-synchrotron/) | L419-L421 | proof obligation | formal proof obligation checked | — |
| `theorem` | [brightness_eigenvalue_eq_qnm](/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-eigenvalue-eq-qnm/) | L437-L439 | proof obligation | formal proof obligation checked | — |
| `theorem` | [brightness_ratio_is_iota_inv_x1000](/corpus/taulib/docs/book-v-astrophysics-ehtreread/brightness-ratio-is-iota-inv-x1000/) | L445-L446 | proof obligation | formal proof obligation checked | — |
| `theorem` | [birotation_ratio_eq_qnm_ratio](/corpus/taulib/docs/book-v-astrophysics-ehtreread/birotation-ratio-eq-qnm-ratio/) | L456-L457 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_ratios_unified](/corpus/taulib/docs/book-v-astrophysics-ehtreread/all-ratios-unified/) | L461-L465 | proof obligation | formal proof obligation checked | — |
| `structure` | [SMBHPrediction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/smbhprediction/) | L472-L479 | type/data schema | type/data schema | — |
| `def` | [m87_prediction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-prediction/) | L482-L483 | definition | definition | — |
| `def` | [sgra_prediction](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-prediction/) | L486-L487 | definition | definition | — |
| `theorem` | [smbh_universal_t2](/corpus/taulib/docs/book-v-astrophysics-ehtreread/smbh-universal-t2/) | L490-L493 | proof obligation | formal proof obligation checked | — |
| `theorem` | [m87_shadow_in_eht_range](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-shadow-in-eht-range/) | L496-L499 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sgra_shadow_in_eht_2sigma](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-shadow-in-eht-2sigma/) | L502-L505 | proof obligation | formal proof obligation checked | — |
| `def` | [eht_comparison_remark](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-comparison-remark/) | L508-L510 | docstring/data record | docstring/data record | — |
| `structure` | [ToroidalBFieldConfig](/corpus/taulib/docs/book-v-astrophysics-ehtreread/toroidal-bfield-config/) | L519-L531 | type/data schema | type/data schema | `V.D284` |
| `theorem` | [rm_winding_theorem](/corpus/taulib/docs/book-v-astrophysics-ehtreread/rm-winding-theorem/) | L536-L538 | proof obligation | formal proof obligation checked | `V.T227` |
| `theorem` | [rm_winding_t2_is_double_s2](/corpus/taulib/docs/book-v-astrophysics-ehtreread/rm-winding-t2-is-double-s2/) | L541-L541 | proof obligation | formal proof obligation checked | — |
| `structure` | [StokesParameterSuite](/corpus/taulib/docs/book-v-astrophysics-ehtreread/stokes-parameter-suite/) | L550-L566 | type/data schema | type/data schema | `V.D287` |
| `theorem` | [circular_winding_theorem](/corpus/taulib/docs/book-v-astrophysics-ehtreread/circular-winding-theorem/) | L569-L571 | proof obligation | formal proof obligation checked | `V.T229` |
| `theorem` | [all_windings_equal](/corpus/taulib/docs/book-v-astrophysics-ehtreread/all-windings-equal/) | L574-L577 | proof obligation | formal proof obligation checked | — |
| `structure` | [NearHorizonBField](/corpus/taulib/docs/book-v-astrophysics-ehtreread/near-horizon-bfield/) | L585-L596 | type/data schema | type/data schema | `V.D288` |
| `theorem` | [magnetic_ratio_is_iota_inv](/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-ratio-is-iota-inv/) | L599-L601 | proof obligation | formal proof obligation checked | `V.T230` |
| `structure` | [MagneticPredictionSuite](/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-prediction-suite/) | L605-L626 | type/data schema | type/data schema | `V.R412` |
| `theorem` | [magnetic_suite_winding_consistency](/corpus/taulib/docs/book-v-astrophysics-ehtreread/magnetic-suite-winding-consistency/) | L629-L632 | proof obligation | formal proof obligation checked | — |
| `def` | [m87_bfield](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-bfield/) | L635-L636 | definition | definition | — |
| `def` | [sgra_bfield](/corpus/taulib/docs/book-v-astrophysics-ehtreread/sgra-bfield/) | L639-L640 | definition | definition | — |
| `def` | [m87_stokes](/corpus/taulib/docs/book-v-astrophysics-ehtreread/m87-stokes/) | L643-L644 | definition | definition | — |
| `eval` | [#eval L646](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l646/) | L646-L646 | computed check | computed check | — |
| `eval` | [#eval L647](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l647/) | L647-L647 | computed check | computed check | — |
| `eval` | [#eval L648](/corpus/taulib/docs/book-v-astrophysics-ehtreread/eval-l648/) | L648-L650 | computed check | computed check | — |
