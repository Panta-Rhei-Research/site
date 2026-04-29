---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.BHTopoModes",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.BHTopoModes`.",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_slug": "book-v-gravity-bhtopo-modes",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/BHTopoModes.lean",
  "sha256": "8f715aa61644479d99e0d7aa2d036f455f14f05dc531d2d321dfd6ee94bce696",
  "imports": [
    "TauLib.BookV.Gravity.Schwarzschild",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookVI.CosmicLife.BHDist",
    "TauLib.BookVI.CosmicLife.BHSelfDesc"
  ],
  "registry_ids": [
    "V.D234",
    "V.D242",
    "V.D243",
    "V.P124",
    "V.P125",
    "V.P131",
    "V.R373",
    "V.R374",
    "V.R380",
    "V.T168",
    "V.T169",
    "V.T185"
  ],
  "declaration_counts": {
    "def": 43,
    "structure": 11,
    "theorem": 33,
    "eval": 33
  },
  "declarations": [
    {
      "kind": "def",
      "name": "iota_float",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/iota-float/",
      "source_line_start": 46,
      "source_line_end": 46,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TorusMode",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-mode/",
      "source_line_start": 57,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": [
        "V.D234"
      ]
    },
    {
      "kind": "def",
      "name": "primitiveTorusModes",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/primitive-torus-modes/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusEigenvalue",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-eigenvalue/",
      "source_line_start": 71,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusQnmFreq",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-qnm-freq/",
      "source_line_start": 78,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ratio_is_iota_inv",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-is-iota-inv/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T168"
      ]
    },
    {
      "kind": "def",
      "name": "qnm_frequency_ratio",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "schwarzschild_overtone_ratio",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/schwarzschild-overtone-ratio/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "G_Newton",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/g-newton/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c_light",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/c-light/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "M_sun",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/m-sun/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_time_outer",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-outer/",
      "source_line_start": 122,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": [
        "V.T169"
      ]
    },
    {
      "kind": "def",
      "name": "echo_time_inner",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/",
      "source_line_start": 127,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": [
        "V.T169"
      ]
    },
    {
      "kind": "def",
      "name": "echo_separation",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": [
        "V.R373"
      ]
    },
    {
      "kind": "def",
      "name": "echo_separation_ms",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-ms/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_shadow_tau_outer_uas",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-tau-outer-uas/",
      "source_line_start": 147,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": [
        "V.P124"
      ]
    },
    {
      "kind": "def",
      "name": "m87_shadow_gr_uas",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-gr-uas/",
      "source_line_start": 155,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torus_entropy_ratio",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio/",
      "source_line_start": 169,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": [
        "V.P125"
      ]
    },
    {
      "kind": "def",
      "name": "no_hawking_argument",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/no-hawking-argument/",
      "source_line_start": 179,
      "source_line_end": 183,
      "formal_status": "defined",
      "registry_ids": [
        "V.R374"
      ]
    },
    {
      "kind": "theorem",
      "name": "three_primitive_modes",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/three-primitive-modes/",
      "source_line_start": 190,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "outer_mode_has_zero_inner",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/outer-mode-has-zero-inner/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "inner_mode_has_zero_outer",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/inner-mode-has-zero-outer/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ratio_gt_one",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-gt-one/",
      "source_line_start": 203,
      "source_line_end": 206,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "torus_entropy_ratio_gt_one",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio-gt-one/",
      "source_line_start": 209,
      "source_line_end": 212,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "outer_echo_longer_than_inner",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/outer-echo-longer-than-inner/",
      "source_line_start": 218,
      "source_line_end": 220,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_separation_pos",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-pos/",
      "source_line_start": 225,
      "source_line_end": 227,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 243,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l255/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_qnm_eigenvalue_structure",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalue-structure/",
      "source_line_start": 269,
      "source_line_end": 271,
      "formal_status": "defined",
      "registry_ids": [
        "V.D242"
      ]
    },
    {
      "kind": "structure",
      "name": "T2QNMEigenvalues",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnmeigenvalues/",
      "source_line_start": 276,
      "source_line_end": 288,
      "formal_status": "defined",
      "registry_ids": [
        "V.D242"
      ]
    },
    {
      "kind": "theorem",
      "name": "t2_qnm_eigenvalues_conjunction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalues-conjunction/",
      "source_line_start": 291,
      "source_line_end": 295,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_qnm_modes_eq_list",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-modes-eq-list/",
      "source_line_start": 298,
      "source_line_end": 299,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_echo_time_formulas",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/",
      "source_line_start": 305,
      "source_line_end": 307,
      "formal_status": "defined",
      "registry_ids": [
        "V.D243"
      ]
    },
    {
      "kind": "structure",
      "name": "T2EchoFormulas",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas/",
      "source_line_start": 312,
      "source_line_end": 321,
      "formal_status": "defined",
      "registry_ids": [
        "V.D243"
      ]
    },
    {
      "kind": "def",
      "name": "t2_echo_formulas_data",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-data/",
      "source_line_start": 324,
      "source_line_end": 327,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_formulas_conjunction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-conjunction/",
      "source_line_start": 330,
      "source_line_end": 334,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_ratio_approx",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-ratio-approx/",
      "source_line_start": 337,
      "source_line_end": 338,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "qnm_frequency_ratio_discriminator",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio-discriminator/",
      "source_line_start": 345,
      "source_line_end": 347,
      "formal_status": "defined",
      "registry_ids": [
        "V.T185"
      ]
    },
    {
      "kind": "structure",
      "name": "QNMDiscriminator",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnmdiscriminator/",
      "source_line_start": 352,
      "source_line_end": 367,
      "formal_status": "defined",
      "registry_ids": [
        "V.T185"
      ]
    },
    {
      "kind": "def",
      "name": "qnm_discriminator_data",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-data/",
      "source_line_start": 370,
      "source_line_end": 373,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_discriminator_conjunction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-conjunction/",
      "source_line_start": 376,
      "source_line_end": 381,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ranges_separated",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ranges-separated/",
      "source_line_start": 384,
      "source_line_end": 386,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l388/",
      "source_line_start": 388,
      "source_line_end": 388,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l391/",
      "source_line_start": 391,
      "source_line_end": 391,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l392/",
      "source_line_start": 392,
      "source_line_end": 392,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_t2_falsification",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification/",
      "source_line_start": 401,
      "source_line_end": 406,
      "formal_status": "defined",
      "registry_ids": [
        "V.P131"
      ]
    },
    {
      "kind": "structure",
      "name": "BHT2Falsification",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bht2-falsification/",
      "source_line_start": 409,
      "source_line_end": 418,
      "formal_status": "defined",
      "registry_ids": [
        "V.P131"
      ]
    },
    {
      "kind": "def",
      "name": "bh_t2_falsification_data",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-data/",
      "source_line_start": 421,
      "source_line_end": 424,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_t2_falsification_conjunction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-conjunction/",
      "source_line_start": 427,
      "source_line_end": 431,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_predictions_count",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-predictions-count/",
      "source_line_start": 434,
      "source_line_end": 435,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l437/",
      "source_line_start": 437,
      "source_line_end": 437,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "vop5_sprint7e_status",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-sprint7e-status/",
      "source_line_start": 447,
      "source_line_end": 450,
      "formal_status": "defined",
      "registry_ids": [
        "V.R380"
      ]
    },
    {
      "kind": "structure",
      "name": "VOP5Status",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status/",
      "source_line_start": 453,
      "source_line_end": 462,
      "formal_status": "defined",
      "registry_ids": [
        "V.R380"
      ]
    },
    {
      "kind": "def",
      "name": "vop5_data",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-data/",
      "source_line_start": 465,
      "source_line_end": 467,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vop5_status_conjunction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status-conjunction/",
      "source_line_start": 470,
      "source_line_end": 475,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vop5_channels_eq_predictions",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-channels-eq-predictions/",
      "source_line_start": 478,
      "source_line_end": 480,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l482/",
      "source_line_start": 482,
      "source_line_end": 482,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l483/",
      "source_line_start": 483,
      "source_line_end": 483,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHEntropyCatalog",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bhentropy-catalog/",
      "source_line_start": 491,
      "source_line_end": 496,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_entropy_excess_x10000",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-entropy-excess-x10000/",
      "source_line_start": 499,
      "source_line_end": 499,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_entropy_catalog",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-entropy-catalog/",
      "source_line_start": 502,
      "source_line_end": 508,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "entropy_catalog_uniform_excess",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-uniform-excess/",
      "source_line_start": 511,
      "source_line_end": 513,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_catalog_remark",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-remark/",
      "source_line_start": 516,
      "source_line_end": 518,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutGibbsState",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-gibbs-state/",
      "source_line_start": 528,
      "source_line_end": 533,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_readout",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/canonical-readout/",
      "source_line_start": 536,
      "source_line_end": 537,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_no_mass_loss",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-no-mass-loss/",
      "source_line_start": 540,
      "source_line_end": 540,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_is_planckian",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-is-planckian/",
      "source_line_start": 543,
      "source_line_end": 543,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_planckian_gt_mass_loss",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-planckian-gt-mass-loss/",
      "source_line_start": 546,
      "source_line_end": 548,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutTemperatureCatalog",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temperature-catalog/",
      "source_line_start": 551,
      "source_line_end": 555,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "readout_temp_catalog",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temp-catalog/",
      "source_line_start": 558,
      "source_line_end": 564,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_catalog_length",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-catalog-length/",
      "source_line_start": 567,
      "source_line_end": 568,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_temps_all_positive",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temps-all-positive/",
      "source_line_start": 571,
      "source_line_end": 573,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KMSReadout",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kmsreadout/",
      "source_line_start": 587,
      "source_line_end": 598,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kms_readout",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-readout/",
      "source_line_start": 601,
      "source_line_end": 601,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_implies_planckian",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-implies-planckian/",
      "source_line_start": 605,
      "source_line_end": 609,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_no_bogoliubov",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-no-bogoliubov/",
      "source_line_start": 612,
      "source_line_end": 613,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_consistent_with_readout",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-consistent-with-readout/",
      "source_line_start": 616,
      "source_line_end": 617,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l620/",
      "source_line_start": 620,
      "source_line_end": 620,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l623/",
      "source_line_start": 623,
      "source_line_end": 623,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l624/",
      "source_line_start": 624,
      "source_line_end": 624,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EchoSearchEvent",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-event/",
      "source_line_start": 631,
      "source_line_end": 638,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_search_catalog",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-catalog/",
      "source_line_start": 641,
      "source_line_end": 652,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_damping_10mode_x10000",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-10mode-x10000/",
      "source_line_start": 655,
      "source_line_end": 655,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_detection_snr_threshold",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-detection-snr-threshold/",
      "source_line_start": 658,
      "source_line_end": 658,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "stacked_echo_snr_x10",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/stacked-echo-snr-x10/",
      "source_line_start": 661,
      "source_line_end": 661,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "events_needed_3sigma",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/events-needed-3sigma/",
      "source_line_start": 664,
      "source_line_end": 664,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "et_sensitivity_factor",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-sensitivity-factor/",
      "source_line_start": 667,
      "source_line_end": 667,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "et_single_echo_snr_x10",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-single-echo-snr-x10/",
      "source_line_start": 670,
      "source_line_end": 670,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_catalog_length",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-catalog-length/",
      "source_line_start": 673,
      "source_line_end": 674,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "et_single_event_detectable",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-single-event-detectable/",
      "source_line_start": 677,
      "source_line_end": 679,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "o1o3_stack_below_threshold",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/o1o3-stack-below-threshold/",
      "source_line_start": 682,
      "source_line_end": 684,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_search_remark",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-remark/",
      "source_line_start": 687,
      "source_line_end": 690,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_lyapunov_correction_x10000",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-correction-x10000/",
      "source_line_start": 699,
      "source_line_end": 699,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "s2_lyapunov_x10000",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/s2-lyapunov-x10000/",
      "source_line_start": 702,
      "source_line_end": 702,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_lyapunov_exceeds_s2",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-exceeds-s2/",
      "source_line_start": 705,
      "source_line_end": 706,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_damping_t2_bound_x10000",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-t2-bound-x10000/",
      "source_line_start": 710,
      "source_line_end": 710,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_bound_tighter",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-bound-tighter/",
      "source_line_start": 713,
      "source_line_end": 714,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_reduction",
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-reduction/",
      "source_line_start": 717,
      "source_line_end": 718,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l721/",
      "source_line_start": 721,
      "source_line_end": 721,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l722/",
      "source_line_start": 722,
      "source_line_end": 722,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l725/",
      "source_line_start": 725,
      "source_line_end": 725,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l726/",
      "source_line_start": 726,
      "source_line_end": 726,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l727/",
      "source_line_start": 727,
      "source_line_end": 727,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l728/",
      "source_line_start": 728,
      "source_line_end": 730,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean",
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
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Gravity/BHTopoModes.lean`
- SHA-256: `8f715aa61644479d99e0d7aa2d036f455f14f05dc531d2d321dfd6ee94bce696`

## Registry Links

- `V.D234` — T² QNM Mode Structure
- `V.D242` — T² QNM Eigenvalue Structure: ω_{n,m} = √(n²+m²ι_τ⁻²)/(2πr_s)
- `V.D243` — T² GW Echo Time Formulas with Frequency Bands
- `V.P124` — T² Shadow Radius vs EHT
- `V.P125` — T² Entropy = π·ι_τ × S² Entropy
- `V.P131` — Three Falsifiable BH T² Predictions with Fiber Structure Derivation
- `V.R373` — LIGO Echo Window: Δt = 4GM(1-ι_τ²)/(c³·ι_τ)
- `V.R374` — No-Hawking from τ-vacuum: SA-i Forbids Bogoliubov Modes
- `V.R380` — V.OP5 Status: SOLVED via Sprint 7E Observational Suite
- `V.T168` — QNM Fundamental Frequency Ratio = ι_τ⁻¹
- `V.T169` — GW Echo Times t± = 4GM·ι_τ^{±1}/c³
- `V.T185` — QNM Frequency Ratio = ι_τ⁻¹ ≈ 2.930 as Clean S²/T² Discriminator

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Gravity.Schwarzschild`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookV`
- `TauLib.BookVI.CosmicLife.BHDist`
- `TauLib.BookVI.CosmicLife.BHSelfDesc`

## Declaration Counts

- `def`: 43
- `eval`: 33
- `structure`: 11
- `theorem`: 33

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [iota_float](/verify/taulib/docs/book-v-gravity-bhtopo-modes/iota-float/) | L46-L46 | defined | — |
| `structure` | [TorusMode](/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-mode/) | L57-L62 | defined | `V.D234` |
| `def` | [primitiveTorusModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/primitive-torus-modes/) | L65-L68 | defined | — |
| `def` | [torusEigenvalue](/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-eigenvalue/) | L71-L75 | defined | — |
| `def` | [torusQnmFreq](/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-qnm-freq/) | L78-L79 | defined | — |
| `theorem` | [qnm_ratio_is_iota_inv](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-is-iota-inv/) | L94-L95 | formalized | `V.T168` |
| `def` | [qnm_frequency_ratio](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio/) | L98-L98 | defined | — |
| `def` | [schwarzschild_overtone_ratio](/verify/taulib/docs/book-v-gravity-bhtopo-modes/schwarzschild-overtone-ratio/) | L101-L101 | defined | — |
| `def` | [G_Newton](/verify/taulib/docs/book-v-gravity-bhtopo-modes/g-newton/) | L108-L108 | defined | — |
| `def` | [c_light](/verify/taulib/docs/book-v-gravity-bhtopo-modes/c-light/) | L111-L111 | defined | — |
| `def` | [M_sun](/verify/taulib/docs/book-v-gravity-bhtopo-modes/m-sun/) | L114-L114 | defined | — |
| `def` | [echo_time_outer](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-outer/) | L122-L123 | defined | `V.T169` |
| `def` | [echo_time_inner](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/) | L127-L128 | defined | `V.T169` |
| `def` | [echo_separation](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation/) | L132-L133 | defined | `V.R373` |
| `def` | [echo_separation_ms](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-ms/) | L136-L137 | defined | — |
| `def` | [m87_shadow_tau_outer_uas](/verify/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-tau-outer-uas/) | L147-L151 | defined | `V.P124` |
| `def` | [m87_shadow_gr_uas](/verify/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-gr-uas/) | L155-L159 | defined | — |
| `def` | [torus_entropy_ratio](/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio/) | L169-L170 | defined | `V.P125` |
| `def` | [no_hawking_argument](/verify/taulib/docs/book-v-gravity-bhtopo-modes/no-hawking-argument/) | L179-L183 | defined | `V.R374` |
| `theorem` | [three_primitive_modes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/three-primitive-modes/) | L190-L191 | formalized | — |
| `theorem` | [outer_mode_has_zero_inner](/verify/taulib/docs/book-v-gravity-bhtopo-modes/outer-mode-has-zero-inner/) | L194-L195 | formalized | — |
| `theorem` | [inner_mode_has_zero_outer](/verify/taulib/docs/book-v-gravity-bhtopo-modes/inner-mode-has-zero-outer/) | L198-L199 | formalized | — |
| `theorem` | [qnm_ratio_gt_one](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-gt-one/) | L203-L206 | formalized | — |
| `theorem` | [torus_entropy_ratio_gt_one](/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio-gt-one/) | L209-L212 | formalized | — |
| `theorem` | [outer_echo_longer_than_inner](/verify/taulib/docs/book-v-gravity-bhtopo-modes/outer-echo-longer-than-inner/) | L218-L220 | formalized | — |
| `theorem` | [echo_separation_pos](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-pos/) | L225-L227 | formalized | — |
| `eval` | [#eval L234](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l234/) | L234-L234 | computed | — |
| `eval` | [#eval L237](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l237/) | L237-L237 | computed | — |
| `eval` | [#eval L238](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l238/) | L238-L238 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L242](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l242/) | L242-L242 | computed | — |
| `eval` | [#eval L243](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l243/) | L243-L243 | computed | — |
| `eval` | [#eval L246](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l246/) | L246-L246 | computed | — |
| `eval` | [#eval L247](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l247/) | L247-L247 | computed | — |
| `eval` | [#eval L250](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l250/) | L250-L250 | computed | — |
| `eval` | [#eval L253](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l253/) | L253-L253 | computed | — |
| `eval` | [#eval L254](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l254/) | L254-L254 | computed | — |
| `eval` | [#eval L255](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l255/) | L255-L255 | computed | — |
| `eval` | [#eval L256](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l256/) | L256-L256 | computed | — |
| `eval` | [#eval L259](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l259/) | L259-L259 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l260/) | L260-L260 | computed | — |
| `def` | [t2_qnm_eigenvalue_structure](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalue-structure/) | L269-L271 | defined | `V.D242` |
| `structure` | [T2QNMEigenvalues](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnmeigenvalues/) | L276-L288 | defined | `V.D242` |
| `theorem` | [t2_qnm_eigenvalues_conjunction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalues-conjunction/) | L291-L295 | formalized | — |
| `theorem` | [t2_qnm_modes_eq_list](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-modes-eq-list/) | L298-L299 | formalized | — |
| `eval` | [#eval L301](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l301/) | L301-L301 | computed | — |
| `def` | [t2_echo_time_formulas](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/) | L305-L307 | defined | `V.D243` |
| `structure` | [T2EchoFormulas](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas/) | L312-L321 | defined | `V.D243` |
| `def` | [t2_echo_formulas_data](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-data/) | L324-L327 | defined | — |
| `theorem` | [t2_echo_formulas_conjunction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-conjunction/) | L330-L334 | formalized | — |
| `theorem` | [echo_ratio_approx](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-ratio-approx/) | L337-L338 | formalized | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l340/) | L340-L340 | computed | — |
| `def` | [qnm_frequency_ratio_discriminator](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio-discriminator/) | L345-L347 | defined | `V.T185` |
| `structure` | [QNMDiscriminator](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnmdiscriminator/) | L352-L367 | defined | `V.T185` |
| `def` | [qnm_discriminator_data](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-data/) | L370-L373 | defined | — |
| `theorem` | [qnm_discriminator_conjunction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-conjunction/) | L376-L381 | formalized | — |
| `theorem` | [qnm_ranges_separated](/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ranges-separated/) | L384-L386 | formalized | — |
| `eval` | [#eval L388](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l388/) | L388-L388 | computed | — |
| `eval` | [#eval L391](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l391/) | L391-L391 | computed | — |
| `eval` | [#eval L392](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l392/) | L392-L392 | computed | — |
| `def` | [bh_t2_falsification](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification/) | L401-L406 | defined | `V.P131` |
| `structure` | [BHT2Falsification](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bht2-falsification/) | L409-L418 | defined | `V.P131` |
| `def` | [bh_t2_falsification_data](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-data/) | L421-L424 | defined | — |
| `theorem` | [bh_t2_falsification_conjunction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-conjunction/) | L427-L431 | formalized | — |
| `theorem` | [bh_predictions_count](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-predictions-count/) | L434-L435 | formalized | — |
| `eval` | [#eval L437](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l437/) | L437-L437 | computed | — |
| `eval` | [#eval L438](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l438/) | L438-L438 | computed | — |
| `def` | [vop5_sprint7e_status](/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-sprint7e-status/) | L447-L450 | defined | `V.R380` |
| `structure` | [VOP5Status](/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status/) | L453-L462 | defined | `V.R380` |
| `def` | [vop5_data](/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-data/) | L465-L467 | defined | — |
| `theorem` | [vop5_status_conjunction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status-conjunction/) | L470-L475 | formalized | — |
| `theorem` | [vop5_channels_eq_predictions](/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-channels-eq-predictions/) | L478-L480 | formalized | — |
| `eval` | [#eval L482](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l482/) | L482-L482 | computed | — |
| `eval` | [#eval L483](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l483/) | L483-L483 | computed | — |
| `structure` | [BHEntropyCatalog](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bhentropy-catalog/) | L491-L496 | defined | — |
| `def` | [t2_entropy_excess_x10000](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-entropy-excess-x10000/) | L499-L499 | defined | — |
| `def` | [bh_entropy_catalog](/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-entropy-catalog/) | L502-L508 | defined | — |
| `theorem` | [entropy_catalog_uniform_excess](/verify/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-uniform-excess/) | L511-L513 | formalized | — |
| `def` | [entropy_catalog_remark](/verify/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-remark/) | L516-L518 | defined | — |
| `structure` | [ReadoutGibbsState](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-gibbs-state/) | L528-L533 | defined | — |
| `def` | [canonical_readout](/verify/taulib/docs/book-v-gravity-bhtopo-modes/canonical-readout/) | L536-L537 | defined | — |
| `theorem` | [readout_no_mass_loss](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-no-mass-loss/) | L540-L540 | formalized | — |
| `theorem` | [readout_is_planckian](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-is-planckian/) | L543-L543 | formalized | — |
| `theorem` | [readout_planckian_gt_mass_loss](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-planckian-gt-mass-loss/) | L546-L548 | formalized | — |
| `structure` | [ReadoutTemperatureCatalog](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temperature-catalog/) | L551-L555 | defined | — |
| `def` | [readout_temp_catalog](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temp-catalog/) | L558-L564 | defined | — |
| `theorem` | [readout_catalog_length](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-catalog-length/) | L567-L568 | formalized | — |
| `theorem` | [readout_temps_all_positive](/verify/taulib/docs/book-v-gravity-bhtopo-modes/readout-temps-all-positive/) | L571-L573 | formalized | — |
| `structure` | [KMSReadout](/verify/taulib/docs/book-v-gravity-bhtopo-modes/kmsreadout/) | L587-L598 | defined | — |
| `def` | [kms_readout](/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-readout/) | L601-L601 | defined | — |
| `theorem` | [kms_implies_planckian](/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-implies-planckian/) | L605-L609 | formalized | — |
| `theorem` | [kms_no_bogoliubov](/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-no-bogoliubov/) | L612-L613 | formalized | — |
| `theorem` | [kms_consistent_with_readout](/verify/taulib/docs/book-v-gravity-bhtopo-modes/kms-consistent-with-readout/) | L616-L617 | formalized | — |
| `eval` | [#eval L620](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l620/) | L620-L620 | computed | — |
| `eval` | [#eval L623](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l623/) | L623-L623 | computed | — |
| `eval` | [#eval L624](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l624/) | L624-L624 | computed | — |
| `structure` | [EchoSearchEvent](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-event/) | L631-L638 | defined | — |
| `def` | [echo_search_catalog](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-catalog/) | L641-L652 | defined | — |
| `def` | [echo_damping_10mode_x10000](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-10mode-x10000/) | L655-L655 | defined | — |
| `def` | [echo_detection_snr_threshold](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-detection-snr-threshold/) | L658-L658 | defined | — |
| `def` | [stacked_echo_snr_x10](/verify/taulib/docs/book-v-gravity-bhtopo-modes/stacked-echo-snr-x10/) | L661-L661 | defined | — |
| `def` | [events_needed_3sigma](/verify/taulib/docs/book-v-gravity-bhtopo-modes/events-needed-3sigma/) | L664-L664 | defined | — |
| `def` | [et_sensitivity_factor](/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-sensitivity-factor/) | L667-L667 | defined | — |
| `def` | [et_single_echo_snr_x10](/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-single-echo-snr-x10/) | L670-L670 | defined | — |
| `theorem` | [echo_catalog_length](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-catalog-length/) | L673-L674 | formalized | — |
| `theorem` | [et_single_event_detectable](/verify/taulib/docs/book-v-gravity-bhtopo-modes/et-single-event-detectable/) | L677-L679 | formalized | — |
| `theorem` | [o1o3_stack_below_threshold](/verify/taulib/docs/book-v-gravity-bhtopo-modes/o1o3-stack-below-threshold/) | L682-L684 | formalized | — |
| `def` | [echo_search_remark](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-remark/) | L687-L690 | defined | — |
| `def` | [t2_lyapunov_correction_x10000](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-correction-x10000/) | L699-L699 | defined | — |
| `def` | [s2_lyapunov_x10000](/verify/taulib/docs/book-v-gravity-bhtopo-modes/s2-lyapunov-x10000/) | L702-L702 | defined | — |
| `theorem` | [t2_lyapunov_exceeds_s2](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-exceeds-s2/) | L705-L706 | formalized | — |
| `def` | [echo_damping_t2_bound_x10000](/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-t2-bound-x10000/) | L710-L710 | defined | — |
| `theorem` | [t2_echo_bound_tighter](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-bound-tighter/) | L713-L714 | formalized | — |
| `theorem` | [t2_echo_reduction](/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-reduction/) | L717-L718 | formalized | — |
| `eval` | [#eval L721](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l721/) | L721-L721 | computed | — |
| `eval` | [#eval L722](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l722/) | L722-L722 | computed | — |
| `eval` | [#eval L725](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l725/) | L725-L725 | computed | — |
| `eval` | [#eval L726](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l726/) | L726-L726 | computed | — |
| `eval` | [#eval L727](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l727/) | L727-L727 | computed | — |
| `eval` | [#eval L728](/verify/taulib/docs/book-v-gravity-bhtopo-modes/eval-l728/) | L728-L730 | computed | — |
