---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.TauEinsteinEq",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_slug": "book-v-gravity-field-tau-einstein-eq",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/TauEinsteinEq.lean",
  "sha256": "8060be497814cadd8908e516f2bb9baa228de43d2d13981353b03908be0b5c89",
  "imports": [
    "TauLib.BookV.GravityField.LorentzNoMinkowski"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.LinearEinstein"
  ],
  "registry_ids": [
    "V.C03",
    "V.D49",
    "V.D50",
    "V.D51",
    "V.R65",
    "V.R67",
    "V.R68",
    "V.T26",
    "V.T27"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 5,
    "theorem": 5,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CurvatureCharH",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/curvature-char-h/",
      "source_line_start": 82,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D49"
      ]
    },
    {
      "kind": "def",
      "name": "CurvatureCharH.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/to-float/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MatterCharField",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/matter-char-field/",
      "source_line_start": 116,
      "source_line_end": 131,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D50"
      ]
    },
    {
      "kind": "def",
      "name": "MatterCharField.total_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/total-numer/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "MatterCharField.totalFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/total-float/",
      "source_line_start": 138,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauEinsteinField",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/tau-einstein-field/",
      "source_line_start": 161,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D51"
      ]
    },
    {
      "kind": "theorem",
      "name": "bianchi_from_einstein",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/bianchi-from-einstein/",
      "source_line_start": 191,
      "source_line_end": 194,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C03"
      ]
    },
    {
      "kind": "theorem",
      "name": "chart_recovers_efe",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/chart-recovers-efe/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T26"
      ]
    },
    {
      "kind": "theorem",
      "name": "hartogs_from_boundary",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/hartogs-from-boundary/",
      "source_line_start": 223,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T27"
      ]
    },
    {
      "kind": "theorem",
      "name": "matter_three_sectors",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/matter-three-sectors/",
      "source_line_start": 232,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "curvature_is_gravity",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/curvature-is-gravity/",
      "source_line_start": 236,
      "source_line_end": 237,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_curvature",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/example-curvature/",
      "source_line_start": 271,
      "source_line_end": 276,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R65",
        "V.R67",
        "V.R68"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_matter",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/example-matter/",
      "source_line_start": 282,
      "source_line_end": 289,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 294,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean",
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
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/TauEinsteinEq.lean`
- SHA-256: `8060be497814cadd8908e516f2bb9baa228de43d2d13981353b03908be0b5c89`

## Registry Links

- `V.C03` — tau-Bianchi identity --- V.R01
- `V.D49` — Curvature character --- V.D04
- `V.D50` — Matter character --- V.D03
- `V.D51` — tau-Einstein equation --- V.D06
- `V.R65` — The GR coupling kappa_tau --- V.D05
- `V.R67` — Singularities are chart artifacts
- `V.R68` — No admissible refinement without compensation
- `V.T26` — Chart shadow recovery
- `V.T27` — Well-posedness via Hartogs

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.LorentzNoMinkowski`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.LinearEinstein`

## Declaration Counts

- `def`: 5
- `eval`: 4
- `structure`: 3
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CurvatureCharH](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/curvature-char-h/) | L82-L97 | type/data schema | type/data schema | `V.D49` |
| `def` | [CurvatureCharH.toFloat](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/to-float/) | L100-L101 | data/computed value | data/computed value | — |
| `structure` | [MatterCharField](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/matter-char-field/) | L116-L131 | type/data schema | type/data schema | `V.D50` |
| `def` | [MatterCharField.total_numer](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/total-numer/) | L134-L135 | data/computed value | data/computed value | — |
| `def` | [MatterCharField.totalFloat](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/total-float/) | L138-L139 | data/computed value | data/computed value | — |
| `structure` | [TauEinsteinField](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/tau-einstein-field/) | L161-L174 | type/data schema | type/data schema | `V.D51` |
| `theorem` | [bianchi_from_einstein](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/bianchi-from-einstein/) | L191-L194 | proof obligation | formal proof obligation checked | `V.C03` |
| `theorem` | [chart_recovers_efe](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/chart-recovers-efe/) | L206-L208 | proof obligation | formal proof obligation checked | `V.T26` |
| `theorem` | [hartogs_from_boundary](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/hartogs-from-boundary/) | L223-L225 | proof obligation | formal proof obligation checked | `V.T27` |
| `theorem` | [matter_three_sectors](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/matter-three-sectors/) | L232-L233 | proof obligation | formal proof obligation checked | — |
| `theorem` | [curvature_is_gravity](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/curvature-is-gravity/) | L236-L237 | proof obligation | formal proof obligation checked | — |
| `def` | [example_curvature](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/example-curvature/) | L271-L276 | definition | definition | `V.R65`, `V.R67`, `V.R68` |
| `eval` | [#eval L278](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l279/) | L279-L279 | computed check | computed check | — |
| `def` | [example_matter](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/example-matter/) | L282-L289 | definition | definition | — |
| `eval` | [#eval L291](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l291/) | L291-L291 | computed check | computed check | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-v-gravity-field-tau-einstein-eq/eval-l292/) | L292-L294 | computed check | computed check | — |
