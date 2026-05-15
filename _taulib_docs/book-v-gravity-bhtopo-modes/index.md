---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.BHTopoModes",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.BHTopoModes`.",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_slug": "book-v-gravity-bhtopo-modes",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/BHTopoModes.lean",
  "sha256": "7d4b5858cff9c04f68f3826ed8276b9fce65e189468f743bab613817e714d468",
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
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/iota-float/",
      "source_line_start": 46,
      "source_line_end": 46,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TorusMode",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-mode/",
      "source_line_start": 57,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D234"
      ]
    },
    {
      "kind": "def",
      "name": "primitiveTorusModes",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/primitive-torus-modes/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusEigenvalue",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-eigenvalue/",
      "source_line_start": 71,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusQnmFreq",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-qnm-freq/",
      "source_line_start": 78,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ratio_is_iota_inv",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-is-iota-inv/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T168"
      ]
    },
    {
      "kind": "def",
      "name": "qnm_frequency_ratio",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "schwarzschild_overtone_ratio",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/schwarzschild-overtone-ratio/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "G_Newton",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/g-newton/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c_light",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/c-light/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "M_sun",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m-sun/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_time_outer",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-outer/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.T169"
      ]
    },
    {
      "kind": "def",
      "name": "echo_time_inner",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.T169"
      ]
    },
    {
      "kind": "def",
      "name": "echo_separation",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.R373"
      ]
    },
    {
      "kind": "def",
      "name": "echo_separation_ms",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-ms/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_shadow_tau_outer_uas",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-tau-outer-uas/",
      "source_line_start": 151,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.P124"
      ]
    },
    {
      "kind": "def",
      "name": "m87_shadow_gr_uas",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-gr-uas/",
      "source_line_start": 159,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torus_entropy_ratio",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio/",
      "source_line_start": 173,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.P125"
      ]
    },
    {
      "kind": "def",
      "name": "no_hawking_argument",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/no-hawking-argument/",
      "source_line_start": 183,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.R374"
      ]
    },
    {
      "kind": "theorem",
      "name": "three_primitive_modes",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/three-primitive-modes/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "outer_mode_has_zero_inner",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/outer-mode-has-zero-inner/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "inner_mode_has_zero_outer",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/inner-mode-has-zero-outer/",
      "source_line_start": 202,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ratio_gt_one",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-gt-one/",
      "source_line_start": 207,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "torus_entropy_ratio_gt_one",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio-gt-one/",
      "source_line_start": 213,
      "source_line_end": 216,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "outer_echo_longer_than_inner",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/outer-echo-longer-than-inner/",
      "source_line_start": 222,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_separation_pos",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-pos/",
      "source_line_start": 229,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 243,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_qnm_eigenvalue_structure",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalue-structure/",
      "source_line_start": 273,
      "source_line_end": 275,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.D242"
      ]
    },
    {
      "kind": "structure",
      "name": "T2QNMEigenvalues",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnmeigenvalues/",
      "source_line_start": 280,
      "source_line_end": 292,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D242"
      ]
    },
    {
      "kind": "theorem",
      "name": "t2_qnm_eigenvalues_conjunction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalues-conjunction/",
      "source_line_start": 295,
      "source_line_end": 299,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_qnm_modes_eq_list",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-modes-eq-list/",
      "source_line_start": 302,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_echo_time_formulas",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/",
      "source_line_start": 309,
      "source_line_end": 312,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.D243"
      ]
    },
    {
      "kind": "structure",
      "name": "T2EchoFormulas",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas/",
      "source_line_start": 317,
      "source_line_end": 326,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D243"
      ]
    },
    {
      "kind": "def",
      "name": "t2_echo_formulas_data",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-data/",
      "source_line_start": 329,
      "source_line_end": 332,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_formulas_conjunction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-conjunction/",
      "source_line_start": 335,
      "source_line_end": 339,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_ratio_approx",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-ratio-approx/",
      "source_line_start": 342,
      "source_line_end": 343,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "qnm_frequency_ratio_discriminator",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio-discriminator/",
      "source_line_start": 350,
      "source_line_end": 352,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.T185"
      ]
    },
    {
      "kind": "structure",
      "name": "QNMDiscriminator",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnmdiscriminator/",
      "source_line_start": 357,
      "source_line_end": 372,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T185"
      ]
    },
    {
      "kind": "def",
      "name": "qnm_discriminator_data",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-data/",
      "source_line_start": 375,
      "source_line_end": 378,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_discriminator_conjunction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-conjunction/",
      "source_line_start": 381,
      "source_line_end": 386,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qnm_ranges_separated",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ranges-separated/",
      "source_line_start": 389,
      "source_line_end": 391,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l393/",
      "source_line_start": 393,
      "source_line_end": 393,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l396/",
      "source_line_start": 396,
      "source_line_end": 396,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l397/",
      "source_line_start": 397,
      "source_line_end": 397,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_t2_falsification",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification/",
      "source_line_start": 406,
      "source_line_end": 412,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.P131"
      ]
    },
    {
      "kind": "structure",
      "name": "BHT2Falsification",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bht2-falsification/",
      "source_line_start": 415,
      "source_line_end": 424,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P131"
      ]
    },
    {
      "kind": "def",
      "name": "bh_t2_falsification_data",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-data/",
      "source_line_start": 427,
      "source_line_end": 430,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_t2_falsification_conjunction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-conjunction/",
      "source_line_start": 433,
      "source_line_end": 437,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_predictions_count",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-predictions-count/",
      "source_line_start": 440,
      "source_line_end": 441,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l443/",
      "source_line_start": 443,
      "source_line_end": 443,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l444/",
      "source_line_start": 444,
      "source_line_end": 444,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "vop5_sprint7e_status",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-sprint7e-status/",
      "source_line_start": 453,
      "source_line_end": 456,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.R380"
      ]
    },
    {
      "kind": "structure",
      "name": "VOP5Status",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status/",
      "source_line_start": 459,
      "source_line_end": 468,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R380"
      ]
    },
    {
      "kind": "def",
      "name": "vop5_data",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-data/",
      "source_line_start": 471,
      "source_line_end": 473,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vop5_status_conjunction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status-conjunction/",
      "source_line_start": 476,
      "source_line_end": 481,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vop5_channels_eq_predictions",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-channels-eq-predictions/",
      "source_line_start": 484,
      "source_line_end": 486,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l488/",
      "source_line_start": 488,
      "source_line_end": 488,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l489/",
      "source_line_start": 489,
      "source_line_end": 489,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHEntropyCatalog",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bhentropy-catalog/",
      "source_line_start": 497,
      "source_line_end": 502,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_entropy_excess_x10000",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-entropy-excess-x10000/",
      "source_line_start": 505,
      "source_line_end": 505,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_entropy_catalog",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-entropy-catalog/",
      "source_line_start": 508,
      "source_line_end": 514,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "entropy_catalog_uniform_excess",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-uniform-excess/",
      "source_line_start": 517,
      "source_line_end": 519,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_catalog_remark",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-remark/",
      "source_line_start": 522,
      "source_line_end": 524,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutGibbsState",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-gibbs-state/",
      "source_line_start": 534,
      "source_line_end": 539,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_readout",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/canonical-readout/",
      "source_line_start": 542,
      "source_line_end": 543,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_no_mass_loss",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-no-mass-loss/",
      "source_line_start": 546,
      "source_line_end": 546,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_is_planckian",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-is-planckian/",
      "source_line_start": 549,
      "source_line_end": 549,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_planckian_gt_mass_loss",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-planckian-gt-mass-loss/",
      "source_line_start": 552,
      "source_line_end": 554,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutTemperatureCatalog",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temperature-catalog/",
      "source_line_start": 557,
      "source_line_end": 561,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "readout_temp_catalog",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temp-catalog/",
      "source_line_start": 564,
      "source_line_end": 570,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_catalog_length",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-catalog-length/",
      "source_line_start": 573,
      "source_line_end": 574,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_temps_all_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temps-all-positive/",
      "source_line_start": 577,
      "source_line_end": 579,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KMSReadout",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kmsreadout/",
      "source_line_start": 593,
      "source_line_end": 604,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kms_readout",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-readout/",
      "source_line_start": 607,
      "source_line_end": 607,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_implies_planckian",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-implies-planckian/",
      "source_line_start": 611,
      "source_line_end": 615,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_no_bogoliubov",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-no-bogoliubov/",
      "source_line_start": 618,
      "source_line_end": 619,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kms_consistent_with_readout",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-consistent-with-readout/",
      "source_line_start": 622,
      "source_line_end": 623,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l626/",
      "source_line_start": 626,
      "source_line_end": 626,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l629/",
      "source_line_start": 629,
      "source_line_end": 629,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l630/",
      "source_line_start": 630,
      "source_line_end": 630,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EchoSearchEvent",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-event/",
      "source_line_start": 639,
      "source_line_end": 646,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_search_catalog",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-catalog/",
      "source_line_start": 649,
      "source_line_end": 660,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_damping_10mode_x10000",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-10mode-x10000/",
      "source_line_start": 663,
      "source_line_end": 663,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_detection_snr_threshold",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-detection-snr-threshold/",
      "source_line_start": 666,
      "source_line_end": 666,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "stacked_echo_snr_x10",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/stacked-echo-snr-x10/",
      "source_line_start": 669,
      "source_line_end": 669,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "events_needed_3sigma",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/events-needed-3sigma/",
      "source_line_start": 672,
      "source_line_end": 672,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "et_sensitivity_factor",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-sensitivity-factor/",
      "source_line_start": 675,
      "source_line_end": 675,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "et_single_echo_snr_x10",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-single-echo-snr-x10/",
      "source_line_start": 678,
      "source_line_end": 678,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "echo_catalog_length",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-catalog-length/",
      "source_line_start": 681,
      "source_line_end": 682,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "et_single_event_detectable",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-single-event-detectable/",
      "source_line_start": 685,
      "source_line_end": 687,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "o1o3_stack_below_threshold",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/o1o3-stack-below-threshold/",
      "source_line_start": 690,
      "source_line_end": 692,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_search_remark",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-remark/",
      "source_line_start": 695,
      "source_line_end": 699,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_lyapunov_correction_x10000",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-correction-x10000/",
      "source_line_start": 708,
      "source_line_end": 708,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "s2_lyapunov_x10000",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/s2-lyapunov-x10000/",
      "source_line_start": 711,
      "source_line_end": 711,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_lyapunov_exceeds_s2",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-exceeds-s2/",
      "source_line_start": 714,
      "source_line_end": 715,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "echo_damping_t2_bound_x10000",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-t2-bound-x10000/",
      "source_line_start": 719,
      "source_line_end": 719,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_bound_tighter",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-bound-tighter/",
      "source_line_start": 722,
      "source_line_end": 723,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "t2_echo_reduction",
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-reduction/",
      "source_line_start": 726,
      "source_line_end": 727,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l730/",
      "source_line_start": 730,
      "source_line_end": 730,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l731/",
      "source_line_start": 731,
      "source_line_end": 731,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l734/",
      "source_line_start": 734,
      "source_line_end": 734,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l735/",
      "source_line_start": 735,
      "source_line_end": 735,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l736/",
      "source_line_start": 736,
      "source_line_end": 736,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l737/",
      "source_line_start": 737,
      "source_line_end": 739,
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
- SHA-256: `7d4b5858cff9c04f68f3826ed8276b9fce65e189468f743bab613817e714d468`

## Registry Links

- `V.D234` — T² QNM Mode Structure
- `V.D242` — T² QNM Eigenvalue Structure: ω_{n,m} = √(n²+m²ι_τ⁻²)/(2πr_s)
- `V.D243` — T² GW Cycle-Delay Time Formulas with Frequency Bands
- `V.P124` — T² Shadow Radius vs EHT
- `V.P125` — T² Entropy = π·ι_τ × S² Entropy
- `V.P131` — Three Falsifiable BH T² Predictions with Fiber Structure Derivation
- `V.R373` — LIGO Echo Window: Δt = 4GM(1-ι_τ²)/(c³·ι_τ)
- `V.R374` — No-Hawking from τ-vacuum: SA-i Forbids Bogoliubov Modes
- `V.R380` — V.OP5 Status: SOLVED via Sprint 7E Observational Suite
- `V.T168` — QNM Fundamental Frequency Ratio = ι_τ⁻¹
- `V.T169` — GW Cycle-Delay Times t± = 4GM·ι_τ^{±1}/c³
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [iota_float](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/iota-float/) | L46-L46 | data/computed value | data/computed value | — |
| `structure` | [TorusMode](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-mode/) | L57-L62 | type/data schema | type/data schema | `V.D234` |
| `def` | [primitiveTorusModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/primitive-torus-modes/) | L65-L68 | data/computed value | data/computed value | — |
| `def` | [torusEigenvalue](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-eigenvalue/) | L71-L75 | data/computed value | data/computed value | — |
| `def` | [torusQnmFreq](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-qnm-freq/) | L78-L79 | data/computed value | data/computed value | — |
| `theorem` | [qnm_ratio_is_iota_inv](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-is-iota-inv/) | L94-L95 | proof obligation | formal proof obligation checked | `V.T168` |
| `def` | [qnm_frequency_ratio](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio/) | L98-L98 | data/computed value | data/computed value | — |
| `def` | [schwarzschild_overtone_ratio](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/schwarzschild-overtone-ratio/) | L101-L101 | data/computed value | data/computed value | — |
| `def` | [G_Newton](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/g-newton/) | L108-L108 | data/computed value | data/computed value | — |
| `def` | [c_light](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/c-light/) | L111-L111 | data/computed value | data/computed value | — |
| `def` | [M_sun](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m-sun/) | L114-L114 | data/computed value | data/computed value | — |
| `def` | [echo_time_outer](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-outer/) | L124-L125 | data/computed value | data/computed value | `V.T169` |
| `def` | [echo_time_inner](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/) | L131-L132 | data/computed value | data/computed value | `V.T169` |
| `def` | [echo_separation](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation/) | L136-L137 | data/computed value | data/computed value | `V.R373` |
| `def` | [echo_separation_ms](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-ms/) | L140-L141 | data/computed value | data/computed value | — |
| `def` | [m87_shadow_tau_outer_uas](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-tau-outer-uas/) | L151-L155 | data/computed value | data/computed value | `V.P124` |
| `def` | [m87_shadow_gr_uas](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-gr-uas/) | L159-L163 | data/computed value | data/computed value | — |
| `def` | [torus_entropy_ratio](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio/) | L173-L174 | data/computed value | data/computed value | `V.P125` |
| `def` | [no_hawking_argument](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/no-hawking-argument/) | L183-L187 | docstring/data record | docstring/data record | `V.R374` |
| `theorem` | [three_primitive_modes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/three-primitive-modes/) | L194-L195 | proof obligation | formal proof obligation checked | — |
| `theorem` | [outer_mode_has_zero_inner](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/outer-mode-has-zero-inner/) | L198-L199 | proof obligation | formal proof obligation checked | — |
| `theorem` | [inner_mode_has_zero_outer](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/inner-mode-has-zero-outer/) | L202-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qnm_ratio_gt_one](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-gt-one/) | L207-L210 | proof obligation | formal proof obligation checked | — |
| `theorem` | [torus_entropy_ratio_gt_one](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio-gt-one/) | L213-L216 | proof obligation | formal proof obligation checked | — |
| `theorem` | [outer_echo_longer_than_inner](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/outer-echo-longer-than-inner/) | L222-L224 | proof obligation | formal proof obligation checked | — |
| `theorem` | [echo_separation_pos](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation-pos/) | L229-L231 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L238](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l238/) | L238-L238 | computed check | computed check | — |
| `eval` | [#eval L241](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l241/) | L241-L241 | computed check | computed check | — |
| `eval` | [#eval L242](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l242/) | L242-L242 | computed check | computed check | — |
| `eval` | [#eval L243](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l243/) | L243-L243 | computed check | computed check | — |
| `eval` | [#eval L246](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l246/) | L246-L246 | computed check | computed check | — |
| `eval` | [#eval L247](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l247/) | L247-L247 | computed check | computed check | — |
| `eval` | [#eval L250](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l250/) | L250-L250 | computed check | computed check | — |
| `eval` | [#eval L251](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l251/) | L251-L251 | computed check | computed check | — |
| `eval` | [#eval L254](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l254/) | L254-L254 | computed check | computed check | — |
| `eval` | [#eval L257](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l257/) | L257-L257 | computed check | computed check | — |
| `eval` | [#eval L258](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l258/) | L258-L258 | computed check | computed check | — |
| `eval` | [#eval L259](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l259/) | L259-L259 | computed check | computed check | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l264/) | L264-L264 | computed check | computed check | — |
| `def` | [t2_qnm_eigenvalue_structure](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalue-structure/) | L273-L275 | docstring/data record | docstring/data record | `V.D242` |
| `structure` | [T2QNMEigenvalues](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnmeigenvalues/) | L280-L292 | type/data schema | type/data schema | `V.D242` |
| `theorem` | [t2_qnm_eigenvalues_conjunction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalues-conjunction/) | L295-L299 | proof obligation | formal proof obligation checked | — |
| `theorem` | [t2_qnm_modes_eq_list](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-modes-eq-list/) | L302-L303 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L305](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l305/) | L305-L305 | computed check | computed check | — |
| `def` | [t2_echo_time_formulas](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/) | L309-L312 | docstring/data record | docstring/data record | `V.D243` |
| `structure` | [T2EchoFormulas](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas/) | L317-L326 | type/data schema | type/data schema | `V.D243` |
| `def` | [t2_echo_formulas_data](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-data/) | L329-L332 | definition | definition | — |
| `theorem` | [t2_echo_formulas_conjunction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas-conjunction/) | L335-L339 | proof obligation | formal proof obligation checked | — |
| `theorem` | [echo_ratio_approx](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-ratio-approx/) | L342-L343 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L345](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l345/) | L345-L345 | computed check | computed check | — |
| `def` | [qnm_frequency_ratio_discriminator](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio-discriminator/) | L350-L352 | docstring/data record | docstring/data record | `V.T185` |
| `structure` | [QNMDiscriminator](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnmdiscriminator/) | L357-L372 | type/data schema | type/data schema | `V.T185` |
| `def` | [qnm_discriminator_data](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-data/) | L375-L378 | definition | definition | — |
| `theorem` | [qnm_discriminator_conjunction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-discriminator-conjunction/) | L381-L386 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qnm_ranges_separated](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ranges-separated/) | L389-L391 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L393](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l393/) | L393-L393 | computed check | computed check | — |
| `eval` | [#eval L396](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l396/) | L396-L396 | computed check | computed check | — |
| `eval` | [#eval L397](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l397/) | L397-L397 | computed check | computed check | — |
| `def` | [bh_t2_falsification](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification/) | L406-L412 | docstring/data record | docstring/data record | `V.P131` |
| `structure` | [BHT2Falsification](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bht2-falsification/) | L415-L424 | type/data schema | type/data schema | `V.P131` |
| `def` | [bh_t2_falsification_data](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-data/) | L427-L430 | definition | definition | — |
| `theorem` | [bh_t2_falsification_conjunction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification-conjunction/) | L433-L437 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bh_predictions_count](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-predictions-count/) | L440-L441 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L443](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l443/) | L443-L443 | computed check | computed check | — |
| `eval` | [#eval L444](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l444/) | L444-L444 | computed check | computed check | — |
| `def` | [vop5_sprint7e_status](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-sprint7e-status/) | L453-L456 | docstring/data record | docstring/data record | `V.R380` |
| `structure` | [VOP5Status](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status/) | L459-L468 | type/data schema | type/data schema | `V.R380` |
| `def` | [vop5_data](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-data/) | L471-L473 | definition | definition | — |
| `theorem` | [vop5_status_conjunction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status-conjunction/) | L476-L481 | proof obligation | formal proof obligation checked | — |
| `theorem` | [vop5_channels_eq_predictions](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/vop5-channels-eq-predictions/) | L484-L486 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L488](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l488/) | L488-L488 | computed check | computed check | — |
| `eval` | [#eval L489](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l489/) | L489-L489 | computed check | computed check | — |
| `structure` | [BHEntropyCatalog](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bhentropy-catalog/) | L497-L502 | type/data schema | type/data schema | — |
| `def` | [t2_entropy_excess_x10000](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-entropy-excess-x10000/) | L505-L505 | data/computed value | data/computed value | — |
| `def` | [bh_entropy_catalog](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bh-entropy-catalog/) | L508-L514 | data/computed value | data/computed value | — |
| `theorem` | [entropy_catalog_uniform_excess](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-uniform-excess/) | L517-L519 | proof obligation | formal proof obligation checked | — |
| `def` | [entropy_catalog_remark](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/entropy-catalog-remark/) | L522-L524 | docstring/data record | docstring/data record | — |
| `structure` | [ReadoutGibbsState](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-gibbs-state/) | L534-L539 | type/data schema | type/data schema | — |
| `def` | [canonical_readout](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/canonical-readout/) | L542-L543 | definition | definition | — |
| `theorem` | [readout_no_mass_loss](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-no-mass-loss/) | L546-L546 | proof obligation | formal proof obligation checked | — |
| `theorem` | [readout_is_planckian](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-is-planckian/) | L549-L549 | proof obligation | formal proof obligation checked | — |
| `theorem` | [readout_planckian_gt_mass_loss](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-planckian-gt-mass-loss/) | L552-L554 | proof obligation | formal proof obligation checked | — |
| `structure` | [ReadoutTemperatureCatalog](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temperature-catalog/) | L557-L561 | type/data schema | type/data schema | — |
| `def` | [readout_temp_catalog](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temp-catalog/) | L564-L570 | data/computed value | data/computed value | — |
| `theorem` | [readout_catalog_length](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-catalog-length/) | L573-L574 | proof obligation | formal proof obligation checked | — |
| `theorem` | [readout_temps_all_positive](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/readout-temps-all-positive/) | L577-L579 | proof obligation | formal proof obligation checked | — |
| `structure` | [KMSReadout](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kmsreadout/) | L593-L604 | type/data schema | type/data schema | — |
| `def` | [kms_readout](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-readout/) | L607-L607 | definition | definition | — |
| `theorem` | [kms_implies_planckian](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-implies-planckian/) | L611-L615 | proof obligation | formal proof obligation checked | — |
| `theorem` | [kms_no_bogoliubov](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-no-bogoliubov/) | L618-L619 | proof obligation | formal proof obligation checked | — |
| `theorem` | [kms_consistent_with_readout](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-consistent-with-readout/) | L622-L623 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L626](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l626/) | L626-L626 | computed check | computed check | — |
| `eval` | [#eval L629](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l629/) | L629-L629 | computed check | computed check | — |
| `eval` | [#eval L630](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l630/) | L630-L630 | computed check | computed check | — |
| `structure` | [EchoSearchEvent](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-event/) | L639-L646 | type/data schema | type/data schema | — |
| `def` | [echo_search_catalog](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-catalog/) | L649-L660 | data/computed value | data/computed value | — |
| `def` | [echo_damping_10mode_x10000](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-10mode-x10000/) | L663-L663 | data/computed value | data/computed value | — |
| `def` | [echo_detection_snr_threshold](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-detection-snr-threshold/) | L666-L666 | data/computed value | data/computed value | — |
| `def` | [stacked_echo_snr_x10](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/stacked-echo-snr-x10/) | L669-L669 | data/computed value | data/computed value | — |
| `def` | [events_needed_3sigma](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/events-needed-3sigma/) | L672-L672 | data/computed value | data/computed value | — |
| `def` | [et_sensitivity_factor](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-sensitivity-factor/) | L675-L675 | data/computed value | data/computed value | — |
| `def` | [et_single_echo_snr_x10](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-single-echo-snr-x10/) | L678-L678 | data/computed value | data/computed value | — |
| `theorem` | [echo_catalog_length](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-catalog-length/) | L681-L682 | proof obligation | formal proof obligation checked | — |
| `theorem` | [et_single_event_detectable](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/et-single-event-detectable/) | L685-L687 | proof obligation | formal proof obligation checked | — |
| `theorem` | [o1o3_stack_below_threshold](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/o1o3-stack-below-threshold/) | L690-L692 | proof obligation | formal proof obligation checked | — |
| `def` | [echo_search_remark](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-remark/) | L695-L699 | docstring/data record | docstring/data record | — |
| `def` | [t2_lyapunov_correction_x10000](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-correction-x10000/) | L708-L708 | data/computed value | data/computed value | — |
| `def` | [s2_lyapunov_x10000](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/s2-lyapunov-x10000/) | L711-L711 | data/computed value | data/computed value | — |
| `theorem` | [t2_lyapunov_exceeds_s2](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-lyapunov-exceeds-s2/) | L714-L715 | proof obligation | formal proof obligation checked | — |
| `def` | [echo_damping_t2_bound_x10000](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-damping-t2-bound-x10000/) | L719-L719 | data/computed value | data/computed value | — |
| `theorem` | [t2_echo_bound_tighter](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-bound-tighter/) | L722-L723 | proof obligation | formal proof obligation checked | — |
| `theorem` | [t2_echo_reduction](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-reduction/) | L726-L727 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L730](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l730/) | L730-L730 | computed check | computed check | — |
| `eval` | [#eval L731](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l731/) | L731-L731 | computed check | computed check | — |
| `eval` | [#eval L734](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l734/) | L734-L734 | computed check | computed check | — |
| `eval` | [#eval L735](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l735/) | L735-L735 | computed check | computed check | — |
| `eval` | [#eval L736](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l736/) | L736-L736 | computed check | computed check | — |
| `eval` | [#eval L737](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/eval-l737/) | L737-L739 | computed check | computed check | — |
