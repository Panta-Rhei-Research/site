---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Regularity.PositiveRegularity",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Regularity.PositiveRegularity`.",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_slug": "book-ii-regularity-positive-regularity",
  "book": "BookII",
  "family": "Regularity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Regularity/PositiveRegularity.lean",
  "sha256": "e7973b0ccb665fced444ba426a411e70594c74a6e9f4c458bc8195c0aafb5b06",
  "imports": [
    "TauLib.BookII.Regularity.ThreeLemmaChain"
  ],
  "imported_by": [
    "TauLib.BookII"
  ],
  "registry_ids": [
    "II.D49",
    "II.T34"
  ],
  "declaration_counts": {
    "def": 12,
    "eval": 14,
    "theorem": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "b_stabilization_depth",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/b-stabilization-depth/",
      "source_line_start": 53,
      "source_line_end": 72,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "def",
      "name": "c_stabilization_depth",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/c-stabilization-depth/",
      "source_line_start": 76,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "def",
      "name": "regularity_depth",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-depth/",
      "source_line_start": 101,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "def",
      "name": "is_regular",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-regular/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "def",
      "name": "is_b_regular",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-b-regular/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "is_c_regular",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-c-regular/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "regularity_depth_max_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-depth-max-check/",
      "source_line_start": 153,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T34"
      ]
    },
    {
      "kind": "def",
      "name": "regularity_criterion_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-criterion-check/",
      "source_line_start": 179,
      "source_line_end": 192,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T34"
      ]
    },
    {
      "kind": "def",
      "name": "small_point_regularity_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/small-point-regularity-check/",
      "source_line_start": 201,
      "source_line_end": 211,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "evolution_stabilization_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/evolution-stabilization-check/",
      "source_line_start": 215,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "channel_stabilization_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/channel-stabilization-check/",
      "source_line_start": 248,
      "source_line_end": 282,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "full_regularity_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/full-regularity-check/",
      "source_line_start": 294,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l312/",
      "source_line_start": 312,
      "source_line_end": 312,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l313/",
      "source_line_start": 313,
      "source_line_end": 313,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l321/",
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
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l324/",
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
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l330/",
      "source_line_start": 330,
      "source_line_end": 330,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "depth_max_20_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/depth-max-20-4/",
      "source_line_start": 340,
      "source_line_end": 341,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T34"
      ]
    },
    {
      "kind": "theorem",
      "name": "criterion_20_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/criterion-20-4/",
      "source_line_start": 344,
      "source_line_end": 345,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T34"
      ]
    },
    {
      "kind": "theorem",
      "name": "small_point_3",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/small-point-3/",
      "source_line_start": 348,
      "source_line_end": 349,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "theorem",
      "name": "evolution_stab_20_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/evolution-stab-20-4/",
      "source_line_start": 352,
      "source_line_end": 353,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D49"
      ]
    },
    {
      "kind": "theorem",
      "name": "channel_stab_20_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/channel-stab-20-4/",
      "source_line_start": 356,
      "source_line_end": 357,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "full_regularity_15_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-positive-regularity/full-regularity-15-4/",
      "source_line_start": 360,
      "source_line_end": 363,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean",
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
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Regularity/PositiveRegularity.lean`
- SHA-256: `e7973b0ccb665fced444ba426a411e70594c74a6e9f4c458bc8195c0aafb5b06`

## Registry Links

- `II.D49` — Tau-Regularity
- `II.T34` — Regularity Criterion

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Regularity.ThreeLemmaChain`

## Imported By

- `TauLib.BookII`

## Declaration Counts

- `def`: 12
- `eval`: 14
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [b_stabilization_depth](/corpus/taulib/docs/book-ii-regularity-positive-regularity/b-stabilization-depth/) | L53-L72 | data/computed value | data/computed value | `II.D49` |
| `def` | [c_stabilization_depth](/corpus/taulib/docs/book-ii-regularity-positive-regularity/c-stabilization-depth/) | L76-L94 | data/computed value | data/computed value | `II.D49` |
| `def` | [regularity_depth](/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-depth/) | L101-L123 | data/computed value | data/computed value | `II.D49` |
| `def` | [is_regular](/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-regular/) | L132-L133 | data/computed value | data/computed value | `II.D49` |
| `def` | [is_b_regular](/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-b-regular/) | L136-L137 | data/computed value | data/computed value | — |
| `def` | [is_c_regular](/corpus/taulib/docs/book-ii-regularity-positive-regularity/is-c-regular/) | L140-L141 | data/computed value | data/computed value | — |
| `def` | [regularity_depth_max_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-depth-max-check/) | L153-L165 | data/computed value | data/computed value | `II.T34` |
| `def` | [regularity_criterion_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/regularity-criterion-check/) | L179-L192 | data/computed value | data/computed value | `II.T34` |
| `def` | [small_point_regularity_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/small-point-regularity-check/) | L201-L211 | data/computed value | data/computed value | — |
| `def` | [evolution_stabilization_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/evolution-stabilization-check/) | L215-L239 | data/computed value | data/computed value | — |
| `def` | [channel_stabilization_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/channel-stabilization-check/) | L248-L282 | data/computed value | data/computed value | — |
| `def` | [full_regularity_check](/corpus/taulib/docs/book-ii-regularity-positive-regularity/full-regularity-check/) | L294-L299 | data/computed value | data/computed value | — |
| `eval` | [#eval L306](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l306/) | L306-L306 | computed check | computed check | — |
| `eval` | [#eval L307](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l307/) | L307-L307 | computed check | computed check | — |
| `eval` | [#eval L308](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l308/) | L308-L308 | computed check | computed check | — |
| `eval` | [#eval L311](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l311/) | L311-L311 | computed check | computed check | — |
| `eval` | [#eval L312](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l312/) | L312-L312 | computed check | computed check | — |
| `eval` | [#eval L313](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l313/) | L313-L313 | computed check | computed check | — |
| `eval` | [#eval L314](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l314/) | L314-L314 | computed check | computed check | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l318/) | L318-L318 | computed check | computed check | — |
| `eval` | [#eval L321](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l321/) | L321-L321 | computed check | computed check | — |
| `eval` | [#eval L324](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l324/) | L324-L324 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l327/) | L327-L327 | computed check | computed check | — |
| `eval` | [#eval L330](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l330/) | L330-L330 | computed check | computed check | — |
| `eval` | [#eval L333](/corpus/taulib/docs/book-ii-regularity-positive-regularity/eval-l333/) | L333-L333 | computed check | computed check | — |
| `theorem` | [depth_max_20_4](/corpus/taulib/docs/book-ii-regularity-positive-regularity/depth-max-20-4/) | L340-L341 | proof obligation | formal proof obligation checked | `II.T34` |
| `theorem` | [criterion_20_4](/corpus/taulib/docs/book-ii-regularity-positive-regularity/criterion-20-4/) | L344-L345 | proof obligation | formal proof obligation checked | `II.T34` |
| `theorem` | [small_point_3](/corpus/taulib/docs/book-ii-regularity-positive-regularity/small-point-3/) | L348-L349 | proof obligation | formal proof obligation checked | `II.D49` |
| `theorem` | [evolution_stab_20_4](/corpus/taulib/docs/book-ii-regularity-positive-regularity/evolution-stab-20-4/) | L352-L353 | proof obligation | formal proof obligation checked | `II.D49` |
| `theorem` | [channel_stab_20_4](/corpus/taulib/docs/book-ii-regularity-positive-regularity/channel-stab-20-4/) | L356-L357 | proof obligation | formal proof obligation checked | — |
| `theorem` | [full_regularity_15_4](/corpus/taulib/docs/book-ii-regularity-positive-regularity/full-regularity-15-4/) | L360-L363 | proof obligation | formal proof obligation checked | — |
