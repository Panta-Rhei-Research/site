---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.GravitationalConstant",
  "permalink": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.GravitationalConstant`.",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_slug": "book-v-gravity-gravitational-constant",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/GravitationalConstant.lean",
  "sha256": "2f671b06efd8e6ec87ae94f90fff3ea92f421d759e84e27371e8fbe8613be922",
  "imports": [
    "TauLib.BookI.Boundary.Iota",
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Gravity.CoRotorCoupling",
    "TauLib.BookV.Gravity.EinsteinEquation"
  ],
  "registry_ids": [
    "V.D01",
    "V.D02",
    "V.P01",
    "V.T01"
  ],
  "declaration_counts": {
    "structure": 2,
    "def": 9,
    "theorem": 5,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TorusVacuum",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/torus-vacuum/",
      "source_line_start": 74,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D01"
      ]
    },
    {
      "kind": "def",
      "name": "TorusVacuum.minorFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/minor-float/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusVacuum.majorFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/major-float/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusVacuum.ratioFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/ratio-float/",
      "source_line_start": 102,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "unit_torus_vacuum",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/unit-torus-vacuum/",
      "source_line_start": 111,
      "source_line_end": 119,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GravConstant",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/grav-constant/",
      "source_line_start": 138,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D02"
      ]
    },
    {
      "kind": "def",
      "name": "GravConstant.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/to-float/",
      "source_line_start": 150,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "g_tau_iota_factor_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-iota-factor-numer/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "g_tau_iota_factor_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-iota-factor-denom/",
      "source_line_start": 161,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_self_coupling_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-self-coupling-numer/",
      "source_line_start": 164,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_self_coupling_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-self-coupling-denom/",
      "source_line_start": 165,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_shape_ratio_holds",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/vacuum-shape-ratio-holds/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T01"
      ]
    },
    {
      "kind": "theorem",
      "name": "unit_torus_has_iota_ratio",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/unit-torus-has-iota-ratio/",
      "source_line_start": 179,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "g_tau_well_defined",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-well-defined/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P01"
      ]
    },
    {
      "kind": "theorem",
      "name": "gravity_coupling_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-coupling-positive/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "g_tau_factor_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-factor-positive/",
      "source_line_start": 196,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l204/",
      "source_line_start": 204,
      "source_line_end": 204,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l205/",
      "source_line_start": 205,
      "source_line_end": 205,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l206/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l213/",
      "source_line_start": 213,
      "source_line_end": 216,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean",
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
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Gravity/GravitationalConstant.lean`
- SHA-256: `2f671b06efd8e6ec87ae94f90fff3ea92f421d759e84e27371e8fbe8613be922`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Iota`
- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Gravity.CoRotorCoupling`
- `TauLib.BookV.Gravity.EinsteinEquation`

## Declaration Counts

- `def`: 9
- `eval`: 5
- `structure`: 2
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TorusVacuum](/corpus/taulib/docs/book-v-gravity-gravitational-constant/torus-vacuum/) | L74-L91 | type/data schema | type/data schema | `V.D01` |
| `def` | [TorusVacuum.minorFloat](/corpus/taulib/docs/book-v-gravity-gravitational-constant/minor-float/) | L94-L95 | data/computed value | data/computed value | — |
| `def` | [TorusVacuum.majorFloat](/corpus/taulib/docs/book-v-gravity-gravitational-constant/major-float/) | L98-L99 | data/computed value | data/computed value | — |
| `def` | [TorusVacuum.ratioFloat](/corpus/taulib/docs/book-v-gravity-gravitational-constant/ratio-float/) | L102-L103 | data/computed value | data/computed value | — |
| `def` | [unit_torus_vacuum](/corpus/taulib/docs/book-v-gravity-gravitational-constant/unit-torus-vacuum/) | L111-L119 | definition | definition | — |
| `structure` | [GravConstant](/corpus/taulib/docs/book-v-gravity-gravitational-constant/grav-constant/) | L138-L147 | type/data schema | type/data schema | `V.D02` |
| `def` | [GravConstant.toFloat](/corpus/taulib/docs/book-v-gravity-gravitational-constant/to-float/) | L150-L151 | data/computed value | data/computed value | — |
| `def` | [g_tau_iota_factor_numer](/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-iota-factor-numer/) | L160-L160 | data/computed value | data/computed value | — |
| `def` | [g_tau_iota_factor_denom](/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-iota-factor-denom/) | L161-L161 | data/computed value | data/computed value | — |
| `def` | [gravity_self_coupling_numer](/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-self-coupling-numer/) | L164-L164 | data/computed value | data/computed value | — |
| `def` | [gravity_self_coupling_denom](/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-self-coupling-denom/) | L165-L165 | data/computed value | data/computed value | — |
| `theorem` | [vacuum_shape_ratio_holds](/corpus/taulib/docs/book-v-gravity-gravitational-constant/vacuum-shape-ratio-holds/) | L173-L176 | proof obligation | formal proof obligation checked | `V.T01` |
| `theorem` | [unit_torus_has_iota_ratio](/corpus/taulib/docs/book-v-gravity-gravitational-constant/unit-torus-has-iota-ratio/) | L179-L182 | proof obligation | formal proof obligation checked | — |
| `theorem` | [g_tau_well_defined](/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-well-defined/) | L186-L188 | proof obligation | formal proof obligation checked | `V.P01` |
| `theorem` | [gravity_coupling_positive](/corpus/taulib/docs/book-v-gravity-gravitational-constant/gravity-coupling-positive/) | L191-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [g_tau_factor_positive](/corpus/taulib/docs/book-v-gravity-gravitational-constant/g-tau-factor-positive/) | L196-L198 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L204](/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l204/) | L204-L204 | computed check | computed check | — |
| `eval` | [#eval L205](/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l205/) | L205-L205 | computed check | computed check | — |
| `eval` | [#eval L206](/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l206/) | L206-L206 | computed check | computed check | — |
| `eval` | [#eval L209](/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l209/) | L209-L209 | computed check | computed check | — |
| `eval` | [#eval L213](/corpus/taulib/docs/book-v-gravity-gravitational-constant/eval-l213/) | L213-L216 | computed check | computed check | — |
