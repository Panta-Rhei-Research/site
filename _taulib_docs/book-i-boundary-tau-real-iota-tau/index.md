---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRealIotaTau",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRealIotaTau`.",
  "module_name": "TauLib.BookI.Boundary.TauRealIotaTau",
  "module_slug": "book-i-boundary-tau-real-iota-tau",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRealIotaTau.lean",
  "sha256": "ac14490782a5ad73ed03e93b437102acb9ea3ecfb0459048b3facec6813ca3bb",
  "imports": [
    "TauLib.BookI.Boundary.TauRealPiPlusE",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push",
    "Mathlib.Tactic.FieldSimp",
    "Mathlib.Tactic.Positivity"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.IotaTauStructural"
  ],
  "registry_ids": [
    "I.D114",
    "I.D117",
    "I.D118",
    "I.D119",
    "I.D84"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 2
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauReal.two",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/two/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.two_approx_toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/two-approx-to-rat/",
      "source_line_start": 81,
      "source_line_end": 85,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauReal.iota_tau",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.iota_tau_mul_pi_plus_e_eq_two",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau-mul-pi-plus-e-eq-two/",
      "source_line_start": 118,
      "source_line_end": 167,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRealIotaTau.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRealIotaTau.lean`
- SHA-256: `ac14490782a5ad73ed03e93b437102acb9ea3ecfb0459048b3facec6813ca3bb`

## Registry Links

- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRealPiPlusE`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`
- `Mathlib.Tactic.FieldSimp`
- `Mathlib.Tactic.Positivity`

## Imported By

- `TauLib.BookI.Boundary.IotaTauStructural`

## Declaration Counts

- `def`: 2
- `theorem`: 2

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauReal.two](/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/two/) | L77-L78 | definition | definition | — |
| `theorem` | [TauReal.two_approx_toRat](/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/two-approx-to-rat/) | L81-L85 | proof obligation | formal proof obligation checked | — |
| `def` | [TauReal.iota_tau](/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau/) | L98-L99 | definition | definition | — |
| `theorem` | [TauReal.iota_tau_mul_pi_plus_e_eq_two](/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau-mul-pi-plus-e-eq-two/) | L118-L167 | proof obligation | formal proof obligation checked | — |
