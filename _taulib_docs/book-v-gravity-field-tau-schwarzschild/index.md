---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.TauSchwarzschild",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_slug": "book-v-gravity-field-tau-schwarzschild",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/TauSchwarzschild.lean",
  "sha256": "38d6bbd519fa2b3d7ce083d877952b863f8130a7f8668c3b65b02e3a5b93a5a0",
  "imports": [
    "TauLib.BookV.Gravity.Schwarzschild"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.TOVStarBuilder",
    "TauLib.BookV.GravityField.TauSchwarzschildScale"
  ],
  "registry_ids": [
    "V.D61",
    "V.D62",
    "V.D63",
    "V.D64",
    "V.D65",
    "V.P17",
    "V.P18",
    "V.R82",
    "V.R85",
    "V.R87",
    "V.R88",
    "V.T38",
    "V.T39",
    "V.T40",
    "V.T41"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 5,
    "theorem": 6,
    "inductive": 1,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "FieldTorusVacuum",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-torus-vacuum/",
      "source_line_start": 65,
      "source_line_end": 72,
      "formal_status": "defined",
      "registry_ids": [
        "V.D61"
      ]
    },
    {
      "kind": "def",
      "name": "vacuum_is_regular",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/vacuum-is-regular/",
      "source_line_start": 75,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": [
        "V.P18"
      ]
    },
    {
      "kind": "structure",
      "name": "FieldGravConstant",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-grav-constant/",
      "source_line_start": 86,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": [
        "V.D62"
      ]
    },
    {
      "kind": "theorem",
      "name": "field_g_tau_well_defined",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-g-tau-well-defined/",
      "source_line_start": 94,
      "source_line_end": 96,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P17"
      ]
    },
    {
      "kind": "structure",
      "name": "GeometricRelaxation",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/geometric-relaxation/",
      "source_line_start": 107,
      "source_line_end": 120,
      "formal_status": "defined",
      "registry_ids": [
        "V.D63"
      ]
    },
    {
      "kind": "def",
      "name": "GeometricRelaxation.bindingFractionFloat",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/binding-fraction-float/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TopologicalRelaxation",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/topological-relaxation/",
      "source_line_start": 133,
      "source_line_end": 144,
      "formal_status": "defined",
      "registry_ids": [
        "V.D64"
      ]
    },
    {
      "kind": "inductive",
      "name": "FieldEvolutionMode",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-evolution-mode/",
      "source_line_start": 154,
      "source_line_end": 161,
      "formal_status": "defined",
      "registry_ids": [
        "V.D65"
      ]
    },
    {
      "kind": "def",
      "name": "FieldEvolutionMode.changes_mass",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/changes-mass/",
      "source_line_start": 164,
      "source_line_end": 167,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_field_modes",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/five-field-modes/",
      "source_line_start": 170,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "field_vacuum_shape_ratio",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-vacuum-shape-ratio/",
      "source_line_start": 182,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T38"
      ]
    },
    {
      "kind": "theorem",
      "name": "chart_readout_schwarzschild",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/chart-readout-schwarzschild/",
      "source_line_start": 188,
      "source_line_end": 190,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T39"
      ]
    },
    {
      "kind": "theorem",
      "name": "field_schwarzschild_relation",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-schwarzschild-relation/",
      "source_line_start": 193,
      "source_line_end": 196,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T40"
      ]
    },
    {
      "kind": "theorem",
      "name": "field_no_shrink",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-no-shrink/",
      "source_line_start": 199,
      "source_line_end": 200,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T41"
      ]
    },
    {
      "kind": "def",
      "name": "example_field_vacuum",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/example-field-vacuum/",
      "source_line_start": 216,
      "source_line_end": 219,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_field_g",
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/example-field-g/",
      "source_line_start": 222,
      "source_line_end": 228,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 243,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l244/",
      "source_line_start": 244,
      "source_line_end": 246,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean",
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
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/TauSchwarzschild.lean`
- SHA-256: `38d6bbd519fa2b3d7ce083d877952b863f8130a7f8668c3b65b02e3a5b93a5a0`

## Registry Links

- `V.D61` — Torus vacuum --- V.D01
- `V.D62` — Gravitational constant --- V.D02
- `V.D63` — Geometric relaxation
- `V.D64` — Topological relaxation
- `V.D65` — BH evolution modes --- V.D09
- `V.P17` — G_tau well-defined --- V.P01
- `V.P18` — Schwarzschild regularity
- `V.R82` — Torus, not sphere
- `V.R85` — The torus core
- `V.R87` — Hawking evaporation forbidden --- V.R02
- `V.R88` — Chandrasekhar limit as maturity threshold --- V.R02
- `V.T38` — Vacuum shape ratio --- V.T01
- `V.T39` — Schwarzschild as readout
- `V.T40` — The tau-Schwarzschild relation --- V.D08
- `V.T41` — No-Shrink --- V.T03, preview

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Gravity.Schwarzschild`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.TOVStarBuilder`
- `TauLib.BookV.GravityField.TauSchwarzschildScale`

## Declaration Counts

- `def`: 5
- `eval`: 9
- `inductive`: 1
- `structure`: 4
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [FieldTorusVacuum](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-torus-vacuum/) | L65-L72 | defined | `V.D61` |
| `def` | [vacuum_is_regular](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/vacuum-is-regular/) | L75-L76 | defined | `V.P18` |
| `structure` | [FieldGravConstant](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-grav-constant/) | L86-L91 | defined | `V.D62` |
| `theorem` | [field_g_tau_well_defined](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-g-tau-well-defined/) | L94-L96 | formalized | `V.P17` |
| `structure` | [GeometricRelaxation](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/geometric-relaxation/) | L107-L120 | defined | `V.D63` |
| `def` | [GeometricRelaxation.bindingFractionFloat](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/binding-fraction-float/) | L123-L125 | defined | — |
| `structure` | [TopologicalRelaxation](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/topological-relaxation/) | L133-L144 | defined | `V.D64` |
| `inductive` | [FieldEvolutionMode](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-evolution-mode/) | L154-L161 | defined | `V.D65` |
| `def` | [FieldEvolutionMode.changes_mass](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/changes-mass/) | L164-L167 | defined | — |
| `theorem` | [five_field_modes](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/five-field-modes/) | L170-L175 | formalized | — |
| `theorem` | [field_vacuum_shape_ratio](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-vacuum-shape-ratio/) | L182-L185 | formalized | `V.T38` |
| `theorem` | [chart_readout_schwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/chart-readout-schwarzschild/) | L188-L190 | formalized | `V.T39` |
| `theorem` | [field_schwarzschild_relation](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-schwarzschild-relation/) | L193-L196 | formalized | `V.T40` |
| `theorem` | [field_no_shrink](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-no-shrink/) | L199-L200 | formalized | `V.T41` |
| `def` | [example_field_vacuum](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/example-field-vacuum/) | L216-L219 | defined | — |
| `def` | [example_field_g](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/example-field-g/) | L222-L228 | defined | — |
| `eval` | [#eval L234](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l234/) | L234-L234 | computed | — |
| `eval` | [#eval L235](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l235/) | L235-L235 | computed | — |
| `eval` | [#eval L236](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l236/) | L236-L236 | computed | — |
| `eval` | [#eval L238](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l238/) | L238-L238 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L241](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l241/) | L241-L241 | computed | — |
| `eval` | [#eval L242](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l242/) | L242-L242 | computed | — |
| `eval` | [#eval L243](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l243/) | L243-L243 | computed | — |
| `eval` | [#eval L244](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/eval-l244/) | L244-L246 | computed | — |
