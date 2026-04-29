---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.HeatEM",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.HeatEM`.",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_slug": "book-v-thermodynamics-heat-em",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/HeatEM.lean",
  "sha256": "dc87416d0041e3d40cdfc08ab0cefdcab715e6cbe31b8c07ac6d4200738ff824",
  "imports": [
    "TauLib.BookV.Thermodynamics.DefectExhaustion"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Thermodynamics.VacuumNoVoid"
  ],
  "registry_ids": [
    "V.D91",
    "V.D92",
    "V.D93",
    "V.P34",
    "V.P35",
    "V.P36",
    "V.P37",
    "V.R128",
    "V.R129",
    "V.T63",
    "V.T64"
  ],
  "declaration_counts": {
    "theorem": 10,
    "inductive": 1,
    "def": 4,
    "structure": 4,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "artificial_trichotomy",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/artificial-trichotomy/",
      "source_line_start": 64,
      "source_line_end": 66,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R128"
      ]
    },
    {
      "kind": "inductive",
      "name": "TransportMode",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/transport-mode/",
      "source_line_start": 73,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TransportMode.sector",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/sector/",
      "source_line_start": 83,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EMEnergyTransport",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/emenergy-transport/",
      "source_line_start": 90,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": [
        "V.D91"
      ]
    },
    {
      "kind": "theorem",
      "name": "transport_default_b",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/transport-default-b/",
      "source_line_start": 104,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "radiation_is_b_sector",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/radiation-is-b-sector/",
      "source_line_start": 115,
      "source_line_end": 116,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P34"
      ]
    },
    {
      "kind": "theorem",
      "name": "conduction_is_b_sector",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/conduction-is-b-sector/",
      "source_line_start": 127,
      "source_line_end": 128,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P35"
      ]
    },
    {
      "kind": "theorem",
      "name": "convection_is_b_sector",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/convection-is-b-sector/",
      "source_line_start": 139,
      "source_line_end": 140,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P36"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_governs_transport",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/alpha-governs-transport/",
      "source_line_start": 154,
      "source_line_end": 156,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T63"
      ]
    },
    {
      "kind": "theorem",
      "name": "why_alpha_not_iota_sq",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/why-alpha-not-iota-sq/",
      "source_line_start": 168,
      "source_line_end": 170,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R129"
      ]
    },
    {
      "kind": "structure",
      "name": "GeometricRelaxation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/geometric-relaxation/",
      "source_line_start": 183,
      "source_line_end": 196,
      "formal_status": "defined",
      "registry_ids": [
        "V.D92"
      ]
    },
    {
      "kind": "structure",
      "name": "TopologicalRelaxation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/topological-relaxation/",
      "source_line_start": 208,
      "source_line_end": 217,
      "formal_status": "defined",
      "registry_ids": [
        "V.D93"
      ]
    },
    {
      "kind": "theorem",
      "name": "relaxation_hierarchy",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/relaxation-hierarchy/",
      "source_line_start": 229,
      "source_line_end": 231,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P37"
      ]
    },
    {
      "kind": "structure",
      "name": "HeatIsEM",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/heat-is-em/",
      "source_line_start": 244,
      "source_line_end": 252,
      "formal_status": "defined",
      "registry_ids": [
        "V.T64"
      ]
    },
    {
      "kind": "theorem",
      "name": "heat_is_em_unified",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/heat-is-em-unified/",
      "source_line_start": 255,
      "source_line_end": 256,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_modes_b_sector",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/all-modes-b-sector/",
      "source_line_start": 259,
      "source_line_end": 261,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_radiation",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/example-radiation/",
      "source_line_start": 268,
      "source_line_end": 272,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l275/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_geo_relax",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/example-geo-relax/",
      "source_line_start": 278,
      "source_line_end": 283,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_top_relax",
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/example-top-relax/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l293/",
      "source_line_start": 293,
      "source_line_end": 295,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/HeatEM.lean`
- SHA-256: `dc87416d0041e3d40cdfc08ab0cefdcab715e6cbe31b8c07ac6d4200738ff824`

## Registry Links

- `V.D91` — EM energy transport
- `V.D92` — Geometric relaxation
- `V.D93` — Topological relaxation
- `V.P34` — Radiation is B-sector transport
- `V.P35` — Conduction is near-field B-sector transport
- `V.P36` — Convective transport is B-sector displacement
- `V.P37` — Hierarchy of relaxation times
- `V.R128` — The artificial trichotomy
- `V.R129` — Why alpha and not iota_tau^2
- `V.T63` — alpha governs macroscopic energy transport
- `V.T64` — Heat is electromagnetism

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Thermodynamics.DefectExhaustion`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Thermodynamics.VacuumNoVoid`

## Declaration Counts

- `def`: 4
- `eval`: 4
- `inductive`: 1
- `structure`: 4
- `theorem`: 10

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [artificial_trichotomy](/verify/taulib/docs/book-v-thermodynamics-heat-em/artificial-trichotomy/) | L64-L66 | formalized | `V.R128` |
| `inductive` | [TransportMode](/verify/taulib/docs/book-v-thermodynamics-heat-em/transport-mode/) | L73-L80 | defined | — |
| `def` | [TransportMode.sector](/verify/taulib/docs/book-v-thermodynamics-heat-em/sector/) | L83-L83 | defined | — |
| `structure` | [EMEnergyTransport](/verify/taulib/docs/book-v-thermodynamics-heat-em/emenergy-transport/) | L90-L101 | defined | `V.D91` |
| `theorem` | [transport_default_b](/verify/taulib/docs/book-v-thermodynamics-heat-em/transport-default-b/) | L104-L105 | formalized | — |
| `theorem` | [radiation_is_b_sector](/verify/taulib/docs/book-v-thermodynamics-heat-em/radiation-is-b-sector/) | L115-L116 | formalized | `V.P34` |
| `theorem` | [conduction_is_b_sector](/verify/taulib/docs/book-v-thermodynamics-heat-em/conduction-is-b-sector/) | L127-L128 | formalized | `V.P35` |
| `theorem` | [convection_is_b_sector](/verify/taulib/docs/book-v-thermodynamics-heat-em/convection-is-b-sector/) | L139-L140 | formalized | `V.P36` |
| `theorem` | [alpha_governs_transport](/verify/taulib/docs/book-v-thermodynamics-heat-em/alpha-governs-transport/) | L154-L156 | formalized | `V.T63` |
| `theorem` | [why_alpha_not_iota_sq](/verify/taulib/docs/book-v-thermodynamics-heat-em/why-alpha-not-iota-sq/) | L168-L170 | formalized | `V.R129` |
| `structure` | [GeometricRelaxation](/verify/taulib/docs/book-v-thermodynamics-heat-em/geometric-relaxation/) | L183-L196 | defined | `V.D92` |
| `structure` | [TopologicalRelaxation](/verify/taulib/docs/book-v-thermodynamics-heat-em/topological-relaxation/) | L208-L217 | defined | `V.D93` |
| `theorem` | [relaxation_hierarchy](/verify/taulib/docs/book-v-thermodynamics-heat-em/relaxation-hierarchy/) | L229-L231 | formalized | `V.P37` |
| `structure` | [HeatIsEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/heat-is-em/) | L244-L252 | defined | `V.T64` |
| `theorem` | [heat_is_em_unified](/verify/taulib/docs/book-v-thermodynamics-heat-em/heat-is-em-unified/) | L255-L256 | formalized | — |
| `theorem` | [all_modes_b_sector](/verify/taulib/docs/book-v-thermodynamics-heat-em/all-modes-b-sector/) | L259-L261 | formalized | — |
| `def` | [example_radiation](/verify/taulib/docs/book-v-thermodynamics-heat-em/example-radiation/) | L268-L272 | defined | — |
| `eval` | [#eval L274](/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l274/) | L274-L274 | computed | — |
| `eval` | [#eval L275](/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l275/) | L275-L275 | computed | — |
| `def` | [example_geo_relax](/verify/taulib/docs/book-v-thermodynamics-heat-em/example-geo-relax/) | L278-L283 | defined | — |
| `eval` | [#eval L285](/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l285/) | L285-L285 | computed | — |
| `def` | [example_top_relax](/verify/taulib/docs/book-v-thermodynamics-heat-em/example-top-relax/) | L288-L291 | defined | — |
| `eval` | [#eval L293](/verify/taulib/docs/book-v-thermodynamics-heat-em/eval-l293/) | L293-L295 | computed | — |
