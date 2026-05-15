---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.FrameHolonomy",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/clopen-frame/",
      "source_line_start": 71,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D41"
      ]
    },
    {
      "kind": "def",
      "name": "ClopenFrame.same_depth",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/same-depth/",
      "source_line_start": 85,
      "source_line_end": 86,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FrameHolonomy",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/frame-holonomy/",
      "source_line_start": 101,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D42"
      ]
    },
    {
      "kind": "def",
      "name": "FrameHolonomy.gapFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gap-float/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LocalGap",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/local-gap/",
      "source_line_start": 133,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D43"
      ]
    },
    {
      "kind": "def",
      "name": "LocalGap.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TorusVacuumRestated",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/torus-vacuum-restated/",
      "source_line_start": 163,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D44"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_torus_restated",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-torus-restated/",
      "source_line_start": 172,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GTauFromShape",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gtau-from-shape/",
      "source_line_start": 188,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D45"
      ]
    },
    {
      "kind": "def",
      "name": "g_tau_from_shape",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/g-tau-from-shape/",
      "source_line_start": 201,
      "source_line_end": 207,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GTauFromShape.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l210/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GravitationalCoupling",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gravitational-coupling/",
      "source_line_start": 226,
      "source_line_end": 238,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D46"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_grav_coupling",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-grav-coupling/",
      "source_line_start": 241,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GravitationalCoupling.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l248/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_complement",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement/",
      "source_line_start": 261,
      "source_line_end": 263,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C01"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_complement_sectors",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement-sectors/",
      "source_line_start": 266,
      "source_line_end": 268,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "d_sector_holonomy_gap",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/d-sector-holonomy-gap/",
      "source_line_start": 279,
      "source_line_end": 281,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T20"
      ]
    },
    {
      "kind": "theorem",
      "name": "shape_ratio_is_iota",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/shape-ratio-is-iota/",
      "source_line_start": 289,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T21"
      ]
    },
    {
      "kind": "theorem",
      "name": "g_from_iota_squared",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/g-from-iota-squared/",
      "source_line_start": 301,
      "source_line_end": 306,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T22"
      ]
    },
    {
      "kind": "theorem",
      "name": "kappa_sigma_fixed_thm",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/kappa-sigma-fixed-thm/",
      "source_line_start": 314,
      "source_line_end": 315,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T23"
      ]
    },
    {
      "kind": "theorem",
      "name": "frame_adjacency_coherent",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/frame-adjacency-coherent/",
      "source_line_start": 323,
      "source_line_end": 325,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P10"
      ]
    },
    {
      "kind": "theorem",
      "name": "gap_refinement_invariant",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gap-refinement-invariant/",
      "source_line_start": 334,
      "source_line_end": 336,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P11"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R56"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 354,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_holonomy",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/example-holonomy/",
      "source_line_start": 357,
      "source_line_end": 362,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l364/",
      "source_line_start": 364,
      "source_line_end": 364,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_gap",
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/example-gap/",
      "source_line_start": 366,
      "source_line_end": 372,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 376,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [ClopenFrame](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/clopen-frame/) | L71-L82 | type/data schema | type/data schema | `V.D41` |
| `def` | [ClopenFrame.same_depth](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/same-depth/) | L85-L86 | data/computed value | data/computed value | — |
| `structure` | [FrameHolonomy](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/frame-holonomy/) | L101-L114 | type/data schema | type/data schema | `V.D42` |
| `def` | [FrameHolonomy.gapFloat](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gap-float/) | L117-L118 | data/computed value | data/computed value | — |
| `structure` | [LocalGap](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/local-gap/) | L133-L146 | type/data schema | type/data schema | `V.D43` |
| `def` | [LocalGap.toFloat](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float/) | L149-L150 | data/computed value | data/computed value | — |
| `structure` | [TorusVacuumRestated](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/torus-vacuum-restated/) | L163-L169 | type/data schema | type/data schema | `V.D44` |
| `def` | [canonical_torus_restated](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-torus-restated/) | L172-L174 | definition | definition | — |
| `structure` | [GTauFromShape](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gtau-from-shape/) | L188-L198 | type/data schema | type/data schema | `V.D45` |
| `def` | [g_tau_from_shape](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/g-tau-from-shape/) | L201-L207 | definition | definition | — |
| `def` | [GTauFromShape.toFloat](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l210/) | L210-L211 | data/computed value | data/computed value | — |
| `structure` | [GravitationalCoupling](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gravitational-coupling/) | L226-L238 | type/data schema | type/data schema | `V.D46` |
| `def` | [canonical_grav_coupling](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/canonical-grav-coupling/) | L241-L245 | definition | definition | — |
| `def` | [GravitationalCoupling.toFloat](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l248/) | L248-L249 | data/computed value | data/computed value | — |
| `theorem` | [temporal_complement](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement/) | L261-L263 | proof obligation | formal proof obligation checked | `V.C01` |
| `theorem` | [temporal_complement_sectors](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement-sectors/) | L266-L268 | proof obligation | formal proof obligation checked | — |
| `theorem` | [d_sector_holonomy_gap](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/d-sector-holonomy-gap/) | L279-L281 | proof obligation | formal proof obligation checked | `V.T20` |
| `theorem` | [shape_ratio_is_iota](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/shape-ratio-is-iota/) | L289-L292 | proof obligation | formal proof obligation checked | `V.T21` |
| `theorem` | [g_from_iota_squared](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/g-from-iota-squared/) | L301-L306 | proof obligation | formal proof obligation checked | `V.T22` |
| `theorem` | [kappa_sigma_fixed_thm](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/kappa-sigma-fixed-thm/) | L314-L315 | proof obligation | formal proof obligation checked | `V.T23` |
| `theorem` | [frame_adjacency_coherent](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/frame-adjacency-coherent/) | L323-L325 | proof obligation | formal proof obligation checked | `V.P10` |
| `theorem` | [gap_refinement_invariant](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/gap-refinement-invariant/) | L334-L336 | proof obligation | formal proof obligation checked | `V.P11` |
| `eval` | [#eval L350](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l350/) | L350-L350 | computed check | computed check | `V.R56` |
| `eval` | [#eval L351](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l351/) | L351-L351 | computed check | computed check | — |
| `eval` | [#eval L353](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l353/) | L353-L354 | computed check | computed check | — |
| `def` | [example_holonomy](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/example-holonomy/) | L357-L362 | definition | definition | — |
| `eval` | [#eval L364](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l364/) | L364-L364 | computed check | computed check | — |
| `def` | [example_gap](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/example-gap/) | L366-L372 | definition | definition | — |
| `eval` | [#eval L374](/corpus/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l374/) | L374-L376 | computed check | computed check | — |
