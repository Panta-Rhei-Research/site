---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.TauMHD",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
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
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mhdapprox/",
      "source_line_start": 71,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauMHDSystem",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/tau-mhdsystem/",
      "source_line_start": 85,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "V.D107"
      ]
    },
    {
      "kind": "def",
      "name": "TauMHDSystem.magReynolds",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mag-reynolds/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagneticPressureTension",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-pressure-tension/",
      "source_line_start": 114,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": [
        "V.D108"
      ]
    },
    {
      "kind": "theorem",
      "name": "tension_pressure_ratio",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/tension-pressure-ratio/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FrozenFluxTheorem",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem/",
      "source_line_start": 142,
      "source_line_end": 149,
      "formal_status": "defined",
      "registry_ids": [
        "V.T75"
      ]
    },
    {
      "kind": "theorem",
      "name": "frozen_flux_theorem",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem-l152/",
      "source_line_start": 152,
      "source_line_end": 153,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "DynamoType",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-type/",
      "source_line_start": 160,
      "source_line_end": 167,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MHDDynamo",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mhddynamo/",
      "source_line_start": 174,
      "source_line_end": 183,
      "formal_status": "defined",
      "registry_ids": [
        "V.D109"
      ]
    },
    {
      "kind": "theorem",
      "name": "dynamo_requires_broken_symmetry",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-requires-broken-symmetry/",
      "source_line_start": 186,
      "source_line_end": 189,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetic_energy_bound",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-energy-bound/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P49"
      ]
    },
    {
      "kind": "structure",
      "name": "ReconnectionEvent",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-event/",
      "source_line_start": 214,
      "source_line_end": 221,
      "formal_status": "defined",
      "registry_ids": [
        "V.D110"
      ]
    },
    {
      "kind": "structure",
      "name": "ReconnectionRate",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate/",
      "source_line_start": 235,
      "source_line_end": 240,
      "formal_status": "defined",
      "registry_ids": [
        "V.P50"
      ]
    },
    {
      "kind": "theorem",
      "name": "reconnection_rate",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate-l243/",
      "source_line_start": 243,
      "source_line_end": 246,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ForceFreeConfig",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-config/",
      "source_line_start": 257,
      "source_line_end": 264,
      "formal_status": "defined",
      "registry_ids": [
        "V.P51"
      ]
    },
    {
      "kind": "theorem",
      "name": "force_free_equilibrium",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-equilibrium/",
      "source_line_start": 267,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FastReconnectionRate",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate/",
      "source_line_start": 283,
      "source_line_end": 296,
      "formal_status": "defined",
      "registry_ids": [
        "V.D311"
      ]
    },
    {
      "kind": "def",
      "name": "fast_reconnection_rate_tau",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate-tau/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fast_reconnection_is_iota_sq",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-is-iota-sq/",
      "source_line_start": 310,
      "source_line_end": 311,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T252"
      ]
    },
    {
      "kind": "structure",
      "name": "SolarFlareConsistency",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency/",
      "source_line_start": 322,
      "source_line_end": 331,
      "formal_status": "defined",
      "registry_ids": [
        "V.P172"
      ]
    },
    {
      "kind": "def",
      "name": "solar_flare_consistency",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_mhd",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-mhd/",
      "source_line_start": 353,
      "source_line_end": 358,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l360/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l361/",
      "source_line_start": 361,
      "source_line_end": 361,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_mpt",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-mpt/",
      "source_line_start": 364,
      "source_line_end": 369,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l371/",
      "source_line_start": 371,
      "source_line_end": 371,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l372/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_reconnection",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-reconnection/",
      "source_line_start": 375,
      "source_line_end": 377,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 381,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [MHDApprox](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mhdapprox/) | L71-L78 | defined | — |
| `structure` | [TauMHDSystem](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/tau-mhdsystem/) | L85-L98 | defined | `V.D107` |
| `def` | [TauMHDSystem.magReynolds](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mag-reynolds/) | L101-L102 | defined | — |
| `structure` | [MagneticPressureTension](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-pressure-tension/) | L114-L125 | defined | `V.D108` |
| `theorem` | [tension_pressure_ratio](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/tension-pressure-ratio/) | L128-L129 | formalized | — |
| `structure` | [FrozenFluxTheorem](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem/) | L142-L149 | defined | `V.T75` |
| `theorem` | [frozen_flux_theorem](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem-l152/) | L152-L153 | formalized | — |
| `inductive` | [DynamoType](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-type/) | L160-L167 | defined | — |
| `structure` | [MHDDynamo](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mhddynamo/) | L174-L183 | defined | `V.D109` |
| `theorem` | [dynamo_requires_broken_symmetry](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/dynamo-requires-broken-symmetry/) | L186-L189 | formalized | — |
| `theorem` | [magnetic_energy_bound](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-energy-bound/) | L201-L203 | formalized | `V.P49` |
| `structure` | [ReconnectionEvent](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-event/) | L214-L221 | defined | `V.D110` |
| `structure` | [ReconnectionRate](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate/) | L235-L240 | defined | `V.P50` |
| `theorem` | [reconnection_rate](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate-l243/) | L243-L246 | formalized | — |
| `structure` | [ForceFreeConfig](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-config/) | L257-L264 | defined | `V.P51` |
| `theorem` | [force_free_equilibrium](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-equilibrium/) | L267-L269 | formalized | — |
| `structure` | [FastReconnectionRate](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate/) | L283-L296 | defined | `V.D311` |
| `def` | [fast_reconnection_rate_tau](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate-tau/) | L299-L299 | defined | — |
| `theorem` | [fast_reconnection_is_iota_sq](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-is-iota-sq/) | L310-L311 | formalized | `V.T252` |
| `structure` | [SolarFlareConsistency](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency/) | L322-L331 | defined | `V.P172` |
| `def` | [solar_flare_consistency](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency-l334/) | L334-L334 | defined | — |
| `def` | [example_mhd](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-mhd/) | L353-L358 | defined | — |
| `eval` | [#eval L360](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l360/) | L360-L360 | computed | — |
| `eval` | [#eval L361](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l361/) | L361-L361 | computed | — |
| `def` | [example_mpt](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-mpt/) | L364-L369 | defined | — |
| `eval` | [#eval L371](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l371/) | L371-L371 | computed | — |
| `eval` | [#eval L372](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l372/) | L372-L372 | computed | — |
| `def` | [example_reconnection](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/example-reconnection/) | L375-L377 | defined | — |
| `eval` | [#eval L379](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/eval-l379/) | L379-L381 | computed | — |
