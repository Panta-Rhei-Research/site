---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealOrder",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-order/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealOrder`.",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_slug": "book-i-boundary-tau-real-order",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealOrder.lean",
  "sha256": "79d255ba904f3d3f344e549f2e6cba9c0efe85398ac7e75f534f22704d644e16",
  "imports": [
    "TauLib.BookI.Boundary.ConstructiveReals",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRealAbs"
  ],
  "registry_ids": [
    "I.D112",
    "I.D113",
    "I.D84",
    "I.P49"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauReal.lt",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt/",
      "source_line_start": 80,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.lt_irrefl",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-irrefl/",
      "source_line_start": 85,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.le",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le/",
      "source_line_start": 105,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.le_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-refl/",
      "source_line_start": 110,
      "source_line_end": 121,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.le_of_lt",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-lt/",
      "source_line_start": 128,
      "source_line_end": 151,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.le_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-trans/",
      "source_line_start": 161,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.lt_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-trans/",
      "source_line_start": 191,
      "source_line_end": 212,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.lt_asymm",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-asymm/",
      "source_line_start": 215,
      "source_line_end": 217,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.lt_of_equiv_left",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-of-equiv-left/",
      "source_line_start": 224,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.lt_of_equiv_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-of-equiv-right/",
      "source_line_start": 260,
      "source_line_end": 283,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.le_of_equiv_left",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-left/",
      "source_line_start": 286,
      "source_line_end": 310,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.le_of_equiv_right",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-right/",
      "source_line_start": 313,
      "source_line_end": 359,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealOrder.lean`
- SHA-256: `79d255ba904f3d3f344e549f2e6cba9c0efe85398ac7e75f534f22704d644e16`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.ConstructiveReals`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`

## Imported By

- `TauLib.BookI.Boundary.TauRealAbs`

## Declaration Counts

- `def`: 2
- `theorem`: 10

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauReal.lt](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt/) | L80-L82 | definition | definition | — |
| `theorem` | [TauReal.lt_irrefl](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-irrefl/) | L85-L96 | proof obligation | formal proof obligation checked | — |
| `def` | [TauReal.le](/corpus/taulib/docs/book-i-boundary-tau-real-order/le/) | L105-L107 | definition | definition | — |
| `theorem` | [TauReal.le_refl](/corpus/taulib/docs/book-i-boundary-tau-real-order/le-refl/) | L110-L121 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.le_of_lt](/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-lt/) | L128-L151 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.le_trans](/corpus/taulib/docs/book-i-boundary-tau-real-order/le-trans/) | L161-L181 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.lt_trans](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-trans/) | L191-L212 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.lt_asymm](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-asymm/) | L215-L217 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.lt_of_equiv_left](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-of-equiv-left/) | L224-L257 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.lt_of_equiv_right](/corpus/taulib/docs/book-i-boundary-tau-real-order/lt-of-equiv-right/) | L260-L283 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.le_of_equiv_left](/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-left/) | L286-L310 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.le_of_equiv_right](/corpus/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-right/) | L313-L359 | proof obligation | formal proof obligation checked | — |
