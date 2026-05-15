---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_slug": "book-v-cosmology-bbnbaryogenesis",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/BBNBaryogenesis.lean",
  "sha256": "2c67b9add7260f5a6a60bbaa2fe5b4df5b9b8543ed17a80551c7dde638bbb215",
  "imports": [
    "TauLib.BookV.Cosmology.ThresholdLadder",
    "TauLib.BookV.Cosmology.HeliumFraction"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.BBNNuclearNetwork",
    "TauLib.BookV.Cosmology.NeutrinoBackground"
  ],
  "registry_ids": [
    "V.D197",
    "V.D198",
    "V.D238",
    "V.P113",
    "V.P130",
    "V.R323",
    "V.R324",
    "V.R325",
    "V.R326",
    "V.R379",
    "V.T151",
    "V.T179",
    "V.T180"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 7,
    "def": 11,
    "theorem": 22,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "AdmissibilityCategory",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/admissibility-category/",
      "source_line_start": 66,
      "source_line_end": 71,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdDependentAdmissibility",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-dependent-admissibility/",
      "source_line_start": 81,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D197"
      ]
    },
    {
      "kind": "def",
      "name": "threshold_admissibility",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-admissibility/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pre_confinement_admits_B_violation",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/pre-confinement-admits-b-violation/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "post_confinement_conserves_B",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/post-confinement-conserves-b/",
      "source_line_start": 102,
      "source_line_end": 104,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BaryogenesisWindow",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window/",
      "source_line_start": 116,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D198"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_window",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window-l128/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_finite",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-finite/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleosynthesis_after_window",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/nucleosynthesis-after-window/",
      "source_line_start": 139,
      "source_line_end": 142,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_matches_ladder",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-matches-ladder/",
      "source_line_start": 146,
      "source_line_end": 151,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "n_gauge_generators",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-generators/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "n_total_generators",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-total-generators/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "n_gauge_from_total",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-from-total/",
      "source_line_start": 168,
      "source_line_end": 170,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "n_eff_eq_three",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-eq-three/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T151"
      ]
    },
    {
      "kind": "theorem",
      "name": "n_eff_upper_bound",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-upper-bound/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P113"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_dark_sector",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/no-dark-sector/",
      "source_line_start": 191,
      "source_line_end": 192,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_within_ladder",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-within-ladder/",
      "source_line_start": 200,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "clean_threshold_count",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/clean-threshold-count/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R323",
        "V.R324",
        "V.R325",
        "V.R326"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l238/",
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
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BaryogenesisSAIMechanism",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-saimechanism/",
      "source_line_start": 257,
      "source_line_end": 272,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D238"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_sai_mechanism",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-mechanism/",
      "source_line_start": 275,
      "source_line_end": 280,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "baryogenesis_sai_thm",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-thm/",
      "source_line_start": 283,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fifteen_window_product",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/fifteen-window-product/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T179"
      ]
    },
    {
      "kind": "theorem",
      "name": "five_sixths_structure",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-structure/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T180"
      ]
    },
    {
      "kind": "structure",
      "name": "BaryogenesisFirstPrinciples",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles/",
      "source_line_start": 310,
      "source_line_end": 319,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P130"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_fp",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-fp/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "baryogenesis_first_principles",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles-l325/",
      "source_line_start": 325,
      "source_line_end": 330,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sai_mod_comparison",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-comparison/",
      "source_line_start": 333,
      "source_line_end": 335,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "vop2_status_sprint6c",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/vop2-status-sprint6c/",
      "source_line_start": 338,
      "source_line_end": 341,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "V.R379"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeneratorOrbitSuppression",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression/",
      "source_line_start": 369,
      "source_line_end": 382,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "generator_orbit_suppression",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression-l384/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "generator_orbit_produces_15",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-produces-15/",
      "source_line_start": 388,
      "source_line_end": 393,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fiber_dimension_decomposition",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/fiber-dimension-decomposition/",
      "source_line_start": 396,
      "source_line_end": 397,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sai_mod_hierarchy",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-hierarchy/",
      "source_line_start": 402,
      "source_line_end": 403,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdUniquenessFiveSixths",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-five-sixths/",
      "source_line_start": 420,
      "source_line_end": 433,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "threshold_uniqueness_56",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-56/",
      "source_line_start": 435,
      "source_line_end": 437,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sixths_uniquely_forced",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-uniquely-forced/",
      "source_line_start": 440,
      "source_line_end": 445,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sixths_cross_check_yp",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-cross-check-yp/",
      "source_line_start": 448,
      "source_line_end": 449,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "threshold_uniqueness_matches_ladder",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-matches-ladder/",
      "source_line_start": 452,
      "source_line_end": 454,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CPAsymmetryFromPolarity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cpasymmetry-from-polarity/",
      "source_line_start": 473,
      "source_line_end": 484,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cp_asymmetry_polarity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-polarity/",
      "source_line_start": 486,
      "source_line_end": 486,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cp_asymmetry_structural",
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-structural/",
      "source_line_start": 489,
      "source_line_end": 493,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l496/",
      "source_line_start": 496,
      "source_line_end": 496,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l497/",
      "source_line_start": 497,
      "source_line_end": 497,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l498/",
      "source_line_start": 498,
      "source_line_end": 498,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l499/",
      "source_line_start": 499,
      "source_line_end": 501,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean",
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
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/BBNBaryogenesis.lean`
- SHA-256: `2c67b9add7260f5a6a60bbaa2fe5b4df5b9b8543ed17a80551c7dde638bbb215`

## Registry Links

- `V.D197` — Threshold-Dependent Admissibility
- `V.D198` — Baryogenesis Window
- `V.D238` — SA-i mod-W₃(4) Baryogenesis Mechanism: ι_τ¹⁵ = (ι_τ³)^W₃(4)
- `V.P113` — Dark Sector Closure
- `V.P130` — Baryogenesis First Principles: Generator Orbit + Threshold Uniqueness
- `V.R323` — Commutator Magnitude at omega-Crossing
- `V.R324` — eta_B Structural Candidate
- `V.R325` — Primorial-Confinement Bridge
- `V.R326` — Confinement Multiplicity Estimate
- `V.R379` — V.OP2 Status after Sprint 6C: SA-i mod-5 Mechanism Proposed
- `V.T151` — N_eff from Sector Exhaustion
- `V.T179` — ι_τ¹⁵ from Generator Orbit: 15 = dim(τ³) × |generators|
- `V.T180` — (5/6) Uniquely Forced from Threshold Topology

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.ThresholdLadder`
- `TauLib.BookV.Cosmology.HeliumFraction`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.BBNNuclearNetwork`
- `TauLib.BookV.Cosmology.NeutrinoBackground`

## Declaration Counts

- `def`: 11
- `eval`: 14
- `inductive`: 1
- `structure`: 7
- `theorem`: 22

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [AdmissibilityCategory](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/admissibility-category/) | L66-L71 | type/data schema | type/data schema | — |
| `structure` | [ThresholdDependentAdmissibility](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-dependent-admissibility/) | L81-L90 | type/data schema | type/data schema | `V.D197` |
| `def` | [threshold_admissibility](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-admissibility/) | L93-L94 | definition | definition | — |
| `theorem` | [pre_confinement_admits_B_violation](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/pre-confinement-admits-b-violation/) | L97-L99 | proof obligation | formal proof obligation checked | — |
| `theorem` | [post_confinement_conserves_B](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/post-confinement-conserves-b/) | L102-L104 | proof obligation | formal proof obligation checked | — |
| `structure` | [BaryogenesisWindow](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window/) | L116-L125 | type/data schema | type/data schema | `V.D198` |
| `def` | [baryogenesis_window](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window-l128/) | L128-L130 | definition | definition | — |
| `theorem` | [window_finite](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-finite/) | L133-L135 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nucleosynthesis_after_window](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/nucleosynthesis-after-window/) | L139-L142 | proof obligation | formal proof obligation checked | — |
| `theorem` | [window_matches_ladder](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-matches-ladder/) | L146-L151 | proof obligation | formal proof obligation checked | — |
| `def` | [n_gauge_generators](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-generators/) | L160-L160 | data/computed value | data/computed value | — |
| `def` | [n_total_generators](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-total-generators/) | L163-L163 | data/computed value | data/computed value | — |
| `theorem` | [n_gauge_from_total](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-from-total/) | L168-L170 | proof obligation | formal proof obligation checked | — |
| `theorem` | [n_eff_eq_three](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-eq-three/) | L176-L176 | proof obligation | formal proof obligation checked | `V.T151` |
| `theorem` | [n_eff_upper_bound](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-upper-bound/) | L188-L188 | proof obligation | formal proof obligation checked | `V.P113` |
| `theorem` | [no_dark_sector](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/no-dark-sector/) | L191-L192 | proof obligation | formal proof obligation checked | — |
| `theorem` | [window_within_ladder](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-within-ladder/) | L200-L204 | proof obligation | formal proof obligation checked | — |
| `theorem` | [clean_threshold_count](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/clean-threshold-count/) | L208-L210 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L236](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l236/) | L236-L236 | computed check | computed check | `V.R323`, `V.R324`, `V.R325`, `V.R326` |
| `eval` | [#eval L237](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l237/) | L237-L237 | computed check | computed check | — |
| `eval` | [#eval L238](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l238/) | L238-L238 | computed check | computed check | — |
| `eval` | [#eval L239](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l239/) | L239-L239 | computed check | computed check | — |
| `eval` | [#eval L240](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l240/) | L240-L240 | computed check | computed check | — |
| `structure` | [BaryogenesisSAIMechanism](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-saimechanism/) | L257-L272 | type/data schema | type/data schema | `V.D238` |
| `def` | [baryogenesis_sai_mechanism](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-mechanism/) | L275-L280 | definition | definition | — |
| `theorem` | [baryogenesis_sai_thm](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-thm/) | L283-L288 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fifteen_window_product](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/fifteen-window-product/) | L291-L291 | proof obligation | formal proof obligation checked | `V.T179` |
| `theorem` | [five_sixths_structure](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-structure/) | L294-L294 | proof obligation | formal proof obligation checked | `V.T180` |
| `structure` | [BaryogenesisFirstPrinciples](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles/) | L310-L319 | type/data schema | type/data schema | `V.P130` |
| `def` | [baryogenesis_fp](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-fp/) | L322-L322 | definition | definition | — |
| `theorem` | [baryogenesis_first_principles](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles-l325/) | L325-L330 | proof obligation | formal proof obligation checked | — |
| `def` | [sai_mod_comparison](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-comparison/) | L333-L335 | docstring/data record | docstring/data record | — |
| `def` | [vop2_status_sprint6c](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/vop2-status-sprint6c/) | L338-L341 | docstring/data record | docstring/data record | `V.R379` |
| `eval` | [#eval L344](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l344/) | L344-L344 | computed check | computed check | — |
| `eval` | [#eval L345](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l345/) | L345-L345 | computed check | computed check | — |
| `eval` | [#eval L346](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l346/) | L346-L346 | computed check | computed check | — |
| `eval` | [#eval L347](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l347/) | L347-L347 | computed check | computed check | — |
| `eval` | [#eval L348](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l348/) | L348-L348 | computed check | computed check | — |
| `structure` | [GeneratorOrbitSuppression](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression/) | L369-L382 | type/data schema | type/data schema | — |
| `def` | [generator_orbit_suppression](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression-l384/) | L384-L385 | definition | definition | — |
| `theorem` | [generator_orbit_produces_15](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-produces-15/) | L388-L393 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fiber_dimension_decomposition](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/fiber-dimension-decomposition/) | L396-L397 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sai_mod_hierarchy](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-hierarchy/) | L402-L403 | proof obligation | formal proof obligation checked | — |
| `structure` | [ThresholdUniquenessFiveSixths](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-five-sixths/) | L420-L433 | type/data schema | type/data schema | — |
| `def` | [threshold_uniqueness_56](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-56/) | L435-L437 | definition | definition | — |
| `theorem` | [five_sixths_uniquely_forced](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-uniquely-forced/) | L440-L445 | proof obligation | formal proof obligation checked | — |
| `theorem` | [five_sixths_cross_check_yp](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-cross-check-yp/) | L448-L449 | proof obligation | formal proof obligation checked | — |
| `theorem` | [threshold_uniqueness_matches_ladder](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-matches-ladder/) | L452-L454 | proof obligation | formal proof obligation checked | — |
| `structure` | [CPAsymmetryFromPolarity](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cpasymmetry-from-polarity/) | L473-L484 | type/data schema | type/data schema | — |
| `def` | [cp_asymmetry_polarity](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-polarity/) | L486-L486 | definition | definition | — |
| `theorem` | [cp_asymmetry_structural](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-structural/) | L489-L493 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L496](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l496/) | L496-L496 | computed check | computed check | — |
| `eval` | [#eval L497](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l497/) | L497-L497 | computed check | computed check | — |
| `eval` | [#eval L498](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l498/) | L498-L498 | computed check | computed check | — |
| `eval` | [#eval L499](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l499/) | L499-L501 | computed check | computed check | — |
