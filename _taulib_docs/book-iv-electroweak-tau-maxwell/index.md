---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.TauMaxwell",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_slug": "book-iv-electroweak-tau-maxwell",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/TauMaxwell.lean",
  "sha256": "a4c0aeca5acbd922fe15d3ccb570c5f14f823969d91bc661e17194e3b0494552",
  "imports": [
    "TauLib.BookIV.Electroweak.GaugeInvariance2"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.AlphaDerivation"
  ],
  "registry_ids": [
    "IV.D100",
    "IV.D101",
    "IV.D102",
    "IV.D103",
    "IV.D98",
    "IV.D99",
    "IV.P44",
    "IV.P45",
    "IV.P46",
    "IV.P47",
    "IV.P48",
    "IV.P49",
    "IV.T42",
    "IV.T43",
    "IV.T44",
    "IV.T45",
    "IV.T46",
    "IV.T47"
  ],
  "declaration_counts": {
    "structure": 18,
    "def": 19,
    "theorem": 13,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "EMGaugeBundle",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emgauge-bundle/",
      "source_line_start": 71,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D98"
      ]
    },
    {
      "kind": "def",
      "name": "em_gauge_trivial",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-gauge-trivial/",
      "source_line_start": 84,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EMConnectionA",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emconnection-a/",
      "source_line_start": 96,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D99"
      ]
    },
    {
      "kind": "def",
      "name": "em_connection_a",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-connection-a/",
      "source_line_start": 108,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EMFieldTensor",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emfield-tensor/",
      "source_line_start": 121,
      "source_line_end": 132,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D100"
      ]
    },
    {
      "kind": "def",
      "name": "faraday_tensor",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/faraday-tensor/",
      "source_line_start": 135,
      "source_line_end": 139,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EBFields",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/ebfields/",
      "source_line_start": 148,
      "source_line_end": 158,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D101"
      ]
    },
    {
      "kind": "def",
      "name": "eb_fields",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eb-fields/",
      "source_line_start": 161,
      "source_line_end": 167,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "eb_total_eq_f",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eb-total-eq-f/",
      "source_line_start": 170,
      "source_line_end": 170,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HodgeDual",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/hodge-dual/",
      "source_line_start": 178,
      "source_line_end": 185,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D102"
      ]
    },
    {
      "kind": "structure",
      "name": "EMCurrent",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emcurrent/",
      "source_line_start": 194,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D103"
      ]
    },
    {
      "kind": "def",
      "name": "em_current",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-current/",
      "source_line_start": 206,
      "source_line_end": 210,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BianchiIdentity",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-identity/",
      "source_line_start": 219,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T42"
      ]
    },
    {
      "kind": "def",
      "name": "bianchi_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-instance/",
      "source_line_start": 229,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bianchi_identity",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-identity-l233/",
      "source_line_start": 233,
      "source_line_end": 233,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SourceEquation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-equation/",
      "source_line_start": 241,
      "source_line_end": 247,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T43"
      ]
    },
    {
      "kind": "def",
      "name": "source_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-instance/",
      "source_line_start": 249,
      "source_line_end": 251,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "source_equation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-equation-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MaxwellEquations",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-equations/",
      "source_line_start": 263,
      "source_line_end": 271,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T44"
      ]
    },
    {
      "kind": "def",
      "name": "maxwell_eqs",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-eqs/",
      "source_line_start": 274,
      "source_line_end": 278,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "maxwell_equations",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-equations-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectSources",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources/",
      "source_line_start": 289,
      "source_line_end": 294,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T45"
      ]
    },
    {
      "kind": "def",
      "name": "defect_sources_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources-instance/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "defect_sources",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources-l298/",
      "source_line_start": 298,
      "source_line_end": 299,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoulombLimit",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-limit/",
      "source_line_start": 308,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T46"
      ]
    },
    {
      "kind": "def",
      "name": "coulomb_3d",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-3d/",
      "source_line_start": 318,
      "source_line_end": 322,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coulomb_limit",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-limit-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WaveEquation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation/",
      "source_line_start": 332,
      "source_line_end": 339,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T47"
      ]
    },
    {
      "kind": "def",
      "name": "wave_equation_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation-instance/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wave_equation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation-l343/",
      "source_line_start": 343,
      "source_line_end": 344,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ContinuityEquation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-equation/",
      "source_line_start": 353,
      "source_line_end": 358,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P44"
      ]
    },
    {
      "kind": "def",
      "name": "continuity_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-instance/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "continuity_equation",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-equation-l362/",
      "source_line_start": 362,
      "source_line_end": 363,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChargeDensity",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density/",
      "source_line_start": 372,
      "source_line_end": 377,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P45"
      ]
    },
    {
      "kind": "def",
      "name": "charge_density_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density-instance/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "charge_density",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density-l381/",
      "source_line_start": 381,
      "source_line_end": 382,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CurrentDensity",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density/",
      "source_line_start": 390,
      "source_line_end": 396,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P46"
      ]
    },
    {
      "kind": "def",
      "name": "current_density_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density-instance/",
      "source_line_start": 398,
      "source_line_end": 400,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "current_density",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density-l402/",
      "source_line_start": 402,
      "source_line_end": 403,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PhotonEMWave",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-emwave/",
      "source_line_start": 412,
      "source_line_end": 419,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P47"
      ]
    },
    {
      "kind": "def",
      "name": "photon_em_wave_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-em-wave-instance/",
      "source_line_start": 421,
      "source_line_end": 421,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "photon_is_em_wave",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-is-em-wave/",
      "source_line_start": 423,
      "source_line_end": 424,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagneticForce",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force/",
      "source_line_start": 432,
      "source_line_end": 437,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P48"
      ]
    },
    {
      "kind": "def",
      "name": "magnetic_force_instance",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force-instance/",
      "source_line_start": 439,
      "source_line_end": 439,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetic_force_perpendicular",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force-perpendicular/",
      "source_line_start": 441,
      "source_line_end": 443,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QEDCorrections",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qedcorrections/",
      "source_line_start": 452,
      "source_line_end": 461,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P49"
      ]
    },
    {
      "kind": "def",
      "name": "qed_standard",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qed-standard/",
      "source_line_start": 464,
      "source_line_end": 468,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qed_corrections",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qed-corrections/",
      "source_line_start": 470,
      "source_line_end": 470,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l476/",
      "source_line_start": 476,
      "source_line_end": 476,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l477/",
      "source_line_start": 477,
      "source_line_end": 477,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l478/",
      "source_line_start": 478,
      "source_line_end": 478,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l479/",
      "source_line_start": 479,
      "source_line_end": 479,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l480/",
      "source_line_start": 480,
      "source_line_end": 480,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l481/",
      "source_line_start": 481,
      "source_line_end": 481,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l482/",
      "source_line_start": 482,
      "source_line_end": 482,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l483/",
      "source_line_start": 483,
      "source_line_end": 483,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_hodge",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/example-hodge/",
      "source_line_start": 484,
      "source_line_end": 484,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l485/",
      "source_line_start": 485,
      "source_line_end": 485,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_wave",
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/example-wave/",
      "source_line_start": 486,
      "source_line_end": 486,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l487/",
      "source_line_start": 487,
      "source_line_end": 489,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/TauMaxwell.lean`
- SHA-256: `a4c0aeca5acbd922fe15d3ccb570c5f14f823969d91bc661e17194e3b0494552`

## Registry Links

- `IV.D100` — Electromagnetic Field Tensor
- `IV.D101` — Electric and Magnetic Field Extraction
- `IV.D102` — Hodge Dual of F
- `IV.D103` — Electromagnetic Current 4-Vector
- `IV.D98` — EM Gauge Bundle
- `IV.D99` — EM Connection 1-Form
- `IV.P44` — Current Conservation from Gauge Invariance
- `IV.P45` — Charge Density as Winding-Number Density
- `IV.P46` — Current as Defect Transport
- `IV.P47` — Photon-Wave Identity
- `IV.P48` — Magnetic Force Does No Work
- `IV.P49` — Perturbative Expansion in alpha
- `IV.T42` — Homogeneous Maxwell Equations
- `IV.T43` — Inhomogeneous Maxwell Equations
- `IV.T44` — Complete tau-Maxwell System
- `IV.T45` — Source-Defect Correspondence
- `IV.T46` — Coulomb's Law from tau-Maxwell
- `IV.T47` — EM Wave Equation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.GaugeInvariance2`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.AlphaDerivation`

## Declaration Counts

- `def`: 19
- `eval`: 10
- `structure`: 18
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [EMGaugeBundle](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emgauge-bundle/) | L71-L81 | defined | `IV.D98` |
| `def` | [em_gauge_trivial](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-gauge-trivial/) | L84-L87 | defined | — |
| `structure` | [EMConnectionA](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emconnection-a/) | L96-L105 | defined | `IV.D99` |
| `def` | [em_connection_a](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-connection-a/) | L108-L112 | defined | — |
| `structure` | [EMFieldTensor](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emfield-tensor/) | L121-L132 | defined | `IV.D100` |
| `def` | [faraday_tensor](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/faraday-tensor/) | L135-L139 | defined | — |
| `structure` | [EBFields](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/ebfields/) | L148-L158 | defined | `IV.D101` |
| `def` | [eb_fields](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eb-fields/) | L161-L167 | defined | — |
| `theorem` | [eb_total_eq_f](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eb-total-eq-f/) | L170-L170 | formalized | — |
| `structure` | [HodgeDual](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/hodge-dual/) | L178-L185 | defined | `IV.D102` |
| `structure` | [EMCurrent](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emcurrent/) | L194-L203 | defined | `IV.D103` |
| `def` | [em_current](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/em-current/) | L206-L210 | defined | — |
| `structure` | [BianchiIdentity](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-identity/) | L219-L227 | defined | `IV.T42` |
| `def` | [bianchi_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-instance/) | L229-L231 | defined | — |
| `theorem` | [bianchi_identity](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-identity-l233/) | L233-L233 | formalized | — |
| `structure` | [SourceEquation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-equation/) | L241-L247 | defined | `IV.T43` |
| `def` | [source_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-instance/) | L249-L251 | defined | — |
| `theorem` | [source_equation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-equation-l253/) | L253-L253 | formalized | — |
| `structure` | [MaxwellEquations](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-equations/) | L263-L271 | defined | `IV.T44` |
| `def` | [maxwell_eqs](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-eqs/) | L274-L278 | defined | — |
| `theorem` | [maxwell_equations](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-equations-l280/) | L280-L280 | formalized | — |
| `structure` | [DefectSources](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources/) | L289-L294 | defined | `IV.T45` |
| `def` | [defect_sources_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources-instance/) | L296-L296 | defined | — |
| `theorem` | [defect_sources](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/defect-sources-l298/) | L298-L299 | formalized | — |
| `structure` | [CoulombLimit](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-limit/) | L308-L315 | defined | `IV.T46` |
| `def` | [coulomb_3d](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-3d/) | L318-L322 | defined | — |
| `theorem` | [coulomb_limit](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-limit-l324/) | L324-L324 | formalized | — |
| `structure` | [WaveEquation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation/) | L332-L339 | defined | `IV.T47` |
| `def` | [wave_equation_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation-instance/) | L341-L341 | defined | — |
| `theorem` | [wave_equation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation-l343/) | L343-L344 | formalized | — |
| `structure` | [ContinuityEquation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-equation/) | L353-L358 | defined | `IV.P44` |
| `def` | [continuity_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-instance/) | L360-L360 | defined | — |
| `theorem` | [continuity_equation](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-equation-l362/) | L362-L363 | formalized | — |
| `structure` | [ChargeDensity](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density/) | L372-L377 | defined | `IV.P45` |
| `def` | [charge_density_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density-instance/) | L379-L379 | defined | — |
| `theorem` | [charge_density](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density-l381/) | L381-L382 | formalized | — |
| `structure` | [CurrentDensity](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density/) | L390-L396 | defined | `IV.P46` |
| `def` | [current_density_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density-instance/) | L398-L400 | defined | — |
| `theorem` | [current_density](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density-l402/) | L402-L403 | formalized | — |
| `structure` | [PhotonEMWave](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-emwave/) | L412-L419 | defined | `IV.P47` |
| `def` | [photon_em_wave_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-em-wave-instance/) | L421-L421 | defined | — |
| `theorem` | [photon_is_em_wave](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-is-em-wave/) | L423-L424 | formalized | — |
| `structure` | [MagneticForce](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force/) | L432-L437 | defined | `IV.P48` |
| `def` | [magnetic_force_instance](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force-instance/) | L439-L439 | defined | — |
| `theorem` | [magnetic_force_perpendicular](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force-perpendicular/) | L441-L443 | formalized | — |
| `structure` | [QEDCorrections](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qedcorrections/) | L452-L461 | defined | `IV.P49` |
| `def` | [qed_standard](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qed-standard/) | L464-L468 | defined | — |
| `theorem` | [qed_corrections](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qed-corrections/) | L470-L470 | formalized | — |
| `eval` | [#eval L476](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l476/) | L476-L476 | computed | — |
| `eval` | [#eval L477](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l477/) | L477-L477 | computed | — |
| `eval` | [#eval L478](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l478/) | L478-L478 | computed | — |
| `eval` | [#eval L479](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l479/) | L479-L479 | computed | — |
| `eval` | [#eval L480](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l480/) | L480-L480 | computed | — |
| `eval` | [#eval L481](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l481/) | L481-L481 | computed | — |
| `eval` | [#eval L482](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l482/) | L482-L482 | computed | — |
| `eval` | [#eval L483](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l483/) | L483-L483 | computed | — |
| `def` | [example_hodge](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/example-hodge/) | L484-L484 | defined | — |
| `eval` | [#eval L485](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l485/) | L485-L485 | computed | — |
| `def` | [example_wave](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/example-wave/) | L486-L486 | defined | — |
| `eval` | [#eval L487](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/eval-l487/) | L487-L489 | computed | — |
