---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_slug": "book-v-astrophysics-h0-tension-lcdm",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/H0TensionLCDM.lean",
  "sha256": "7867dc72679d74f8a76a065634d81d0b4ed4f11dea3ec4d5aadbf5a056f1c94e",
  "imports": [
    "TauLib.BookV.Astrophysics.SectorExhaustion"
  ],
  "imported_by": [
    "TauLib.BookV"
  ],
  "registry_ids": [
    "V.D148",
    "V.D149",
    "V.D150",
    "V.D151",
    "V.D295",
    "V.D296",
    "V.D297",
    "V.D298",
    "V.D319",
    "V.D324",
    "V.D330",
    "V.P160",
    "V.P161",
    "V.P162",
    "V.P178",
    "V.P182",
    "V.P88",
    "V.P89",
    "V.R205",
    "V.R206",
    "V.R207",
    "V.R208",
    "V.R419",
    "V.R420",
    "V.R421",
    "V.R453",
    "V.T101",
    "V.T102",
    "V.T235",
    "V.T236",
    "V.T237",
    "V.T238",
    "V.T259",
    "V.T263",
    "V.T266"
  ],
  "declaration_counts": {
    "inductive": 3,
    "def": 17,
    "structure": 12,
    "theorem": 23,
    "eval": 21
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "H0Method",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-method/",
      "source_line_start": 74,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "H0Method.isEarlyTime",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/is-early-time/",
      "source_line_start": 90,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "H0MeasurementData",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-measurement-data/",
      "source_line_start": 97,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": [
        "V.D148"
      ]
    },
    {
      "kind": "def",
      "name": "planck_h0",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/planck-h0/",
      "source_line_start": 111,
      "source_line_end": 116,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "shoes_h0",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/shoes-h0/",
      "source_line_start": 119,
      "source_line_end": 124,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "H0TensionType",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-type/",
      "source_line_start": 131,
      "source_line_end": 140,
      "formal_status": "defined",
      "registry_ids": [
        "V.D149"
      ]
    },
    {
      "kind": "def",
      "name": "h0_tension_magnitude",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-magnitude/",
      "source_line_start": 147,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h0_tension_positive",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-positive/",
      "source_line_start": 150,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h0_tension_artifact",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-artifact/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T101"
      ]
    },
    {
      "kind": "theorem",
      "name": "early_late_depth",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/early-late-depth/",
      "source_line_start": 178,
      "source_line_end": 180,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P88"
      ]
    },
    {
      "kind": "inductive",
      "name": "LCDMLimitation",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/lcdmlimitation/",
      "source_line_start": 188,
      "source_line_end": 201,
      "formal_status": "defined",
      "registry_ids": [
        "V.D150"
      ]
    },
    {
      "kind": "theorem",
      "name": "lcdm_limitations_complete",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/lcdm-limitations-complete/",
      "source_line_start": 204,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauResolutionData",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-resolution-data/",
      "source_line_start": 216,
      "source_line_end": 223,
      "formal_status": "defined",
      "registry_ids": [
        "V.D151"
      ]
    },
    {
      "kind": "def",
      "name": "h0_resolution",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-resolution/",
      "source_line_start": 226,
      "source_line_end": 229,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "de_resolution",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/de-resolution/",
      "source_line_start": 232,
      "source_line_end": 235,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cosmo_const_boundary",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cosmo-const-boundary/",
      "source_line_start": 248,
      "source_line_end": 250,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P89"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_lambda_fine_tuning",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-lambda-fine-tuning/",
      "source_line_start": 265,
      "source_line_end": 267,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T102"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "registry_ids": [
        "V.R205",
        "V.R206",
        "V.R207",
        "V.R208"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CPLMapping",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cplmapping/",
      "source_line_start": 314,
      "source_line_end": 327,
      "formal_status": "defined",
      "registry_ids": [
        "V.D295"
      ]
    },
    {
      "kind": "structure",
      "name": "NoPhantomCrossing",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-crossing/",
      "source_line_start": 332,
      "source_line_end": 339,
      "formal_status": "defined",
      "registry_ids": [
        "V.T235"
      ]
    },
    {
      "kind": "def",
      "name": "cpl_canonical",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cpl-canonical/",
      "source_line_start": 342,
      "source_line_end": 345,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_phantom_canonical",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-canonical/",
      "source_line_start": 348,
      "source_line_end": 351,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_phantom_crossing",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-crossing-l354/",
      "source_line_start": 354,
      "source_line_end": 355,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_closer_to_desi",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-closer-to-desi/",
      "source_line_start": 358,
      "source_line_end": 360,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P160"
      ]
    },
    {
      "kind": "structure",
      "name": "HolonomySuppression",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/holonomy-suppression/",
      "source_line_start": 372,
      "source_line_end": 379,
      "formal_status": "defined",
      "registry_ids": [
        "V.D296"
      ]
    },
    {
      "kind": "structure",
      "name": "Sigma8TauNative",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-tau-native/",
      "source_line_start": 384,
      "source_line_end": 397,
      "formal_status": "defined",
      "registry_ids": [
        "V.D297"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_supp_canonical",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/holonomy-supp-canonical/",
      "source_line_start": 400,
      "source_line_end": 403,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sigma8_canonical",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-canonical/",
      "source_line_start": 406,
      "source_line_end": 409,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma8_suppression_theorem",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-suppression-theorem/",
      "source_line_start": 412,
      "source_line_end": 414,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T236"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_wl_aligned",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-wl-aligned/",
      "source_line_start": 417,
      "source_line_end": 419,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P161"
      ]
    },
    {
      "kind": "structure",
      "name": "TauGrowthFactor",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-growth-factor/",
      "source_line_start": 431,
      "source_line_end": 444,
      "formal_status": "defined",
      "registry_ids": [
        "V.D298"
      ]
    },
    {
      "kind": "structure",
      "name": "GrowthIndex",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index/",
      "source_line_start": 447,
      "source_line_end": 454,
      "formal_status": "defined",
      "registry_ids": [
        "V.T238"
      ]
    },
    {
      "kind": "def",
      "name": "growth_z03",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-z03/",
      "source_line_start": 457,
      "source_line_end": 463,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "growth_z10",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-z10/",
      "source_line_start": 466,
      "source_line_end": 472,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "growth_index_canonical",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index-canonical/",
      "source_line_start": 475,
      "source_line_end": 477,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "growth_below_lcdm_z03",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-below-lcdm-z03/",
      "source_line_start": 480,
      "source_line_end": 482,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T237"
      ]
    },
    {
      "kind": "theorem",
      "name": "growth_index_departure",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index-departure/",
      "source_line_start": 485,
      "source_line_end": 487,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T238"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l492/",
      "source_line_start": 492,
      "source_line_end": 492,
      "formal_status": "computed",
      "registry_ids": [
        "V.P162",
        "V.R421"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l493/",
      "source_line_start": 493,
      "source_line_end": 493,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l494/",
      "source_line_start": 494,
      "source_line_end": 494,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l495/",
      "source_line_start": 495,
      "source_line_end": 495,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l496/",
      "source_line_start": 496,
      "source_line_end": 496,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DESISigma8Falsification",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desisigma8-falsification/",
      "source_line_start": 505,
      "source_line_end": 514,
      "formal_status": "defined",
      "registry_ids": [
        "V.R453"
      ]
    },
    {
      "kind": "def",
      "name": "desi_sigma8_data",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desi-sigma8-data/",
      "source_line_start": 516,
      "source_line_end": 516,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "desi_sigma8_detectable",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desi-sigma8-detectable/",
      "source_line_start": 519,
      "source_line_end": 522,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l525/",
      "source_line_start": 525,
      "source_line_end": 525,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l526/",
      "source_line_start": 526,
      "source_line_end": 526,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HubbleDerivationChain",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-derivation-chain/",
      "source_line_start": 536,
      "source_line_end": 553,
      "formal_status": "defined",
      "registry_ids": [
        "V.D319"
      ]
    },
    {
      "kind": "def",
      "name": "hubble_derivation_data",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-derivation-data/",
      "source_line_start": 555,
      "source_line_end": 555,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "hubble_uniqueness",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-uniqueness/",
      "source_line_start": 558,
      "source_line_end": 561,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T259"
      ]
    },
    {
      "kind": "theorem",
      "name": "hubble_self_consistency",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-self-consistency/",
      "source_line_start": 566,
      "source_line_end": 569,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P178"
      ]
    },
    {
      "kind": "theorem",
      "name": "hubble_sub_permille",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-sub-permille/",
      "source_line_start": 572,
      "source_line_end": 574,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l577/",
      "source_line_start": 577,
      "source_line_end": 577,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l578/",
      "source_line_start": 578,
      "source_line_end": 578,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l579/",
      "source_line_start": 579,
      "source_line_end": 579,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "S8TensionResolution",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-tension-resolution/",
      "source_line_start": 589,
      "source_line_end": 612,
      "formal_status": "defined",
      "registry_ids": [
        "V.D324"
      ]
    },
    {
      "kind": "def",
      "name": "s8_resolution_data",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-resolution-data/",
      "source_line_start": 614,
      "source_line_end": 614,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s8_between_cmb_and_wl",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-between-cmb-and-wl/",
      "source_line_start": 617,
      "source_line_end": 620,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T263"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_within_1sigma_deskids",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-within-1sigma-deskids/",
      "source_line_start": 623,
      "source_line_end": 626,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P182"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_zero_params",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-zero-params/",
      "source_line_start": 629,
      "source_line_end": 631,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l634/",
      "source_line_start": 634,
      "source_line_end": 634,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l635/",
      "source_line_start": 635,
      "source_line_end": 635,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l636/",
      "source_line_start": 636,
      "source_line_end": 636,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "S8NNLO",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo/",
      "source_line_start": 647,
      "source_line_end": 672,
      "formal_status": "defined",
      "registry_ids": [
        "V.D330"
      ]
    },
    {
      "kind": "def",
      "name": "s8_nnlo_data",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-data/",
      "source_line_start": 674,
      "source_line_end": 674,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s8_nnlo_within_kids",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-within-kids/",
      "source_line_start": 678,
      "source_line_end": 681,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T266"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_nnlo_within_hsc",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-within-hsc/",
      "source_line_start": 685,
      "source_line_end": 688,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T266"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_nnlo_below_nlo",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-below-nlo/",
      "source_line_start": 691,
      "source_line_end": 693,
      "formal_status": "formalized",
      "registry_ids": [
        "V.D330"
      ]
    },
    {
      "kind": "theorem",
      "name": "s8_nnlo_zero_params",
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-zero-params/",
      "source_line_start": 696,
      "source_line_end": 698,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l701/",
      "source_line_start": 701,
      "source_line_end": 701,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l702/",
      "source_line_start": 702,
      "source_line_end": 702,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l703/",
      "source_line_start": 703,
      "source_line_end": 705,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/H0TensionLCDM.lean`
- SHA-256: `7867dc72679d74f8a76a065634d81d0b4ed4f11dea3ec4d5aadbf5a056f1c94e`

## Registry Links

- `V.D148` — Orbit-Depth-Dependent Readout
- `V.D149` — Depth-Projected Hubble Parameter
- `V.D150` — Category Error (LCDM)
- `V.D151` — Readout Projection Table
- `V.D295` — CPL Mapping of τ-EoS
- `V.D296` — Holonomy Suppression Factor
- `V.D297` — σ₈ τ-Native
- `V.D298` — τ-Native Growth Factor
- `V.D319` — Hubble Derivation Chain
- `V.D324` — S₈ NLO
- `V.D330` — S₈ NNLO Density-Regime Value
- `V.P160` — DESI Comparison
- `V.P161` — S₈ Tension Resolution
- `V.P162` — f·σ₈ Comparison Table
- `V.P178` — Hubble Self-Consistency Check
- `V.P182` — Lensing Consistency
- `V.P88` — Depth-Hubble Monotonicity
- `V.P89` — Sigma8 as Defect Amplitude
- `V.R205` — Both Measurements Correct
- `V.R206` — Correct Parameters Wrong Ontology
- `V.R207` — What Would Reopen the Case
- `V.R208` — From Part V to Part VI
- `V.R419` — DESI DR2 Confrontation
- `V.R420` — Weak Lensing Comparison
- `V.R421` — RSD Data Comparison
- `V.R453` — DESI σ₈ Falsification Window
- `V.T101` — H0 Tension Resolution
- `V.T102` — Dark Sector Closure
- `V.T235` — No Phantom Crossing Theorem
- `V.T236` — σ₈ Suppression Theorem
- `V.T237` — Growth Equation with τ-EoS
- `V.T238` — Growth Index Theorem
- `V.T259` — Uniqueness of Hubble Formula
- `V.T263` — S₈ Tension Resolution
- `V.T266` — S₈ NNLO Consistent with KiDS and HSC

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.SectorExhaustion`

## Imported By

- `TauLib.BookV`

## Declaration Counts

- `def`: 17
- `eval`: 21
- `inductive`: 3
- `structure`: 12
- `theorem`: 23

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [H0Method](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-method/) | L74-L87 | defined | — |
| `def` | [H0Method.isEarlyTime](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/is-early-time/) | L90-L93 | defined | — |
| `structure` | [H0MeasurementData](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-measurement-data/) | L97-L108 | defined | `V.D148` |
| `def` | [planck_h0](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/planck-h0/) | L111-L116 | defined | — |
| `def` | [shoes_h0](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/shoes-h0/) | L119-L124 | defined | — |
| `inductive` | [H0TensionType](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-type/) | L131-L140 | defined | `V.D149` |
| `def` | [h0_tension_magnitude](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-magnitude/) | L147-L147 | defined | — |
| `theorem` | [h0_tension_positive](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-positive/) | L150-L151 | formalized | — |
| `theorem` | [h0_tension_artifact](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-artifact/) | L163-L165 | formalized | `V.T101` |
| `theorem` | [early_late_depth](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/early-late-depth/) | L178-L180 | formalized | `V.P88` |
| `inductive` | [LCDMLimitation](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/lcdmlimitation/) | L188-L201 | defined | `V.D150` |
| `theorem` | [lcdm_limitations_complete](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/lcdm-limitations-complete/) | L204-L208 | formalized | — |
| `structure` | [TauResolutionData](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-resolution-data/) | L216-L223 | defined | `V.D151` |
| `def` | [h0_resolution](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-resolution/) | L226-L229 | defined | — |
| `def` | [de_resolution](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/de-resolution/) | L232-L235 | defined | — |
| `theorem` | [cosmo_const_boundary](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cosmo-const-boundary/) | L248-L250 | formalized | `V.P89` |
| `theorem` | [no_lambda_fine_tuning](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-lambda-fine-tuning/) | L265-L267 | formalized | `V.T102` |
| `eval` | [#eval L298](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l298/) | L298-L298 | computed | `V.R205`, `V.R206`, `V.R207`, `V.R208` |
| `eval` | [#eval L299](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l299/) | L299-L299 | computed | — |
| `eval` | [#eval L300](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l300/) | L300-L300 | computed | — |
| `eval` | [#eval L301](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l301/) | L301-L301 | computed | — |
| `eval` | [#eval L302](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l302/) | L302-L302 | computed | — |
| `structure` | [CPLMapping](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cplmapping/) | L314-L327 | defined | `V.D295` |
| `structure` | [NoPhantomCrossing](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-crossing/) | L332-L339 | defined | `V.T235` |
| `def` | [cpl_canonical](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cpl-canonical/) | L342-L345 | defined | — |
| `def` | [no_phantom_canonical](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-canonical/) | L348-L351 | defined | — |
| `theorem` | [no_phantom_crossing](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-crossing-l354/) | L354-L355 | formalized | — |
| `theorem` | [tau_closer_to_desi](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-closer-to-desi/) | L358-L360 | formalized | `V.P160` |
| `structure` | [HolonomySuppression](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/holonomy-suppression/) | L372-L379 | defined | `V.D296` |
| `structure` | [Sigma8TauNative](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-tau-native/) | L384-L397 | defined | `V.D297` |
| `def` | [holonomy_supp_canonical](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/holonomy-supp-canonical/) | L400-L403 | defined | — |
| `def` | [sigma8_canonical](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-canonical/) | L406-L409 | defined | — |
| `theorem` | [sigma8_suppression_theorem](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-suppression-theorem/) | L412-L414 | formalized | `V.T236` |
| `theorem` | [s8_wl_aligned](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-wl-aligned/) | L417-L419 | formalized | `V.P161` |
| `structure` | [TauGrowthFactor](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-growth-factor/) | L431-L444 | defined | `V.D298` |
| `structure` | [GrowthIndex](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index/) | L447-L454 | defined | `V.T238` |
| `def` | [growth_z03](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-z03/) | L457-L463 | defined | — |
| `def` | [growth_z10](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-z10/) | L466-L472 | defined | — |
| `def` | [growth_index_canonical](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index-canonical/) | L475-L477 | defined | — |
| `theorem` | [growth_below_lcdm_z03](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-below-lcdm-z03/) | L480-L482 | formalized | `V.T237` |
| `theorem` | [growth_index_departure](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index-departure/) | L485-L487 | formalized | `V.T238` |
| `eval` | [#eval L492](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l492/) | L492-L492 | computed | `V.P162`, `V.R421` |
| `eval` | [#eval L493](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l493/) | L493-L493 | computed | — |
| `eval` | [#eval L494](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l494/) | L494-L494 | computed | — |
| `eval` | [#eval L495](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l495/) | L495-L495 | computed | — |
| `eval` | [#eval L496](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l496/) | L496-L496 | computed | — |
| `structure` | [DESISigma8Falsification](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desisigma8-falsification/) | L505-L514 | defined | `V.R453` |
| `def` | [desi_sigma8_data](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desi-sigma8-data/) | L516-L516 | defined | — |
| `theorem` | [desi_sigma8_detectable](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desi-sigma8-detectable/) | L519-L522 | formalized | — |
| `eval` | [#eval L525](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l525/) | L525-L525 | computed | — |
| `eval` | [#eval L526](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l526/) | L526-L526 | computed | — |
| `structure` | [HubbleDerivationChain](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-derivation-chain/) | L536-L553 | defined | `V.D319` |
| `def` | [hubble_derivation_data](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-derivation-data/) | L555-L555 | defined | — |
| `theorem` | [hubble_uniqueness](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-uniqueness/) | L558-L561 | formalized | `V.T259` |
| `theorem` | [hubble_self_consistency](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-self-consistency/) | L566-L569 | formalized | `V.P178` |
| `theorem` | [hubble_sub_permille](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-sub-permille/) | L572-L574 | formalized | — |
| `eval` | [#eval L577](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l577/) | L577-L577 | computed | — |
| `eval` | [#eval L578](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l578/) | L578-L578 | computed | — |
| `eval` | [#eval L579](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l579/) | L579-L579 | computed | — |
| `structure` | [S8TensionResolution](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-tension-resolution/) | L589-L612 | defined | `V.D324` |
| `def` | [s8_resolution_data](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-resolution-data/) | L614-L614 | defined | — |
| `theorem` | [s8_between_cmb_and_wl](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-between-cmb-and-wl/) | L617-L620 | formalized | `V.T263` |
| `theorem` | [s8_within_1sigma_deskids](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-within-1sigma-deskids/) | L623-L626 | formalized | `V.P182` |
| `theorem` | [s8_zero_params](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-zero-params/) | L629-L631 | formalized | — |
| `eval` | [#eval L634](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l634/) | L634-L634 | computed | — |
| `eval` | [#eval L635](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l635/) | L635-L635 | computed | — |
| `eval` | [#eval L636](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l636/) | L636-L636 | computed | — |
| `structure` | [S8NNLO](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo/) | L647-L672 | defined | `V.D330` |
| `def` | [s8_nnlo_data](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-data/) | L674-L674 | defined | — |
| `theorem` | [s8_nnlo_within_kids](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-within-kids/) | L678-L681 | formalized | `V.T266` |
| `theorem` | [s8_nnlo_within_hsc](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-within-hsc/) | L685-L688 | formalized | `V.T266` |
| `theorem` | [s8_nnlo_below_nlo](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-below-nlo/) | L691-L693 | formalized | `V.D330` |
| `theorem` | [s8_nnlo_zero_params](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-zero-params/) | L696-L698 | formalized | — |
| `eval` | [#eval L701](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l701/) | L701-L701 | computed | — |
| `eval` | [#eval L702](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l702/) | L702-L702 | computed | — |
| `eval` | [#eval L703](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l703/) | L703-L705 | computed | — |
