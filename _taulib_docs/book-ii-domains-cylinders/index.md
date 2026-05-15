---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Domains.Cylinders",
  "permalink": "/corpus/taulib/docs/book-ii-domains-cylinders/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Domains.Cylinders`.",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_slug": "book-ii-domains-cylinders",
  "book": "BookII",
  "family": "Domains",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Domains/Cylinders.lean",
  "sha256": "980d0e163fd030044eaa9af9d5a153c9467c92286679dcc5ed2b04f3070c4216",
  "imports": [
    "TauLib.BookI.Polarity.ModArith"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Domains.Ultrametric"
  ],
  "registry_ids": [
    "II.D09",
    "II.D10",
    "II.D11",
    "II.T04"
  ],
  "declaration_counts": {
    "def": 8,
    "inductive": 1,
    "eval": 17,
    "theorem": 8
  },
  "declarations": [
    {
      "kind": "def",
      "name": "cylinder_mem",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-mem/",
      "source_line_start": 36,
      "source_line_end": 37,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D09"
      ]
    },
    {
      "kind": "def",
      "name": "cylinder_count",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-count/",
      "source_line_start": 40,
      "source_line_end": 47,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CylinderDomain",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-domain/",
      "source_line_start": 54,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D10"
      ]
    },
    {
      "kind": "def",
      "name": "eval_domain",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-domain/",
      "source_line_start": 61,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cylinder_clopen",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-clopen/",
      "source_line_start": 76,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D11"
      ]
    },
    {
      "kind": "def",
      "name": "nesting_check",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/nesting-check/",
      "source_line_start": 88,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "stage_zero_check",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/stage-zero-check/",
      "source_line_start": 100,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "partition_check",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/partition-check/",
      "source_line_start": 111,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "separation_check",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/separation-check/",
      "source_line_start": 130,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l144/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l145/",
      "source_line_start": 145,
      "source_line_end": 145,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l146/",
      "source_line_start": 146,
      "source_line_end": 146,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l147/",
      "source_line_start": 147,
      "source_line_end": 147,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l149/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l150/",
      "source_line_start": 150,
      "source_line_end": 150,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l152/",
      "source_line_start": 152,
      "source_line_end": 152,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l153/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l154/",
      "source_line_start": 154,
      "source_line_end": 154,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l156/",
      "source_line_start": 156,
      "source_line_end": 156,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l157/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l158/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l159/",
      "source_line_start": 159,
      "source_line_end": 159,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l160/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l161/",
      "source_line_start": 161,
      "source_line_end": 161,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l162/",
      "source_line_start": 162,
      "source_line_end": 162,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/eval-l163/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nesting_7_1_50",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/nesting-7-1-50/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nesting_7_2_50",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/nesting-7-2-50/",
      "source_line_start": 167,
      "source_line_end": 167,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "stage_zero",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/stage-zero/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "partition_1",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/partition-1/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "partition_2",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/partition-2/",
      "source_line_start": 170,
      "source_line_end": 170,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "partition_3",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/partition-3/",
      "source_line_start": 171,
      "source_line_end": 171,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sep_3_5",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/sep-3-5/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sep_7_13",
      "url": "/corpus/taulib/docs/book-ii-domains-cylinders/sep-7-13/",
      "source_line_start": 173,
      "source_line_end": 175,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean",
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
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Domains/Cylinders.lean`
- SHA-256: `980d0e163fd030044eaa9af9d5a153c9467c92286679dcc5ed2b04f3070c4216`

## Registry Links

- `II.D09` — Cylinder Domain
- `II.D10` — Stage-k Cylinder
- `II.D11` — Clopen Basis
- `II.T04` — Cylinder Basis Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.ModArith`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Domains.Ultrametric`

## Declaration Counts

- `def`: 8
- `eval`: 17
- `inductive`: 1
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [cylinder_mem](/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-mem/) | L36-L37 | data/computed value | data/computed value | `II.D09` |
| `def` | [cylinder_count](/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-count/) | L40-L47 | data/computed value | data/computed value | — |
| `inductive` | [CylinderDomain](/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-domain/) | L54-L58 | type/data schema | type/data schema | `II.D10` |
| `def` | [eval_domain](/corpus/taulib/docs/book-ii-domains-cylinders/eval-domain/) | L61-L66 | data/computed value | data/computed value | — |
| `def` | [cylinder_clopen](/corpus/taulib/docs/book-ii-domains-cylinders/cylinder-clopen/) | L76-L80 | definition | definition | `II.D11` |
| `def` | [nesting_check](/corpus/taulib/docs/book-ii-domains-cylinders/nesting-check/) | L88-L96 | data/computed value | data/computed value | — |
| `def` | [stage_zero_check](/corpus/taulib/docs/book-ii-domains-cylinders/stage-zero-check/) | L100-L107 | data/computed value | data/computed value | — |
| `def` | [partition_check](/corpus/taulib/docs/book-ii-domains-cylinders/partition-check/) | L111-L126 | data/computed value | data/computed value | — |
| `def` | [separation_check](/corpus/taulib/docs/book-ii-domains-cylinders/separation-check/) | L130-L138 | data/computed value | data/computed value | — |
| `eval` | [#eval L144](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l144/) | L144-L144 | computed check | computed check | — |
| `eval` | [#eval L145](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l145/) | L145-L145 | computed check | computed check | — |
| `eval` | [#eval L146](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l146/) | L146-L146 | computed check | computed check | — |
| `eval` | [#eval L147](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l147/) | L147-L147 | computed check | computed check | — |
| `eval` | [#eval L149](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l149/) | L149-L149 | computed check | computed check | — |
| `eval` | [#eval L150](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l150/) | L150-L150 | computed check | computed check | — |
| `eval` | [#eval L152](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l152/) | L152-L152 | computed check | computed check | — |
| `eval` | [#eval L153](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l153/) | L153-L153 | computed check | computed check | — |
| `eval` | [#eval L154](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l154/) | L154-L154 | computed check | computed check | — |
| `eval` | [#eval L156](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l156/) | L156-L156 | computed check | computed check | — |
| `eval` | [#eval L157](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l157/) | L157-L157 | computed check | computed check | — |
| `eval` | [#eval L158](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l158/) | L158-L158 | computed check | computed check | — |
| `eval` | [#eval L159](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l159/) | L159-L159 | computed check | computed check | — |
| `eval` | [#eval L160](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l160/) | L160-L160 | computed check | computed check | — |
| `eval` | [#eval L161](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l161/) | L161-L161 | computed check | computed check | — |
| `eval` | [#eval L162](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l162/) | L162-L162 | computed check | computed check | — |
| `eval` | [#eval L163](/corpus/taulib/docs/book-ii-domains-cylinders/eval-l163/) | L163-L163 | computed check | computed check | — |
| `theorem` | [nesting_7_1_50](/corpus/taulib/docs/book-ii-domains-cylinders/nesting-7-1-50/) | L166-L166 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nesting_7_2_50](/corpus/taulib/docs/book-ii-domains-cylinders/nesting-7-2-50/) | L167-L167 | proof obligation | formal proof obligation checked | — |
| `theorem` | [stage_zero](/corpus/taulib/docs/book-ii-domains-cylinders/stage-zero/) | L168-L168 | proof obligation | formal proof obligation checked | — |
| `theorem` | [partition_1](/corpus/taulib/docs/book-ii-domains-cylinders/partition-1/) | L169-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [partition_2](/corpus/taulib/docs/book-ii-domains-cylinders/partition-2/) | L170-L170 | proof obligation | formal proof obligation checked | — |
| `theorem` | [partition_3](/corpus/taulib/docs/book-ii-domains-cylinders/partition-3/) | L171-L171 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sep_3_5](/corpus/taulib/docs/book-ii-domains-cylinders/sep-3-5/) | L172-L172 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sep_7_13](/corpus/taulib/docs/book-ii-domains-cylinders/sep-7-13/) | L173-L175 | proof obligation | formal proof obligation checked | — |
