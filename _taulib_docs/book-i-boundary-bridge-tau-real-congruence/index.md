---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_slug": "book-i-boundary-bridge-tau-real-congruence",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean",
  "sha256": "d053cd5b0033bdedcd34a7580ce8f5300f3eab1422dd0bad4cc1c56f439d4a70",
  "imports": [
    "TauLib.BookI.Boundary.TauRealMulCongr",
    "Mathlib.Algebra.Order.Ring.Abs",
    "Mathlib.Algebra.Order.Archimedean.Basic",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp",
    "Mathlib.Tactic.Positivity"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.Bridge.TauRealQuotient"
  ],
  "registry_ids": [
    "I.D111",
    "I.D112",
    "I.D84"
  ],
  "declaration_counts": {
    "theorem": 7
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "TauReal.add_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/add-respects-equiv/",
      "source_line_start": 78,
      "source_line_end": 117,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.negate_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/negate-respects-equiv/",
      "source_line_start": 127,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.IsCauchy_add",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-add/",
      "source_line_start": 150,
      "source_line_end": 180,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.IsCauchy_negate",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-negate/",
      "source_line_start": 183,
      "source_line_end": 197,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.IsCauchy.bounded",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/bounded/",
      "source_line_start": 212,
      "source_line_end": 257,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.mul_respects_equiv_under_cauchy",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/mul-respects-equiv-under-cauchy/",
      "source_line_start": 272,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.IsCauchy_mul",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-mul/",
      "source_line_start": 308,
      "source_line_end": 430,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`
- SHA-256: `d053cd5b0033bdedcd34a7580ce8f5300f3eab1422dd0bad4cc1c56f439d4a70`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealMulCongr`
- `Mathlib.Algebra.Order.Ring.Abs`
- `Mathlib.Algebra.Order.Archimedean.Basic`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`
- `Mathlib.Tactic.Positivity`

## Imported By

- `TauLib.BookI.Boundary.Bridge.TauRealQuotient`

## Declaration Counts

- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [TauReal.add_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/add-respects-equiv/) | L78-L117 | formalized | — |
| `theorem` | [TauReal.negate_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/negate-respects-equiv/) | L127-L143 | formalized | — |
| `theorem` | [TauReal.IsCauchy_add](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-add/) | L150-L180 | formalized | — |
| `theorem` | [TauReal.IsCauchy_negate](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-negate/) | L183-L197 | formalized | — |
| `theorem` | [TauReal.IsCauchy.bounded](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/bounded/) | L212-L257 | formalized | — |
| `theorem` | [TauReal.mul_respects_equiv_under_cauchy](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/mul-respects-equiv-under-cauchy/) | L272-L293 | formalized | — |
| `theorem` | [TauReal.IsCauchy_mul](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-mul/) | L308-L430 | formalized | — |
