---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.CalibrationTriangle",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_slug": "book-v-gravity-field-calibration-triangle",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/CalibrationTriangle.lean",
  "sha256": "2a7d8b76f3b6684049792f23efeafcf0a50fa2b1a8a7230f9e1e3278430b85d2",
  "imports": [
    "TauLib.BookV.GravityField.TOVPhaseBoundary"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.ClosingIdentity"
  ],
  "registry_ids": [
    "V.D78",
    "V.D79",
    "V.D80",
    "V.P22",
    "V.P23",
    "V.R100",
    "V.R101",
    "V.R102",
    "V.T49",
    "V.T50"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 3,
    "inductive": 1,
    "theorem": 6,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CalibrationConstant",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-constant/",
      "source_line_start": 72,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D78"
      ]
    },
    {
      "kind": "def",
      "name": "CalibrationConstant.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/to-float/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CalibrationVertex",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-vertex/",
      "source_line_start": 94,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CalibrationTriangle",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle/",
      "source_line_start": 112,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D79"
      ]
    },
    {
      "kind": "def",
      "name": "calibration_triangle",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle-l128/",
      "source_line_start": 128,
      "source_line_end": 134,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BoundaryHomomorphism",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/boundary-homomorphism/",
      "source_line_start": 150,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D80"
      ]
    },
    {
      "kind": "theorem",
      "name": "edge_ratios_from_iota",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/edge-ratios-from-iota/",
      "source_line_start": 170,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "dimensional_bridge_complete",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/dimensional-bridge-complete/",
      "source_line_start": 178,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T50"
      ]
    },
    {
      "kind": "theorem",
      "name": "xi_refinement_stable",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/xi-refinement-stable/",
      "source_line_start": 184,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P22"
      ]
    },
    {
      "kind": "theorem",
      "name": "a_sector_preserved",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/a-sector-preserved/",
      "source_line_start": 190,
      "source_line_end": 192,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P23"
      ]
    },
    {
      "kind": "theorem",
      "name": "three_distinct_vertices",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/three-distinct-vertices/",
      "source_line_start": 195,
      "source_line_end": 199,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "triangle_vertex_count",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/triangle-vertex-count/",
      "source_line_start": 202,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R100",
        "V.R101",
        "V.R102"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_xi",
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/example-xi/",
      "source_line_start": 229,
      "source_line_end": 232,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 237,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean",
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/CalibrationTriangle.lean`
- SHA-256: `2a7d8b76f3b6684049792f23efeafcf0a50fa2b1a8a7230f9e1e3278430b85d2`

## Registry Links

- `V.D78` — Calibration Constant Xi_tau
- `V.D79` — Calibration Triangle
- `V.D80` — Ring Homomorphism Phi_p,n
- `V.P22` — Xi_tau is refinement-stable
- `V.P23` — Phi_p,n
- `V.R100` — No SI units enter Xi_tau
- `V.R101` — The delta_A thread through the triangle
- `V.R102` — The unit problem in orthodox physics
- `V.T49` — Micro--Macro Bridge
- `V.T50` — Complete Dimensional Bridge

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.TOVPhaseBoundary`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.ClosingIdentity`

## Declaration Counts

- `def`: 3
- `eval`: 5
- `inductive`: 1
- `structure`: 3
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CalibrationConstant](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-constant/) | L72-L83 | type/data schema | type/data schema | `V.D78` |
| `def` | [CalibrationConstant.toFloat](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/to-float/) | L86-L87 | data/computed value | data/computed value | — |
| `inductive` | [CalibrationVertex](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-vertex/) | L94-L101 | type/data schema | type/data schema | — |
| `structure` | [CalibrationTriangle](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle/) | L112-L125 | type/data schema | type/data schema | `V.D79` |
| `def` | [calibration_triangle](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle-l128/) | L128-L134 | definition | definition | — |
| `structure` | [BoundaryHomomorphism](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/boundary-homomorphism/) | L150-L157 | type/data schema | type/data schema | `V.D80` |
| `theorem` | [edge_ratios_from_iota](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/edge-ratios-from-iota/) | L170-L172 | proof obligation | formal proof obligation checked | `V.T49` |
| `theorem` | [dimensional_bridge_complete](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/dimensional-bridge-complete/) | L178-L181 | proof obligation | formal proof obligation checked | `V.T50` |
| `theorem` | [xi_refinement_stable](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/xi-refinement-stable/) | L184-L186 | proof obligation | formal proof obligation checked | `V.P22` |
| `theorem` | [a_sector_preserved](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/a-sector-preserved/) | L190-L192 | proof obligation | formal proof obligation checked | `V.P23` |
| `theorem` | [three_distinct_vertices](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/three-distinct-vertices/) | L195-L199 | proof obligation | formal proof obligation checked | — |
| `theorem` | [triangle_vertex_count](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/triangle-vertex-count/) | L202-L204 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l224/) | L224-L224 | computed check | computed check | `V.R100`, `V.R101`, `V.R102` |
| `eval` | [#eval L225](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l225/) | L225-L225 | computed check | computed check | — |
| `eval` | [#eval L226](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l226/) | L226-L226 | computed check | computed check | — |
| `def` | [example_xi](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/example-xi/) | L229-L232 | definition | definition | — |
| `eval` | [#eval L234](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l234/) | L234-L234 | computed check | computed check | — |
| `eval` | [#eval L235](/corpus/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l235/) | L235-L237 | computed check | computed check | — |
