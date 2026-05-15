---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.TOVStarBuilder",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_slug": "book-v-gravity-field-tovstar-builder",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/TOVStarBuilder.lean",
  "sha256": "109c9bb198750616c2d289dc8116e2c042a2cc66a82d0cb1a152f11446ba74e7",
  "imports": [
    "TauLib.BookV.GravityField.TauSchwarzschild"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.TOVPhaseBoundary"
  ],
  "registry_ids": [
    "V.D66",
    "V.D67",
    "V.D68",
    "V.D69",
    "V.D70",
    "V.D71",
    "V.D72",
    "V.D73",
    "V.D74",
    "V.P19",
    "V.P20",
    "V.P21",
    "V.R89",
    "V.R90",
    "V.R91",
    "V.R92",
    "V.R93",
    "V.T42",
    "V.T43",
    "V.T44"
  ],
  "declaration_counts": {
    "structure": 9,
    "def": 7,
    "theorem": 7,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "SphericalCarrier",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/spherical-carrier/",
      "source_line_start": 69,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D66"
      ]
    },
    {
      "kind": "def",
      "name": "SphericalCarrier.radiusFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/radius-float/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EquilibriumCarrier",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/equilibrium-carrier/",
      "source_line_start": 92,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D67"
      ]
    },
    {
      "kind": "structure",
      "name": "GRTensionFunctional",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/grtension-functional/",
      "source_line_start": 112,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D68"
      ]
    },
    {
      "kind": "def",
      "name": "GRTensionFunctional.tensionFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-float/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TensionProfile",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-profile/",
      "source_line_start": 133,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D69"
      ]
    },
    {
      "kind": "structure",
      "name": "StarBuilder",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder/",
      "source_line_start": 162,
      "source_line_end": 185,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D70"
      ]
    },
    {
      "kind": "structure",
      "name": "NeutronNode",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/neutron-node/",
      "source_line_start": 193,
      "source_line_end": 200,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D71"
      ]
    },
    {
      "kind": "structure",
      "name": "NodeDensity",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/node-density/",
      "source_line_start": 207,
      "source_line_end": 214,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D72"
      ]
    },
    {
      "kind": "def",
      "name": "NodeDensity.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/to-float/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EWStability",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/ewstability/",
      "source_line_start": 230,
      "source_line_end": 241,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D73"
      ]
    },
    {
      "kind": "structure",
      "name": "ChandrasekharThreshold",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-threshold/",
      "source_line_start": 254,
      "source_line_end": 265,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D74"
      ]
    },
    {
      "kind": "def",
      "name": "ChandrasekharThreshold.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/to-float-l268/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chandrasekhar_canonical",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-canonical/",
      "source_line_start": 272,
      "source_line_end": 276,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "star_builder_coherent",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder-coherent/",
      "source_line_start": 283,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T42"
      ]
    },
    {
      "kind": "theorem",
      "name": "interior_ew_stable",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/interior-ew-stable/",
      "source_line_start": 287,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "chandrasekhar_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-positive/",
      "source_line_start": 291,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "chandrasekhar_in_range",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-in-range/",
      "source_line_start": 295,
      "source_line_end": 298,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tension_bounded",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-bounded/",
      "source_line_start": 302,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P19"
      ]
    },
    {
      "kind": "theorem",
      "name": "tov_balance",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tov-balance/",
      "source_line_start": 306,
      "source_line_end": 308,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P20"
      ]
    },
    {
      "kind": "theorem",
      "name": "truncation_coherent",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/truncation-coherent/",
      "source_line_start": 312,
      "source_line_end": 313,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P21"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R89",
        "V.R90",
        "V.R91",
        "V.R92",
        "V.R93"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_node",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/example-node/",
      "source_line_start": 337,
      "source_line_end": 340,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_density",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/example-density/",
      "source_line_start": 347,
      "source_line_end": 350,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 354,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/TOVStarBuilder.lean`
- SHA-256: `109c9bb198750616c2d289dc8116e2c042a2cc66a82d0cb1a152f11446ba74e7`

## Registry Links

- `V.D66` — Spherical carrier predicate
- `V.D67` — Equilibrium carrier
- `V.D68` — GR tension functional
- `V.D69` — Tension profile
- `V.D70` — Canonical star builder
- `V.D71` — Neutron node
- `V.D72` — Node density and confinement tension
- `V.D73` — EW-stable node
- `V.D74` — Chandrasekhar threshold
- `V.P19` — Tension bounds
- `V.P20` — TOV balance as tension equilibrium
- `V.P21` — Truncation invariance of the star builder
- `V.R89` — Spherical neq static
- `V.R90` — The star builder as constructive proof
- `V.R91` — Not an ODE
- `V.R92` — No free parameter
- `V.R93` — The TOV maximum mass
- `V.T42` — Star builder existence and uniqueness
- `V.T43` — Neutron node EW stability
- `V.T44` — Chandrasekhar limit

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.TauSchwarzschild`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.TOVPhaseBoundary`

## Declaration Counts

- `def`: 7
- `eval`: 7
- `structure`: 9
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [SphericalCarrier](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/spherical-carrier/) | L69-L80 | type/data schema | type/data schema | `V.D66` |
| `def` | [SphericalCarrier.radiusFloat](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/radius-float/) | L83-L84 | data/computed value | data/computed value | — |
| `structure` | [EquilibriumCarrier](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/equilibrium-carrier/) | L92-L99 | type/data schema | type/data schema | `V.D67` |
| `structure` | [GRTensionFunctional](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/grtension-functional/) | L112-L121 | type/data schema | type/data schema | `V.D68` |
| `def` | [GRTensionFunctional.tensionFloat](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-float/) | L124-L125 | data/computed value | data/computed value | — |
| `structure` | [TensionProfile](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-profile/) | L133-L144 | type/data schema | type/data schema | `V.D69` |
| `structure` | [StarBuilder](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder/) | L162-L185 | type/data schema | type/data schema | `V.D70` |
| `structure` | [NeutronNode](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/neutron-node/) | L193-L200 | type/data schema | type/data schema | `V.D71` |
| `structure` | [NodeDensity](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/node-density/) | L207-L214 | type/data schema | type/data schema | `V.D72` |
| `def` | [NodeDensity.toFloat](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/to-float/) | L217-L218 | data/computed value | data/computed value | — |
| `structure` | [EWStability](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/ewstability/) | L230-L241 | type/data schema | type/data schema | `V.D73` |
| `structure` | [ChandrasekharThreshold](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-threshold/) | L254-L265 | type/data schema | type/data schema | `V.D74` |
| `def` | [ChandrasekharThreshold.toFloat](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/to-float-l268/) | L268-L269 | data/computed value | data/computed value | — |
| `def` | [chandrasekhar_canonical](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-canonical/) | L272-L276 | definition | definition | — |
| `theorem` | [star_builder_coherent](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder-coherent/) | L283-L284 | proof obligation | formal proof obligation checked | `V.T42` |
| `theorem` | [interior_ew_stable](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/interior-ew-stable/) | L287-L288 | proof obligation | formal proof obligation checked | `V.T43` |
| `theorem` | [chandrasekhar_positive](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-positive/) | L291-L292 | proof obligation | formal proof obligation checked | `V.T44` |
| `theorem` | [chandrasekhar_in_range](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-in-range/) | L295-L298 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tension_bounded](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tension-bounded/) | L302-L303 | proof obligation | formal proof obligation checked | `V.P19` |
| `theorem` | [tov_balance](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/tov-balance/) | L306-L308 | proof obligation | formal proof obligation checked | `V.P20` |
| `theorem` | [truncation_coherent](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/truncation-coherent/) | L312-L313 | proof obligation | formal proof obligation checked | `V.P21` |
| `eval` | [#eval L332](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l332/) | L332-L332 | computed check | computed check | `V.R89`, `V.R90`, `V.R91`, `V.R92`, `V.R93` |
| `eval` | [#eval L333](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l334/) | L334-L334 | computed check | computed check | — |
| `def` | [example_node](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/example-node/) | L337-L340 | definition | definition | — |
| `eval` | [#eval L342](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l342/) | L342-L342 | computed check | computed check | — |
| `eval` | [#eval L343](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l343/) | L343-L343 | computed check | computed check | — |
| `eval` | [#eval L344](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l344/) | L344-L344 | computed check | computed check | — |
| `def` | [example_density](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/example-density/) | L347-L350 | definition | definition | — |
| `eval` | [#eval L352](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l352/) | L352-L354 | computed check | computed check | — |
