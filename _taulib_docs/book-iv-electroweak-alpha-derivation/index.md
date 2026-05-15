---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_slug": "book-iv-electroweak-alpha-derivation",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/AlphaDerivation.lean",
  "sha256": "fc7c5ebdc509b20e4c8da7941d93b2b69688daf15c4cc75519ebfbd3c8e4dd65",
  "imports": [
    "TauLib.BookIV.Electroweak.TauMaxwell"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.WeakChirality",
    "TauLib.Tour.GuidedTour.BookIV",
    "TauLib.Tour.OneConstant"
  ],
  "registry_ids": [
    "IV.D104",
    "IV.D105",
    "IV.D106",
    "IV.D384",
    "IV.D385",
    "IV.L02",
    "IV.L03",
    "IV.L04",
    "IV.P225",
    "IV.P50",
    "IV.P51",
    "IV.R27",
    "IV.R365",
    "IV.R366",
    "IV.R367",
    "IV.R368",
    "IV.R369",
    "IV.R370",
    "IV.R371",
    "IV.R372",
    "IV.R373",
    "IV.R439",
    "IV.R440",
    "IV.T204",
    "IV.T205",
    "IV.T49",
    "IV.T50"
  ],
  "declaration_counts": {
    "structure": 13,
    "def": 17,
    "theorem": 9,
    "eval": 18
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "AlphaTau",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau/",
      "source_line_start": 68,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D104"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_tau",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau-l86/",
      "source_line_start": 86,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_tau_float",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau-float/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NullTransportMode",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/null-transport-mode/",
      "source_line_start": 108,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D105"
      ]
    },
    {
      "kind": "def",
      "name": "photon_null",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-null/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "graviton_null",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/graviton-null/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyCorrectionR",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-correction-r/",
      "source_line_start": 135,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D106"
      ]
    },
    {
      "kind": "def",
      "name": "HolonomyCorrectionR.toFloat",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/to-float/",
      "source_line_start": 146,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "correction_r",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/correction-r/",
      "source_line_start": 150,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyFormulaExact",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula-exact/",
      "source_line_start": 165,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T49"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_formula",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula/",
      "source_line_start": 180,
      "source_line_end": 186,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "holonomy_formula_exact",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula-exact-l188/",
      "source_line_start": 188,
      "source_line_end": 189,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OnticInvariant",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ontic-invariant/",
      "source_line_start": 198,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T50"
      ]
    },
    {
      "kind": "def",
      "name": "ontic_invariant_instance",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ontic-invariant-instance/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_ontic_invariant",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-ontic-invariant/",
      "source_line_start": 212,
      "source_line_end": 213,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ABHolonomyLemma",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/abholonomy-lemma/",
      "source_line_start": 222,
      "source_line_end": 232,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.L02"
      ]
    },
    {
      "kind": "def",
      "name": "ab_holonomy",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ab-holonomy/",
      "source_line_start": 235,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ab_holonomy_lemma",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ab-holonomy-lemma/",
      "source_line_start": 242,
      "source_line_end": 243,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PhotonPhaseQuantum",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-phase-quantum/",
      "source_line_start": 252,
      "source_line_end": 259,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.L03"
      ]
    },
    {
      "kind": "def",
      "name": "phase_quantum_instance",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/phase-quantum-instance/",
      "source_line_start": 261,
      "source_line_end": 265,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "photon_phase_quantum",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-phase-quantum-l267/",
      "source_line_start": 267,
      "source_line_end": 268,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlphaRelationalUnits",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-relational-units/",
      "source_line_start": 278,
      "source_line_end": 294,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.L04"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_rel",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-rel/",
      "source_line_start": 297,
      "source_line_end": 307,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_relational_units",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-relational-units-l309/",
      "source_line_start": 309,
      "source_line_end": 310,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UniqueMassless",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless/",
      "source_line_start": 319,
      "source_line_end": 326,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P50"
      ]
    },
    {
      "kind": "def",
      "name": "unique_massless_instance",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless-instance/",
      "source_line_start": 328,
      "source_line_end": 331,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "unique_massless_transport",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless-transport/",
      "source_line_start": 333,
      "source_line_end": 334,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "StructuralIndependence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-independence/",
      "source_line_start": 344,
      "source_line_end": 351,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P51"
      ]
    },
    {
      "kind": "def",
      "name": "structural_indep_instance",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-indep-instance/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_independence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-independence-l355/",
      "source_line_start": 355,
      "source_line_end": 357,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l393/",
      "source_line_start": 393,
      "source_line_end": 393,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "IV.R27",
        "IV.R365",
        "IV.R366",
        "IV.R367",
        "IV.R368",
        "IV.R369",
        "IV.R370",
        "IV.R371",
        "IV.R372",
        "IV.R373"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l394/",
      "source_line_start": 394,
      "source_line_end": 394,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l395/",
      "source_line_start": 395,
      "source_line_end": 395,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l396/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l397/",
      "source_line_start": 397,
      "source_line_end": 397,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l398/",
      "source_line_start": 398,
      "source_line_end": 398,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l399/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l400/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l401/",
      "source_line_start": 401,
      "source_line_end": 401,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l402/",
      "source_line_start": 402,
      "source_line_end": 402,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_null",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/example-null/",
      "source_line_start": 403,
      "source_line_end": 403,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l404/",
      "source_line_start": 404,
      "source_line_end": 404,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TwoLoopWindowCoeff",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/two-loop-window-coeff/",
      "source_line_start": 416,
      "source_line_end": 427,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D384"
      ]
    },
    {
      "kind": "def",
      "name": "two_loop_window",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/two-loop-window/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_depth_loop_correspondence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/window-depth-loop-correspondence/",
      "source_line_start": 432,
      "source_line_end": 433,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T204"
      ]
    },
    {
      "kind": "theorem",
      "name": "c2_alpha_sub_1_ppm",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/c2-alpha-sub-1-ppm/",
      "source_line_start": 437,
      "source_line_end": 439,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P225"
      ]
    },
    {
      "kind": "structure",
      "name": "AlphaNLOCatalog",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-nlocatalog/",
      "source_line_start": 455,
      "source_line_end": 464,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D385"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_nlo_catalog",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-nlo-catalog/",
      "source_line_start": 466,
      "source_line_end": 466,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlphaPrecisionBarrier",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-precision-barrier/",
      "source_line_start": 471,
      "source_line_end": 478,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T205"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_precision_barrier",
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-precision-barrier-l480/",
      "source_line_start": 480,
      "source_line_end": 480,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l486/",
      "source_line_start": 486,
      "source_line_end": 486,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "IV.R440"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l487/",
      "source_line_start": 487,
      "source_line_end": 487,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l488/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l489/",
      "source_line_start": 489,
      "source_line_end": 489,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l490/",
      "source_line_start": 490,
      "source_line_end": 490,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l491/",
      "source_line_start": 491,
      "source_line_end": 491,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l492/",
      "source_line_start": 492,
      "source_line_end": 494,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/AlphaDerivation.lean`
- SHA-256: `fc7c5ebdc509b20e4c8da7941d93b2b69688daf15c4cc75519ebfbd3c8e4dd65`

## Registry Links

- `IV.D104` — tau-Native Fine-Structure Constant
- `IV.D105` — Null Transport Mode
- `IV.D106` — Holonomy Correction Factor
- `IV.D384` — Two-Loop Window Coefficient c₂
- `IV.D385` — α NLO Correction Candidate Catalog
- `IV.L02` — Holonomy Normalization
- `IV.L03` — Photon Phase Quantum
- `IV.L04` — Mediator Ratio
- `IV.P225` — c₂ Numerical Bound from W₄(3)
- `IV.P50` — Photon Uniqueness
- `IV.P51` — alpha_em versus iota_tau
- `IV.R27` — sqrt(3) Triad
- `IV.R365` — Why alpha_mathrmem
- `IV.R366` — Measuring alpha_mathrmem
- `IV.R367` — No external input
- `IV.R368` — Why (1,0) winding
- `IV.R369` — Compactness is essential
- `IV.R370` — The iota_tau^2 cancellation
- `IV.R371` — The meaning of 0.6%
- `IV.R372` — Lean verification
- `IV.R373` — pi^3 approx 31: not a Mersenne prime
- `IV.R439` — OQ-B4 Status: PARTIAL
- `IV.R440` — α Precision Assessment
- `IV.T204` — Window Depth–Loop Order Correspondence
- `IV.T205` — α Precision Barrier at 9.8 ppm
- `IV.T49` — Holonomy Formula for alpha_em
- `IV.T50` — No-Running Principle for alpha_em

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.TauMaxwell`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.WeakChirality`
- `TauLib.Tour.GuidedTour.BookIV`
- `TauLib.Tour.OneConstant`

## Declaration Counts

- `def`: 17
- `eval`: 18
- `structure`: 13
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [AlphaTau](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau/) | L68-L83 | type/data schema | type/data schema | `IV.D104` |
| `def` | [alpha_tau](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau-l86/) | L86-L95 | definition | definition | — |
| `def` | [alpha_tau_float](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau-float/) | L98-L99 | data/computed value | data/computed value | — |
| `structure` | [NullTransportMode](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/null-transport-mode/) | L108-L117 | type/data schema | type/data schema | `IV.D105` |
| `def` | [photon_null](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-null/) | L120-L121 | definition | definition | — |
| `def` | [graviton_null](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/graviton-null/) | L124-L125 | definition | definition | — |
| `structure` | [HolonomyCorrectionR](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-correction-r/) | L135-L144 | type/data schema | type/data schema | `IV.D106` |
| `def` | [HolonomyCorrectionR.toFloat](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/to-float/) | L146-L147 | data/computed value | data/computed value | — |
| `def` | [correction_r](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/correction-r/) | L150-L155 | definition | definition | — |
| `structure` | [HolonomyFormulaExact](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula-exact/) | L165-L177 | type/data schema | type/data schema | `IV.T49` |
| `def` | [holonomy_formula](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula/) | L180-L186 | definition | definition | — |
| `theorem` | [holonomy_formula_exact](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula-exact-l188/) | L188-L189 | proof obligation | formal proof obligation checked | — |
| `structure` | [OnticInvariant](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ontic-invariant/) | L198-L206 | type/data schema | type/data schema | `IV.T50` |
| `def` | [ontic_invariant_instance](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ontic-invariant-instance/) | L208-L210 | definition | definition | — |
| `theorem` | [alpha_ontic_invariant](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-ontic-invariant/) | L212-L213 | proof obligation | formal proof obligation checked | — |
| `structure` | [ABHolonomyLemma](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/abholonomy-lemma/) | L222-L232 | type/data schema | type/data schema | `IV.L02` |
| `def` | [ab_holonomy](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ab-holonomy/) | L235-L240 | definition | definition | — |
| `theorem` | [ab_holonomy_lemma](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/ab-holonomy-lemma/) | L242-L243 | proof obligation | formal proof obligation checked | — |
| `structure` | [PhotonPhaseQuantum](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-phase-quantum/) | L252-L259 | type/data schema | type/data schema | `IV.L03` |
| `def` | [phase_quantum_instance](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/phase-quantum-instance/) | L261-L265 | definition | definition | — |
| `theorem` | [photon_phase_quantum](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/photon-phase-quantum-l267/) | L267-L268 | proof obligation | formal proof obligation checked | — |
| `structure` | [AlphaRelationalUnits](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-relational-units/) | L278-L294 | type/data schema | type/data schema | `IV.L04` |
| `def` | [alpha_rel](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-rel/) | L297-L307 | definition | definition | — |
| `theorem` | [alpha_relational_units](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-relational-units-l309/) | L309-L310 | proof obligation | formal proof obligation checked | — |
| `structure` | [UniqueMassless](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless/) | L319-L326 | type/data schema | type/data schema | `IV.P50` |
| `def` | [unique_massless_instance](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless-instance/) | L328-L331 | definition | definition | — |
| `theorem` | [unique_massless_transport](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless-transport/) | L333-L334 | proof obligation | formal proof obligation checked | — |
| `structure` | [StructuralIndependence](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-independence/) | L344-L351 | type/data schema | type/data schema | `IV.P51` |
| `def` | [structural_indep_instance](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-indep-instance/) | L353-L353 | definition | definition | — |
| `theorem` | [structural_independence](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/structural-independence-l355/) | L355-L357 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L393](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l393/) | L393-L393 | computed check | computed check | `IV.R27`, `IV.R365`, `IV.R366`, `IV.R367`, `IV.R368`, `IV.R369`, `IV.R370`, `IV.R371`, `IV.R372`, `IV.R373` |
| `eval` | [#eval L394](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l394/) | L394-L394 | computed check | computed check | — |
| `eval` | [#eval L395](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l395/) | L395-L395 | computed check | computed check | — |
| `eval` | [#eval L396](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l396/) | L396-L396 | computed check | computed check | — |
| `eval` | [#eval L397](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l397/) | L397-L397 | computed check | computed check | — |
| `eval` | [#eval L398](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l398/) | L398-L398 | computed check | computed check | — |
| `eval` | [#eval L399](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l399/) | L399-L399 | computed check | computed check | — |
| `eval` | [#eval L400](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l400/) | L400-L400 | computed check | computed check | — |
| `eval` | [#eval L401](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l401/) | L401-L401 | computed check | computed check | — |
| `eval` | [#eval L402](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l402/) | L402-L402 | computed check | computed check | — |
| `def` | [example_null](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/example-null/) | L403-L403 | definition | definition | — |
| `eval` | [#eval L404](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l404/) | L404-L404 | computed check | computed check | — |
| `structure` | [TwoLoopWindowCoeff](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/two-loop-window-coeff/) | L416-L427 | type/data schema | type/data schema | `IV.D384` |
| `def` | [two_loop_window](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/two-loop-window/) | L429-L429 | definition | definition | — |
| `theorem` | [window_depth_loop_correspondence](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/window-depth-loop-correspondence/) | L432-L433 | proof obligation | formal proof obligation checked | `IV.T204` |
| `theorem` | [c2_alpha_sub_1_ppm](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/c2-alpha-sub-1-ppm/) | L437-L439 | proof obligation | formal proof obligation checked | `IV.P225` |
| `structure` | [AlphaNLOCatalog](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-nlocatalog/) | L455-L464 | type/data schema | type/data schema | `IV.D385` |
| `def` | [alpha_nlo_catalog](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-nlo-catalog/) | L466-L466 | definition | definition | — |
| `structure` | [AlphaPrecisionBarrier](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-precision-barrier/) | L471-L478 | type/data schema | type/data schema | `IV.T205` |
| `def` | [alpha_precision_barrier](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-precision-barrier-l480/) | L480-L480 | definition | definition | — |
| `eval` | [#eval L486](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l486/) | L486-L486 | computed check | computed check | `IV.R440` |
| `eval` | [#eval L487](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l487/) | L487-L487 | computed check | computed check | — |
| `eval` | [#eval L488](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l488/) | L488-L488 | computed check | computed check | — |
| `eval` | [#eval L489](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l489/) | L489-L489 | computed check | computed check | — |
| `eval` | [#eval L490](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l490/) | L490-L490 | computed check | computed check | — |
| `eval` | [#eval L491](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l491/) | L491-L491 | computed check | computed check | — |
| `eval` | [#eval L492](/corpus/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l492/) | L492-L494 | computed check | computed check | — |
