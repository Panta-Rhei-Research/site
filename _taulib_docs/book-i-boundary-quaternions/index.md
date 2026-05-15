---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Quaternions",
  "permalink": "/corpus/taulib/docs/book-i-boundary-quaternions/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Quaternions`.",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_slug": "book-i-boundary-quaternions",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Quaternions.lean",
  "sha256": "186adf0fe169aa6044606f7aec488f690e2a0cc8dd654c870a36196fe93ac870",
  "imports": [
    "TauLib.BookI.Boundary.ConstructiveReals",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI"
  ],
  "registry_ids": [
    "I.D87",
    "I.R22",
    "I.T44"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 12,
    "theorem": 14
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauQuaternion",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tau-quaternion/",
      "source_line_start": 45,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D87"
      ]
    },
    {
      "kind": "def",
      "name": "TauQuaternion.equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/equiv/",
      "source_line_start": 56,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauQuaternion.equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/equiv-refl/",
      "source_line_start": 61,
      "source_line_end": 63,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauQuaternion.equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/equiv-symm/",
      "source_line_start": 66,
      "source_line_end": 69,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/zero/",
      "source_line_start": 76,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.one",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/one/",
      "source_line_start": 80,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.qi",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qi/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.qj",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qj/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.qk",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qk/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.add",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/add/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.negate",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/negate/",
      "source_line_start": 104,
      "source_line_end": 105,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/mul/",
      "source_line_start": 113,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.conj",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/conj/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.normSq",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/norm-sq/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_const_bridge",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/taureal-const-bridge/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauQuaternion.neg_one",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/neg-one/",
      "source_line_start": 142,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qi_squared",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qi-squared/",
      "source_line_start": 145,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qj_squared",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qj-squared/",
      "source_line_start": 162,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qk_squared",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/qk-squared/",
      "source_line_start": 179,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ijk_relation",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/ijk-relation/",
      "source_line_start": 196,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "non_commutativity_witness",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/non-commutativity-witness/",
      "source_line_start": 224,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_add_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-comm/",
      "source_line_start": 249,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_add_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-assoc/",
      "source_line_start": 255,
      "source_line_end": 259,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_add_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-zero/",
      "source_line_start": 262,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_add_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-negate/",
      "source_line_start": 268,
      "source_line_end": 271,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_mul_one",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-mul-one/",
      "source_line_start": 278,
      "source_line_end": 290,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauquat_one_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-one-mul/",
      "source_line_start": 293,
      "source_line_end": 321,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean",
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
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Quaternions.lean`
- SHA-256: `186adf0fe169aa6044606f7aec488f690e2a0cc8dd654c870a36196fe93ac870`

## Registry Links

- `I.D87` — Elliptic Quaternions
- `I.R22` — Hurwitz Classification Preview
- `I.T44` — Quaternion Non-Commutativity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.ConstructiveReals`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`

## Declaration Counts

- `def`: 12
- `structure`: 1
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauQuaternion](/corpus/taulib/docs/book-i-boundary-quaternions/tau-quaternion/) | L45-L49 | type/data schema | type/data schema | `I.D87` |
| `def` | [TauQuaternion.equiv](/corpus/taulib/docs/book-i-boundary-quaternions/equiv/) | L56-L58 | definition | definition | — |
| `theorem` | [TauQuaternion.equiv_refl](/corpus/taulib/docs/book-i-boundary-quaternions/equiv-refl/) | L61-L63 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauQuaternion.equiv_symm](/corpus/taulib/docs/book-i-boundary-quaternions/equiv-symm/) | L66-L69 | proof obligation | formal proof obligation checked | — |
| `def` | [TauQuaternion.zero](/corpus/taulib/docs/book-i-boundary-quaternions/zero/) | L76-L77 | definition | definition | — |
| `def` | [TauQuaternion.one](/corpus/taulib/docs/book-i-boundary-quaternions/one/) | L80-L81 | definition | definition | — |
| `def` | [TauQuaternion.qi](/corpus/taulib/docs/book-i-boundary-quaternions/qi/) | L84-L85 | definition | definition | — |
| `def` | [TauQuaternion.qj](/corpus/taulib/docs/book-i-boundary-quaternions/qj/) | L88-L89 | definition | definition | — |
| `def` | [TauQuaternion.qk](/corpus/taulib/docs/book-i-boundary-quaternions/qk/) | L92-L93 | definition | definition | — |
| `def` | [TauQuaternion.add](/corpus/taulib/docs/book-i-boundary-quaternions/add/) | L100-L101 | definition | definition | — |
| `def` | [TauQuaternion.negate](/corpus/taulib/docs/book-i-boundary-quaternions/negate/) | L104-L105 | definition | definition | — |
| `def` | [TauQuaternion.mul](/corpus/taulib/docs/book-i-boundary-quaternions/mul/) | L113-L117 | definition | definition | — |
| `def` | [TauQuaternion.conj](/corpus/taulib/docs/book-i-boundary-quaternions/conj/) | L120-L121 | definition | definition | — |
| `def` | [TauQuaternion.normSq](/corpus/taulib/docs/book-i-boundary-quaternions/norm-sq/) | L124-L125 | definition | definition | — |
| `theorem` | [taureal_const_bridge](/corpus/taulib/docs/book-i-boundary-quaternions/taureal-const-bridge/) | L133-L135 | proof obligation | formal proof obligation checked | — |
| `def` | [TauQuaternion.neg_one](/corpus/taulib/docs/book-i-boundary-quaternions/neg-one/) | L142-L142 | definition | definition | — |
| `theorem` | [qi_squared](/corpus/taulib/docs/book-i-boundary-quaternions/qi-squared/) | L145-L159 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qj_squared](/corpus/taulib/docs/book-i-boundary-quaternions/qj-squared/) | L162-L176 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qk_squared](/corpus/taulib/docs/book-i-boundary-quaternions/qk-squared/) | L179-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ijk_relation](/corpus/taulib/docs/book-i-boundary-quaternions/ijk-relation/) | L196-L211 | proof obligation | formal proof obligation checked | — |
| `theorem` | [non_commutativity_witness](/corpus/taulib/docs/book-i-boundary-quaternions/non-commutativity-witness/) | L224-L242 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_add_comm](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-comm/) | L249-L252 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_add_assoc](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-assoc/) | L255-L259 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_add_zero](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-zero/) | L262-L265 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_add_negate](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-add-negate/) | L268-L271 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_mul_one](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-mul-one/) | L278-L290 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauquat_one_mul](/corpus/taulib/docs/book-i-boundary-quaternions/tauquat-one-mul/) | L293-L321 | proof obligation | formal proof obligation checked | — |
