---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRatField",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRatField`.",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_slug": "book-i-boundary-tau-rat-field",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRatField.lean",
  "sha256": "81facbd681cb3443b265ea35711510adf5fbace4cd47a1dfecd9491f07fc5941",
  "imports": [
    "TauLib.BookI.Boundary.NumberTower",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
    "TauLib.BookI.Boundary.TauRatOrder"
  ],
  "registry_ids": [
    "I.D107",
    "I.D35",
    "I.D84",
    "I.P48"
  ],
  "declaration_counts": {
    "theorem": 14,
    "def": 2,
    "example": 3
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "TauRat.equiv_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-trans/",
      "source_line_start": 59,
      "source_line_end": 76,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.equivalence",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/equivalence/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat/",
      "source_line_start": 89,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.den_pos_rat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/den-pos-rat/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.den_ne_zero_rat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/den-ne-zero-rat/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.equiv_iff_int_cross",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-int-cross/",
      "source_line_start": 102,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_iff_toRat_eq",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-to-rat-eq/",
      "source_line_start": 115,
      "source_line_end": 133,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-zero/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_one",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-one/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_add",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-add/",
      "source_line_start": 148,
      "source_line_end": 156,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-mul/",
      "source_line_start": 159,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-negate/",
      "source_line_start": 166,
      "source_line_end": 170,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_sub",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-sub/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.is_nonzero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.is_nonzero_iff_toRat_ne_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero-iff-to-rat-ne-zero/",
      "source_line_start": 186,
      "source_line_end": 201,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.is_nonzero_of_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero-of-equiv/",
      "source_line_start": 204,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l215/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l219/",
      "source_line_start": 219,
      "source_line_end": 221,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l224/",
      "source_line_start": 224,
      "source_line_end": 230,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRatField.lean`
- SHA-256: `81facbd681cb3443b265ea35711510adf5fbace4cd47a1dfecd9491f07fc5941`

## Registry Links

- `I.D35` — Number Tower
- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.NumberTower`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`

## Imported By

- `TauLib.BookI.Boundary.Bridge.TauRatQuotient`
- `TauLib.BookI.Boundary.TauRatOrder`

## Declaration Counts

- `def`: 2
- `example`: 3
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `theorem` | [TauRat.equiv_trans](/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-trans/) | L59-L76 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.equivalence](/corpus/taulib/docs/book-i-boundary-tau-rat-field/equivalence/) | L79-L80 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.toRat](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat/) | L89-L90 | definition | definition | — |
| `theorem` | [TauRat.den_pos_rat](/corpus/taulib/docs/book-i-boundary-tau-rat-field/den-pos-rat/) | L93-L94 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.den_ne_zero_rat](/corpus/taulib/docs/book-i-boundary-tau-rat-field/den-ne-zero-rat/) | L97-L98 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.equiv_iff_int_cross](/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-int-cross/) | L102-L112 | proof obligation | formal proof obligation checked | — |
| `theorem` | [equiv_iff_toRat_eq](/corpus/taulib/docs/book-i-boundary-tau-rat-field/equiv-iff-to-rat-eq/) | L115-L133 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_zero](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-zero/) | L140-L141 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_one](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-one/) | L144-L145 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_add](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-add/) | L148-L156 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_mul](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-mul/) | L159-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_negate](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-negate/) | L166-L170 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_sub](/corpus/taulib/docs/book-i-boundary-tau-rat-field/to-rat-sub/) | L173-L176 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.is_nonzero](/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero/) | L183-L183 | definition | definition | — |
| `theorem` | [TauRat.is_nonzero_iff_toRat_ne_zero](/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero-iff-to-rat-ne-zero/) | L186-L201 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.is_nonzero_of_equiv](/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero-of-equiv/) | L204-L208 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L215](/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l215/) | L215-L216 | example check | example | — |
| `example` | [#eval L219](/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l219/) | L219-L221 | example check | example | — |
| `example` | [#eval L224](/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l224/) | L224-L230 | example check | example | — |
