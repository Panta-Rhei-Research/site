---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealSum",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealSum`.",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_slug": "book-i-boundary-tau-real-sum",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealSum.lean",
  "sha256": "4c07219f9c7db9efb46762bbcd06a7ecb3c42976f4547ea91c669d9e1d8c39d0",
  "imports": [
    "TauLib.BookI.Boundary.TauRealInv",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRealAnalyticalHelpers"
  ],
  "registry_ids": [
    "I.D107",
    "I.D109",
    "I.D35"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauRat.factorial",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial/",
      "source_line_start": 57,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.factorial_pos",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-pos/",
      "source_line_start": 61,
      "source_line_end": 66,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.factorial_toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-to-rat/",
      "source_line_start": 69,
      "source_line_end": 72,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.factorial_ne_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-ne-zero/",
      "source_line_start": 75,
      "source_line_end": 76,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.sum",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum/",
      "source_line_start": 83,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.sumFromTo",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to/",
      "source_line_start": 99,
      "source_line_end": 106,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.sumFromTo_self",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-self/",
      "source_line_start": 108,
      "source_line_end": 114,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.sum_sub_toRat_eq_sumFromTo",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-sub-to-rat-eq-sum-from-to/",
      "source_line_start": 122,
      "source_line_end": 147,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.sumFromTo_abs_le",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-abs-le/",
      "source_line_start": 158,
      "source_line_end": 192,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealSum.lean`
- SHA-256: `4c07219f9c7db9efb46762bbcd06a7ecb3c42976f4547ea91c669d9e1d8c39d0`

## Registry Links

- `I.D35` — Number Tower

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealInv`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`

## Imported By

- `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`

## Declaration Counts

- `def`: 3
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauRat.factorial](/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial/) | L57-L58 | data/computed value | data/computed value | — |
| `theorem` | [TauRat.factorial_pos](/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-pos/) | L61-L66 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.factorial_toRat](/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-to-rat/) | L69-L72 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.factorial_ne_zero](/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-ne-zero/) | L75-L76 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.sum](/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum/) | L83-L91 | data/computed value | data/computed value | — |
| `def` | [TauRat.sumFromTo](/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to/) | L99-L106 | data/computed value | data/computed value | — |
| `theorem` | [TauRat.sumFromTo_self](/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-self/) | L108-L114 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.sum_sub_toRat_eq_sumFromTo](/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-sub-to-rat-eq-sum-from-to/) | L122-L147 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.sumFromTo_abs_le](/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-abs-le/) | L158-L192 | proof obligation | formal proof obligation checked | — |
