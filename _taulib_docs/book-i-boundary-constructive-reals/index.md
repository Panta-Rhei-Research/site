---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.ConstructiveReals",
  "permalink": "/corpus/taulib/docs/book-i-boundary-constructive-reals/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.ConstructiveReals`.",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_slug": "book-i-boundary-constructive-reals",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/ConstructiveReals.lean",
  "sha256": "d70b5d6b1d2161b1522b99aae67fc04b8456fe2c9ca314603828091fe99f630e",
  "imports": [
    "TauLib.BookI.Boundary.TauRatAbs",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.ComplexField",
    "TauLib.BookI.Boundary.Quaternions",
    "TauLib.BookI.Boundary.TauRealOrder"
  ],
  "registry_ids": [
    "I.D111",
    "I.D112",
    "I.D84",
    "I.P39",
    "I.T42"
  ],
  "declaration_counts": {
    "theorem": 29,
    "structure": 1,
    "def": 12
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "taurat_add_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-add-assoc/",
      "source_line_start": 63,
      "source_line_end": 68,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_zero_add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-zero-add/",
      "source_line_start": 71,
      "source_line_end": 76,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_negate_add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-negate-add/",
      "source_line_start": 79,
      "source_line_end": 84,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_mul_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-mul-assoc/",
      "source_line_start": 87,
      "source_line_end": 92,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_one_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-one-mul/",
      "source_line_start": 95,
      "source_line_end": 100,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_left_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-left-distrib/",
      "source_line_start": 103,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_right_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-right-distrib/",
      "source_line_start": 111,
      "source_line_end": 116,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_zero_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-zero-mul/",
      "source_line_start": 119,
      "source_line_end": 124,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauReal",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/tau-real/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D84"
      ]
    },
    {
      "kind": "def",
      "name": "TauReal.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/zero/",
      "source_line_start": 141,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.one",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/one/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/add/",
      "source_line_start": 147,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/mul/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.negate",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/negate/",
      "source_line_start": 155,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.sub",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/sub/",
      "source_line_start": 159,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.fromTauRat",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.fromNat",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/from-nat/",
      "source_line_start": 166,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.IsCauchy",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/is-cauchy/",
      "source_line_start": 178,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D111"
      ]
    },
    {
      "kind": "def",
      "name": "TauReal.equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv/",
      "source_line_start": 199,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "TauReal.equiv_of_pointwise",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-of-pointwise/",
      "source_line_start": 215,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-refl/",
      "source_line_start": 232,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-symm/",
      "source_line_start": 236,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.equiv_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-trans/",
      "source_line_start": 249,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_add_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-comm/",
      "source_line_start": 282,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_add_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-assoc/",
      "source_line_start": 287,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_add_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-zero/",
      "source_line_start": 292,
      "source_line_end": 294,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_zero_add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-zero-add/",
      "source_line_start": 297,
      "source_line_end": 299,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_add_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-negate/",
      "source_line_start": 302,
      "source_line_end": 304,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_negate_add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-negate-add/",
      "source_line_start": 307,
      "source_line_end": 309,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_mul_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-comm/",
      "source_line_start": 312,
      "source_line_end": 314,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_mul_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-assoc/",
      "source_line_start": 317,
      "source_line_end": 319,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_mul_one",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-one/",
      "source_line_start": 322,
      "source_line_end": 324,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_one_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-one-mul/",
      "source_line_start": 327,
      "source_line_end": 329,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_left_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-left-distrib/",
      "source_line_start": 332,
      "source_line_end": 334,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_right_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-right-distrib/",
      "source_line_start": 337,
      "source_line_end": 339,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_zero_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-zero-mul/",
      "source_line_start": 342,
      "source_line_end": 344,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_ring_axioms",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-ring-axioms/",
      "source_line_start": 347,
      "source_line_end": 357,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fromTauRat_add",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat-add/",
      "source_line_start": 364,
      "source_line_end": 367,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fromTauRat_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat-mul/",
      "source_line_start": 370,
      "source_line_end": 373,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taureal_archimedean_embedding",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-archimedean-embedding/",
      "source_line_start": 387,
      "source_line_end": 411,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T42"
      ]
    },
    {
      "kind": "def",
      "name": "real_half",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/real-half/",
      "source_line_start": 417,
      "source_line_end": 417,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "real_third",
      "url": "/corpus/taulib/docs/book-i-boundary-constructive-reals/real-third/",
      "source_line_start": 418,
      "source_line_end": 428,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean",
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
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/ConstructiveReals.lean`
- SHA-256: `d70b5d6b1d2161b1522b99aae67fc04b8456fe2c9ca314603828091fe99f630e`

## Registry Links

- `I.D84` — Constructive Reals
- `I.P39` — TauReal Ring Axioms
- `I.T42` — Archimedean Property

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRatAbs`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.ComplexField`
- `TauLib.BookI.Boundary.Quaternions`
- `TauLib.BookI.Boundary.TauRealOrder`

## Declaration Counts

- `def`: 12
- `structure`: 1
- `theorem`: 29

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `theorem` | [taurat_add_assoc](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-add-assoc/) | L63-L68 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_zero_add](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-zero-add/) | L71-L76 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_negate_add](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-negate-add/) | L79-L84 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_mul_assoc](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-mul-assoc/) | L87-L92 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_one_mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-one-mul/) | L95-L100 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_left_distrib](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-left-distrib/) | L103-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_right_distrib](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-right-distrib/) | L111-L116 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_zero_mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/taurat-zero-mul/) | L119-L124 | proof obligation | formal proof obligation checked | — |
| `structure` | [TauReal](/corpus/taulib/docs/book-i-boundary-constructive-reals/tau-real/) | L136-L138 | type/data schema | type/data schema | `I.D84` |
| `def` | [TauReal.zero](/corpus/taulib/docs/book-i-boundary-constructive-reals/zero/) | L141-L141 | definition | definition | — |
| `def` | [TauReal.one](/corpus/taulib/docs/book-i-boundary-constructive-reals/one/) | L144-L144 | definition | definition | — |
| `def` | [TauReal.add](/corpus/taulib/docs/book-i-boundary-constructive-reals/add/) | L147-L148 | definition | definition | — |
| `def` | [TauReal.mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/mul/) | L151-L152 | definition | definition | — |
| `def` | [TauReal.negate](/corpus/taulib/docs/book-i-boundary-constructive-reals/negate/) | L155-L156 | definition | definition | — |
| `def` | [TauReal.sub](/corpus/taulib/docs/book-i-boundary-constructive-reals/sub/) | L159-L160 | definition | definition | — |
| `def` | [TauReal.fromTauRat](/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat/) | L163-L163 | definition | definition | — |
| `def` | [TauReal.fromNat](/corpus/taulib/docs/book-i-boundary-constructive-reals/from-nat/) | L166-L167 | definition | definition | — |
| `def` | [TauReal.IsCauchy](/corpus/taulib/docs/book-i-boundary-constructive-reals/is-cauchy/) | L178-L181 | definition | definition | `I.D111` |
| `def` | [TauReal.equiv](/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv/) | L199-L202 | definition | definition | `I.D112` |
| `theorem` | [TauReal.equiv_of_pointwise](/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-of-pointwise/) | L215-L225 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.equiv_refl](/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-refl/) | L232-L233 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.equiv_symm](/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-symm/) | L236-L246 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.equiv_trans](/corpus/taulib/docs/book-i-boundary-constructive-reals/equiv-trans/) | L249-L275 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_add_comm](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-comm/) | L282-L284 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_add_assoc](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-assoc/) | L287-L289 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_add_zero](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-zero/) | L292-L294 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_zero_add](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-zero-add/) | L297-L299 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_add_negate](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-add-negate/) | L302-L304 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_negate_add](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-negate-add/) | L307-L309 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_mul_comm](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-comm/) | L312-L314 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_mul_assoc](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-assoc/) | L317-L319 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_mul_one](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-mul-one/) | L322-L324 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_one_mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-one-mul/) | L327-L329 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_left_distrib](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-left-distrib/) | L332-L334 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_right_distrib](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-right-distrib/) | L337-L339 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_zero_mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-zero-mul/) | L342-L344 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_ring_axioms](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-ring-axioms/) | L347-L357 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fromTauRat_add](/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat-add/) | L364-L367 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fromTauRat_mul](/corpus/taulib/docs/book-i-boundary-constructive-reals/from-tau-rat-mul/) | L370-L373 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taureal_archimedean_embedding](/corpus/taulib/docs/book-i-boundary-constructive-reals/taureal-archimedean-embedding/) | L387-L411 | proof obligation | formal proof obligation checked | `I.T42` |
| `def` | [real_half](/corpus/taulib/docs/book-i-boundary-constructive-reals/real-half/) | L417-L417 | definition | definition | — |
| `def` | [real_third](/corpus/taulib/docs/book-i-boundary-constructive-reals/real-third/) | L418-L428 | definition | definition | — |
