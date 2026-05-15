---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.TauHiggs2",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_slug": "book-iv-electroweak-tau-higgs2",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/TauHiggs2.lean",
  "sha256": "c2d95bfeca80c3883a726e87051d110812457ef0b1780ccc6288ed7609ef2885",
  "imports": [
    "TauLib.BookIV.Electroweak.TauHiggs"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.EWSynthesis"
  ],
  "registry_ids": [
    "IV.D140",
    "IV.D141",
    "IV.D142",
    "IV.D320",
    "IV.D348",
    "IV.D358",
    "IV.D376",
    "IV.L07",
    "IV.P188",
    "IV.P199",
    "IV.P220",
    "IV.P74",
    "IV.P75",
    "IV.P76",
    "IV.P77",
    "IV.R35",
    "IV.R36",
    "IV.R399",
    "IV.R408",
    "IV.T150",
    "IV.T155",
    "IV.T166",
    "IV.T194",
    "IV.T65"
  ],
  "declaration_counts": {
    "structure": 14,
    "def": 34,
    "theorem": 14,
    "eval": 28,
    "inductive": 1
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CoherenceHessian",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian/",
      "source_line_start": 57,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D140"
      ]
    },
    {
      "kind": "def",
      "name": "coherence_hessian",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian-l70/",
      "source_line_start": 70,
      "source_line_end": 70,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauHiggsMass",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass/",
      "source_line_start": 84,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D141"
      ]
    },
    {
      "kind": "def",
      "name": "tau_higgs_mass",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass-l96/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_mass_GeV",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-ge-v/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauYukawaCoupling",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-yukawa-coupling/",
      "source_line_start": 114,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D142"
      ]
    },
    {
      "kind": "def",
      "name": "TauYukawaCoupling.toFloat",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/to-float/",
      "source_line_start": 126,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_top",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-top/",
      "source_line_start": 130,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_bottom",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-bottom/",
      "source_line_start": 136,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_electron",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-electron/",
      "source_line_start": 142,
      "source_line_end": 145,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EWScale",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/ewscale/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D320"
      ]
    },
    {
      "kind": "def",
      "name": "ew_scale",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/ew-scale/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HessianConvergence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-convergence/",
      "source_line_start": 178,
      "source_line_end": 185,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.L07"
      ]
    },
    {
      "kind": "def",
      "name": "hessian_eigenvalue_convergence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-eigenvalue-convergence/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoFundamentalScalar",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar/",
      "source_line_start": 203,
      "source_line_end": 212,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T65"
      ]
    },
    {
      "kind": "def",
      "name": "no_fundamental_scalar",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_hierarchy_problem",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-hierarchy-problem/",
      "source_line_start": 216,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "hessian_one_positive",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-one-positive/",
      "source_line_start": 229,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P74"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_mass_range",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-range/",
      "source_line_start": 241,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P75"
      ]
    },
    {
      "kind": "structure",
      "name": "GoldstoneAbsorption",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-absorption/",
      "source_line_start": 258,
      "source_line_end": 271,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P76"
      ]
    },
    {
      "kind": "def",
      "name": "goldstone_eaten",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-eaten/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DecayBranching",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching/",
      "source_line_start": 292,
      "source_line_end": 297,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P77"
      ]
    },
    {
      "kind": "def",
      "name": "br_bb",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-bb/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_WW",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-ww/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_gg",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-gg/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_tautau",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-tautau/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_cc",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-cc/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_ZZ",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-zz/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decay_branching",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching-l307/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "branching_sum_approx",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/branching-sum-approx/",
      "source_line_start": 311,
      "source_line_end": 313,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_hierarchy_dissolution",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-hierarchy-dissolution/",
      "source_line_start": 325,
      "source_line_end": 326,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R35"
      ]
    },
    {
      "kind": "def",
      "name": "remark_deviation_signatures",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-deviation-signatures/",
      "source_line_start": 340,
      "source_line_end": 341,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R36"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l347/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l358/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l359/",
      "source_line_start": 359,
      "source_line_end": 359,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "NonOmegaGenerator",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/non-omega-generator/",
      "source_line_start": 368,
      "source_line_end": 370,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four/",
      "source_line_start": 374,
      "source_line_end": 375,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four_lobes",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-lobes/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four_betti",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-betti/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_mass_nlo_formula_n5",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n5/",
      "source_line_start": 391,
      "source_line_end": 392,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.D348"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_mass_nlo_formula_n6",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n6/",
      "source_line_start": 397,
      "source_line_end": 398,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R399"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_w_ratio_comparison",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-w-ratio-comparison/",
      "source_line_start": 404,
      "source_line_end": 405,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.P188"
      ]
    },
    {
      "kind": "def",
      "name": "remark_omega_self_energy_open",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-omega-self-energy-open/",
      "source_line_start": 409,
      "source_line_end": 410,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R399"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 414,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l415/",
      "source_line_start": 415,
      "source_line_end": 415,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l416/",
      "source_line_start": 416,
      "source_line_end": 416,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l417/",
      "source_line_start": 417,
      "source_line_end": 417,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n6_cf_sum",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-cf-sum/",
      "source_line_start": 430,
      "source_line_end": 430,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n6_formula",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-formula/",
      "source_line_start": 433,
      "source_line_end": 434,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_inv_cf_expansion",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/iota-inv-cf-expansion/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cf_sum_five_is_not_six",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/cf-sum-five-is-not-six/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l443/",
      "source_line_start": 443,
      "source_line_end": 443,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_formula",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-formula/",
      "source_line_start": 453,
      "source_line_end": 455,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsN7",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7/",
      "source_line_start": 461,
      "source_line_end": 470,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_data",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-data/",
      "source_line_start": 472,
      "source_line_end": 475,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n7_tau_effective",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-tau-effective/",
      "source_line_start": 477,
      "source_line_end": 480,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "muon_mass_nnlo_open",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/muon-mass-nnlo-open/",
      "source_line_start": 491,
      "source_line_end": 493,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nnlo_ratio_n7_n5",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/nnlo-ratio-n7-n5/",
      "source_line_start": 496,
      "source_line_end": 496,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l499/",
      "source_line_start": 499,
      "source_line_end": 499,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l500/",
      "source_line_start": 500,
      "source_line_end": 500,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoherenceFunctionalLevel",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-functional-level/",
      "source_line_start": 522,
      "source_line_end": 533,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "coherence_level_7",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-level-7/",
      "source_line_start": 535,
      "source_line_end": 538,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsN7Uniqueness",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness/",
      "source_line_start": 555,
      "source_line_end": 576,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_uniqueness",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-l578/",
      "source_line_start": 578,
      "source_line_end": 580,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n7_uniqueness_thm",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-thm/",
      "source_line_start": 583,
      "source_line_end": 588,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WindowRGPeriod",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-rgperiod/",
      "source_line_start": 604,
      "source_line_end": 613,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "window_rg_period",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-rg-period/",
      "source_line_start": 615,
      "source_line_end": 616,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_nnlo_period",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-nnlo-period/",
      "source_line_start": 619,
      "source_line_end": 623,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l626/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l627/",
      "source_line_start": 627,
      "source_line_end": 627,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l628/",
      "source_line_start": 628,
      "source_line_end": 628,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l629/",
      "source_line_start": 629,
      "source_line_end": 629,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsSelfCoupling",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling/",
      "source_line_start": 641,
      "source_line_end": 656,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D376"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_self_coupling",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling-l658/",
      "source_line_start": 658,
      "source_line_end": 658,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_lambda_sub_100ppm",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-sub-100ppm/",
      "source_line_start": 662,
      "source_line_end": 665,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T194"
      ]
    },
    {
      "kind": "structure",
      "name": "HiggsLambdaFalsification",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification/",
      "source_line_start": 670,
      "source_line_end": 679,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P220"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_lambda_falsification",
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification-l681/",
      "source_line_start": 681,
      "source_line_end": 681,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l684/",
      "source_line_start": 684,
      "source_line_end": 684,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l685/",
      "source_line_start": 685,
      "source_line_end": 685,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l686/",
      "source_line_start": 686,
      "source_line_end": 688,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/TauHiggs2.lean`
- SHA-256: `c2d95bfeca80c3883a726e87051d110812457ef0b1780ccc6288ed7609ef2885`

## Registry Links

- `IV.D140` — Vacuum Hessian at Crossing Point
- `IV.D141` — τ-Higgs Mass
- `IV.D142` — τ-Yukawa Coupling (Ch34)
- `IV.D320` — Electroweak scale in Category~tau
- `IV.D348` — Higgs Mass omega-Sector Formula
- `IV.D358` — Higgs n=7: Structural Identification as 2*lobes + sectors
- `IV.D376` — Higgs Self-Coupling from τ-Chain
- `IV.L07` — Discrete Hessian Spectrum
- `IV.P188` — m_H/m_W Ratio [auto-upgrades with IV.P199]
- `IV.P199` — n=7 Structural Uniqueness: Coherence Functional Samples Lobe+Sector
- `IV.P220` — HL-LHC and FCC-hh Falsification Window
- `IV.P74` — Finite-Stage Hessian Properties
- `IV.P75` — Higgs Mass Readout
- `IV.P76` — Goldstone Modes at Crossing Point
- `IV.P77` — Decay Mode Consistency
- `IV.R35` — Structural Resolution of Hierarchy
- `IV.R36` — Where τ and SM Could Diverge
- `IV.R399` — Open: omega Self-Energy Correction and Coefficient-6 Identification
- `IV.R408` — m_mu/m_e Sub-100 ppm NNLO Status and Higgs n Comparison Table
- `IV.T150` — Factor-4 from Non-omega Generator Count
- `IV.T155` — Higgs Bonus Coefficient n=6 [SUPERSEDED by IV.T166 n=7]
- `IV.T166` — Higgs n=7 Formula at +8.0 ppm from PDG 125.20 GeV (tau-effective)
- `IV.T194` — τ-Chain Higgs Self-Coupling at +16 ppm
- `IV.T65` — No Hierarchy Problem in Category τ

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.TauHiggs`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.EWSynthesis`

## Declaration Counts

- `def`: 34
- `eval`: 28
- `inductive`: 1
- `structure`: 14
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CoherenceHessian](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian/) | L57-L68 | type/data schema | type/data schema | `IV.D140` |
| `def` | [coherence_hessian](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian-l70/) | L70-L70 | definition | definition | — |
| `structure` | [TauHiggsMass](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass/) | L84-L93 | type/data schema | type/data schema | `IV.D141` |
| `def` | [tau_higgs_mass](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass-l96/) | L96-L98 | definition | definition | — |
| `def` | [higgs_mass_GeV](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-ge-v/) | L101-L102 | data/computed value | data/computed value | — |
| `structure` | [TauYukawaCoupling](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/tau-yukawa-coupling/) | L114-L123 | type/data schema | type/data schema | `IV.D142` |
| `def` | [TauYukawaCoupling.toFloat](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/to-float/) | L126-L127 | data/computed value | data/computed value | — |
| `def` | [yukawa_top](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-top/) | L130-L133 | definition | definition | — |
| `def` | [yukawa_bottom](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-bottom/) | L136-L139 | definition | definition | — |
| `def` | [yukawa_electron](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-electron/) | L142-L145 | definition | definition | — |
| `structure` | [EWScale](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/ewscale/) | L157-L164 | type/data schema | type/data schema | `IV.D320` |
| `def` | [ew_scale](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/ew-scale/) | L166-L166 | definition | definition | — |
| `structure` | [HessianConvergence](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-convergence/) | L178-L185 | type/data schema | type/data schema | `IV.L07` |
| `def` | [hessian_eigenvalue_convergence](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-eigenvalue-convergence/) | L187-L187 | definition | definition | — |
| `structure` | [NoFundamentalScalar](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar/) | L203-L212 | type/data schema | type/data schema | `IV.T65` |
| `def` | [no_fundamental_scalar](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar-l214/) | L214-L214 | definition | definition | — |
| `theorem` | [no_hierarchy_problem](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/no-hierarchy-problem/) | L216-L220 | proof obligation | formal proof obligation checked | — |
| `theorem` | [hessian_one_positive](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-one-positive/) | L229-L233 | proof obligation | formal proof obligation checked | `IV.P74` |
| `theorem` | [higgs_mass_range](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-range/) | L241-L244 | proof obligation | formal proof obligation checked | `IV.P75` |
| `structure` | [GoldstoneAbsorption](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-absorption/) | L258-L271 | type/data schema | type/data schema | `IV.P76` |
| `def` | [goldstone_eaten](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-eaten/) | L273-L273 | definition | definition | — |
| `structure` | [DecayBranching](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching/) | L292-L297 | type/data schema | type/data schema | `IV.P77` |
| `def` | [br_bb](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-bb/) | L299-L299 | definition | definition | — |
| `def` | [br_WW](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-ww/) | L300-L300 | definition | definition | — |
| `def` | [br_gg](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-gg/) | L301-L301 | definition | definition | — |
| `def` | [br_tautau](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-tautau/) | L302-L302 | definition | definition | — |
| `def` | [br_cc](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-cc/) | L303-L303 | definition | definition | — |
| `def` | [br_ZZ](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/br-zz/) | L304-L304 | definition | definition | — |
| `def` | [decay_branching](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching-l307/) | L307-L308 | data/computed value | data/computed value | — |
| `theorem` | [branching_sum_approx](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/branching-sum-approx/) | L311-L313 | proof obligation | formal proof obligation checked | — |
| `def` | [remark_hierarchy_dissolution](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-hierarchy-dissolution/) | L325-L326 | docstring/data record | docstring/data record | `IV.R35` |
| `def` | [remark_deviation_signatures](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-deviation-signatures/) | L340-L341 | docstring/data record | docstring/data record | `IV.R36` |
| `eval` | [#eval L347](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l347/) | L347-L347 | computed check | computed check | — |
| `eval` | [#eval L348](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l348/) | L348-L348 | computed check | computed check | — |
| `eval` | [#eval L349](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l349/) | L349-L349 | computed check | computed check | — |
| `eval` | [#eval L350](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l350/) | L350-L350 | computed check | computed check | — |
| `eval` | [#eval L351](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l351/) | L351-L351 | computed check | computed check | — |
| `eval` | [#eval L352](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l352/) | L352-L352 | computed check | computed check | — |
| `eval` | [#eval L353](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l353/) | L353-L353 | computed check | computed check | — |
| `eval` | [#eval L354](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l354/) | L354-L354 | computed check | computed check | — |
| `eval` | [#eval L355](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l355/) | L355-L355 | computed check | computed check | — |
| `eval` | [#eval L356](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l356/) | L356-L356 | computed check | computed check | — |
| `eval` | [#eval L357](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l357/) | L357-L357 | computed check | computed check | — |
| `eval` | [#eval L358](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l358/) | L358-L358 | computed check | computed check | — |
| `eval` | [#eval L359](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l359/) | L359-L359 | computed check | computed check | — |
| `inductive` | [NonOmegaGenerator](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/non-omega-generator/) | L368-L370 | type/data schema | type/data schema | `IV.T150` |
| `theorem` | [higgs_factor_four](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four/) | L374-L375 | proof obligation | formal proof obligation checked | `IV.T150` |
| `theorem` | [higgs_factor_four_lobes](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-lobes/) | L378-L378 | proof obligation | formal proof obligation checked | `IV.T150` |
| `theorem` | [higgs_factor_four_betti](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-betti/) | L384-L385 | proof obligation | formal proof obligation checked | `IV.T150` |
| `def` | [higgs_mass_nlo_formula_n5](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n5/) | L391-L392 | docstring/data record | docstring/data record | `IV.D348` |
| `def` | [higgs_mass_nlo_formula_n6](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n6/) | L397-L398 | docstring/data record | docstring/data record | `IV.R399` |
| `def` | [higgs_w_ratio_comparison](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-w-ratio-comparison/) | L404-L405 | docstring/data record | docstring/data record | `IV.P188` |
| `def` | [remark_omega_self_energy_open](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/remark-omega-self-energy-open/) | L409-L410 | docstring/data record | docstring/data record | `IV.R399` |
| `eval` | [#eval L413](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l413/) | L413-L413 | computed check | computed check | — |
| `eval` | [#eval L414](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l414/) | L414-L414 | computed check | computed check | — |
| `eval` | [#eval L415](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l415/) | L415-L415 | computed check | computed check | — |
| `eval` | [#eval L416](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l416/) | L416-L416 | computed check | computed check | — |
| `eval` | [#eval L417](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l417/) | L417-L417 | computed check | computed check | — |
| `theorem` | [higgs_n6_cf_sum](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-cf-sum/) | L430-L430 | proof obligation | formal proof obligation checked | — |
| `def` | [higgs_n6_formula](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-formula/) | L433-L434 | docstring/data record | docstring/data record | — |
| `def` | [iota_inv_cf_expansion](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/iota-inv-cf-expansion/) | L438-L438 | data/computed value | data/computed value | — |
| `theorem` | [cf_sum_five_is_not_six](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/cf-sum-five-is-not-six/) | L440-L441 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L443](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l443/) | L443-L443 | computed check | computed check | — |
| `def` | [higgs_n7_formula](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-formula/) | L453-L455 | docstring/data record | docstring/data record | — |
| `structure` | [HiggsN7](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7/) | L461-L470 | type/data schema | type/data schema | — |
| `def` | [higgs_n7_data](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-data/) | L472-L475 | definition | definition | — |
| `theorem` | [higgs_n7_tau_effective](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-tau-effective/) | L477-L480 | proof obligation | formal proof obligation checked | — |
| `def` | [muon_mass_nnlo_open](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/muon-mass-nnlo-open/) | L491-L493 | docstring/data record | docstring/data record | — |
| `theorem` | [nnlo_ratio_n7_n5](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/nnlo-ratio-n7-n5/) | L496-L496 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L499](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l499/) | L499-L499 | computed check | computed check | — |
| `eval` | [#eval L500](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l500/) | L500-L500 | computed check | computed check | — |
| `structure` | [CoherenceFunctionalLevel](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-functional-level/) | L522-L533 | type/data schema | type/data schema | — |
| `def` | [coherence_level_7](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-level-7/) | L535-L538 | definition | definition | — |
| `structure` | [HiggsN7Uniqueness](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness/) | L555-L576 | type/data schema | type/data schema | — |
| `def` | [higgs_n7_uniqueness](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-l578/) | L578-L580 | definition | definition | — |
| `theorem` | [higgs_n7_uniqueness_thm](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-thm/) | L583-L588 | proof obligation | formal proof obligation checked | — |
| `structure` | [WindowRGPeriod](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-rgperiod/) | L604-L613 | type/data schema | type/data schema | — |
| `def` | [window_rg_period](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-rg-period/) | L615-L616 | definition | definition | — |
| `theorem` | [window_nnlo_period](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-nnlo-period/) | L619-L623 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L626](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l626/) | L626-L626 | computed check | computed check | — |
| `eval` | [#eval L627](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l627/) | L627-L627 | computed check | computed check | — |
| `eval` | [#eval L628](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l628/) | L628-L628 | computed check | computed check | — |
| `eval` | [#eval L629](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l629/) | L629-L629 | computed check | computed check | — |
| `structure` | [HiggsSelfCoupling](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling/) | L641-L656 | type/data schema | type/data schema | `IV.D376` |
| `def` | [higgs_self_coupling](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling-l658/) | L658-L658 | definition | definition | — |
| `theorem` | [higgs_lambda_sub_100ppm](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-sub-100ppm/) | L662-L665 | proof obligation | formal proof obligation checked | `IV.T194` |
| `structure` | [HiggsLambdaFalsification](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification/) | L670-L679 | type/data schema | type/data schema | `IV.P220` |
| `def` | [higgs_lambda_falsification](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification-l681/) | L681-L681 | definition | definition | — |
| `eval` | [#eval L684](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l684/) | L684-L684 | computed check | computed check | — |
| `eval` | [#eval L685](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l685/) | L685-L685 | computed check | computed check | — |
| `eval` | [#eval L686](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l686/) | L686-L688 | computed check | computed check | — |
