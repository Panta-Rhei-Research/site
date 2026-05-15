---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Particles.BetaDecay",
  "permalink": "/corpus/taulib/docs/book-iv-particles-beta-decay/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Particles.BetaDecay`.",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_slug": "book-iv-particles-beta-decay",
  "book": "BookIV",
  "family": "Particles",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Particles/BetaDecay.lean",
  "sha256": "470c473795e9228895d3d67bd6eadcde78924b5e111e56183dd26d55621ed77d",
  "imports": [
    "TauLib.BookIV.Particles.ThreeGenerations"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Particles.HadronsNuclei",
    "TauLib.Tour.GuidedTour.BookIV"
  ],
  "registry_ids": [
    "IV.D199",
    "IV.D383",
    "IV.P125",
    "IV.P126",
    "IV.P127",
    "IV.P224",
    "IV.R121",
    "IV.R122",
    "IV.R123",
    "IV.R124",
    "IV.R125",
    "IV.R126",
    "IV.R127",
    "IV.T202",
    "IV.T203",
    "IV.T85",
    "IV.T86",
    "IV.T87"
  ],
  "declaration_counts": {
    "structure": 16,
    "def": 17,
    "theorem": 10,
    "eval": 15
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "NeutronParent",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-parent/",
      "source_line_start": 57,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R121"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_as_parent",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-as-parent/",
      "source_line_start": 68,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_products",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/three-products/",
      "source_line_start": 70,
      "source_line_end": 70,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BetaDecayQValue",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/beta-decay-qvalue/",
      "source_line_start": 84,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P125"
      ]
    },
    {
      "kind": "def",
      "name": "beta_decay_q_value",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/beta-decay-q-value/",
      "source_line_start": 97,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "q_value_consistency",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/q-value-consistency/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LifetimeStructural",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/lifetime-structural/",
      "source_line_start": 111,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R122"
      ]
    },
    {
      "kind": "def",
      "name": "lifetime_structural",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/lifetime-structural-l120/",
      "source_line_start": 120,
      "source_line_end": 120,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BohrRadius",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-radius/",
      "source_line_start": 131,
      "source_line_end": 140,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P126"
      ]
    },
    {
      "kind": "def",
      "name": "bohr_radius",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-radius-l142/",
      "source_line_start": 142,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bohr_from_iota",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-from-iota/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HydrogenLevels",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/hydrogen-levels/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T85"
      ]
    },
    {
      "kind": "def",
      "name": "hydrogen_levels",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/hydrogen-levels-l166/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ground_state_energy",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/ground-state-energy/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RydbergConstant",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-constant/",
      "source_line_start": 181,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D199"
      ]
    },
    {
      "kind": "def",
      "name": "rydberg_constant",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-constant-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RydbergPrediction",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-prediction/",
      "source_line_start": 201,
      "source_line_end": 208,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T86"
      ]
    },
    {
      "kind": "def",
      "name": "rydberg_prediction",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-prediction-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rydberg_seven_sig_figs",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-seven-sig-figs/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rydberg_testable",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-testable/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R124"
      ]
    },
    {
      "kind": "structure",
      "name": "SpectralModeSwitching",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/spectral-mode-switching/",
      "source_line_start": 232,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P127"
      ]
    },
    {
      "kind": "def",
      "name": "spectral_mode_switching",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/spectral-mode-switching-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ForbiddenTransitions",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/forbidden-transitions/",
      "source_line_start": 251,
      "source_line_end": 258,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R125"
      ]
    },
    {
      "kind": "def",
      "name": "forbidden_transitions",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/forbidden-transitions-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FineStructureHolonomy",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-holonomy/",
      "source_line_start": 272,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T87"
      ]
    },
    {
      "kind": "def",
      "name": "fine_structure_holonomy",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-holonomy-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fine_structure_fourth_order",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-fourth-order/",
      "source_line_start": 285,
      "source_line_end": 286,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LambShift",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/lamb-shift/",
      "source_line_start": 295,
      "source_line_end": 302,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R126"
      ]
    },
    {
      "kind": "def",
      "name": "lamb_shift_tau",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/lamb-shift-tau/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AllRoadsME",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/all-roads-me/",
      "source_line_start": 319,
      "source_line_end": 326,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R127"
      ]
    },
    {
      "kind": "def",
      "name": "all_roads_m_e",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/all-roads-m-e/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_quantities_depend",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/four-quantities-depend/",
      "source_line_start": 330,
      "source_line_end": 330,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ProtonChargeRadiusNLO",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/proton-charge-radius-nlo/",
      "source_line_start": 339,
      "source_line_end": 354,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T202"
      ]
    },
    {
      "kind": "def",
      "name": "proton_charge_radius_nlo",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/proton-charge-radius-nlo-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_improves_lo",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/nlo-improves-lo/",
      "source_line_start": 358,
      "source_line_end": 360,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutronLifetimeInputs",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-inputs/",
      "source_line_start": 368,
      "source_line_end": 379,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D383"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_lifetime_inputs",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-inputs-l381/",
      "source_line_start": 381,
      "source_line_end": 381,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutronLifetimePrecision",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-precision/",
      "source_line_start": 389,
      "source_line_end": 402,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T203"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_lifetime_precision",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-precision-l404/",
      "source_line_start": 404,
      "source_line_end": 404,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "selects_bottle_value",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/selects-bottle-value/",
      "source_line_start": 406,
      "source_line_end": 407,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CancelledFormBudget",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-budget/",
      "source_line_start": 416,
      "source_line_end": 429,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P224"
      ]
    },
    {
      "kind": "def",
      "name": "cancelled_form_budget",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-budget-l431/",
      "source_line_start": 431,
      "source_line_end": 431,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cancelled_form_improves",
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-improves/",
      "source_line_start": 433,
      "source_line_end": 434,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l440/",
      "source_line_start": 440,
      "source_line_end": 440,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l441/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l442/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l443/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l444/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l445/",
      "source_line_start": 445,
      "source_line_end": 445,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l446/",
      "source_line_start": 446,
      "source_line_end": 446,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l447/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l448/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l449/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l450/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l451/",
      "source_line_start": 451,
      "source_line_end": 451,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l452/",
      "source_line_start": 452,
      "source_line_end": 452,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l453/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l454/",
      "source_line_start": 454,
      "source_line_end": 456,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean",
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
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Particles/BetaDecay.lean`
- SHA-256: `470c473795e9228895d3d67bd6eadcde78924b5e111e56183dd26d55621ed77d`

## Registry Links

- `IV.D199` — Rydberg constant
- `IV.D383` — Neutron Lifetime Input Table (Wave 46)
- `IV.P125` — Beta-decay Q-value
- `IV.P126` — Bohr radius from iota_tau
- `IV.P127` — Spectral transition as mode-switching
- `IV.P224` — Cancelled-Form Error Budget (77 ppm RSS)
- `IV.R121` — Neutron as parent of atomic matter
- `IV.R122` — Structural lifetime estimate
- `IV.R123` — No classical trajectory
- `IV.R124` — A testable prediction
- `IV.R125` — Forbidden transitions
- `IV.R126` — Lamb shift in tau-framework
- `IV.R127` — All roads lead through m_e
- `IV.T202` — Proton Charge Radius NLO at +12 ppm
- `IV.T203` — Neutron Lifetime Precision Prediction
- `IV.T85` — Hydrogen energy levels
- `IV.T86` — Rydberg prediction at 0.025 ppm
- `IV.T87` — Fine structure from holonomy corrections

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Particles.ThreeGenerations`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Particles.HadronsNuclei`
- `TauLib.Tour.GuidedTour.BookIV`

## Declaration Counts

- `def`: 17
- `eval`: 15
- `structure`: 16
- `theorem`: 10

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [NeutronParent](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-parent/) | L57-L66 | type/data schema | type/data schema | `IV.R121` |
| `def` | [neutron_as_parent](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-as-parent/) | L68-L68 | definition | definition | — |
| `theorem` | [three_products](/corpus/taulib/docs/book-iv-particles-beta-decay/three-products/) | L70-L70 | proof obligation | formal proof obligation checked | — |
| `structure` | [BetaDecayQValue](/corpus/taulib/docs/book-iv-particles-beta-decay/beta-decay-qvalue/) | L84-L95 | type/data schema | type/data schema | `IV.P125` |
| `def` | [beta_decay_q_value](/corpus/taulib/docs/book-iv-particles-beta-decay/beta-decay-q-value/) | L97-L97 | definition | definition | — |
| `theorem` | [q_value_consistency](/corpus/taulib/docs/book-iv-particles-beta-decay/q-value-consistency/) | L100-L102 | proof obligation | formal proof obligation checked | — |
| `structure` | [LifetimeStructural](/corpus/taulib/docs/book-iv-particles-beta-decay/lifetime-structural/) | L111-L118 | type/data schema | type/data schema | `IV.R122` |
| `def` | [lifetime_structural](/corpus/taulib/docs/book-iv-particles-beta-decay/lifetime-structural-l120/) | L120-L120 | definition | definition | — |
| `structure` | [BohrRadius](/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-radius/) | L131-L140 | type/data schema | type/data schema | `IV.P126` |
| `def` | [bohr_radius](/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-radius-l142/) | L142-L142 | definition | definition | — |
| `theorem` | [bohr_from_iota](/corpus/taulib/docs/book-iv-particles-beta-decay/bohr-from-iota/) | L144-L144 | proof obligation | formal proof obligation checked | — |
| `structure` | [HydrogenLevels](/corpus/taulib/docs/book-iv-particles-beta-decay/hydrogen-levels/) | L157-L164 | type/data schema | type/data schema | `IV.T85` |
| `def` | [hydrogen_levels](/corpus/taulib/docs/book-iv-particles-beta-decay/hydrogen-levels-l166/) | L166-L166 | definition | definition | — |
| `theorem` | [ground_state_energy](/corpus/taulib/docs/book-iv-particles-beta-decay/ground-state-energy/) | L168-L168 | proof obligation | formal proof obligation checked | — |
| `structure` | [RydbergConstant](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-constant/) | L181-L188 | type/data schema | type/data schema | `IV.D199` |
| `def` | [rydberg_constant](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-constant-l190/) | L190-L190 | definition | definition | — |
| `structure` | [RydbergPrediction](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-prediction/) | L201-L208 | type/data schema | type/data schema | `IV.T86` |
| `def` | [rydberg_prediction](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-prediction-l210/) | L210-L210 | definition | definition | — |
| `theorem` | [rydberg_seven_sig_figs](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-seven-sig-figs/) | L212-L212 | proof obligation | formal proof obligation checked | — |
| `def` | [rydberg_testable](/corpus/taulib/docs/book-iv-particles-beta-decay/rydberg-testable/) | L221-L222 | docstring/data record | docstring/data record | `IV.R124` |
| `structure` | [SpectralModeSwitching](/corpus/taulib/docs/book-iv-particles-beta-decay/spectral-mode-switching/) | L232-L239 | type/data schema | type/data schema | `IV.P127` |
| `def` | [spectral_mode_switching](/corpus/taulib/docs/book-iv-particles-beta-decay/spectral-mode-switching-l241/) | L241-L241 | definition | definition | — |
| `structure` | [ForbiddenTransitions](/corpus/taulib/docs/book-iv-particles-beta-decay/forbidden-transitions/) | L251-L258 | type/data schema | type/data schema | `IV.R125` |
| `def` | [forbidden_transitions](/corpus/taulib/docs/book-iv-particles-beta-decay/forbidden-transitions-l260/) | L260-L260 | definition | definition | — |
| `structure` | [FineStructureHolonomy](/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-holonomy/) | L272-L281 | type/data schema | type/data schema | `IV.T87` |
| `def` | [fine_structure_holonomy](/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-holonomy-l283/) | L283-L283 | definition | definition | — |
| `theorem` | [fine_structure_fourth_order](/corpus/taulib/docs/book-iv-particles-beta-decay/fine-structure-fourth-order/) | L285-L286 | proof obligation | formal proof obligation checked | — |
| `structure` | [LambShift](/corpus/taulib/docs/book-iv-particles-beta-decay/lamb-shift/) | L295-L302 | type/data schema | type/data schema | `IV.R126` |
| `def` | [lamb_shift_tau](/corpus/taulib/docs/book-iv-particles-beta-decay/lamb-shift-tau/) | L304-L304 | definition | definition | — |
| `structure` | [AllRoadsME](/corpus/taulib/docs/book-iv-particles-beta-decay/all-roads-me/) | L319-L326 | type/data schema | type/data schema | `IV.R127` |
| `def` | [all_roads_m_e](/corpus/taulib/docs/book-iv-particles-beta-decay/all-roads-m-e/) | L328-L328 | definition | definition | — |
| `theorem` | [four_quantities_depend](/corpus/taulib/docs/book-iv-particles-beta-decay/four-quantities-depend/) | L330-L330 | proof obligation | formal proof obligation checked | — |
| `structure` | [ProtonChargeRadiusNLO](/corpus/taulib/docs/book-iv-particles-beta-decay/proton-charge-radius-nlo/) | L339-L354 | type/data schema | type/data schema | `IV.T202` |
| `def` | [proton_charge_radius_nlo](/corpus/taulib/docs/book-iv-particles-beta-decay/proton-charge-radius-nlo-l356/) | L356-L356 | definition | definition | — |
| `theorem` | [nlo_improves_lo](/corpus/taulib/docs/book-iv-particles-beta-decay/nlo-improves-lo/) | L358-L360 | proof obligation | formal proof obligation checked | — |
| `structure` | [NeutronLifetimeInputs](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-inputs/) | L368-L379 | type/data schema | type/data schema | `IV.D383` |
| `def` | [neutron_lifetime_inputs](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-inputs-l381/) | L381-L381 | definition | definition | — |
| `structure` | [NeutronLifetimePrecision](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-precision/) | L389-L402 | type/data schema | type/data schema | `IV.T203` |
| `def` | [neutron_lifetime_precision](/corpus/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-precision-l404/) | L404-L404 | definition | definition | — |
| `theorem` | [selects_bottle_value](/corpus/taulib/docs/book-iv-particles-beta-decay/selects-bottle-value/) | L406-L407 | proof obligation | formal proof obligation checked | — |
| `structure` | [CancelledFormBudget](/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-budget/) | L416-L429 | type/data schema | type/data schema | `IV.P224` |
| `def` | [cancelled_form_budget](/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-budget-l431/) | L431-L431 | definition | definition | — |
| `theorem` | [cancelled_form_improves](/corpus/taulib/docs/book-iv-particles-beta-decay/cancelled-form-improves/) | L433-L434 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L440](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l440/) | L440-L440 | computed check | computed check | — |
| `eval` | [#eval L441](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l441/) | L441-L441 | computed check | computed check | — |
| `eval` | [#eval L442](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l442/) | L442-L442 | computed check | computed check | — |
| `eval` | [#eval L443](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l443/) | L443-L443 | computed check | computed check | — |
| `eval` | [#eval L444](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l444/) | L444-L444 | computed check | computed check | — |
| `eval` | [#eval L445](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l445/) | L445-L445 | computed check | computed check | — |
| `eval` | [#eval L446](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l446/) | L446-L446 | computed check | computed check | — |
| `eval` | [#eval L447](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l447/) | L447-L447 | computed check | computed check | — |
| `eval` | [#eval L448](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l448/) | L448-L448 | computed check | computed check | — |
| `eval` | [#eval L449](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l449/) | L449-L449 | computed check | computed check | — |
| `eval` | [#eval L450](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l450/) | L450-L450 | computed check | computed check | — |
| `eval` | [#eval L451](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l451/) | L451-L451 | computed check | computed check | — |
| `eval` | [#eval L452](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l452/) | L452-L452 | computed check | computed check | — |
| `eval` | [#eval L453](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l453/) | L453-L453 | computed check | computed check | — |
| `eval` | [#eval L454](/corpus/taulib/docs/book-iv-particles-beta-decay/eval-l454/) | L454-L456 | computed check | computed check | — |
