---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.ComplexField",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.ComplexField`.",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_slug": "book-i-boundary-complex-field",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/ComplexField.lean",
  "sha256": "c5c8ff8e251be7ee4e53b1e2f59197c32206fc74d5b442c9d6042b803121159e",
  "imports": [
    "TauLib.BookI.Boundary.ConstructiveReals",
    "TauLib.BookI.Boundary.SplitComplex",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI"
  ],
  "registry_ids": [
    "I.D85",
    "I.D86",
    "I.T43"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 9,
    "theorem": 17
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauComplex",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/tau-complex/",
      "source_line_start": 46,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": [
        "I.D85"
      ]
    },
    {
      "kind": "def",
      "name": "TauComplex.equiv",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/equiv/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauComplex.equiv_refl",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/equiv-refl/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauComplex.equiv_symm",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/equiv-symm/",
      "source_line_start": 66,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.zero",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/zero/",
      "source_line_start": 75,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.one",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/one/",
      "source_line_start": 78,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.i_unit",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/i-unit/",
      "source_line_start": 81,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.add",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/add/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.mul",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/mul/",
      "source_line_start": 89,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.negate",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/negate/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.conj",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/conj/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_i_squared",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-i-squared/",
      "source_line_start": 107,
      "source_line_end": 128,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_comm",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-comm/",
      "source_line_start": 135,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-assoc/",
      "source_line_start": 140,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_zero",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-zero/",
      "source_line_start": 146,
      "source_line_end": 148,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_negate",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-negate/",
      "source_line_start": 151,
      "source_line_end": 153,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_comm",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-comm/",
      "source_line_start": 157,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-assoc/",
      "source_line_start": 179,
      "source_line_end": 198,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_one",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-one/",
      "source_line_start": 201,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_left_distrib",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-left-distrib/",
      "source_line_start": 225,
      "source_line_end": 246,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_ring_axioms",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-ring-axioms/",
      "source_line_start": 249,
      "source_line_end": 260,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_j_squared",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/sc-j-squared/",
      "source_line_start": 274,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D86"
      ]
    },
    {
      "kind": "theorem",
      "name": "elliptic_hyperbolic_dichotomy",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/elliptic-hyperbolic-dichotomy/",
      "source_line_start": 279,
      "source_line_end": 287,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.fromTauReal",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/from-tau-real/",
      "source_line_start": 294,
      "source_line_end": 295,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fromTauReal_add",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/from-tau-real-add/",
      "source_line_start": 298,
      "source_line_end": 301,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_conj_involution",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-involution/",
      "source_line_start": 308,
      "source_line_end": 319,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_conj_add",
      "url": "/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-add/",
      "source_line_start": 322,
      "source_line_end": 362,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/ComplexField.lean`
- SHA-256: `c5c8ff8e251be7ee4e53b1e2f59197c32206fc74d5b442c9d6042b803121159e`

## Registry Links

- `I.D85` — Elliptic Complex Field
- `I.D86` — Elliptic-Hyperbolic Dichotomy
- `I.T43` — TauComplex Ring Axioms

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.ConstructiveReals`
- `TauLib.BookI.Boundary.SplitComplex`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`

## Declaration Counts

- `def`: 9
- `structure`: 1
- `theorem`: 17

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TauComplex](/verify/taulib/docs/book-i-boundary-complex-field/tau-complex/) | L46-L50 | defined | `I.D85` |
| `def` | [TauComplex.equiv](/verify/taulib/docs/book-i-boundary-complex-field/equiv/) | L58-L59 | defined | — |
| `theorem` | [TauComplex.equiv_refl](/verify/taulib/docs/book-i-boundary-complex-field/equiv-refl/) | L62-L63 | formalized | — |
| `theorem` | [TauComplex.equiv_symm](/verify/taulib/docs/book-i-boundary-complex-field/equiv-symm/) | L66-L68 | formalized | — |
| `def` | [TauComplex.zero](/verify/taulib/docs/book-i-boundary-complex-field/zero/) | L75-L75 | defined | — |
| `def` | [TauComplex.one](/verify/taulib/docs/book-i-boundary-complex-field/one/) | L78-L78 | defined | — |
| `def` | [TauComplex.i_unit](/verify/taulib/docs/book-i-boundary-complex-field/i-unit/) | L81-L81 | defined | — |
| `def` | [TauComplex.add](/verify/taulib/docs/book-i-boundary-complex-field/add/) | L84-L85 | defined | — |
| `def` | [TauComplex.mul](/verify/taulib/docs/book-i-boundary-complex-field/mul/) | L89-L91 | defined | — |
| `def` | [TauComplex.negate](/verify/taulib/docs/book-i-boundary-complex-field/negate/) | L94-L95 | defined | — |
| `def` | [TauComplex.conj](/verify/taulib/docs/book-i-boundary-complex-field/conj/) | L98-L99 | defined | — |
| `theorem` | [taucomplex_i_squared](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-i-squared/) | L107-L128 | formalized | — |
| `theorem` | [taucomplex_add_comm](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-comm/) | L135-L137 | formalized | — |
| `theorem` | [taucomplex_add_assoc](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-assoc/) | L140-L143 | formalized | — |
| `theorem` | [taucomplex_add_zero](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-zero/) | L146-L148 | formalized | — |
| `theorem` | [taucomplex_add_negate](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-add-negate/) | L151-L153 | formalized | — |
| `theorem` | [taucomplex_mul_comm](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-comm/) | L157-L175 | formalized | — |
| `theorem` | [taucomplex_mul_assoc](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-assoc/) | L179-L198 | formalized | — |
| `theorem` | [taucomplex_mul_one](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-one/) | L201-L222 | formalized | — |
| `theorem` | [taucomplex_left_distrib](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-left-distrib/) | L225-L246 | formalized | — |
| `theorem` | [taucomplex_ring_axioms](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-ring-axioms/) | L249-L260 | formalized | — |
| `theorem` | [sc_j_squared](/verify/taulib/docs/book-i-boundary-complex-field/sc-j-squared/) | L274-L276 | formalized | `I.D86` |
| `theorem` | [elliptic_hyperbolic_dichotomy](/verify/taulib/docs/book-i-boundary-complex-field/elliptic-hyperbolic-dichotomy/) | L279-L287 | formalized | — |
| `def` | [TauComplex.fromTauReal](/verify/taulib/docs/book-i-boundary-complex-field/from-tau-real/) | L294-L295 | defined | — |
| `theorem` | [fromTauReal_add](/verify/taulib/docs/book-i-boundary-complex-field/from-tau-real-add/) | L298-L301 | formalized | — |
| `theorem` | [taucomplex_conj_involution](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-involution/) | L308-L319 | formalized | — |
| `theorem` | [taucomplex_conj_add](/verify/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-add/) | L322-L362 | formalized | — |
