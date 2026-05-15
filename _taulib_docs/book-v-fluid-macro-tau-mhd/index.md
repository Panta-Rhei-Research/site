---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.TauMHD",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.TauMHD`.",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_slug": "book-v-fluid-macro-tau-mhd",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/TauMHD.lean",
  "sha256": "5d23e42c1ee3eb866d2a7fe0e463d7782e2c9006d70eeb1b6ea2ee7dc563409b",
  "imports": [
    "TauLib.BookV.FluidMacro.TauPlasma"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.TauAlfven"
  ],
  "registry_ids": [
    "V.D107",
    "V.D108",
    "V.D109",
    "V.D110",
    "V.D311",
    "V.P172",
    "V.P49",
    "V.P50",
    "V.P51",
    "V.R154",
    "V.R443",
    "V.R444",
    "V.T252",
    "V.T75"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 9,
    "def": 6,
    "theorem": 7,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "MHDApprox",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mhdapprox/",
      "source_line_start": 71,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauMHDSystem",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/tau-mhdsystem/",
      "source_line_start": 85,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D107"
      ]
    },
    {
      "kind": "def",
      "name": "TauMHDSystem.magReynolds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mag-reynolds/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagneticPressureTension",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-pressure-tension/",
      "source_line_start": 114,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D108"
      ]
    },
    {
      "kind": "theorem",
      "name": "tension_pressure_ratio",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/tension-pressure-ratio/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FrozenFluxTheorem",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem/",
      "source_line_start": 142,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T75"
      ]
    },
    {
      "kind": "theorem",
      "name": "frozen_flux_theorem",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem-l152/",
      "source_line_start": 152,
      "source_line_end": 153,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "DynamoType",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-type/",
      "source_line_start": 160,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MHDDynamo",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mhddynamo/",
      "source_line_start": 174,
      "source_line_end": 183,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D109"
      ]
    },
    {
      "kind": "theorem",
      "name": "dynamo_requires_broken_symmetry",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-requires-broken-symmetry/",
      "source_line_start": 186,
      "source_line_end": 189,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetic_energy_bound",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-energy-bound/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P49"
      ]
    },
    {
      "kind": "structure",
      "name": "ReconnectionEvent",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-event/",
      "source_line_start": 214,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D110"
      ]
    },
    {
      "kind": "structure",
      "name": "ReconnectionRate",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate/",
      "source_line_start": 235,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P50"
      ]
    },
    {
      "kind": "theorem",
      "name": "reconnection_rate",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate-l243/",
      "source_line_start": 243,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ForceFreeConfig",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-config/",
      "source_line_start": 257,
      "source_line_end": 264,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P51"
      ]
    },
    {
      "kind": "theorem",
      "name": "force_free_equilibrium",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-equilibrium/",
      "source_line_start": 267,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FastReconnectionRate",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate/",
      "source_line_start": 283,
      "source_line_end": 296,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D311"
      ]
    },
    {
      "kind": "def",
      "name": "fast_reconnection_rate_tau",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate-tau/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fast_reconnection_is_iota_sq",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-is-iota-sq/",
      "source_line_start": 310,
      "source_line_end": 311,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T252"
      ]
    },
    {
      "kind": "structure",
      "name": "SolarFlareConsistency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency/",
      "source_line_start": 322,
      "source_line_end": 331,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P172"
      ]
    },
    {
      "kind": "def",
      "name": "solar_flare_consistency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_mhd",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-mhd/",
      "source_line_start": 353,
      "source_line_end": 358,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l360/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l361/",
      "source_line_start": 361,
      "source_line_end": 361,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_mpt",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-mpt/",
      "source_line_start": 364,
      "source_line_end": 369,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l371/",
      "source_line_start": 371,
      "source_line_end": 371,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l372/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_reconnection",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-reconnection/",
      "source_line_start": 375,
      "source_line_end": 377,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 381,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/TauMHD.lean`
- SHA-256: `5d23e42c1ee3eb866d2a7fe0e463d7782e2c9006d70eeb1b6ea2ee7dc563409b`

## Registry Links

- `V.D107` — tau-MHD system
- `V.D108` — Magnetic Reynolds number
- `V.D109` — tau-reconnection event
- `V.D110` — MHD instability condition
- `V.D311` — Fast Reconnection Rate
- `V.P172` — Solar Flare Consistency
- `V.P49` — Reconnection energy bound
- `V.P50` — Alfv'en wave dispersion
- `V.P51` — Magnetosonic dispersion
- `V.R154` — Sweet--Parker and Petschek
- `V.R443` — Sweet-Parker vs τ-Rate
- `V.R444` — B-Sector Topological Transition
- `V.T252` — v_rec = ι_τ² v_A
- `V.T75` — Frozen-flux invariant

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.TauPlasma`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.TauAlfven`

## Declaration Counts

- `def`: 6
- `eval`: 5
- `inductive`: 2
- `structure`: 9
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [MHDApprox](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mhdapprox/) | L71-L78 | type/data schema | type/data schema | — |
| `structure` | [TauMHDSystem](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/tau-mhdsystem/) | L85-L98 | type/data schema | type/data schema | `V.D107` |
| `def` | [TauMHDSystem.magReynolds](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mag-reynolds/) | L101-L102 | data/computed value | data/computed value | — |
| `structure` | [MagneticPressureTension](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-pressure-tension/) | L114-L125 | type/data schema | type/data schema | `V.D108` |
| `theorem` | [tension_pressure_ratio](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/tension-pressure-ratio/) | L128-L129 | proof obligation | formal proof obligation checked | — |
| `structure` | [FrozenFluxTheorem](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem/) | L142-L149 | type/data schema | type/data schema | `V.T75` |
| `theorem` | [frozen_flux_theorem](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem-l152/) | L152-L153 | proof obligation | formal proof obligation checked | — |
| `inductive` | [DynamoType](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-type/) | L160-L167 | type/data schema | type/data schema | — |
| `structure` | [MHDDynamo](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mhddynamo/) | L174-L183 | type/data schema | type/data schema | `V.D109` |
| `theorem` | [dynamo_requires_broken_symmetry](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-requires-broken-symmetry/) | L186-L189 | proof obligation | formal proof obligation checked | — |
| `theorem` | [magnetic_energy_bound](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-energy-bound/) | L201-L203 | proof obligation | formal proof obligation checked | `V.P49` |
| `structure` | [ReconnectionEvent](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-event/) | L214-L221 | type/data schema | type/data schema | `V.D110` |
| `structure` | [ReconnectionRate](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate/) | L235-L240 | type/data schema | type/data schema | `V.P50` |
| `theorem` | [reconnection_rate](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate-l243/) | L243-L246 | proof obligation | formal proof obligation checked | — |
| `structure` | [ForceFreeConfig](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-config/) | L257-L264 | type/data schema | type/data schema | `V.P51` |
| `theorem` | [force_free_equilibrium](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-equilibrium/) | L267-L269 | proof obligation | formal proof obligation checked | — |
| `structure` | [FastReconnectionRate](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate/) | L283-L296 | type/data schema | type/data schema | `V.D311` |
| `def` | [fast_reconnection_rate_tau](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate-tau/) | L299-L299 | definition | definition | — |
| `theorem` | [fast_reconnection_is_iota_sq](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-is-iota-sq/) | L310-L311 | proof obligation | formal proof obligation checked | `V.T252` |
| `structure` | [SolarFlareConsistency](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency/) | L322-L331 | type/data schema | type/data schema | `V.P172` |
| `def` | [solar_flare_consistency](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency-l334/) | L334-L334 | definition | definition | — |
| `def` | [example_mhd](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-mhd/) | L353-L358 | definition | definition | — |
| `eval` | [#eval L360](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l360/) | L360-L360 | computed check | computed check | — |
| `eval` | [#eval L361](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l361/) | L361-L361 | computed check | computed check | — |
| `def` | [example_mpt](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-mpt/) | L364-L369 | definition | definition | — |
| `eval` | [#eval L371](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l371/) | L371-L371 | computed check | computed check | — |
| `eval` | [#eval L372](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l372/) | L372-L372 | computed check | computed check | — |
| `def` | [example_reconnection](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/example-reconnection/) | L375-L377 | definition | definition | — |
| `eval` | [#eval L379](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l379/) | L379-L381 | computed check | computed check | — |
