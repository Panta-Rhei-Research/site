---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealAbs",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealAbs`.",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_slug": "book-i-boundary-tau-real-abs",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealAbs.lean",
  "sha256": "9224cc7930defa79ac93634dd6c89a0539b694d88bf682cbfff769f296c7eb4e",
  "imports": [
    "TauLib.BookI.Boundary.TauRealOrder",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRealInv"
  ],
  "registry_ids": [
    "I.D109",
    "I.D112",
    "I.D114",
    "I.D84",
    "I.P49"
  ],
  "declaration_counts": {
    "def": 1,
    "theorem": 5
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauReal.abs",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs/",
      "source_line_start": 50,
      "source_line_end": 60,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.abs_nonneg",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-nonneg/",
      "source_line_start": 68,
      "source_line_end": 88,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_sub_abs_le_abs_sub_toRat",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-sub-abs-le-abs-sub-to-rat/",
      "source_line_start": 96,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.abs_of_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-of-equiv/",
      "source_line_start": 103,
      "source_line_end": 114,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.abs_preserves_cauchy",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-preserves-cauchy/",
      "source_line_start": 122,
      "source_line_end": 132,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.abs_triangle",
      "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-triangle/",
      "source_line_start": 146,
      "source_line_end": 172,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealAbs.lean`
- SHA-256: `9224cc7930defa79ac93634dd6c89a0539b694d88bf682cbfff769f296c7eb4e`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealOrder`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`

## Imported By

- `TauLib.BookI.Boundary.TauRealInv`

## Declaration Counts

- `def`: 1
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [TauReal.abs](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs/) | L50-L60 | defined | — |
| `theorem` | [TauReal.abs_nonneg](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-nonneg/) | L68-L88 | formalized | — |
| `theorem` | [TauRat.abs_sub_abs_le_abs_sub_toRat](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-sub-abs-le-abs-sub-to-rat/) | L96-L99 | formalized | — |
| `theorem` | [TauReal.abs_of_equiv](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-of-equiv/) | L103-L114 | formalized | — |
| `theorem` | [TauReal.abs_preserves_cauchy](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-preserves-cauchy/) | L122-L132 | formalized | — |
| `theorem` | [TauReal.abs_triangle](/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-triangle/) | L146-L172 | formalized | — |
