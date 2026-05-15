---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.ComplexField",
  "permalink": "/corpus/taulib/docs/book-i-boundary-complex-field/",
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
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/tau-complex/",
      "source_line_start": 46,
      "source_line_end": 50,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D85"
      ]
    },
    {
      "kind": "def",
      "name": "TauComplex.equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/equiv/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauComplex.equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/equiv-refl/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauComplex.equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/equiv-symm/",
      "source_line_start": 66,
      "source_line_end": 68,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/zero/",
      "source_line_start": 75,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.one",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/one/",
      "source_line_start": 78,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.i_unit",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/i-unit/",
      "source_line_start": 81,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.add",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/add/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/mul/",
      "source_line_start": 89,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.negate",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/negate/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.conj",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/conj/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_i_squared",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-i-squared/",
      "source_line_start": 107,
      "source_line_end": 128,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-comm/",
      "source_line_start": 135,
      "source_line_end": 137,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-assoc/",
      "source_line_start": 140,
      "source_line_end": 143,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-zero/",
      "source_line_start": 146,
      "source_line_end": 148,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_add_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-negate/",
      "source_line_start": 151,
      "source_line_end": 153,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-comm/",
      "source_line_start": 157,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-assoc/",
      "source_line_start": 179,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_mul_one",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-one/",
      "source_line_start": 201,
      "source_line_end": 222,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_left_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-left-distrib/",
      "source_line_start": 225,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_ring_axioms",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-ring-axioms/",
      "source_line_start": 249,
      "source_line_end": 260,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_j_squared",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/sc-j-squared/",
      "source_line_start": 274,
      "source_line_end": 276,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.D86"
      ]
    },
    {
      "kind": "theorem",
      "name": "elliptic_hyperbolic_dichotomy",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/elliptic-hyperbolic-dichotomy/",
      "source_line_start": 279,
      "source_line_end": 287,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComplex.fromTauReal",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/from-tau-real/",
      "source_line_start": 294,
      "source_line_end": 295,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fromTauReal_add",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/from-tau-real-add/",
      "source_line_start": 298,
      "source_line_end": 301,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_conj_involution",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-involution/",
      "source_line_start": 308,
      "source_line_end": 319,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taucomplex_conj_add",
      "url": "/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-add/",
      "source_line_start": 322,
      "source_line_end": 362,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauComplex](/corpus/taulib/docs/book-i-boundary-complex-field/tau-complex/) | L46-L50 | type/data schema | type/data schema | `I.D85` |
| `def` | [TauComplex.equiv](/corpus/taulib/docs/book-i-boundary-complex-field/equiv/) | L58-L59 | definition | definition | — |
| `theorem` | [TauComplex.equiv_refl](/corpus/taulib/docs/book-i-boundary-complex-field/equiv-refl/) | L62-L63 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauComplex.equiv_symm](/corpus/taulib/docs/book-i-boundary-complex-field/equiv-symm/) | L66-L68 | proof obligation | formal proof obligation checked | — |
| `def` | [TauComplex.zero](/corpus/taulib/docs/book-i-boundary-complex-field/zero/) | L75-L75 | definition | definition | — |
| `def` | [TauComplex.one](/corpus/taulib/docs/book-i-boundary-complex-field/one/) | L78-L78 | definition | definition | — |
| `def` | [TauComplex.i_unit](/corpus/taulib/docs/book-i-boundary-complex-field/i-unit/) | L81-L81 | definition | definition | — |
| `def` | [TauComplex.add](/corpus/taulib/docs/book-i-boundary-complex-field/add/) | L84-L85 | definition | definition | — |
| `def` | [TauComplex.mul](/corpus/taulib/docs/book-i-boundary-complex-field/mul/) | L89-L91 | definition | definition | — |
| `def` | [TauComplex.negate](/corpus/taulib/docs/book-i-boundary-complex-field/negate/) | L94-L95 | definition | definition | — |
| `def` | [TauComplex.conj](/corpus/taulib/docs/book-i-boundary-complex-field/conj/) | L98-L99 | definition | definition | — |
| `theorem` | [taucomplex_i_squared](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-i-squared/) | L107-L128 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_add_comm](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-comm/) | L135-L137 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_add_assoc](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-assoc/) | L140-L143 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_add_zero](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-zero/) | L146-L148 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_add_negate](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-add-negate/) | L151-L153 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_mul_comm](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-comm/) | L157-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_mul_assoc](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-assoc/) | L179-L198 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_mul_one](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-mul-one/) | L201-L222 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_left_distrib](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-left-distrib/) | L225-L246 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_ring_axioms](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-ring-axioms/) | L249-L260 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sc_j_squared](/corpus/taulib/docs/book-i-boundary-complex-field/sc-j-squared/) | L274-L276 | proof obligation | formal proof obligation checked | `I.D86` |
| `theorem` | [elliptic_hyperbolic_dichotomy](/corpus/taulib/docs/book-i-boundary-complex-field/elliptic-hyperbolic-dichotomy/) | L279-L287 | proof obligation | formal proof obligation checked | — |
| `def` | [TauComplex.fromTauReal](/corpus/taulib/docs/book-i-boundary-complex-field/from-tau-real/) | L294-L295 | definition | definition | — |
| `theorem` | [fromTauReal_add](/corpus/taulib/docs/book-i-boundary-complex-field/from-tau-real-add/) | L298-L301 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_conj_involution](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-involution/) | L308-L319 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taucomplex_conj_add](/corpus/taulib/docs/book-i-boundary-complex-field/taucomplex-conj-add/) | L322-L362 | proof obligation | formal proof obligation checked | — |
