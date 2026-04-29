---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Denotation.Arithmetic",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Denotation.Arithmetic`.",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_slug": "book-i-denotation-arithmetic",
  "book": "BookI",
  "family": "Denotation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Denotation/Arithmetic.lean",
  "sha256": "1303e6ed0bf06c1293f7ac730240b6d558e632886f4f8a6282c42010c665573c",
  "imports": [
    "TauLib.BookI.Denotation.RankTransfer",
    "TauLib.BookI.Orbit.Ladder"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.NumberTower",
    "TauLib.BookI.Coordinates.Primes",
    "TauLib.BookI.Denotation.ProgramMonoid",
    "TauLib.Tour.Foundations"
  ],
  "registry_ids": [
    "I.D10",
    "I.D11",
    "I.D12",
    "I.D13",
    "I.P05",
    "I.P06"
  ],
  "declaration_counts": {
    "def": 4,
    "theorem": 23
  },
  "declarations": [
    {
      "kind": "def",
      "name": "idx_add",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add/",
      "source_line_start": 46,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": [
        "I.D10"
      ]
    },
    {
      "kind": "theorem",
      "name": "idx_add_eq_nat_add",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-eq-nat-add/",
      "source_line_start": 50,
      "source_line_end": 51,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_mul",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul/",
      "source_line_start": 58,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": [
        "I.D11"
      ]
    },
    {
      "kind": "theorem",
      "name": "idx_mul_eq_nat_mul",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-eq-nat-mul/",
      "source_line_start": 64,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_exp",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp/",
      "source_line_start": 76,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "I.D12"
      ]
    },
    {
      "kind": "theorem",
      "name": "idx_exp_eq_nat_pow",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-eq-nat-pow/",
      "source_line_start": 82,
      "source_line_end": 87,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_tetration",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration/",
      "source_line_start": 95,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "I.D13"
      ]
    },
    {
      "kind": "theorem",
      "name": "idx_tetration_eq",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration-eq/",
      "source_line_start": 101,
      "source_line_end": 106,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladderOp_add_eq_idx",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-add-eq-idx/",
      "source_line_start": 113,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladderOp_mul_eq_idx",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-mul-eq-idx/",
      "source_line_start": 118,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladderOp_exp_eq_idx",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-exp-eq-idx/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladderOp_tet_eq_idx",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-tet-eq-idx/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fold_chain",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/fold-chain/",
      "source_line_start": 135,
      "source_line_end": 140,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_add_comm",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-comm/",
      "source_line_start": 147,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_add_assoc",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-assoc/",
      "source_line_start": 152,
      "source_line_end": 155,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_add_zero",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-zero/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_zero_add",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-zero-add/",
      "source_line_start": 162,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_mul_comm",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-comm/",
      "source_line_start": 166,
      "source_line_end": 167,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_mul_assoc",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-assoc/",
      "source_line_start": 170,
      "source_line_end": 172,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_mul_one",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-one/",
      "source_line_start": 175,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_one_mul",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-one-mul/",
      "source_line_start": 179,
      "source_line_end": 180,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_mul_zero",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-zero/",
      "source_line_start": 183,
      "source_line_end": 184,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_distrib",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-distrib/",
      "source_line_start": 187,
      "source_line_end": 190,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_add_injective",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-injective/",
      "source_line_start": 197,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P05"
      ]
    },
    {
      "kind": "theorem",
      "name": "idx_mul_injective",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-injective/",
      "source_line_start": 204,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_exp_injective",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-injective/",
      "source_line_start": 211,
      "source_line_end": 215,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_exp_non_comm",
      "url": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-non-comm/",
      "source_line_start": 218,
      "source_line_end": 225,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean",
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
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Denotation/Arithmetic.lean`
- SHA-256: `1303e6ed0bf06c1293f7ac730240b6d558e632886f4f8a6282c42010c665573c`

## Registry Links

- `I.D10` — Index Addition
- `I.D11` — Index Multiplication
- `I.D12` — Index Exponentiation
- `I.D13` — Index Tetration
- `I.P05` — Tetration Injectivity
- `I.P06` — Arithmetic Laws

## Construction Spine Links

- [Recover Core Mathematics](/corpus/construction-spine/recover-core-mathematics/)

## Imports

- `TauLib.BookI.Denotation.RankTransfer`
- `TauLib.BookI.Orbit.Ladder`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.NumberTower`
- `TauLib.BookI.Coordinates.Primes`
- `TauLib.BookI.Denotation.ProgramMonoid`
- `TauLib.Tour.Foundations`

## Declaration Counts

- `def`: 4
- `theorem`: 23

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [idx_add](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add/) | L46-L47 | defined | `I.D10` |
| `theorem` | [idx_add_eq_nat_add](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-eq-nat-add/) | L50-L51 | formalized | — |
| `def` | [idx_mul](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul/) | L58-L61 | defined | `I.D11` |
| `theorem` | [idx_mul_eq_nat_mul](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-eq-nat-mul/) | L64-L69 | formalized | — |
| `def` | [idx_exp](/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp/) | L76-L79 | defined | `I.D12` |
| `theorem` | [idx_exp_eq_nat_pow](/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-eq-nat-pow/) | L82-L87 | formalized | — |
| `def` | [idx_tetration](/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration/) | L95-L98 | defined | `I.D13` |
| `theorem` | [idx_tetration_eq](/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration-eq/) | L101-L106 | formalized | — |
| `theorem` | [ladderOp_add_eq_idx](/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-add-eq-idx/) | L113-L115 | formalized | — |
| `theorem` | [ladderOp_mul_eq_idx](/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-mul-eq-idx/) | L118-L120 | formalized | — |
| `theorem` | [ladderOp_exp_eq_idx](/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-exp-eq-idx/) | L123-L125 | formalized | — |
| `theorem` | [ladderOp_tet_eq_idx](/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-tet-eq-idx/) | L128-L130 | formalized | — |
| `theorem` | [fold_chain](/verify/taulib/docs/book-i-denotation-arithmetic/fold-chain/) | L135-L140 | formalized | — |
| `theorem` | [idx_add_comm](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-comm/) | L147-L149 | formalized | — |
| `theorem` | [idx_add_assoc](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-assoc/) | L152-L155 | formalized | — |
| `theorem` | [idx_add_zero](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-zero/) | L158-L159 | formalized | — |
| `theorem` | [idx_zero_add](/verify/taulib/docs/book-i-denotation-arithmetic/idx-zero-add/) | L162-L163 | formalized | — |
| `theorem` | [idx_mul_comm](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-comm/) | L166-L167 | formalized | — |
| `theorem` | [idx_mul_assoc](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-assoc/) | L170-L172 | formalized | — |
| `theorem` | [idx_mul_one](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-one/) | L175-L176 | formalized | — |
| `theorem` | [idx_one_mul](/verify/taulib/docs/book-i-denotation-arithmetic/idx-one-mul/) | L179-L180 | formalized | — |
| `theorem` | [idx_mul_zero](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-zero/) | L183-L184 | formalized | — |
| `theorem` | [idx_distrib](/verify/taulib/docs/book-i-denotation-arithmetic/idx-distrib/) | L187-L190 | formalized | — |
| `theorem` | [idx_add_injective](/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-injective/) | L197-L201 | formalized | `I.P05` |
| `theorem` | [idx_mul_injective](/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul-injective/) | L204-L208 | formalized | — |
| `theorem` | [idx_exp_injective](/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-injective/) | L211-L215 | formalized | — |
| `theorem` | [idx_exp_non_comm](/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp-non-comm/) | L218-L225 | formalized | — |
