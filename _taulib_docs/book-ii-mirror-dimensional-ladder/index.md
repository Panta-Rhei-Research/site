---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Mirror.DimensionalLadder",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Mirror.DimensionalLadder`.",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_slug": "book-ii-mirror-dimensional-ladder",
  "book": "BookII",
  "family": "Mirror",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Mirror/DimensionalLadder.lean",
  "sha256": "464788cd3709254b78bf65d7e5ba8d55740c3fa45b369055f2719bbc9bfacb91",
  "imports": [
    "TauLib.BookII.Mirror.PhysicsQuadrant"
  ],
  "imported_by": [
    "TauLib.BookII"
  ],
  "registry_ids": [
    "II.D75",
    "II.D76",
    "II.R31",
    "II.R32",
    "II.T47",
    "II.T48"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 15,
    "theorem": 36,
    "structure": 2,
    "eval": 25
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "SCVDimension",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/scvdimension/",
      "source_line_start": 74,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SCVDimension.toNat",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/to-nat/",
      "source_line_start": 82,
      "source_line_end": 86,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SCVDimension.le",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/le/",
      "source_line_start": 89,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "SCVFeature",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/scvfeature/",
      "source_line_start": 98,
      "source_line_end": 111,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "feature_origin",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/feature-origin/",
      "source_line_start": 114,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "features_present",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/features-present/",
      "source_line_start": 133,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "features_new",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/features-new/",
      "source_line_start": 149,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c1_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c1-count/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c2_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c2-count/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c3_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c3-count/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c4plus_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c4plus-count/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladder_monotone",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-monotone/",
      "source_line_start": 169,
      "source_line_end": 173,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c4plus_saturated",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c4plus-saturated/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_features",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-features/",
      "source_line_start": 184,
      "source_line_end": 189,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T47"
      ]
    },
    {
      "kind": "def",
      "name": "tau_absent",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-absent/",
      "source_line_start": 192,
      "source_line_end": 199,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_feature_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-feature-count/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_absent_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-absent-count/",
      "source_line_start": 205,
      "source_line_end": 205,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_coverage",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-coverage/",
      "source_line_start": 209,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_feature_origins",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-feature-origins/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_origins_value",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-origins-value/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_distinct_rungs",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-distinct-rungs/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rung_present",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rung-present/",
      "source_line_start": 228,
      "source_line_end": 229,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c1_present",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c1-present/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c2_present",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c2-present/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c3_present",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c3-present/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_spans_three_rungs",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-spans-three-rungs/",
      "source_line_start": 241,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "simultaneous_rung",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/simultaneous-rung/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_rungs_are_c1_c2_c3",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-rungs-are-c1-c2-c3/",
      "source_line_start": 252,
      "source_line_end": 253,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_violates_monotone_acquisition",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-violates-monotone-acquisition/",
      "source_line_start": 259,
      "source_line_end": 266,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ArchimedeanEllipticEngine",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/archimedean-elliptic-engine/",
      "source_line_start": 281,
      "source_line_end": 289,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D75"
      ]
    },
    {
      "kind": "def",
      "name": "engine_active",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-active/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D75"
      ]
    },
    {
      "kind": "def",
      "name": "engine_for_quadrant",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-for-quadrant/",
      "source_line_start": 296,
      "source_line_end": 302,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "engine_active_qft",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-active-qft/",
      "source_line_start": 305,
      "source_line_end": 306,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "engine_inactive_gr",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-inactive-gr/",
      "source_line_start": 310,
      "source_line_end": 311,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "engine_inactive_padic",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-inactive-padic/",
      "source_line_start": 315,
      "source_line_end": 316,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_engine_inactive",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-engine-inactive/",
      "source_line_start": 323,
      "source_line_end": 324,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T48"
      ]
    },
    {
      "kind": "theorem",
      "name": "ladder_collapse",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-collapse/",
      "source_line_start": 329,
      "source_line_end": 334,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T48"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_engine_both_absent",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-engine-both-absent/",
      "source_line_start": 337,
      "source_line_end": 340,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "engine_unique_to_qft",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-unique-to-qft/",
      "source_line_start": 343,
      "source_line_end": 348,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DimensionalRigidity",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/dimensional-rigidity/",
      "source_line_start": 356,
      "source_line_end": 365,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "def",
      "name": "tau_rigidity",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-rigidity/",
      "source_line_start": 368,
      "source_line_end": 372,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "theorem",
      "name": "fibration_forced",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/fibration-forced/",
      "source_line_start": 375,
      "source_line_end": 377,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "theorem",
      "name": "refinement_is_abcd",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/refinement-is-abcd/",
      "source_line_start": 380,
      "source_line_end": 381,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "theorem",
      "name": "fibration_is_three",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/fibration-is-three/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "theorem",
      "name": "rigidity_no_free_parameter",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rigidity-no-free-parameter/",
      "source_line_start": 389,
      "source_line_end": 393,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "def",
      "name": "tau_moduli_count",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-moduli-count/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.R31"
      ]
    },
    {
      "kind": "def",
      "name": "categoricity_no_ladder",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-no-ladder/",
      "source_line_start": 403,
      "source_line_end": 404,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.R31"
      ]
    },
    {
      "kind": "theorem",
      "name": "categoricity_kills_ladder",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-kills-ladder/",
      "source_line_start": 407,
      "source_line_end": 408,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R31"
      ]
    },
    {
      "kind": "theorem",
      "name": "moduli_singleton",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/moduli-singleton/",
      "source_line_start": 411,
      "source_line_end": 412,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R31"
      ]
    },
    {
      "kind": "theorem",
      "name": "full_ladder_collapse",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/full-ladder-collapse/",
      "source_line_start": 421,
      "source_line_end": 430,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l437/",
      "source_line_start": 437,
      "source_line_end": 437,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l441/",
      "source_line_start": 441,
      "source_line_end": 441,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l442/",
      "source_line_start": 442,
      "source_line_end": 442,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l443/",
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
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l444/",
      "source_line_start": 444,
      "source_line_end": 444,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l447/",
      "source_line_start": 447,
      "source_line_end": 447,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l448/",
      "source_line_start": 448,
      "source_line_end": 448,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l449/",
      "source_line_start": 449,
      "source_line_end": 449,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l450/",
      "source_line_start": 450,
      "source_line_end": 450,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l453/",
      "source_line_start": 453,
      "source_line_end": 453,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l454/",
      "source_line_start": 454,
      "source_line_end": 454,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l457/",
      "source_line_start": 457,
      "source_line_end": 457,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l458/",
      "source_line_start": 458,
      "source_line_end": 458,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l459/",
      "source_line_start": 459,
      "source_line_end": 459,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l462/",
      "source_line_start": 462,
      "source_line_end": 462,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l463/",
      "source_line_start": 463,
      "source_line_end": 463,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l464/",
      "source_line_start": 464,
      "source_line_end": 464,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l465/",
      "source_line_start": 465,
      "source_line_end": 465,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l468/",
      "source_line_start": 468,
      "source_line_end": 468,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l469/",
      "source_line_start": 469,
      "source_line_end": 469,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l470/",
      "source_line_start": 470,
      "source_line_end": 470,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l473/",
      "source_line_start": 473,
      "source_line_end": 473,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l476/",
      "source_line_start": 476,
      "source_line_end": 476,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l477/",
      "source_line_start": 477,
      "source_line_end": 477,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "engine_only_qft_native",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-only-qft-native/",
      "source_line_start": 484,
      "source_line_end": 489,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "rigidity_native",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rigidity-native/",
      "source_line_start": 492,
      "source_line_end": 497,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D76"
      ]
    },
    {
      "kind": "theorem",
      "name": "simultaneous_rung_native",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/simultaneous-rung-native/",
      "source_line_start": 500,
      "source_line_end": 501,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "ladder_collapse_native",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-collapse-native/",
      "source_line_start": 504,
      "source_line_end": 505,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T48"
      ]
    },
    {
      "kind": "theorem",
      "name": "categoricity_native",
      "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-native/",
      "source_line_start": 508,
      "source_line_end": 511,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R31"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Mirror/DimensionalLadder.lean`
- SHA-256: `464788cd3709254b78bf65d7e5ba8d55740c3fa45b369055f2719bbc9bfacb91`

## Registry Links

- `II.D75` — Archimedean-Elliptic Engine
- `II.D76` — Dimensional Rigidity
- `II.R31` — Categoricity Implies No Ladder
- `II.R32` — Honest Scope: Ladder vs. SCV
- `II.T47` — Simultaneous Rung Theorem
- `II.T48` — Fourth Quadrant Ladder Collapse

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Mirror.PhysicsQuadrant`

## Imported By

- `TauLib.BookII`

## Declaration Counts

- `def`: 15
- `eval`: 25
- `inductive`: 2
- `structure`: 2
- `theorem`: 36

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [SCVDimension](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/scvdimension/) | L74-L79 | type/data schema | type/data schema | — |
| `def` | [SCVDimension.toNat](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/to-nat/) | L82-L86 | definition | definition | — |
| `def` | [SCVDimension.le](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/le/) | L89-L90 | data/computed value | data/computed value | — |
| `inductive` | [SCVFeature](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/scvfeature/) | L98-L111 | type/data schema | type/data schema | — |
| `def` | [feature_origin](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/feature-origin/) | L114-L126 | definition | definition | — |
| `def` | [features_present](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/features-present/) | L133-L146 | definition | definition | — |
| `def` | [features_new](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/features-new/) | L149-L154 | definition | definition | — |
| `theorem` | [c1_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c1-count/) | L157-L157 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c2_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c2-count/) | L160-L160 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c3_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c3-count/) | L163-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c4plus_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c4plus-count/) | L166-L166 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ladder_monotone](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-monotone/) | L169-L173 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c4plus_saturated](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c4plus-saturated/) | L176-L176 | proof obligation | formal proof obligation checked | — |
| `def` | [tau_features](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-features/) | L184-L189 | data/computed value | data/computed value | `II.T47` |
| `def` | [tau_absent](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-absent/) | L192-L199 | data/computed value | data/computed value | — |
| `theorem` | [tau_feature_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-feature-count/) | L202-L202 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_absent_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-absent-count/) | L205-L205 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_coverage](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-coverage/) | L209-L210 | proof obligation | formal proof obligation checked | — |
| `def` | [tau_feature_origins](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-feature-origins/) | L217-L218 | data/computed value | data/computed value | — |
| `theorem` | [tau_origins_value](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-origins-value/) | L221-L222 | proof obligation | formal proof obligation checked | — |
| `def` | [tau_distinct_rungs](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-distinct-rungs/) | L225-L225 | data/computed value | data/computed value | — |
| `def` | [rung_present](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rung-present/) | L228-L229 | data/computed value | data/computed value | — |
| `theorem` | [c1_present](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c1-present/) | L232-L232 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c2_present](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c2-present/) | L235-L235 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c3_present](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/c3-present/) | L238-L238 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_spans_three_rungs](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-spans-three-rungs/) | L241-L242 | proof obligation | formal proof obligation checked | `II.T47` |
| `theorem` | [simultaneous_rung](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/simultaneous-rung/) | L248-L249 | proof obligation | formal proof obligation checked | `II.T47` |
| `theorem` | [tau_rungs_are_c1_c2_c3](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-rungs-are-c1-c2-c3/) | L252-L253 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_violates_monotone_acquisition](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-violates-monotone-acquisition/) | L259-L266 | proof obligation | formal proof obligation checked | — |
| `structure` | [ArchimedeanEllipticEngine](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/archimedean-elliptic-engine/) | L281-L289 | type/data schema | type/data schema | `II.D75` |
| `def` | [engine_active](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-active/) | L292-L293 | data/computed value | data/computed value | `II.D75` |
| `def` | [engine_for_quadrant](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-for-quadrant/) | L296-L302 | definition | definition | `II.D75` |
| `theorem` | [engine_active_qft](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-active-qft/) | L305-L306 | proof obligation | formal proof obligation checked | — |
| `theorem` | [engine_inactive_gr](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-inactive-gr/) | L310-L311 | proof obligation | formal proof obligation checked | — |
| `theorem` | [engine_inactive_padic](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-inactive-padic/) | L315-L316 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_engine_inactive](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-engine-inactive/) | L323-L324 | proof obligation | formal proof obligation checked | `II.T48` |
| `theorem` | [ladder_collapse](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-collapse/) | L329-L334 | proof obligation | formal proof obligation checked | `II.T48` |
| `theorem` | [tau_engine_both_absent](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-engine-both-absent/) | L337-L340 | proof obligation | formal proof obligation checked | — |
| `theorem` | [engine_unique_to_qft](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-unique-to-qft/) | L343-L348 | proof obligation | formal proof obligation checked | — |
| `structure` | [DimensionalRigidity](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/dimensional-rigidity/) | L356-L365 | type/data schema | type/data schema | `II.D76` |
| `def` | [tau_rigidity](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-rigidity/) | L368-L372 | definition | definition | `II.D76` |
| `theorem` | [fibration_forced](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/fibration-forced/) | L375-L377 | proof obligation | formal proof obligation checked | `II.D76` |
| `theorem` | [refinement_is_abcd](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/refinement-is-abcd/) | L380-L381 | proof obligation | formal proof obligation checked | `II.D76` |
| `theorem` | [fibration_is_three](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/fibration-is-three/) | L384-L385 | proof obligation | formal proof obligation checked | `II.D76` |
| `theorem` | [rigidity_no_free_parameter](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rigidity-no-free-parameter/) | L389-L393 | proof obligation | formal proof obligation checked | `II.D76` |
| `def` | [tau_moduli_count](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-moduli-count/) | L400-L400 | data/computed value | data/computed value | `II.R31` |
| `def` | [categoricity_no_ladder](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-no-ladder/) | L403-L404 | data/computed value | data/computed value | `II.R31` |
| `theorem` | [categoricity_kills_ladder](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-kills-ladder/) | L407-L408 | proof obligation | formal proof obligation checked | `II.R31` |
| `theorem` | [moduli_singleton](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/moduli-singleton/) | L411-L412 | proof obligation | formal proof obligation checked | `II.R31` |
| `theorem` | [full_ladder_collapse](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/full-ladder-collapse/) | L421-L430 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L437](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l437/) | L437-L437 | computed check | computed check | — |
| `eval` | [#eval L438](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l438/) | L438-L438 | computed check | computed check | — |
| `eval` | [#eval L441](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l441/) | L441-L441 | computed check | computed check | — |
| `eval` | [#eval L442](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l442/) | L442-L442 | computed check | computed check | — |
| `eval` | [#eval L443](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l443/) | L443-L443 | computed check | computed check | — |
| `eval` | [#eval L444](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l444/) | L444-L444 | computed check | computed check | — |
| `eval` | [#eval L447](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l447/) | L447-L447 | computed check | computed check | — |
| `eval` | [#eval L448](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l448/) | L448-L448 | computed check | computed check | — |
| `eval` | [#eval L449](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l449/) | L449-L449 | computed check | computed check | — |
| `eval` | [#eval L450](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l450/) | L450-L450 | computed check | computed check | — |
| `eval` | [#eval L453](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l453/) | L453-L453 | computed check | computed check | — |
| `eval` | [#eval L454](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l454/) | L454-L454 | computed check | computed check | — |
| `eval` | [#eval L457](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l457/) | L457-L457 | computed check | computed check | — |
| `eval` | [#eval L458](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l458/) | L458-L458 | computed check | computed check | — |
| `eval` | [#eval L459](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l459/) | L459-L459 | computed check | computed check | — |
| `eval` | [#eval L462](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l462/) | L462-L462 | computed check | computed check | — |
| `eval` | [#eval L463](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l463/) | L463-L463 | computed check | computed check | — |
| `eval` | [#eval L464](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l464/) | L464-L464 | computed check | computed check | — |
| `eval` | [#eval L465](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l465/) | L465-L465 | computed check | computed check | — |
| `eval` | [#eval L468](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l468/) | L468-L468 | computed check | computed check | — |
| `eval` | [#eval L469](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l469/) | L469-L469 | computed check | computed check | — |
| `eval` | [#eval L470](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l470/) | L470-L470 | computed check | computed check | — |
| `eval` | [#eval L473](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l473/) | L473-L473 | computed check | computed check | — |
| `eval` | [#eval L476](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l476/) | L476-L476 | computed check | computed check | — |
| `eval` | [#eval L477](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/eval-l477/) | L477-L477 | computed check | computed check | — |
| `theorem` | [engine_only_qft_native](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-only-qft-native/) | L484-L489 | proof obligation | formal proof obligation checked | `II.D75` |
| `theorem` | [rigidity_native](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/rigidity-native/) | L492-L497 | proof obligation | formal proof obligation checked | `II.D76` |
| `theorem` | [simultaneous_rung_native](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/simultaneous-rung-native/) | L500-L501 | proof obligation | formal proof obligation checked | `II.T47` |
| `theorem` | [ladder_collapse_native](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-collapse-native/) | L504-L505 | proof obligation | formal proof obligation checked | `II.T48` |
| `theorem` | [categoricity_native](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/categoricity-native/) | L508-L511 | proof obligation | formal proof obligation checked | `II.R31` |
