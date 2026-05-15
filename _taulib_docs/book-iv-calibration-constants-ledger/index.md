---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.ConstantsLedger",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_slug": "book-iv-calibration-constants-ledger",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/ConstantsLedger.lean",
  "sha256": "7ab1abfa4c87c7be47e6e7ced1902ec0552366087924f7c505baff01779b08f3",
  "imports": [
    "TauLib.BookIV.Calibration.DimensionalBridge",
    "TauLib.BookIV.Calibration.DimensionlessNearMatch"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.ConstantsLedgerExt",
    "TauLib.BookIV.Calibration.RunningRegime"
  ],
  "registry_ids": [
    "IV.D38",
    "IV.D39",
    "IV.R09",
    "IV.T09"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 1,
    "def": 6,
    "theorem": 6,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "LedgerScope",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-scope/",
      "source_line_start": 59,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D38"
      ]
    },
    {
      "kind": "structure",
      "name": "LedgerEntry",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-entry/",
      "source_line_start": 71,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D38"
      ]
    },
    {
      "kind": "def",
      "name": "coupling_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/coupling-ledger/",
      "source_line_start": 87,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "formula_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/formula-ledger/",
      "source_line_start": 105,
      "source_line_end": 111,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "identity_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/identity-ledger/",
      "source_line_start": 118,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "near_match_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/near-match-ledger/",
      "source_line_start": 128,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "framework_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/framework-ledger/",
      "source_line_start": 139,
      "source_line_end": 143,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "complete_ledger",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/complete-ledger/",
      "source_line_start": 150,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D39"
      ]
    },
    {
      "kind": "theorem",
      "name": "ledger_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-count/",
      "source_line_start": 159,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T09"
      ]
    },
    {
      "kind": "theorem",
      "name": "ledger_breakdown",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-breakdown/",
      "source_line_start": 162,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "scope_distribution",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/scope-distribution/",
      "source_line_start": 179,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.R09"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_metaphorical",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/no-metaphorical/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_have_ids",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/all-have-ids/",
      "source_line_start": 195,
      "source_line_end": 196,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_have_names",
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/all-have-names/",
      "source_line_start": 199,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l207/",
      "source_line_start": 207,
      "source_line_end": 207,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l213/",
      "source_line_start": 213,
      "source_line_end": 213,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l217/",
      "source_line_start": 217,
      "source_line_end": 217,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l218/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 222,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/ConstantsLedger.lean`
- SHA-256: `7ab1abfa4c87c7be47e6e7ced1902ec0552366087924f7c505baff01779b08f3`

## Registry Links

- `IV.D38` — Ledger Entry
- `IV.D39` — Complete Constants Ledger
- `IV.R09` — Self-Assessment
- `IV.T09` — Ledger Count

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Calibration.DimensionalBridge`
- `TauLib.BookIV.Calibration.DimensionlessNearMatch`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.ConstantsLedgerExt`
- `TauLib.BookIV.Calibration.RunningRegime`

## Declaration Counts

- `def`: 6
- `eval`: 10
- `inductive`: 1
- `structure`: 1
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [LedgerScope](/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-scope/) | L59-L64 | type/data schema | type/data schema | `IV.D38` |
| `structure` | [LedgerEntry](/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-entry/) | L71-L80 | type/data schema | type/data schema | `IV.D38` |
| `def` | [coupling_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/coupling-ledger/) | L87-L98 | data/computed value | data/computed value | — |
| `def` | [formula_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/formula-ledger/) | L105-L111 | data/computed value | data/computed value | — |
| `def` | [identity_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/identity-ledger/) | L118-L121 | data/computed value | data/computed value | — |
| `def` | [near_match_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/near-match-ledger/) | L128-L132 | data/computed value | data/computed value | — |
| `def` | [framework_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/framework-ledger/) | L139-L143 | data/computed value | data/computed value | — |
| `def` | [complete_ledger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/complete-ledger/) | L150-L152 | data/computed value | data/computed value | `IV.D39` |
| `theorem` | [ledger_count](/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-count/) | L159-L159 | proof obligation | formal proof obligation checked | `IV.T09` |
| `theorem` | [ledger_breakdown](/corpus/taulib/docs/book-iv-calibration-constants-ledger/ledger-breakdown/) | L162-L168 | proof obligation | formal proof obligation checked | — |
| `theorem` | [scope_distribution](/corpus/taulib/docs/book-iv-calibration-constants-ledger/scope-distribution/) | L179-L183 | proof obligation | formal proof obligation checked | `IV.R09` |
| `theorem` | [no_metaphorical](/corpus/taulib/docs/book-iv-calibration-constants-ledger/no-metaphorical/) | L186-L188 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_have_ids](/corpus/taulib/docs/book-iv-calibration-constants-ledger/all-have-ids/) | L195-L196 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_have_names](/corpus/taulib/docs/book-iv-calibration-constants-ledger/all-have-names/) | L199-L200 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L207](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l207/) | L207-L207 | computed check | computed check | — |
| `eval` | [#eval L210](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l210/) | L210-L210 | computed check | computed check | — |
| `eval` | [#eval L211](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l211/) | L211-L211 | computed check | computed check | — |
| `eval` | [#eval L212](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l212/) | L212-L212 | computed check | computed check | — |
| `eval` | [#eval L213](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l213/) | L213-L213 | computed check | computed check | — |
| `eval` | [#eval L216](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l216/) | L216-L216 | computed check | computed check | — |
| `eval` | [#eval L217](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l217/) | L217-L217 | computed check | computed check | — |
| `eval` | [#eval L218](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l218/) | L218-L218 | computed check | computed check | — |
| `eval` | [#eval L219](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l219/) | L219-L219 | computed check | computed check | — |
| `eval` | [#eval L220](/corpus/taulib/docs/book-iv-calibration-constants-ledger/eval-l220/) | L220-L222 | computed check | computed check | — |
