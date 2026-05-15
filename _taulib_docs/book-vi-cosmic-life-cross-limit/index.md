---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.CosmicLife.CrossLimit",
  "permalink": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_slug": "book-vi-cosmic-life-cross-limit",
  "book": "BookVI",
  "family": "CosmicLife",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/CosmicLife/CrossLimit.lean",
  "sha256": "ebb43e04c8aad0fe2c5430cf9770e1a7da6facc493a277d9b577eafa371eeacc",
  "imports": [
    "TauLib.BookVI.CosmicLife.BHSelfDesc",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.CosmicLife.GalaxyBasin",
    "TauLib.Tour.GuidedTour.BookVI",
    "TauLib.Tour.LifeFromPhysics"
  ],
  "registry_ids": [
    "V.D171",
    "V.D172",
    "V.T112",
    "V.T116",
    "V.T117",
    "VI.D60",
    "VI.D61",
    "VI.L11",
    "VI.T31",
    "VI.T35",
    "VI.T36"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 6,
    "theorem": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "OmegaRepresentative",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/omega-representative/",
      "source_line_start": 43,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D60"
      ]
    },
    {
      "kind": "def",
      "name": "omega_rep",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/omega-rep/",
      "source_line_start": 56,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LiftOmegaConstructor",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/lift-omega-constructor/",
      "source_line_start": 67,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D61"
      ]
    },
    {
      "kind": "def",
      "name": "lift_omega",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/lift-omega/",
      "source_line_start": 80,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_approx",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-approx/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_stage4_numer",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-stage4-numer/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_stage4_denom",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-stage4-denom/",
      "source_line_start": 93,
      "source_line_end": 93,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_convergence",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-convergence/",
      "source_line_start": 102,
      "source_line_end": 106,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VI.L11"
      ]
    },
    {
      "kind": "structure",
      "name": "FusionConvergence",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-convergence/",
      "source_line_start": 117,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T31"
      ]
    },
    {
      "kind": "def",
      "name": "fusion_conv",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-conv/",
      "source_line_start": 128,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fusion_convergence",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-convergence-l130/",
      "source_line_start": 130,
      "source_line_end": 134,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CrossingLimitTheorem",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit-theorem/",
      "source_line_start": 144,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T35"
      ]
    },
    {
      "kind": "def",
      "name": "crossing_limit",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "crossing_limit_theorem",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit-theorem-l159/",
      "source_line_start": 159,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UniversalBH",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh/",
      "source_line_start": 175,
      "source_line_end": 184,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T36"
      ]
    },
    {
      "kind": "def",
      "name": "universal_bh",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh-l186/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "universal_bh_alive",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh-alive/",
      "source_line_start": 190,
      "source_line_end": 196,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean",
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
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/CosmicLife/CrossLimit.lean`
- SHA-256: `ebb43e04c8aad0fe2c5430cf9770e1a7da6facc493a277d9b577eafa371eeacc`

## Registry Links

- `V.D171` — Blueprint fusion mathrmFuse
- `V.D172` — Blueprint Monoid
- `V.T112` — Blueprint Monoid Closure
- `V.T116` — Finite Motif Theorem
- `V.T117` — Saturation Radius Theorem
- `VI.D60` — ω-Representative of Life
- `VI.D61` — Lift_ω Constructor
- `VI.L11` — Primorial Ladder Convergence
- `VI.T31` — BH ω-Representative: Fusion Convergence
- `VI.T35` — Crossing-Limit Theorem
- `VI.T36` — Universal BH = Fully Alive State

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.CosmicLife.BHSelfDesc`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.CosmicLife.GalaxyBasin`
- `TauLib.Tour.GuidedTour.BookVI`
- `TauLib.Tour.LifeFromPhysics`

## Declaration Counts

- `def`: 6
- `structure`: 5
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [OmegaRepresentative](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/omega-representative/) | L43-L54 | type/data schema | type/data schema | `VI.D60` |
| `def` | [omega_rep](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/omega-rep/) | L56-L58 | definition | definition | — |
| `structure` | [LiftOmegaConstructor](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/lift-omega-constructor/) | L67-L78 | type/data schema | type/data schema | `VI.D61` |
| `def` | [lift_omega](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/lift-omega/) | L80-L80 | definition | definition | — |
| `def` | [primorial_approx](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-approx/) | L87-L88 | data/computed value | data/computed value | — |
| `theorem` | [primorial_stage4_numer](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-stage4-numer/) | L92-L92 | proof obligation | formal proof obligation checked | — |
| `theorem` | [primorial_stage4_denom](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-stage4-denom/) | L93-L93 | proof obligation | formal proof obligation checked | — |
| `theorem` | [primorial_convergence](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-convergence/) | L102-L106 | proof obligation | formal proof obligation checked | `VI.L11` |
| `structure` | [FusionConvergence](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-convergence/) | L117-L126 | type/data schema | type/data schema | `VI.T31` |
| `def` | [fusion_conv](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-conv/) | L128-L128 | definition | definition | — |
| `theorem` | [fusion_convergence](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-convergence-l130/) | L130-L134 | proof obligation | formal proof obligation checked | — |
| `structure` | [CrossingLimitTheorem](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit-theorem/) | L144-L155 | type/data schema | type/data schema | `VI.T35` |
| `def` | [crossing_limit](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit/) | L157-L157 | definition | definition | — |
| `theorem` | [crossing_limit_theorem](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit-theorem-l159/) | L159-L164 | proof obligation | formal proof obligation checked | — |
| `structure` | [UniversalBH](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh/) | L175-L184 | type/data schema | type/data schema | `VI.T36` |
| `def` | [universal_bh](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh-l186/) | L186-L188 | definition | definition | — |
| `theorem` | [universal_bh_alive](/corpus/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh-alive/) | L190-L196 | proof obligation | formal proof obligation checked | — |
