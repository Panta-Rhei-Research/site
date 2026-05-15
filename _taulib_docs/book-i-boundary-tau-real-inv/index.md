---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealInv",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealInv`.",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_slug": "book-i-boundary-tau-real-inv",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealInv.lean",
  "sha256": "2fa7dc16297ab0a20364eef7cd008c9a6effe114444d1336ef1d9a6618f6809c",
  "imports": [
    "TauLib.BookI.Boundary.TauRealAbs",
    "TauLib.BookI.Boundary.TauRatInv",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRealMulCongr",
    "TauLib.BookI.Boundary.TauRealSum"
  ],
  "registry_ids": [
    "I.D110",
    "I.D112",
    "I.D114",
    "I.D84",
    "I.P49"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 4
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauReal.BoundedAwayFromZero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/bounded-away-from-zero/",
      "source_line_start": 68,
      "source_line_end": 70,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.is_nonzero_of_bounded_away",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/is-nonzero-of-bounded-away/",
      "source_line_start": 74,
      "source_line_end": 100,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.inv",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/inv/",
      "source_line_start": 112,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.div",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/div/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.mul_inv_cancel",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/mul-inv-cancel/",
      "source_line_start": 132,
      "source_line_end": 156,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.inv_mul_cancel",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/inv-mul-cancel/",
      "source_line_start": 160,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.div_self",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-inv/div-self/",
      "source_line_start": 166,
      "source_line_end": 170,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealInv.lean`
- SHA-256: `2fa7dc16297ab0a20364eef7cd008c9a6effe114444d1336ef1d9a6618f6809c`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealAbs`
- `TauLib.BookI.Boundary.TauRatInv`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`

## Imported By

- `TauLib.BookI.Boundary.TauRealMulCongr`
- `TauLib.BookI.Boundary.TauRealSum`

## Declaration Counts

- `def`: 3
- `theorem`: 4

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauReal.BoundedAwayFromZero](/corpus/taulib/docs/book-i-boundary-tau-real-inv/bounded-away-from-zero/) | L68-L70 | definition | definition | — |
| `theorem` | [TauReal.is_nonzero_of_bounded_away](/corpus/taulib/docs/book-i-boundary-tau-real-inv/is-nonzero-of-bounded-away/) | L74-L100 | proof obligation | formal proof obligation checked | — |
| `def` | [TauReal.inv](/corpus/taulib/docs/book-i-boundary-tau-real-inv/inv/) | L112-L114 | definition | definition | — |
| `def` | [TauReal.div](/corpus/taulib/docs/book-i-boundary-tau-real-inv/div/) | L117-L118 | definition | definition | — |
| `theorem` | [TauReal.mul_inv_cancel](/corpus/taulib/docs/book-i-boundary-tau-real-inv/mul-inv-cancel/) | L132-L156 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.inv_mul_cancel](/corpus/taulib/docs/book-i-boundary-tau-real-inv/inv-mul-cancel/) | L160-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.div_self](/corpus/taulib/docs/book-i-boundary-tau-real-inv/div-self/) | L166-L170 | proof obligation | formal proof obligation checked | — |
