---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.FrameHolonomy",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.FrameHolonomy`.",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_slug": "book-v-gravity-field-frame-holonomy",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/FrameHolonomy.lean",
  "sha256": "15df2bb51826c48b39e9b6e42ba978a3e24851e52de797e16a0aa54d38f355f7",
  "imports": [
    "TauLib.BookV.Temporal.CosmicAPI",
    "TauLib.BookV.Gravity.EinsteinEquation",
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.LorentzNoMinkowski"
  ],
  "registry_ids": [
    "V.C01",
    "V.D41",
    "V.D42",
    "V.D43",
    "V.D44",
    "V.D45",
    "V.D46",
    "V.P10",
    "V.P11",
    "V.R56",
    "V.T20",
    "V.T21",
    "V.T22",
    "V.T23"
  ],
  "declaration_counts": {
    "structure": 6,
    "def": 10,
    "theorem": 8,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "ClopenFrame",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/clopen-frame/",
      "source_line_start": 71,
      "source_line_end": 82,
      "formal_status": "defined",
      "registry_ids": [
        "V.D41"
      ]
    },
    {
      "kind": "def",
      "name": "ClopenFrame.same_depth",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/same-depth/",
      "source_line_start": 85,
      "source_line_end": 86,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FrameHolonomy",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-holonomy/",
      "source_line_start": 101,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": [
        "V.D42"
      ]
    },
    {
      "kind": "def",
      "name": "FrameHolonomy.gapFloat",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gap-float/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LocalGap",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/local-gap/",
      "source_line_start": 133,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": [
        "V.D43"
      ]
    },
    {
      "kind": "def",
      "name": "LocalGap.toFloat",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TorusVacuumRestated",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/torus-vacuum-restated/",
      "source_line_start": 163,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "V.D44"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_torus_restated",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-torus-restated/",
      "source_line_start": 172,
      "source_line_end": 174,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GTauFromShape",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gtau-from-shape/",
      "source_line_start": 188,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": [
        "V.D45"
      ]
    },
    {
      "kind": "def",
      "name": "g_tau_from_shape",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/g-tau-from-shape/",
      "source_line_start": 201,
      "source_line_end": 207,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GTauFromShape.toFloat",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l210/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GravitationalCoupling",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gravitational-coupling/",
      "source_line_start": 226,
      "source_line_end": 238,
      "formal_status": "defined",
      "registry_ids": [
        "V.D46"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_grav_coupling",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-grav-coupling/",
      "source_line_start": 241,
      "source_line_end": 245,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GravitationalCoupling.toFloat",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l248/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_complement",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement/",
      "source_line_start": 261,
      "source_line_end": 263,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C01"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_complement_sectors",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement-sectors/",
      "source_line_start": 266,
      "source_line_end": 268,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "d_sector_holonomy_gap",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/d-sector-holonomy-gap/",
      "source_line_start": 279,
      "source_line_end": 281,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T20"
      ]
    },
    {
      "kind": "theorem",
      "name": "shape_ratio_is_iota",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/shape-ratio-is-iota/",
      "source_line_start": 289,
      "source_line_end": 292,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T21"
      ]
    },
    {
      "kind": "theorem",
      "name": "g_from_iota_squared",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/g-from-iota-squared/",
      "source_line_start": 301,
      "source_line_end": 306,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T22"
      ]
    },
    {
      "kind": "theorem",
      "name": "kappa_sigma_fixed_thm",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/kappa-sigma-fixed-thm/",
      "source_line_start": 314,
      "source_line_end": 315,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T23"
      ]
    },
    {
      "kind": "theorem",
      "name": "frame_adjacency_coherent",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-adjacency-coherent/",
      "source_line_start": 323,
      "source_line_end": 325,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P10"
      ]
    },
    {
      "kind": "theorem",
      "name": "gap_refinement_invariant",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gap-refinement-invariant/",
      "source_line_start": 334,
      "source_line_end": 336,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P11"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": [
        "V.R56"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_holonomy",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/example-holonomy/",
      "source_line_start": 357,
      "source_line_end": 362,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l364/",
      "source_line_start": 364,
      "source_line_end": 364,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_gap",
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/example-gap/",
      "source_line_start": 366,
      "source_line_end": 372,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 376,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/FrameHolonomy.lean`
- SHA-256: `15df2bb51826c48b39e9b6e42ba978a3e24851e52de797e16a0aa54d38f355f7`

## Registry Links

- `V.C01` — Temporal Complement, revisited
- `V.D41` — Clopen frame
- `V.D42` — Frame holonomy on tau^1
- `V.D43` — Holonomy gap element
- `V.D44` — Torus vacuum --- V.D01
- `V.D45` — Gravitational constant --- V.D02
- `V.D46` — Gravitational coupling kappa_tau
- `V.P10` — Frame transitions are boundary-determined
- `V.P11` — Gap refinement coherence
- `V.R56` — Lean formalization
- `V.T20` — Gravity as frame holonomy gap
- `V.T21` — Vacuum shape ratio --- V.T01
- `V.T22` — G derivation --- V.D02
- `V.T23` — sigma-equivariance of kappa_tau

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.CosmicAPI`
- `TauLib.BookV.Gravity.EinsteinEquation`
- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.LorentzNoMinkowski`

## Declaration Counts

- `def`: 10
- `eval`: 5
- `structure`: 6
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [ClopenFrame](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/clopen-frame/) | L71-L82 | defined | `V.D41` |
| `def` | [ClopenFrame.same_depth](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/same-depth/) | L85-L86 | defined | — |
| `structure` | [FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-holonomy/) | L101-L114 | defined | `V.D42` |
| `def` | [FrameHolonomy.gapFloat](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gap-float/) | L117-L118 | defined | — |
| `structure` | [LocalGap](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/local-gap/) | L133-L146 | defined | `V.D43` |
| `def` | [LocalGap.toFloat](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float/) | L149-L150 | defined | — |
| `structure` | [TorusVacuumRestated](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/torus-vacuum-restated/) | L163-L169 | defined | `V.D44` |
| `def` | [canonical_torus_restated](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-torus-restated/) | L172-L174 | defined | — |
| `structure` | [GTauFromShape](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gtau-from-shape/) | L188-L198 | defined | `V.D45` |
| `def` | [g_tau_from_shape](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/g-tau-from-shape/) | L201-L207 | defined | — |
| `def` | [GTauFromShape.toFloat](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l210/) | L210-L211 | defined | — |
| `structure` | [GravitationalCoupling](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gravitational-coupling/) | L226-L238 | defined | `V.D46` |
| `def` | [canonical_grav_coupling](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-grav-coupling/) | L241-L245 | defined | — |
| `def` | [GravitationalCoupling.toFloat](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l248/) | L248-L249 | defined | — |
| `theorem` | [temporal_complement](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement/) | L261-L263 | formalized | `V.C01` |
| `theorem` | [temporal_complement_sectors](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement-sectors/) | L266-L268 | formalized | — |
| `theorem` | [d_sector_holonomy_gap](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/d-sector-holonomy-gap/) | L279-L281 | formalized | `V.T20` |
| `theorem` | [shape_ratio_is_iota](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/shape-ratio-is-iota/) | L289-L292 | formalized | `V.T21` |
| `theorem` | [g_from_iota_squared](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/g-from-iota-squared/) | L301-L306 | formalized | `V.T22` |
| `theorem` | [kappa_sigma_fixed_thm](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/kappa-sigma-fixed-thm/) | L314-L315 | formalized | `V.T23` |
| `theorem` | [frame_adjacency_coherent](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-adjacency-coherent/) | L323-L325 | formalized | `V.P10` |
| `theorem` | [gap_refinement_invariant](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gap-refinement-invariant/) | L334-L336 | formalized | `V.P11` |
| `eval` | [#eval L350](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l350/) | L350-L350 | computed | `V.R56` |
| `eval` | [#eval L351](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l353/) | L353-L354 | computed | — |
| `def` | [example_holonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/example-holonomy/) | L357-L362 | defined | — |
| `eval` | [#eval L364](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l364/) | L364-L364 | computed | — |
| `def` | [example_gap](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/example-gap/) | L366-L372 | defined | — |
| `eval` | [#eval L374](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l374/) | L374-L376 | computed | — |
