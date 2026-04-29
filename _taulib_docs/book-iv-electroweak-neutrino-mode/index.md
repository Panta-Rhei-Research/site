---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_slug": "book-iv-electroweak-neutrino-mode",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/NeutrinoMode.lean",
  "sha256": "763a9ccd27f9d102fb13d0eda030972722be654ef86d64897edc2c06d1f63bbf",
  "imports": [
    "TauLib.BookIV.Electroweak.WeakHolonomy2"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.EWMixing",
    "TauLib.BookIV.Electroweak.MajoranaStructure"
  ],
  "registry_ids": [
    "IV.D124",
    "IV.D125",
    "IV.D126",
    "IV.D127",
    "IV.D343",
    "IV.P66",
    "IV.P67",
    "IV.R395",
    "IV.T58",
    "IV.T59",
    "V.D233",
    "V.D235",
    "V.D236",
    "V.D237",
    "V.P123",
    "V.P127",
    "V.P128",
    "V.P129",
    "V.R372",
    "V.R376",
    "V.R377",
    "V.R378",
    "V.T165",
    "V.T166",
    "V.T173",
    "V.T174",
    "V.T175",
    "V.T176",
    "V.T177",
    "V.T178"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 28,
    "theorem": 30,
    "structure": 10,
    "eval": 31
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "NeutrinoFlavor",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-flavor/",
      "source_line_start": 36,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D125"
      ]
    },
    {
      "kind": "def",
      "name": "all_neutrino_flavors",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/all-neutrino-flavors/",
      "source_line_start": 46,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_flavors",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-flavors/",
      "source_line_start": 49,
      "source_line_end": 49,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutrinoMode",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-mode/",
      "source_line_start": 62,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D124"
      ]
    },
    {
      "kind": "def",
      "name": "nu_e",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-e/",
      "source_line_start": 81,
      "source_line_end": 86,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nu_mu",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-mu/",
      "source_line_start": 91,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nu_tau",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-tau/",
      "source_line_start": 101,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_neutrino_modes",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/all-neutrino-modes/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_modes",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-modes/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassSuppression",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-suppression/",
      "source_line_start": 134,
      "source_line_end": 144,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T58"
      ]
    },
    {
      "kind": "def",
      "name": "mass_suppression_exponent",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-suppression-exponent/",
      "source_line_start": 147,
      "source_line_end": 153,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exponent_factorization",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/exponent-factorization/",
      "source_line_start": 156,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nu_tau_heaviest",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-tau-heaviest/",
      "source_line_start": 160,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_weak_only",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-weak-only/",
      "source_line_start": 173,
      "source_line_end": 177,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T59"
      ]
    },
    {
      "kind": "theorem",
      "name": "mass_hierarchy",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-hierarchy/",
      "source_line_start": 188,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P66"
      ]
    },
    {
      "kind": "theorem",
      "name": "mass_hierarchy_spacing",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-hierarchy-spacing/",
      "source_line_start": 197,
      "source_line_end": 200,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PMNSMatrix",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsmatrix/",
      "source_line_start": 211,
      "source_line_end": 224,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D126"
      ]
    },
    {
      "kind": "def",
      "name": "pmns_matrix",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-matrix/",
      "source_line_start": 227,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pmns_parameters",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-parameters/",
      "source_line_start": 234,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cp_phase_origin",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cp-phase-origin/",
      "source_line_start": 251,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P67"
      ]
    },
    {
      "kind": "theorem",
      "name": "majorana_phases",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-phases/",
      "source_line_start": 259,
      "source_line_end": 260,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutrinoRecurrence",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-recurrence/",
      "source_line_start": 286,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D127"
      ]
    },
    {
      "kind": "def",
      "name": "neutrino_recurrence",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-recurrence-l306/",
      "source_line_start": 306,
      "source_line_end": 311,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recurrence_three_modes",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/recurrence-three-modes/",
      "source_line_start": 314,
      "source_line_end": 315,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recurrence_sigma_equivariant",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/recurrence-sigma-equivariant/",
      "source_line_start": 318,
      "source_line_end": 319,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "non_equal_spacing",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/non-equal-spacing/",
      "source_line_start": 327,
      "source_line_end": 329,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coupling_hierarchy",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/coupling-hierarchy/",
      "source_line_start": 332,
      "source_line_end": 335,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SigmaPolarityMatrix",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-polarity-matrix/",
      "source_line_start": 375,
      "source_line_end": 381,
      "formal_status": "defined",
      "registry_ids": [
        "V.D233"
      ]
    },
    {
      "kind": "def",
      "name": "sprint3_best_fit",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint3-best-fit/",
      "source_line_start": 385,
      "source_line_end": 386,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bestFitExponents",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/best-fit-exponents/",
      "source_line_start": 392,
      "source_line_end": 396,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D343"
      ]
    },
    {
      "kind": "theorem",
      "name": "off_diagonal_zero_is_structural",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/off-diagonal-zero-is-structural/",
      "source_line_start": 401,
      "source_line_end": 401,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_distinct_eigenvalues",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-distinct-eigenvalues/",
      "source_line_start": 408,
      "source_line_end": 409,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T165"
      ]
    },
    {
      "kind": "def",
      "name": "cosmological_bound",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cosmological-bound/",
      "source_line_start": 413,
      "source_line_end": 415,
      "formal_status": "defined",
      "registry_ids": [
        "V.T166"
      ]
    },
    {
      "kind": "def",
      "name": "remark_normal_ordering",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/remark-normal-ordering/",
      "source_line_start": 423,
      "source_line_end": 426,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R395"
      ]
    },
    {
      "kind": "def",
      "name": "pmns_angles",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angles/",
      "source_line_start": 435,
      "source_line_end": 438,
      "formal_status": "defined",
      "registry_ids": [
        "V.P123"
      ]
    },
    {
      "kind": "structure",
      "name": "PMNSAnglePrediction",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsangle-prediction/",
      "source_line_start": 444,
      "source_line_end": 453,
      "formal_status": "defined",
      "registry_ids": [
        "V.P123"
      ]
    },
    {
      "kind": "def",
      "name": "pmns_angle_prediction",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angle-prediction/",
      "source_line_start": 456,
      "source_line_end": 457,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pmns_angle_prediction_conj",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angle-prediction-conj/",
      "source_line_start": 460,
      "source_line_end": 464,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P123"
      ]
    },
    {
      "kind": "def",
      "name": "theta13_bare_sigma_deg",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/theta13-bare-sigma-deg/",
      "source_line_start": 467,
      "source_line_end": 467,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l469/",
      "source_line_start": 469,
      "source_line_end": 469,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l470/",
      "source_line_start": 470,
      "source_line_end": 470,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l471/",
      "source_line_start": 471,
      "source_line_end": 471,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "majorana_structure",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-structure/",
      "source_line_start": 482,
      "source_line_end": 486,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_sprint4",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/remark-sprint4/",
      "source_line_start": 491,
      "source_line_end": 495,
      "formal_status": "defined",
      "registry_ids": [
        "V.R372"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l501/",
      "source_line_start": 501,
      "source_line_end": 501,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l502/",
      "source_line_start": 502,
      "source_line_end": 502,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l503/",
      "source_line_start": 503,
      "source_line_end": 503,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neutrino_winding_strategy",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-winding-strategy/",
      "source_line_start": 515,
      "source_line_end": 518,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_one_param_family_conjecture",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-one-param-family-conjecture/",
      "source_line_start": 524,
      "source_line_end": 524,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pmns_mixing_angles",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-mixing-angles/",
      "source_line_start": 538,
      "source_line_end": 541,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "normal_mass_ordering_from_sigma_polarity",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/normal-mass-ordering-from-sigma-polarity/",
      "source_line_start": 553,
      "source_line_end": 553,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sprint4a_oqc3_status",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint4a-oqc3-status/",
      "source_line_start": 568,
      "source_line_end": 571,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l577/",
      "source_line_start": 577,
      "source_line_end": 577,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l578/",
      "source_line_start": 578,
      "source_line_end": 578,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l579/",
      "source_line_start": 579,
      "source_line_end": 579,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neutrino_cf_asymmetry",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-cf-asymmetry/",
      "source_line_start": 590,
      "source_line_end": 592,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SigmaExponentGrid",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-grid/",
      "source_line_start": 597,
      "source_line_end": 604,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sigma_grid_data",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-grid-data/",
      "source_line_start": 606,
      "source_line_end": 606,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma_exponent_grid_optimum",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-grid-optimum/",
      "source_line_start": 608,
      "source_line_end": 612,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MajoranaCPPhase",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cpphase/",
      "source_line_start": 619,
      "source_line_end": 626,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "majorana_cp_data",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cp-data/",
      "source_line_start": 628,
      "source_line_end": 628,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "majorana_cp_phases_from_sigma",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cp-phases-from-sigma/",
      "source_line_start": 630,
      "source_line_end": 634,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SigmaExponentAsymmetry",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry/",
      "source_line_start": 639,
      "source_line_end": 648,
      "formal_status": "defined",
      "registry_ids": [
        "V.P128"
      ]
    },
    {
      "kind": "def",
      "name": "sigma_exponent_asymmetry_data",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry-data/",
      "source_line_start": 651,
      "source_line_end": 651,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma_exponent_asymmetry",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry-l654/",
      "source_line_start": 654,
      "source_line_end": 659,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P128"
      ]
    },
    {
      "kind": "theorem",
      "name": "cf_asymmetry_int_check",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cf-asymmetry-int-check/",
      "source_line_start": 662,
      "source_line_end": 662,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l664/",
      "source_line_start": 664,
      "source_line_end": 664,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l665/",
      "source_line_start": 665,
      "source_line_end": 665,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sprint5a_oqc3_status",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint5a-oqc3-status/",
      "source_line_start": 668,
      "source_line_end": 670,
      "formal_status": "defined",
      "registry_ids": [
        "V.R377"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l673/",
      "source_line_start": 673,
      "source_line_end": 673,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l674/",
      "source_line_start": 674,
      "source_line_end": 674,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neutrino_exponent_43_ratio",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-exponent-43-ratio/",
      "source_line_start": 684,
      "source_line_end": 686,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_43_counting",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-43-counting/",
      "source_line_start": 689,
      "source_line_end": 690,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T178"
      ]
    },
    {
      "kind": "theorem",
      "name": "neutrino_span_check",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-span-check/",
      "source_line_start": 692,
      "source_line_end": 692,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_ratio_43",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-ratio-43/",
      "source_line_start": 694,
      "source_line_end": 694,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Neutrino87Candidate",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino87-candidate/",
      "source_line_start": 701,
      "source_line_end": 712,
      "formal_status": "defined",
      "registry_ids": [
        "V.T177"
      ]
    },
    {
      "kind": "def",
      "name": "neutrino_87_data",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-data/",
      "source_line_start": 715,
      "source_line_end": 715,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_87_candidate",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-candidate/",
      "source_line_start": 718,
      "source_line_end": 724,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T177"
      ]
    },
    {
      "kind": "theorem",
      "name": "neutrino_87_cross_ratio",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-cross-ratio/",
      "source_line_start": 727,
      "source_line_end": 727,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_87_span",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-span/",
      "source_line_start": 730,
      "source_line_end": 730,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_n7_scan",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-n7-scan/",
      "source_line_start": 736,
      "source_line_end": 736,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sprint6a_oqc3_status",
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint6a-oqc3-status/",
      "source_line_start": 739,
      "source_line_end": 742,
      "formal_status": "defined",
      "registry_ids": [
        "V.R378"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l745/",
      "source_line_start": 745,
      "source_line_end": 745,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l746/",
      "source_line_start": 746,
      "source_line_end": 748,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/NeutrinoMode.lean`
- SHA-256: `763a9ccd27f9d102fb13d0eda030972722be654ef86d64897edc2c06d1f63bbf`

## Registry Links

- `IV.D124` — Neutrino as Time-Eigenmode
- `IV.D125` — Neutrino Flavor Eigenstates
- `IV.D126` — PMNS Matrix
- `IV.D127` — τ-Hypercharge
- `IV.D343` — Neutrino Exponent Best-Fit
- `IV.P66` — Mass Eigenvalue Ratios
- `IV.P67` — CP Violation from Sigma-Polarity
- `IV.R395` — Normal Ordering from sigma-Structure
- `IV.T58` — Spectral Gap Exponent
- `IV.T59` — Neutrino Interaction Channels
- `V.D233` — sigma-Polarity Neutrino Mass Matrix
- `V.D235` — Neutrino Exponent Derivation: Torus Winding Strategy
- `V.D236` — Neutrino CF-Asymmetry: Grid-Optimal Exponent Offsets from sigma-Polarity Structure
- `V.D237` — Neutrino Exponent 4/3 Ratio: Lemniscate Counting
- `V.P123` — PMNS Mixing Angle Prediction
- `V.P127` — Normal Mass Ordering from sigma-Polarity Structure
- `V.P128` — Asymmetry in sigma-Exponents: Delta_pq - Delta_pr approx 2/13 (CF-structural candidate)
- `V.P129` — Neutrino Span=2=|lobes|; Ratio=4/3 from n=7 Decomposition
- `V.R372` — Sprint 4 Findings and OQ-C3 Status
- `V.R376` — OQ-C3 Status after Sprint 4A: Asymmetry is the Open Question
- `V.R377` — OQ-C3 Status after Sprint 5A: CF Candidate Fails; Grid Optimum Found
- `V.R378` — OQ-C3 Status after Sprint 6A: 4/3 Hypothesis
- `V.T165` — Mass Eigenvalue Ratio Formula
- `V.T166` — Cosmological Bound Satisfaction
- `V.T173` — One-Parameter Neutrino Family: Scale-Invariant Result 39.45
- `V.T174` — PMNS Shared Eigenvector Structure: Identity from sigma-Polarity
- `V.T175` — Best sigma-Matrix Exponent Pair from Grid Scan: (Delta_pq=1.16, Delta_pr=0.87) at +7 ppm
- `V.T176` — Majorana CP Phases from sigma=C_tau Constraint: phi_2 = 0
- `V.T177` — (8/7, 6/7) Candidate: Neutrino Mass Ratio from Lemniscate n=7
- `V.T178` — Structural Derivation: Δpq/Δpr = 4/3 from Lemniscate Counting

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.WeakHolonomy2`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.EWMixing`
- `TauLib.BookIV.Electroweak.MajoranaStructure`

## Declaration Counts

- `def`: 28
- `eval`: 31
- `inductive`: 1
- `structure`: 10
- `theorem`: 30

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [NeutrinoFlavor](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-flavor/) | L36-L43 | defined | `IV.D125` |
| `def` | [all_neutrino_flavors](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/all-neutrino-flavors/) | L46-L47 | defined | — |
| `theorem` | [three_flavors](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-flavors/) | L49-L49 | formalized | — |
| `structure` | [NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-mode/) | L62-L76 | defined | `IV.D124` |
| `def` | [nu_e](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-e/) | L81-L86 | defined | — |
| `def` | [nu_mu](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-mu/) | L91-L96 | defined | — |
| `def` | [nu_tau](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-tau/) | L101-L106 | defined | — |
| `def` | [all_neutrino_modes](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/all-neutrino-modes/) | L109-L109 | defined | — |
| `theorem` | [three_modes](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-modes/) | L111-L111 | formalized | — |
| `structure` | [MassSuppression](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-suppression/) | L134-L144 | defined | `IV.T58` |
| `def` | [mass_suppression_exponent](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-suppression-exponent/) | L147-L153 | defined | — |
| `theorem` | [exponent_factorization](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/exponent-factorization/) | L156-L157 | formalized | — |
| `theorem` | [nu_tau_heaviest](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/nu-tau-heaviest/) | L160-L163 | formalized | — |
| `theorem` | [neutrino_weak_only](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-weak-only/) | L173-L177 | formalized | `IV.T59` |
| `theorem` | [mass_hierarchy](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-hierarchy/) | L188-L191 | formalized | `IV.P66` |
| `theorem` | [mass_hierarchy_spacing](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-hierarchy-spacing/) | L197-L200 | formalized | — |
| `structure` | [PMNSMatrix](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsmatrix/) | L211-L224 | defined | `IV.D126` |
| `def` | [pmns_matrix](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-matrix/) | L227-L231 | defined | — |
| `theorem` | [pmns_parameters](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-parameters/) | L234-L236 | formalized | — |
| `theorem` | [cp_phase_origin](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cp-phase-origin/) | L251-L255 | formalized | `IV.P67` |
| `theorem` | [majorana_phases](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-phases/) | L259-L260 | formalized | — |
| `structure` | [NeutrinoRecurrence](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-recurrence/) | L286-L299 | defined | `IV.D127` |
| `def` | [neutrino_recurrence](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-recurrence-l306/) | L306-L311 | defined | — |
| `theorem` | [recurrence_three_modes](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/recurrence-three-modes/) | L314-L315 | formalized | — |
| `theorem` | [recurrence_sigma_equivariant](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/recurrence-sigma-equivariant/) | L318-L319 | formalized | — |
| `theorem` | [non_equal_spacing](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/non-equal-spacing/) | L327-L329 | formalized | — |
| `theorem` | [coupling_hierarchy](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/coupling-hierarchy/) | L332-L335 | formalized | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l343/) | L343-L343 | computed | — |
| `eval` | [#eval L344](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l350/) | L350-L350 | computed | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l354/) | L354-L354 | computed | — |
| `eval` | [#eval L355](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l355/) | L355-L355 | computed | — |
| `eval` | [#eval L356](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l356/) | L356-L356 | computed | — |
| `structure` | [SigmaPolarityMatrix](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-polarity-matrix/) | L375-L381 | defined | `V.D233` |
| `def` | [sprint3_best_fit](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint3-best-fit/) | L385-L386 | defined | — |
| `def` | [bestFitExponents](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/best-fit-exponents/) | L392-L396 | defined | `IV.D343` |
| `theorem` | [off_diagonal_zero_is_structural](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/off-diagonal-zero-is-structural/) | L401-L401 | formalized | — |
| `theorem` | [three_distinct_eigenvalues](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-distinct-eigenvalues/) | L408-L409 | formalized | `V.T165` |
| `def` | [cosmological_bound](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cosmological-bound/) | L413-L415 | defined | `V.T166` |
| `def` | [remark_normal_ordering](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/remark-normal-ordering/) | L423-L426 | defined | `IV.R395` |
| `def` | [pmns_angles](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angles/) | L435-L438 | defined | `V.P123` |
| `structure` | [PMNSAnglePrediction](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsangle-prediction/) | L444-L453 | defined | `V.P123` |
| `def` | [pmns_angle_prediction](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angle-prediction/) | L456-L457 | defined | — |
| `theorem` | [pmns_angle_prediction_conj](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angle-prediction-conj/) | L460-L464 | formalized | `V.P123` |
| `def` | [theta13_bare_sigma_deg](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/theta13-bare-sigma-deg/) | L467-L467 | defined | — |
| `eval` | [#eval L469](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l469/) | L469-L469 | computed | — |
| `eval` | [#eval L470](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l470/) | L470-L470 | computed | — |
| `eval` | [#eval L471](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l471/) | L471-L471 | computed | — |
| `def` | [majorana_structure](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-structure/) | L482-L486 | defined | — |
| `def` | [remark_sprint4](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/remark-sprint4/) | L491-L495 | defined | `V.R372` |
| `eval` | [#eval L501](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l501/) | L501-L501 | computed | — |
| `eval` | [#eval L502](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l502/) | L502-L502 | computed | — |
| `eval` | [#eval L503](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l503/) | L503-L503 | computed | — |
| `def` | [neutrino_winding_strategy](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-winding-strategy/) | L515-L518 | defined | — |
| `theorem` | [neutrino_one_param_family_conjecture](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-one-param-family-conjecture/) | L524-L524 | formalized | — |
| `def` | [pmns_mixing_angles](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-mixing-angles/) | L538-L541 | defined | — |
| `theorem` | [normal_mass_ordering_from_sigma_polarity](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/normal-mass-ordering-from-sigma-polarity/) | L553-L553 | formalized | — |
| `def` | [sprint4a_oqc3_status](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint4a-oqc3-status/) | L568-L571 | defined | — |
| `eval` | [#eval L577](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l577/) | L577-L577 | computed | — |
| `eval` | [#eval L578](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l578/) | L578-L578 | computed | — |
| `eval` | [#eval L579](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l579/) | L579-L579 | computed | — |
| `def` | [neutrino_cf_asymmetry](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-cf-asymmetry/) | L590-L592 | defined | — |
| `structure` | [SigmaExponentGrid](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-grid/) | L597-L604 | defined | — |
| `def` | [sigma_grid_data](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-grid-data/) | L606-L606 | defined | — |
| `theorem` | [sigma_exponent_grid_optimum](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-grid-optimum/) | L608-L612 | formalized | — |
| `structure` | [MajoranaCPPhase](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cpphase/) | L619-L626 | defined | — |
| `def` | [majorana_cp_data](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cp-data/) | L628-L628 | defined | — |
| `theorem` | [majorana_cp_phases_from_sigma](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cp-phases-from-sigma/) | L630-L634 | formalized | — |
| `structure` | [SigmaExponentAsymmetry](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry/) | L639-L648 | defined | `V.P128` |
| `def` | [sigma_exponent_asymmetry_data](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry-data/) | L651-L651 | defined | — |
| `theorem` | [sigma_exponent_asymmetry](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry-l654/) | L654-L659 | formalized | `V.P128` |
| `theorem` | [cf_asymmetry_int_check](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cf-asymmetry-int-check/) | L662-L662 | formalized | — |
| `eval` | [#eval L664](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l664/) | L664-L664 | computed | — |
| `eval` | [#eval L665](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l665/) | L665-L665 | computed | — |
| `def` | [sprint5a_oqc3_status](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint5a-oqc3-status/) | L668-L670 | defined | `V.R377` |
| `eval` | [#eval L673](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l673/) | L673-L673 | computed | — |
| `eval` | [#eval L674](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l674/) | L674-L674 | computed | — |
| `def` | [neutrino_exponent_43_ratio](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-exponent-43-ratio/) | L684-L686 | defined | — |
| `theorem` | [neutrino_43_counting](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-43-counting/) | L689-L690 | formalized | `V.T178` |
| `theorem` | [neutrino_span_check](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-span-check/) | L692-L692 | formalized | — |
| `theorem` | [neutrino_ratio_43](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-ratio-43/) | L694-L694 | formalized | — |
| `structure` | [Neutrino87Candidate](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino87-candidate/) | L701-L712 | defined | `V.T177` |
| `def` | [neutrino_87_data](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-data/) | L715-L715 | defined | — |
| `theorem` | [neutrino_87_candidate](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-candidate/) | L718-L724 | formalized | `V.T177` |
| `theorem` | [neutrino_87_cross_ratio](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-cross-ratio/) | L727-L727 | formalized | — |
| `theorem` | [neutrino_87_span](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-span/) | L730-L730 | formalized | — |
| `theorem` | [neutrino_n7_scan](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-n7-scan/) | L736-L736 | formalized | — |
| `def` | [sprint6a_oqc3_status](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint6a-oqc3-status/) | L739-L742 | defined | `V.R378` |
| `eval` | [#eval L745](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l745/) | L745-L745 | computed | — |
| `eval` | [#eval L746](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/eval-l746/) | L746-L748 | computed | — |
