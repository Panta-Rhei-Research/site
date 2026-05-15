---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.NonlinearEinstein",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_slug": "book-v-gravity-field-nonlinear-einstein",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/NonlinearEinstein.lean",
  "sha256": "28df1aa3267845871d41d272e445a9a99d3b6b0dcbeac7c6da68da1150fe0c16",
  "imports": [
    "TauLib.BookV.GravityField.LinearEinstein"
  ],
  "imported_by": [
    "TauLib.BookV"
  ],
  "registry_ids": [
    "V.D54",
    "V.D55",
    "V.D56",
    "V.D57",
    "V.D58",
    "V.D59",
    "V.D60",
    "V.P15",
    "V.P16",
    "V.R77",
    "V.R80",
    "V.T33",
    "V.T34",
    "V.T35",
    "V.T36",
    "V.T37"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 11,
    "theorem": 7,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CocycleDefect",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/cocycle-defect/",
      "source_line_start": 90,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D54"
      ]
    },
    {
      "kind": "def",
      "name": "CocycleDefect.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/to-float/",
      "source_line_start": 102,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CocycleDefect.is_zero",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/is-zero/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NFEinsteinIteration",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nfeinstein-iteration/",
      "source_line_start": 124,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D55"
      ]
    },
    {
      "kind": "structure",
      "name": "TruncationCoherentStep",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/truncation-coherent-step/",
      "source_line_start": 145,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D56"
      ]
    },
    {
      "kind": "structure",
      "name": "DensitySaturation",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-saturation/",
      "source_line_start": 178,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D57"
      ]
    },
    {
      "kind": "def",
      "name": "DensitySaturation.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/to-float-l194/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NullAtDepth",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/null-at-depth/",
      "source_line_start": 206,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D58"
      ]
    },
    {
      "kind": "structure",
      "name": "PresentSurface",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/present-surface/",
      "source_line_start": 232,
      "source_line_end": 241,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D59"
      ]
    },
    {
      "kind": "structure",
      "name": "TauHorizon",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/tau-horizon/",
      "source_line_start": 257,
      "source_line_end": 274,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D60"
      ]
    },
    {
      "kind": "def",
      "name": "TauHorizon.radiusFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/radius-float/",
      "source_line_start": 277,
      "source_line_end": 278,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nf_existence",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-existence/",
      "source_line_start": 290,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T33"
      ]
    },
    {
      "kind": "theorem",
      "name": "nf_uniqueness",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-uniqueness/",
      "source_line_start": 302,
      "source_line_end": 305,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T34"
      ]
    },
    {
      "kind": "theorem",
      "name": "minimal_defect_solution",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/minimal-defect-solution/",
      "source_line_start": 316,
      "source_line_end": 320,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T35"
      ]
    },
    {
      "kind": "theorem",
      "name": "density_bound",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-bound/",
      "source_line_start": 331,
      "source_line_end": 333,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T36"
      ]
    },
    {
      "kind": "theorem",
      "name": "causal_disconnection",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/causal-disconnection/",
      "source_line_start": 345,
      "source_line_end": 347,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T37"
      ]
    },
    {
      "kind": "theorem",
      "name": "nf_convergence",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-convergence/",
      "source_line_start": 358,
      "source_line_end": 361,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P15"
      ]
    },
    {
      "kind": "theorem",
      "name": "singularity_replaced",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/singularity-replaced/",
      "source_line_start": 370,
      "source_line_end": 372,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P16"
      ]
    },
    {
      "kind": "def",
      "name": "defect_step0",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-step0/",
      "source_line_start": 398,
      "source_line_end": 402,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R77",
        "V.R80"
      ]
    },
    {
      "kind": "def",
      "name": "defect_step1",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-step1/",
      "source_line_start": 404,
      "source_line_end": 408,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "defect_converged",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-converged/",
      "source_line_start": 410,
      "source_line_end": 414,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l416/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l417/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l418/",
      "source_line_start": 418,
      "source_line_end": 418,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "converged_nf",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/converged-nf/",
      "source_line_start": 421,
      "source_line_end": 425,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l427/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_saturation",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-saturation/",
      "source_line_start": 431,
      "source_line_end": 437,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l439/",
      "source_line_start": 439,
      "source_line_end": 439,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_horizon",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-horizon/",
      "source_line_start": 442,
      "source_line_end": 450,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l452/",
      "source_line_start": 452,
      "source_line_end": 452,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_surface",
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-surface/",
      "source_line_start": 455,
      "source_line_end": 457,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l459/",
      "source_line_start": 459,
      "source_line_end": 461,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean",
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
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/NonlinearEinstein.lean`
- SHA-256: `28df1aa3267845871d41d272e445a9a99d3b6b0dcbeac7c6da68da1150fe0c16`

## Registry Links

- `V.D54` — Cocycle defect
- `V.D55` — tau-NF Einstein iteration
- `V.D56` — Truncation-coherent descent
- `V.D57` — Density-saturated character
- `V.D58` — Null intertwiner
- `V.D59` — Present surface
- `V.D60` — tau-Horizon
- `V.P15` — Convergence in all regimes
- `V.P16` — Saturation replaces singularity
- `V.R77` — Why ``address''?
- `V.R80` — Extremal black holes
- `V.T33` — Existence
- `V.T34` — Uniqueness
- `V.T35` — Selection
- `V.T36` — Density cap
- `V.T37` — Horizon as present-surface contraction

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.LinearEinstein`

## Imported By

- `TauLib.BookV`

## Declaration Counts

- `def`: 11
- `eval`: 8
- `structure`: 7
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CocycleDefect](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/cocycle-defect/) | L90-L99 | type/data schema | type/data schema | `V.D54` |
| `def` | [CocycleDefect.toFloat](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/to-float/) | L102-L103 | data/computed value | data/computed value | — |
| `def` | [CocycleDefect.is_zero](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/is-zero/) | L106-L107 | data/computed value | data/computed value | — |
| `structure` | [NFEinsteinIteration](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nfeinstein-iteration/) | L124-L133 | type/data schema | type/data schema | `V.D55` |
| `structure` | [TruncationCoherentStep](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/truncation-coherent-step/) | L145-L160 | type/data schema | type/data schema | `V.D56` |
| `structure` | [DensitySaturation](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-saturation/) | L178-L191 | type/data schema | type/data schema | `V.D57` |
| `def` | [DensitySaturation.toFloat](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/to-float-l194/) | L194-L195 | data/computed value | data/computed value | — |
| `structure` | [NullAtDepth](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/null-at-depth/) | L206-L217 | type/data schema | type/data schema | `V.D58` |
| `structure` | [PresentSurface](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/present-surface/) | L232-L241 | type/data schema | type/data schema | `V.D59` |
| `structure` | [TauHorizon](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/tau-horizon/) | L257-L274 | type/data schema | type/data schema | `V.D60` |
| `def` | [TauHorizon.radiusFloat](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/radius-float/) | L277-L278 | data/computed value | data/computed value | — |
| `theorem` | [nf_existence](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-existence/) | L290-L292 | proof obligation | formal proof obligation checked | `V.T33` |
| `theorem` | [nf_uniqueness](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-uniqueness/) | L302-L305 | proof obligation | formal proof obligation checked | `V.T34` |
| `theorem` | [minimal_defect_solution](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/minimal-defect-solution/) | L316-L320 | proof obligation | formal proof obligation checked | `V.T35` |
| `theorem` | [density_bound](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-bound/) | L331-L333 | proof obligation | formal proof obligation checked | `V.T36` |
| `theorem` | [causal_disconnection](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/causal-disconnection/) | L345-L347 | proof obligation | formal proof obligation checked | `V.T37` |
| `theorem` | [nf_convergence](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-convergence/) | L358-L361 | proof obligation | formal proof obligation checked | `V.P15` |
| `theorem` | [singularity_replaced](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/singularity-replaced/) | L370-L372 | proof obligation | formal proof obligation checked | `V.P16` |
| `def` | [defect_step0](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-step0/) | L398-L402 | definition | definition | `V.R77`, `V.R80` |
| `def` | [defect_step1](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-step1/) | L404-L408 | definition | definition | — |
| `def` | [defect_converged](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-converged/) | L410-L414 | definition | definition | — |
| `eval` | [#eval L416](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l416/) | L416-L416 | computed check | computed check | — |
| `eval` | [#eval L417](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l417/) | L417-L417 | computed check | computed check | — |
| `eval` | [#eval L418](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l418/) | L418-L418 | computed check | computed check | — |
| `def` | [converged_nf](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/converged-nf/) | L421-L425 | definition | definition | — |
| `eval` | [#eval L427](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l427/) | L427-L427 | computed check | computed check | — |
| `eval` | [#eval L428](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l428/) | L428-L428 | computed check | computed check | — |
| `def` | [example_saturation](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-saturation/) | L431-L437 | definition | definition | — |
| `eval` | [#eval L439](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l439/) | L439-L439 | computed check | computed check | — |
| `def` | [example_horizon](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-horizon/) | L442-L450 | definition | definition | — |
| `eval` | [#eval L452](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l452/) | L452-L452 | computed check | computed check | — |
| `def` | [example_surface](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/example-surface/) | L455-L457 | definition | definition | — |
| `eval` | [#eval L459](/corpus/taulib/docs/book-v-gravity-field-nonlinear-einstein/eval-l459/) | L459-L461 | computed check | computed check | — |
