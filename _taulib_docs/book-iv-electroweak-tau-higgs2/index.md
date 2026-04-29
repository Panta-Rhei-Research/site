---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.TauHiggs2",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
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
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian/",
      "source_line_start": 57,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D140"
      ]
    },
    {
      "kind": "def",
      "name": "coherence_hessian",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian-l70/",
      "source_line_start": 70,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauHiggsMass",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass/",
      "source_line_start": 84,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D141"
      ]
    },
    {
      "kind": "def",
      "name": "tau_higgs_mass",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass-l96/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_mass_GeV",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-ge-v/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauYukawaCoupling",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-yukawa-coupling/",
      "source_line_start": 114,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D142"
      ]
    },
    {
      "kind": "def",
      "name": "TauYukawaCoupling.toFloat",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/to-float/",
      "source_line_start": 126,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_top",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-top/",
      "source_line_start": 130,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_bottom",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-bottom/",
      "source_line_start": 136,
      "source_line_end": 139,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yukawa_electron",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-electron/",
      "source_line_start": 142,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EWScale",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/ewscale/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D320"
      ]
    },
    {
      "kind": "def",
      "name": "ew_scale",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/ew-scale/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HessianConvergence",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-convergence/",
      "source_line_start": 178,
      "source_line_end": 185,
      "formal_status": "defined",
      "registry_ids": [
        "IV.L07"
      ]
    },
    {
      "kind": "def",
      "name": "hessian_eigenvalue_convergence",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-eigenvalue-convergence/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoFundamentalScalar",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar/",
      "source_line_start": 203,
      "source_line_end": 212,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T65"
      ]
    },
    {
      "kind": "def",
      "name": "no_fundamental_scalar",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_hierarchy_problem",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-hierarchy-problem/",
      "source_line_start": 216,
      "source_line_end": 220,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "hessian_one_positive",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-one-positive/",
      "source_line_start": 229,
      "source_line_end": 233,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P74"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_mass_range",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-range/",
      "source_line_start": 241,
      "source_line_end": 244,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P75"
      ]
    },
    {
      "kind": "structure",
      "name": "GoldstoneAbsorption",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-absorption/",
      "source_line_start": 258,
      "source_line_end": 271,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P76"
      ]
    },
    {
      "kind": "def",
      "name": "goldstone_eaten",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-eaten/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DecayBranching",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching/",
      "source_line_start": 292,
      "source_line_end": 297,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P77"
      ]
    },
    {
      "kind": "def",
      "name": "br_bb",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-bb/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_WW",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-ww/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_gg",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-gg/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_tautau",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-tautau/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_cc",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-cc/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "br_ZZ",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-zz/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decay_branching",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching-l307/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "branching_sum_approx",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/branching-sum-approx/",
      "source_line_start": 311,
      "source_line_end": 313,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_hierarchy_dissolution",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-hierarchy-dissolution/",
      "source_line_start": 325,
      "source_line_end": 326,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R35"
      ]
    },
    {
      "kind": "def",
      "name": "remark_deviation_signatures",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-deviation-signatures/",
      "source_line_start": 340,
      "source_line_end": 341,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R36"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 358,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l359/",
      "source_line_start": 359,
      "source_line_end": 359,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "NonOmegaGenerator",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/non-omega-generator/",
      "source_line_start": 368,
      "source_line_end": 370,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four/",
      "source_line_start": 374,
      "source_line_end": 375,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four_lobes",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-lobes/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "theorem",
      "name": "higgs_factor_four_betti",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-betti/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T150"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_mass_nlo_formula_n5",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n5/",
      "source_line_start": 391,
      "source_line_end": 392,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D348"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_mass_nlo_formula_n6",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n6/",
      "source_line_start": 397,
      "source_line_end": 398,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R399"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_w_ratio_comparison",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-w-ratio-comparison/",
      "source_line_start": 404,
      "source_line_end": 405,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P188"
      ]
    },
    {
      "kind": "def",
      "name": "remark_omega_self_energy_open",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-omega-self-energy-open/",
      "source_line_start": 409,
      "source_line_end": 410,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R399"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 414,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l415/",
      "source_line_start": 415,
      "source_line_end": 415,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l416/",
      "source_line_start": 416,
      "source_line_end": 416,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l417/",
      "source_line_start": 417,
      "source_line_end": 417,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n6_cf_sum",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-cf-sum/",
      "source_line_start": 430,
      "source_line_end": 430,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n6_formula",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-formula/",
      "source_line_start": 433,
      "source_line_end": 434,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_inv_cf_expansion",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/iota-inv-cf-expansion/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cf_sum_five_is_not_six",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/cf-sum-five-is-not-six/",
      "source_line_start": 440,
      "source_line_end": 441,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l443/",
      "source_line_start": 443,
      "source_line_end": 443,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_formula",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-formula/",
      "source_line_start": 453,
      "source_line_end": 455,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsN7",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7/",
      "source_line_start": 461,
      "source_line_end": 470,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_data",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-data/",
      "source_line_start": 472,
      "source_line_end": 475,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n7_tau_effective",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-tau-effective/",
      "source_line_start": 477,
      "source_line_end": 480,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "muon_mass_nnlo_open",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/muon-mass-nnlo-open/",
      "source_line_start": 491,
      "source_line_end": 493,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nnlo_ratio_n7_n5",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/nnlo-ratio-n7-n5/",
      "source_line_start": 496,
      "source_line_end": 496,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l499/",
      "source_line_start": 499,
      "source_line_end": 499,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l500/",
      "source_line_start": 500,
      "source_line_end": 500,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoherenceFunctionalLevel",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-functional-level/",
      "source_line_start": 522,
      "source_line_end": 533,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "coherence_level_7",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-level-7/",
      "source_line_start": 535,
      "source_line_end": 538,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsN7Uniqueness",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness/",
      "source_line_start": 555,
      "source_line_end": 576,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "higgs_n7_uniqueness",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-l578/",
      "source_line_start": 578,
      "source_line_end": 580,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_n7_uniqueness_thm",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-thm/",
      "source_line_start": 583,
      "source_line_end": 588,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WindowRGPeriod",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-rgperiod/",
      "source_line_start": 604,
      "source_line_end": 613,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "window_rg_period",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-rg-period/",
      "source_line_start": 615,
      "source_line_end": 616,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_nnlo_period",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-nnlo-period/",
      "source_line_start": 619,
      "source_line_end": 623,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l626/",
      "source_line_start": 626,
      "source_line_end": 626,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l627/",
      "source_line_start": 627,
      "source_line_end": 627,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l628/",
      "source_line_start": 628,
      "source_line_end": 628,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l629/",
      "source_line_start": 629,
      "source_line_end": 629,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HiggsSelfCoupling",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling/",
      "source_line_start": 641,
      "source_line_end": 656,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D376"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_self_coupling",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling-l658/",
      "source_line_start": 658,
      "source_line_end": 658,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "higgs_lambda_sub_100ppm",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-sub-100ppm/",
      "source_line_start": 662,
      "source_line_end": 665,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T194"
      ]
    },
    {
      "kind": "structure",
      "name": "HiggsLambdaFalsification",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification/",
      "source_line_start": 670,
      "source_line_end": 679,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P220"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_lambda_falsification",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification-l681/",
      "source_line_start": 681,
      "source_line_end": 681,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l684/",
      "source_line_start": 684,
      "source_line_end": 684,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l685/",
      "source_line_start": 685,
      "source_line_end": 685,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l686/",
      "source_line_start": 686,
      "source_line_end": 688,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [CoherenceHessian](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian/) | L57-L68 | defined | `IV.D140` |
| `def` | [coherence_hessian](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian-l70/) | L70-L70 | defined | — |
| `structure` | [TauHiggsMass](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass/) | L84-L93 | defined | `IV.D141` |
| `def` | [tau_higgs_mass](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass-l96/) | L96-L98 | defined | — |
| `def` | [higgs_mass_GeV](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-ge-v/) | L101-L102 | defined | — |
| `structure` | [TauYukawaCoupling](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-yukawa-coupling/) | L114-L123 | defined | `IV.D142` |
| `def` | [TauYukawaCoupling.toFloat](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/to-float/) | L126-L127 | defined | — |
| `def` | [yukawa_top](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-top/) | L130-L133 | defined | — |
| `def` | [yukawa_bottom](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-bottom/) | L136-L139 | defined | — |
| `def` | [yukawa_electron](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/yukawa-electron/) | L142-L145 | defined | — |
| `structure` | [EWScale](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/ewscale/) | L157-L164 | defined | `IV.D320` |
| `def` | [ew_scale](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/ew-scale/) | L166-L166 | defined | — |
| `structure` | [HessianConvergence](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-convergence/) | L178-L185 | defined | `IV.L07` |
| `def` | [hessian_eigenvalue_convergence](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-eigenvalue-convergence/) | L187-L187 | defined | — |
| `structure` | [NoFundamentalScalar](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar/) | L203-L212 | defined | `IV.T65` |
| `def` | [no_fundamental_scalar](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar-l214/) | L214-L214 | defined | — |
| `theorem` | [no_hierarchy_problem](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-hierarchy-problem/) | L216-L220 | formalized | — |
| `theorem` | [hessian_one_positive](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-one-positive/) | L229-L233 | formalized | `IV.P74` |
| `theorem` | [higgs_mass_range](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-range/) | L241-L244 | formalized | `IV.P75` |
| `structure` | [GoldstoneAbsorption](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-absorption/) | L258-L271 | defined | `IV.P76` |
| `def` | [goldstone_eaten](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-eaten/) | L273-L273 | defined | — |
| `structure` | [DecayBranching](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching/) | L292-L297 | defined | `IV.P77` |
| `def` | [br_bb](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-bb/) | L299-L299 | defined | — |
| `def` | [br_WW](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-ww/) | L300-L300 | defined | — |
| `def` | [br_gg](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-gg/) | L301-L301 | defined | — |
| `def` | [br_tautau](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-tautau/) | L302-L302 | defined | — |
| `def` | [br_cc](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-cc/) | L303-L303 | defined | — |
| `def` | [br_ZZ](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/br-zz/) | L304-L304 | defined | — |
| `def` | [decay_branching](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching-l307/) | L307-L308 | defined | — |
| `theorem` | [branching_sum_approx](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/branching-sum-approx/) | L311-L313 | formalized | — |
| `def` | [remark_hierarchy_dissolution](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-hierarchy-dissolution/) | L325-L326 | defined | `IV.R35` |
| `def` | [remark_deviation_signatures](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-deviation-signatures/) | L340-L341 | defined | `IV.R36` |
| `eval` | [#eval L347](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l350/) | L350-L350 | computed | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l354/) | L354-L354 | computed | — |
| `eval` | [#eval L355](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l355/) | L355-L355 | computed | — |
| `eval` | [#eval L356](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l356/) | L356-L356 | computed | — |
| `eval` | [#eval L357](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l357/) | L357-L357 | computed | — |
| `eval` | [#eval L358](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l358/) | L358-L358 | computed | — |
| `eval` | [#eval L359](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l359/) | L359-L359 | computed | — |
| `inductive` | [NonOmegaGenerator](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/non-omega-generator/) | L368-L370 | defined | `IV.T150` |
| `theorem` | [higgs_factor_four](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four/) | L374-L375 | formalized | `IV.T150` |
| `theorem` | [higgs_factor_four_lobes](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-lobes/) | L378-L378 | formalized | `IV.T150` |
| `theorem` | [higgs_factor_four_betti](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-betti/) | L384-L385 | formalized | `IV.T150` |
| `def` | [higgs_mass_nlo_formula_n5](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n5/) | L391-L392 | defined | `IV.D348` |
| `def` | [higgs_mass_nlo_formula_n6](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n6/) | L397-L398 | defined | `IV.R399` |
| `def` | [higgs_w_ratio_comparison](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-w-ratio-comparison/) | L404-L405 | defined | `IV.P188` |
| `def` | [remark_omega_self_energy_open](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-omega-self-energy-open/) | L409-L410 | defined | `IV.R399` |
| `eval` | [#eval L413](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l413/) | L413-L413 | computed | — |
| `eval` | [#eval L414](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l414/) | L414-L414 | computed | — |
| `eval` | [#eval L415](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l415/) | L415-L415 | computed | — |
| `eval` | [#eval L416](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l416/) | L416-L416 | computed | — |
| `eval` | [#eval L417](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l417/) | L417-L417 | computed | — |
| `theorem` | [higgs_n6_cf_sum](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-cf-sum/) | L430-L430 | formalized | — |
| `def` | [higgs_n6_formula](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-formula/) | L433-L434 | defined | — |
| `def` | [iota_inv_cf_expansion](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/iota-inv-cf-expansion/) | L438-L438 | defined | — |
| `theorem` | [cf_sum_five_is_not_six](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/cf-sum-five-is-not-six/) | L440-L441 | formalized | — |
| `eval` | [#eval L443](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l443/) | L443-L443 | computed | — |
| `def` | [higgs_n7_formula](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-formula/) | L453-L455 | defined | — |
| `structure` | [HiggsN7](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7/) | L461-L470 | defined | — |
| `def` | [higgs_n7_data](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-data/) | L472-L475 | defined | — |
| `theorem` | [higgs_n7_tau_effective](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-tau-effective/) | L477-L480 | formalized | — |
| `def` | [muon_mass_nnlo_open](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/muon-mass-nnlo-open/) | L491-L493 | defined | — |
| `theorem` | [nnlo_ratio_n7_n5](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/nnlo-ratio-n7-n5/) | L496-L496 | formalized | — |
| `eval` | [#eval L499](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l499/) | L499-L499 | computed | — |
| `eval` | [#eval L500](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l500/) | L500-L500 | computed | — |
| `structure` | [CoherenceFunctionalLevel](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-functional-level/) | L522-L533 | defined | — |
| `def` | [coherence_level_7](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-level-7/) | L535-L538 | defined | — |
| `structure` | [HiggsN7Uniqueness](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness/) | L555-L576 | defined | — |
| `def` | [higgs_n7_uniqueness](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-l578/) | L578-L580 | defined | — |
| `theorem` | [higgs_n7_uniqueness_thm](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness-thm/) | L583-L588 | formalized | — |
| `structure` | [WindowRGPeriod](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-rgperiod/) | L604-L613 | defined | — |
| `def` | [window_rg_period](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-rg-period/) | L615-L616 | defined | — |
| `theorem` | [window_nnlo_period](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-nnlo-period/) | L619-L623 | formalized | — |
| `eval` | [#eval L626](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l626/) | L626-L626 | computed | — |
| `eval` | [#eval L627](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l627/) | L627-L627 | computed | — |
| `eval` | [#eval L628](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l628/) | L628-L628 | computed | — |
| `eval` | [#eval L629](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l629/) | L629-L629 | computed | — |
| `structure` | [HiggsSelfCoupling](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling/) | L641-L656 | defined | `IV.D376` |
| `def` | [higgs_self_coupling](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling-l658/) | L658-L658 | defined | — |
| `theorem` | [higgs_lambda_sub_100ppm](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-sub-100ppm/) | L662-L665 | formalized | `IV.T194` |
| `structure` | [HiggsLambdaFalsification](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification/) | L670-L679 | defined | `IV.P220` |
| `def` | [higgs_lambda_falsification](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification-l681/) | L681-L681 | defined | — |
| `eval` | [#eval L684](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l684/) | L684-L684 | computed | — |
| `eval` | [#eval L685](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l685/) | L685-L685 | computed | — |
| `eval` | [#eval L686](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/eval-l686/) | L686-L688 | computed | — |
