---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_slug": "book-iv-many-body-defect-functional-ext2",
  "book": "BookIV",
  "family": "ManyBody",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean",
  "sha256": "0346e18b92dde2733b8c8378c4043c2dae53b3acc23930dfd86f0c162a708f2a",
  "imports": [
    "TauLib.BookIV.ManyBody.DefectFunctionalExt"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.ManyBody.FluidRegimes"
  ],
  "registry_ids": [
    "IV.D222",
    "IV.D223",
    "IV.D224",
    "IV.D225",
    "IV.D226",
    "IV.D227",
    "IV.D228",
    "IV.D229",
    "IV.D230",
    "IV.P136",
    "IV.P137",
    "IV.P138",
    "IV.P139",
    "IV.R161",
    "IV.R162",
    "IV.R163",
    "IV.R164",
    "IV.R165",
    "IV.R166",
    "IV.R167",
    "IV.R168",
    "IV.R169",
    "IV.T91",
    "IV.T92"
  ],
  "declaration_counts": {
    "structure": 15,
    "def": 18,
    "theorem": 4,
    "eval": 16
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "EulerFluidRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-fluid-regime/",
      "source_line_start": 66,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D222"
      ]
    },
    {
      "kind": "def",
      "name": "euler_fluid_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-fluid-regime-l77/",
      "source_line_start": 77,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauEulerEquation",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/tau-euler-equation/",
      "source_line_start": 89,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P136"
      ]
    },
    {
      "kind": "def",
      "name": "tau_euler_equation",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/tau-euler-equation-l98/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_theta_invariant",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-theta-invariant/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NavierStokesRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/navier-stokes-regime/",
      "source_line_start": 112,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D223"
      ]
    },
    {
      "kind": "def",
      "name": "ns_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/ns-regime/",
      "source_line_start": 123,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MHDRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/mhdregime/",
      "source_line_start": 139,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D224"
      ]
    },
    {
      "kind": "def",
      "name": "mhd_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/mhd-regime/",
      "source_line_start": 150,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PlasmaRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/plasma-regime/",
      "source_line_start": 163,
      "source_line_end": 170,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D225"
      ]
    },
    {
      "kind": "def",
      "name": "plasma_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/plasma-regime-l172/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SuperfluidRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-regime/",
      "source_line_start": 184,
      "source_line_end": 193,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D226"
      ]
    },
    {
      "kind": "def",
      "name": "superfluid_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-regime-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SuperfluidVortexQuantization",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-vortex-quantization/",
      "source_line_start": 206,
      "source_line_end": 213,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P137"
      ]
    },
    {
      "kind": "def",
      "name": "superfluid_vortex_quant",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-vortex-quant/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_helium4",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-helium4/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R163"
      ]
    },
    {
      "kind": "structure",
      "name": "SuperconductorRegime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superconductor-regime/",
      "source_line_start": 231,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D227"
      ]
    },
    {
      "kind": "def",
      "name": "superconductor_regime",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superconductor-regime-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FluxQuantization",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/flux-quantization/",
      "source_line_start": 253,
      "source_line_end": 260,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P138"
      ]
    },
    {
      "kind": "def",
      "name": "flux_quantization",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/flux-quantization-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_cooper_pairing",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-cooper-pairing/",
      "source_line_start": 267,
      "source_line_end": 268,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R164"
      ]
    },
    {
      "kind": "structure",
      "name": "TemperatureAsDefectGradient",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/temperature-as-defect-gradient/",
      "source_line_start": 281,
      "source_line_end": 288,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D228"
      ]
    },
    {
      "kind": "def",
      "name": "temperature_defect_gradient",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/temperature-defect-gradient/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BoltzmannConstantStatus",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-constant-status/",
      "source_line_start": 302,
      "source_line_end": 309,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P139"
      ]
    },
    {
      "kind": "def",
      "name": "boltzmann_status",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-status/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "boltzmann_is_conversion",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-is-conversion/",
      "source_line_start": 313,
      "source_line_end": 314,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SecondLawViaDefect",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-via-defect/",
      "source_line_start": 329,
      "source_line_end": 338,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T91"
      ]
    },
    {
      "kind": "def",
      "name": "second_law_defect",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-defect/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "second_law_total_nondecreasing",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-total-nondecreasing/",
      "source_line_start": 342,
      "source_line_end": 343,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FirstOrderTransition",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/first-order-transition/",
      "source_line_start": 356,
      "source_line_end": 363,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D229"
      ]
    },
    {
      "kind": "def",
      "name": "first_order_transition",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/first-order-transition-l365/",
      "source_line_start": 365,
      "source_line_end": 365,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SecondOrderTransition",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-order-transition/",
      "source_line_start": 370,
      "source_line_end": 377,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D230"
      ]
    },
    {
      "kind": "def",
      "name": "second_order_transition",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-order-transition-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PhaseTransitionRegimeCrossing",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/phase-transition-regime-crossing/",
      "source_line_start": 387,
      "source_line_end": 396,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T92"
      ]
    },
    {
      "kind": "def",
      "name": "phase_transition_crossing",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/phase-transition-crossing/",
      "source_line_start": 398,
      "source_line_end": 398,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_transitions_are_crossings",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/all-transitions-are-crossings/",
      "source_line_start": 400,
      "source_line_end": 401,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_universality",
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-universality/",
      "source_line_start": 407,
      "source_line_end": 409,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R169"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l415/",
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
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l416/",
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
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l417/",
      "source_line_start": 417,
      "source_line_end": 417,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l418/",
      "source_line_start": 418,
      "source_line_end": 418,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l419/",
      "source_line_start": 419,
      "source_line_end": 419,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l420/",
      "source_line_start": 420,
      "source_line_end": 420,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l421/",
      "source_line_start": 421,
      "source_line_end": 421,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l422/",
      "source_line_start": 422,
      "source_line_end": 422,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l424/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l425/",
      "source_line_start": 425,
      "source_line_end": 425,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l426/",
      "source_line_start": 426,
      "source_line_end": 426,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l427/",
      "source_line_start": 427,
      "source_line_end": 427,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l429/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l430/",
      "source_line_start": 430,
      "source_line_end": 432,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`
- SHA-256: `0346e18b92dde2733b8c8378c4043c2dae53b3acc23930dfd86f0c162a708f2a`

## Registry Links

- `IV.D222` — Euler fluid regime
- `IV.D223` — Navier-Stokes regime
- `IV.D224` — MHD regime
- `IV.D225` — Plasma regime
- `IV.D226` — Superfluid regime
- `IV.D227` — Superconductor regime
- `IV.D228` — Temperature as defect gradient
- `IV.D229` — First-order phase transition
- `IV.D230` — Second-order phase transition
- `IV.P136` — tau-Euler equation
- `IV.P137` — Superfluid vortex quantization
- `IV.P138` — Flux quantization
- `IV.P139` — Status of Boltzmann constant
- `IV.R161` — Navier-Stokes regularity
- `IV.R162` — Why MHD lives in B-sector
- `IV.R163` — Helium-4 and beyond
- `IV.R164` — Cooper pairing is topological
- `IV.R165` — Transitions as inequality crossings
- `IV.R166` — Comparison with orthodox thermodynamics
- `IV.R167` — Parallel with hbar and c
- `IV.R168` — No negative temperatures
- `IV.R169` — Universality and critical exponents
- `IV.T91` — Second law via defect functional
- `IV.T92` — Phase transition as regime crossing

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.ManyBody.DefectFunctionalExt`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.ManyBody.FluidRegimes`

## Declaration Counts

- `def`: 18
- `eval`: 16
- `structure`: 15
- `theorem`: 4

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [EulerFluidRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-fluid-regime/) | L66-L75 | type/data schema | type/data schema | `IV.D222` |
| `def` | [euler_fluid_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-fluid-regime-l77/) | L77-L77 | definition | definition | — |
| `structure` | [TauEulerEquation](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/tau-euler-equation/) | L89-L96 | type/data schema | type/data schema | `IV.P136` |
| `def` | [tau_euler_equation](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/tau-euler-equation-l98/) | L98-L98 | definition | definition | — |
| `theorem` | [euler_theta_invariant](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-theta-invariant/) | L100-L101 | proof obligation | formal proof obligation checked | — |
| `structure` | [NavierStokesRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/navier-stokes-regime/) | L112-L121 | type/data schema | type/data schema | `IV.D223` |
| `def` | [ns_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/ns-regime/) | L123-L123 | definition | definition | — |
| `structure` | [MHDRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/mhdregime/) | L139-L148 | type/data schema | type/data schema | `IV.D224` |
| `def` | [mhd_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/mhd-regime/) | L150-L150 | definition | definition | — |
| `structure` | [PlasmaRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/plasma-regime/) | L163-L170 | type/data schema | type/data schema | `IV.D225` |
| `def` | [plasma_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/plasma-regime-l172/) | L172-L172 | definition | definition | — |
| `structure` | [SuperfluidRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-regime/) | L184-L193 | type/data schema | type/data schema | `IV.D226` |
| `def` | [superfluid_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-regime-l195/) | L195-L195 | definition | definition | — |
| `structure` | [SuperfluidVortexQuantization](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-vortex-quantization/) | L206-L213 | type/data schema | type/data schema | `IV.P137` |
| `def` | [superfluid_vortex_quant](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-vortex-quant/) | L215-L215 | definition | definition | — |
| `def` | [remark_helium4](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-helium4/) | L220-L221 | docstring/data record | docstring/data record | `IV.R163` |
| `structure` | [SuperconductorRegime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superconductor-regime/) | L231-L240 | type/data schema | type/data schema | `IV.D227` |
| `def` | [superconductor_regime](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superconductor-regime-l242/) | L242-L242 | definition | definition | — |
| `structure` | [FluxQuantization](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/flux-quantization/) | L253-L260 | type/data schema | type/data schema | `IV.P138` |
| `def` | [flux_quantization](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/flux-quantization-l262/) | L262-L262 | definition | definition | — |
| `def` | [remark_cooper_pairing](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-cooper-pairing/) | L267-L268 | docstring/data record | docstring/data record | `IV.R164` |
| `structure` | [TemperatureAsDefectGradient](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/temperature-as-defect-gradient/) | L281-L288 | type/data schema | type/data schema | `IV.D228` |
| `def` | [temperature_defect_gradient](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/temperature-defect-gradient/) | L290-L290 | definition | definition | — |
| `structure` | [BoltzmannConstantStatus](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-constant-status/) | L302-L309 | type/data schema | type/data schema | `IV.P139` |
| `def` | [boltzmann_status](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-status/) | L311-L311 | definition | definition | — |
| `theorem` | [boltzmann_is_conversion](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-is-conversion/) | L313-L314 | proof obligation | formal proof obligation checked | — |
| `structure` | [SecondLawViaDefect](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-via-defect/) | L329-L338 | type/data schema | type/data schema | `IV.T91` |
| `def` | [second_law_defect](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-defect/) | L340-L340 | definition | definition | — |
| `theorem` | [second_law_total_nondecreasing](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-total-nondecreasing/) | L342-L343 | proof obligation | formal proof obligation checked | — |
| `structure` | [FirstOrderTransition](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/first-order-transition/) | L356-L363 | type/data schema | type/data schema | `IV.D229` |
| `def` | [first_order_transition](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/first-order-transition-l365/) | L365-L365 | definition | definition | — |
| `structure` | [SecondOrderTransition](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-order-transition/) | L370-L377 | type/data schema | type/data schema | `IV.D230` |
| `def` | [second_order_transition](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/second-order-transition-l379/) | L379-L379 | definition | definition | — |
| `structure` | [PhaseTransitionRegimeCrossing](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/phase-transition-regime-crossing/) | L387-L396 | type/data schema | type/data schema | `IV.T92` |
| `def` | [phase_transition_crossing](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/phase-transition-crossing/) | L398-L398 | definition | definition | — |
| `theorem` | [all_transitions_are_crossings](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/all-transitions-are-crossings/) | L400-L401 | proof obligation | formal proof obligation checked | — |
| `def` | [remark_universality](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/remark-universality/) | L407-L409 | docstring/data record | docstring/data record | `IV.R169` |
| `eval` | [#eval L415](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l415/) | L415-L415 | computed check | computed check | — |
| `eval` | [#eval L416](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l416/) | L416-L416 | computed check | computed check | — |
| `eval` | [#eval L417](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l417/) | L417-L417 | computed check | computed check | — |
| `eval` | [#eval L418](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l418/) | L418-L418 | computed check | computed check | — |
| `eval` | [#eval L419](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l419/) | L419-L419 | computed check | computed check | — |
| `eval` | [#eval L420](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l420/) | L420-L420 | computed check | computed check | — |
| `eval` | [#eval L421](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l421/) | L421-L421 | computed check | computed check | — |
| `eval` | [#eval L422](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l422/) | L422-L422 | computed check | computed check | — |
| `eval` | [#eval L423](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l423/) | L423-L423 | computed check | computed check | — |
| `eval` | [#eval L424](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l424/) | L424-L424 | computed check | computed check | — |
| `eval` | [#eval L425](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l425/) | L425-L425 | computed check | computed check | — |
| `eval` | [#eval L426](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l426/) | L426-L426 | computed check | computed check | — |
| `eval` | [#eval L427](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l427/) | L427-L427 | computed check | computed check | — |
| `eval` | [#eval L428](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l428/) | L428-L428 | computed check | computed check | — |
| `eval` | [#eval L429](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l429/) | L429-L429 | computed check | computed check | — |
| `eval` | [#eval L430](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/eval-l430/) | L430-L432 | computed check | computed check | — |
