---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.CoRotorCoupling",
  "permalink": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_slug": "book-v-gravity-co-rotor-coupling",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/CoRotorCoupling.lean",
  "sha256": "42d8cf07fee7bf9ff7184030d98b6da7a590e159fb82f9890ad0f4ab469b7b05",
  "imports": [
    "TauLib.BookI.Boundary.Iota",
    "TauLib.BookIV.Physics.LemniscateCapacity",
    "TauLib.BookV.Gravity.GravitationalConstant"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.ClosingIdentity"
  ],
  "registry_ids": [
    "V.D10",
    "V.D11",
    "V.P02",
    "V.R03",
    "V.T04",
    "V.T05"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 9,
    "theorem": 9,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CoRotorCoupling",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/co-rotor-coupling/",
      "source_line_start": 90,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D10"
      ]
    },
    {
      "kind": "def",
      "name": "c1_three_over_pi_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-three-over-pi-numer/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c1_three_over_pi_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-three-over-pi-denom/",
      "source_line_start": 115,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_coupling",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-coupling/",
      "source_line_start": 118,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kn_required_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-numer/",
      "source_line_start": 134,
      "source_line_end": 134,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kn_required_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-denom/",
      "source_line_start": 135,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kn_required_range",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-range/",
      "source_line_start": 143,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T04"
      ]
    },
    {
      "kind": "def",
      "name": "kn_tree_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-numer/",
      "source_line_start": 154,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kn_tree_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-denom/",
      "source_line_start": 155,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kn_tree_in_range",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-in-range/",
      "source_line_start": 158,
      "source_line_end": 161,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P02"
      ]
    },
    {
      "kind": "theorem",
      "name": "tree_exceeds_required",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/tree-exceeds-required/",
      "source_line_start": 165,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c1_target_numer",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-target-numer/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c1_target_denom",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-target-denom/",
      "source_line_start": 177,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c1_matches_three_over_pi",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-matches-three-over-pi/",
      "source_line_start": 185,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T05"
      ]
    },
    {
      "kind": "theorem",
      "name": "c1_in_range",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-in-range/",
      "source_line_start": 191,
      "source_line_end": 194,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_spectral_distance",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-spectral-distance/",
      "source_line_start": 201,
      "source_line_end": 202,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_tree_factor",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-tree-factor/",
      "source_line_start": 205,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_denom_pos",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-denom-pos/",
      "source_line_start": 209,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "deficit_positive",
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/deficit-positive/",
      "source_line_start": 215,
      "source_line_end": 217,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 244,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean",
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
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Gravity/CoRotorCoupling.lean`
- SHA-256: `42d8cf07fee7bf9ff7184030d98b6da7a590e159fb82f9890ad0f4ab469b7b05`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Iota`
- `TauLib.BookIV.Physics.LemniscateCapacity`
- `TauLib.BookV.Gravity.GravitationalConstant`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.ClosingIdentity`

## Declaration Counts

- `def`: 9
- `eval`: 5
- `structure`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CoRotorCoupling](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/co-rotor-coupling/) | L90-L103 | type/data schema | type/data schema | `V.D10` |
| `def` | [c1_three_over_pi_numer](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-three-over-pi-numer/) | L114-L114 | data/computed value | data/computed value | — |
| `def` | [c1_three_over_pi_denom](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-three-over-pi-denom/) | L115-L115 | data/computed value | data/computed value | — |
| `def` | [canonical_coupling](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-coupling/) | L118-L123 | definition | definition | — |
| `def` | [kn_required_numer](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-numer/) | L134-L134 | data/computed value | data/computed value | — |
| `def` | [kn_required_denom](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-denom/) | L135-L135 | data/computed value | data/computed value | — |
| `theorem` | [kn_required_range](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-range/) | L143-L146 | proof obligation | formal proof obligation checked | `V.T04` |
| `def` | [kn_tree_numer](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-numer/) | L154-L154 | data/computed value | data/computed value | — |
| `def` | [kn_tree_denom](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-denom/) | L155-L155 | data/computed value | data/computed value | — |
| `theorem` | [kn_tree_in_range](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-in-range/) | L158-L161 | proof obligation | formal proof obligation checked | `V.P02` |
| `theorem` | [tree_exceeds_required](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/tree-exceeds-required/) | L165-L168 | proof obligation | formal proof obligation checked | — |
| `def` | [c1_target_numer](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-target-numer/) | L176-L176 | data/computed value | data/computed value | — |
| `def` | [c1_target_denom](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-target-denom/) | L177-L177 | data/computed value | data/computed value | — |
| `theorem` | [c1_matches_three_over_pi](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-matches-three-over-pi/) | L185-L188 | proof obligation | formal proof obligation checked | `V.T05` |
| `theorem` | [c1_in_range](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/c1-in-range/) | L191-L194 | proof obligation | formal proof obligation checked | — |
| `theorem` | [canonical_spectral_distance](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-spectral-distance/) | L201-L202 | proof obligation | formal proof obligation checked | — |
| `theorem` | [canonical_tree_factor](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-tree-factor/) | L205-L206 | proof obligation | formal proof obligation checked | — |
| `theorem` | [canonical_denom_pos](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/canonical-denom-pos/) | L209-L211 | proof obligation | formal proof obligation checked | — |
| `theorem` | [deficit_positive](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/deficit-positive/) | L215-L217 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l224/) | L224-L224 | computed check | computed check | — |
| `eval` | [#eval L228](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l228/) | L228-L228 | computed check | computed check | — |
| `eval` | [#eval L232](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l232/) | L232-L232 | computed check | computed check | — |
| `eval` | [#eval L236](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l236/) | L236-L236 | computed check | computed check | — |
| `eval` | [#eval L240](/corpus/taulib/docs/book-v-gravity-co-rotor-coupling/eval-l240/) | L240-L244 | computed check | computed check | — |
