---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealE",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-e/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealE`.",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_slug": "book-i-boundary-tau-real-e",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealE.lean",
  "sha256": "bcd3fc55f16abbcb2d5e1428d94a3f1f9bd54753e25a2a69f7810ebdcae4d190",
  "imports": [
    "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp",
    "Mathlib.Tactic.Positivity"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.TauRealPiPlusE"
  ],
  "registry_ids": [
    "I.D111",
    "I.D115",
    "I.D116",
    "I.D84"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 7
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauRat.e_term",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term/",
      "source_line_start": 47,
      "source_line_end": 48,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.e_term_toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-to-rat/",
      "source_line_start": 50,
      "source_line_end": 53,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.e_term_pos",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-pos/",
      "source_line_start": 55,
      "source_line_end": 59,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_e_term_toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/abs-e-term-to-rat/",
      "source_line_start": 61,
      "source_line_end": 63,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.e_partial",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-partial/",
      "source_line_start": 66,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.e",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e/",
      "source_line_start": 69,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.e_term_le_geom",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-le-geom/",
      "source_line_start": 76,
      "source_line_end": 91,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.sumFromTo_e_term_bound",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/sum-from-to-e-term-bound/",
      "source_line_start": 99,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.e_partial_cauchy_bound",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-partial-cauchy-bound/",
      "source_line_start": 135,
      "source_line_end": 171,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.e_isCauchy",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-is-cauchy/",
      "source_line_start": 178,
      "source_line_end": 208,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealE.lean`
- SHA-256: `bcd3fc55f16abbcb2d5e1428d94a3f1f9bd54753e25a2a69f7810ebdcae4d190`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`
- `Mathlib.Tactic.Positivity`

## Imported By

- `TauLib.BookI.Boundary.TauRealPiPlusE`

## Declaration Counts

- `def`: 3
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauRat.e_term](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term/) | L47-L48 | data/computed value | data/computed value | — |
| `theorem` | [TauRat.e_term_toRat](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-to-rat/) | L50-L53 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.e_term_pos](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-pos/) | L55-L59 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_e_term_toRat](/corpus/taulib/docs/book-i-boundary-tau-real-e/abs-e-term-to-rat/) | L61-L63 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.e_partial](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-partial/) | L66-L66 | data/computed value | data/computed value | — |
| `def` | [TauReal.e](/corpus/taulib/docs/book-i-boundary-tau-real-e/e/) | L69-L69 | definition | definition | — |
| `theorem` | [TauRat.e_term_le_geom](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term-le-geom/) | L76-L91 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.sumFromTo_e_term_bound](/corpus/taulib/docs/book-i-boundary-tau-real-e/sum-from-to-e-term-bound/) | L99-L129 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.e_partial_cauchy_bound](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-partial-cauchy-bound/) | L135-L171 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.e_isCauchy](/corpus/taulib/docs/book-i-boundary-tau-real-e/e-is-cauchy/) | L178-L208 | proof obligation | formal proof obligation checked | — |
