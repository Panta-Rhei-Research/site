---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRatOrder",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRatOrder`.",
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_slug": "book-i-boundary-tau-rat-order",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRatOrder.lean",
  "sha256": "f52ef5a2493a3cf782ee3427c944c399fc9e534172509ba52cb0624f3cb1a1ac",
  "imports": [
    "TauLib.BookI.Boundary.TauRatField",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRatAbs"
  ],
  "registry_ids": [
    "I.D107",
    "I.D108",
    "I.D35",
    "I.D84",
    "I.P48"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 16,
    "example": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauRat.lt",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt/",
      "source_line_start": 53,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_irrefl",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-irrefl/",
      "source_line_start": 56,
      "source_line_end": 57,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-trans/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_asymm",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-asymm/",
      "source_line_start": 65,
      "source_line_end": 67,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.le",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le/",
      "source_line_start": 74,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-refl/",
      "source_line_start": 77,
      "source_line_end": 77,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-trans/",
      "source_line_start": 80,
      "source_line_end": 82,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_antisymm",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-antisymm/",
      "source_line_start": 86,
      "source_line_end": 89,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_of_lt",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-lt/",
      "source_line_start": 96,
      "source_line_end": 97,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_iff_le_and_not_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-iff-le-and-not-equiv/",
      "source_line_start": 100,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.trichotomy",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/trichotomy/",
      "source_line_start": 119,
      "source_line_end": 124,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_of_equiv_left",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-of-equiv-left/",
      "source_line_start": 131,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.lt_of_equiv_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-of-equiv-right/",
      "source_line_start": 138,
      "source_line_end": 142,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_of_equiv_left",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-equiv-left/",
      "source_line_start": 145,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.le_of_equiv_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-equiv-right/",
      "source_line_start": 152,
      "source_line_end": 156,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.add_lt_add_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-lt-add-right/",
      "source_line_start": 165,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.add_le_add_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-le-add-right/",
      "source_line_start": 172,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.add_lt_add_left",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-lt-add-left/",
      "source_line_start": 179,
      "source_line_end": 209,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l216/",
      "source_line_start": 216,
      "source_line_end": 219,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l222/",
      "source_line_start": 222,
      "source_line_end": 223,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l226/",
      "source_line_start": 226,
      "source_line_end": 227,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l230/",
      "source_line_start": 230,
      "source_line_end": 238,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l241/",
      "source_line_start": 241,
      "source_line_end": 245,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l247/",
      "source_line_start": 247,
      "source_line_end": 250,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRatOrder.lean`
- SHA-256: `f52ef5a2493a3cf782ee3427c944c399fc9e534172509ba52cb0624f3cb1a1ac`

## Registry Links

- `I.D35` — Number Tower
- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRatField`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`

## Imported By

- `TauLib.BookI.Boundary.TauRatAbs`

## Declaration Counts

- `def`: 2
- `example`: 6
- `theorem`: 16

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauRat.lt](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt/) | L53-L53 | definition | definition | — |
| `theorem` | [TauRat.lt_irrefl](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-irrefl/) | L56-L57 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.lt_trans](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-trans/) | L60-L62 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.lt_asymm](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-asymm/) | L65-L67 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.le](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le/) | L74-L74 | definition | definition | — |
| `theorem` | [TauRat.le_refl](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-refl/) | L77-L77 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.le_trans](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-trans/) | L80-L82 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.le_antisymm](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-antisymm/) | L86-L89 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.le_of_lt](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-lt/) | L96-L97 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.lt_iff_le_and_not_equiv](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-iff-le-and-not-equiv/) | L100-L112 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.trichotomy](/corpus/taulib/docs/book-i-boundary-tau-rat-order/trichotomy/) | L119-L124 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.lt_of_equiv_left](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-of-equiv-left/) | L131-L135 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.lt_of_equiv_right](/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-of-equiv-right/) | L138-L142 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.le_of_equiv_left](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-equiv-left/) | L145-L149 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.le_of_equiv_right](/corpus/taulib/docs/book-i-boundary-tau-rat-order/le-of-equiv-right/) | L152-L156 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.add_lt_add_right](/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-lt-add-right/) | L165-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.add_le_add_right](/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-le-add-right/) | L172-L176 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.add_lt_add_left](/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-lt-add-left/) | L179-L209 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L216](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l216/) | L216-L219 | example check | example | — |
| `example` | [#eval L222](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l222/) | L222-L223 | example check | example | — |
| `example` | [#eval L226](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l226/) | L226-L227 | example check | example | — |
| `example` | [#eval L230](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l230/) | L230-L238 | example check | example | — |
| `example` | [#eval L241](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l241/) | L241-L245 | example check | example | — |
| `example` | [#eval L247](/corpus/taulib/docs/book-i-boundary-tau-rat-order/example-l247/) | L247-L250 | example check | example | — |
