---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.PhotonMode",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.PhotonMode`.",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_slug": "book-iv-electroweak-photon-mode",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/PhotonMode.lean",
  "sha256": "d648fa35c0754be0870f8e987743ba0cdd9aec224dd606561c35ba2b985dd15c",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
    "TauLib.BookIV.Calibration.DimensionlessAlpha"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.GaugeInvariance"
  ],
  "registry_ids": [
    "IV.D82",
    "IV.D83",
    "IV.D84",
    "IV.P32",
    "IV.P33",
    "IV.P34",
    "IV.P35",
    "IV.P36",
    "IV.R347",
    "IV.R348",
    "IV.R349",
    "IV.R350",
    "IV.R351",
    "IV.T120",
    "IV.T33",
    "IV.T34",
    "IV.T35",
    "IV.T36"
  ],
  "declaration_counts": {
    "structure": 8,
    "def": 12,
    "theorem": 10,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PhotonMode",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-mode/",
      "source_line_start": 62,
      "source_line_end": 84,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D82"
      ]
    },
    {
      "kind": "def",
      "name": "photon",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon/",
      "source_line_start": 87,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "U1Holonomy",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/u1-holonomy/",
      "source_line_start": 110,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D83"
      ]
    },
    {
      "kind": "def",
      "name": "U1Holonomy.compose",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/compose/",
      "source_line_start": 121,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "U1Holonomy.trivial",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/trivial/",
      "source_line_start": 127,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "U1Holonomy.inv",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/inv/",
      "source_line_start": 133,
      "source_line_end": 136,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ElectricCharge",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/electric-charge/",
      "source_line_start": 145,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D84"
      ]
    },
    {
      "kind": "def",
      "name": "charge_electron",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-electron/",
      "source_line_start": 151,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "charge_proton",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-proton/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "charge_neutron",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-neutron/",
      "source_line_start": 155,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "charge_photon",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-photon/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ElectricCharge.add",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/add/",
      "source_line_start": 160,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "photon_mass_zero",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-mass-zero/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T33"
      ]
    },
    {
      "kind": "structure",
      "name": "PhotonSpeed",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-speed/",
      "source_line_start": 178,
      "source_line_end": 182,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T34"
      ]
    },
    {
      "kind": "theorem",
      "name": "photon_speed_c",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-speed-c/",
      "source_line_start": 184,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyTransport",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/holonomy-transport/",
      "source_line_start": 195,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T35"
      ]
    },
    {
      "kind": "theorem",
      "name": "holonomy_transport",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/holonomy-transport-l204/",
      "source_line_start": 204,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "charge_conservation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-conservation/",
      "source_line_start": 214,
      "source_line_end": 215,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T36"
      ]
    },
    {
      "kind": "theorem",
      "name": "charge_quantized",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-quantized/",
      "source_line_start": 223,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T120"
      ]
    },
    {
      "kind": "structure",
      "name": "NoRestFrame",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/no-rest-frame/",
      "source_line_start": 232,
      "source_line_end": 235,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P32"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_rest_frame",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/no-rest-frame-l237/",
      "source_line_start": 237,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "photon_spin",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-spin/",
      "source_line_start": 246,
      "source_line_end": 247,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P33"
      ]
    },
    {
      "kind": "theorem",
      "name": "particle_charges",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/particle-charges/",
      "source_line_start": 254,
      "source_line_end": 258,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P34"
      ]
    },
    {
      "kind": "structure",
      "name": "PhotonBoundaryChar",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-boundary-char/",
      "source_line_start": 266,
      "source_line_end": 270,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P35"
      ]
    },
    {
      "kind": "theorem",
      "name": "photon_boundary_character",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-boundary-character/",
      "source_line_start": 272,
      "source_line_end": 273,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EmissionAmplitude",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-amplitude/",
      "source_line_start": 281,
      "source_line_end": 286,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P36"
      ]
    },
    {
      "kind": "def",
      "name": "EmissionAmplitude.toFloat",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/to-float/",
      "source_line_start": 288,
      "source_line_end": 289,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "emission_alpha",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-alpha/",
      "source_line_start": 292,
      "source_line_end": 295,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "emission_amplitude",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-amplitude-l297/",
      "source_line_start": 297,
      "source_line_end": 299,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "IV.R347",
        "IV.R348",
        "IV.R349",
        "IV.R350",
        "IV.R351"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_u1_hol",
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/example-u1-hol/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 329,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l330/",
      "source_line_start": 330,
      "source_line_end": 332,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/PhotonMode.lean`
- SHA-256: `d648fa35c0754be0870f8e987743ba0cdd9aec224dd606561c35ba2b985dd15c`

## Registry Links

- `IV.D82` — Photon Mode
- `IV.D83` — U(1) Holonomy on T^2
- `IV.D84` — Electric Charge
- `IV.P32` — No Rest Frame
- `IV.P33` — Photon Spin and Polarization
- `IV.P34` — Charge of Fundamental Modes
- `IV.P35` — Photon as Boundary Character
- `IV.P36` — Photon Coupling Strength
- `IV.R347` — Masslessness is geometric, not postulated
- `IV.R348` — Experimental limits on photon mass
- `IV.R349` — The Planck--Einstein relation in tau^3
- `IV.R350` — Massless spin-1: two, not three
- `IV.R351` — Double slit in tau^3
- `IV.T120` — Charge quantization
- `IV.T33` — Photon Masslessness
- `IV.T34` — Photon Propagation Speed
- `IV.T35` — Dissolution of Wave-Particle Duality
- `IV.T36` — Charge Conservation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.EnergyEntropy`
- `TauLib.BookIV.Calibration.DimensionlessAlpha`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.GaugeInvariance`

## Declaration Counts

- `def`: 12
- `eval`: 10
- `structure`: 8
- `theorem`: 10

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [PhotonMode](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-mode/) | L62-L84 | type/data schema | type/data schema | `IV.D82` |
| `def` | [photon](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon/) | L87-L101 | definition | definition | — |
| `structure` | [U1Holonomy](/corpus/taulib/docs/book-iv-electroweak-photon-mode/u1-holonomy/) | L110-L118 | type/data schema | type/data schema | `IV.D83` |
| `def` | [U1Holonomy.compose](/corpus/taulib/docs/book-iv-electroweak-photon-mode/compose/) | L121-L124 | definition | definition | — |
| `def` | [U1Holonomy.trivial](/corpus/taulib/docs/book-iv-electroweak-photon-mode/trivial/) | L127-L130 | definition | definition | — |
| `def` | [U1Holonomy.inv](/corpus/taulib/docs/book-iv-electroweak-photon-mode/inv/) | L133-L136 | definition | definition | — |
| `structure` | [ElectricCharge](/corpus/taulib/docs/book-iv-electroweak-photon-mode/electric-charge/) | L145-L148 | type/data schema | type/data schema | `IV.D84` |
| `def` | [charge_electron](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-electron/) | L151-L151 | definition | definition | — |
| `def` | [charge_proton](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-proton/) | L153-L153 | definition | definition | — |
| `def` | [charge_neutron](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-neutron/) | L155-L155 | definition | definition | — |
| `def` | [charge_photon](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-photon/) | L157-L157 | definition | definition | — |
| `def` | [ElectricCharge.add](/corpus/taulib/docs/book-iv-electroweak-photon-mode/add/) | L160-L161 | definition | definition | — |
| `theorem` | [photon_mass_zero](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-mass-zero/) | L169-L169 | proof obligation | formal proof obligation checked | `IV.T33` |
| `structure` | [PhotonSpeed](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-speed/) | L178-L182 | type/data schema | type/data schema | `IV.T34` |
| `theorem` | [photon_speed_c](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-speed-c/) | L184-L186 | proof obligation | formal proof obligation checked | — |
| `structure` | [HolonomyTransport](/corpus/taulib/docs/book-iv-electroweak-photon-mode/holonomy-transport/) | L195-L202 | type/data schema | type/data schema | `IV.T35` |
| `theorem` | [holonomy_transport](/corpus/taulib/docs/book-iv-electroweak-photon-mode/holonomy-transport-l204/) | L204-L206 | proof obligation | formal proof obligation checked | — |
| `theorem` | [charge_conservation](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-conservation/) | L214-L215 | proof obligation | formal proof obligation checked | `IV.T36` |
| `theorem` | [charge_quantized](/corpus/taulib/docs/book-iv-electroweak-photon-mode/charge-quantized/) | L223-L224 | proof obligation | formal proof obligation checked | `IV.T120` |
| `structure` | [NoRestFrame](/corpus/taulib/docs/book-iv-electroweak-photon-mode/no-rest-frame/) | L232-L235 | type/data schema | type/data schema | `IV.P32` |
| `theorem` | [no_rest_frame](/corpus/taulib/docs/book-iv-electroweak-photon-mode/no-rest-frame-l237/) | L237-L238 | proof obligation | formal proof obligation checked | — |
| `theorem` | [photon_spin](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-spin/) | L246-L247 | proof obligation | formal proof obligation checked | `IV.P33` |
| `theorem` | [particle_charges](/corpus/taulib/docs/book-iv-electroweak-photon-mode/particle-charges/) | L254-L258 | proof obligation | formal proof obligation checked | `IV.P34` |
| `structure` | [PhotonBoundaryChar](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-boundary-char/) | L266-L270 | type/data schema | type/data schema | `IV.P35` |
| `theorem` | [photon_boundary_character](/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-boundary-character/) | L272-L273 | proof obligation | formal proof obligation checked | — |
| `structure` | [EmissionAmplitude](/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-amplitude/) | L281-L286 | type/data schema | type/data schema | `IV.P36` |
| `def` | [EmissionAmplitude.toFloat](/corpus/taulib/docs/book-iv-electroweak-photon-mode/to-float/) | L288-L289 | data/computed value | data/computed value | — |
| `def` | [emission_alpha](/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-alpha/) | L292-L295 | definition | definition | — |
| `theorem` | [emission_amplitude](/corpus/taulib/docs/book-iv-electroweak-photon-mode/emission-amplitude-l297/) | L297-L299 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L320](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l320/) | L320-L320 | computed check | computed check | `IV.R347`, `IV.R348`, `IV.R349`, `IV.R350`, `IV.R351` |
| `eval` | [#eval L321](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l321/) | L321-L321 | computed check | computed check | — |
| `eval` | [#eval L322](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l322/) | L322-L322 | computed check | computed check | — |
| `eval` | [#eval L323](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l323/) | L323-L323 | computed check | computed check | — |
| `eval` | [#eval L324](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l324/) | L324-L324 | computed check | computed check | — |
| `eval` | [#eval L325](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l325/) | L325-L325 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l327/) | L327-L327 | computed check | computed check | — |
| `def` | [example_u1_hol](/corpus/taulib/docs/book-iv-electroweak-photon-mode/example-u1-hol/) | L328-L328 | definition | definition | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l329/) | L329-L329 | computed check | computed check | — |
| `eval` | [#eval L330](/corpus/taulib/docs/book-iv-electroweak-photon-mode/eval-l330/) | L330-L332 | computed check | computed check | — |
