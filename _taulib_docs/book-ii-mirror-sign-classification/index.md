---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Mirror.SignClassification",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Mirror.SignClassification`.",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_slug": "book-ii-mirror-sign-classification",
  "book": "BookII",
  "family": "Mirror",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Mirror/SignClassification.lean",
  "sha256": "d2972fa32cd6028fe8272118a5f70851e013e5288582e409090171a49d4d7583",
  "imports": [
    "TauLib.BookII.Enrichment.EnrichmentLadder"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Mirror.WaveHolomorphy"
  ],
  "registry_ids": [
    "II.D68",
    "II.D69",
    "II.T43"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 9,
    "theorem": 23,
    "structure": 1,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "SignLevel",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level/",
      "source_line_start": 47,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "def",
      "name": "orthodox_property",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-property/",
      "source_line_start": 69,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "def",
      "name": "tau_property",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-property/",
      "source_line_start": 84,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "def",
      "name": "allSignLevels",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/all-sign-levels/",
      "source_line_start": 103,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sign_level_count",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level-count/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "def",
      "name": "orthodox_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-nonempty/",
      "source_line_start": 112,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-nonempty/",
      "source_line_start": 116,
      "source_line_end": 117,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_orthodox_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/all-orthodox-nonempty/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_tau_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/all-tau-nonempty/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "descriptions_differ",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/descriptions-differ/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_descriptions_differ",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/all-descriptions-differ/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "structure",
      "name": "InfinityTradeOff",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/infinity-trade-off/",
      "source_line_start": 146,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": [
        "II.D69"
      ]
    },
    {
      "kind": "def",
      "name": "orthodox_path",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path/",
      "source_line_start": 155,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": [
        "II.D69"
      ]
    },
    {
      "kind": "def",
      "name": "tau_path",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path/",
      "source_line_start": 163,
      "source_line_end": 167,
      "formal_status": "defined",
      "registry_ids": [
        "II.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "orthodox_path_no_unique_omega",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path-no-unique-omega/",
      "source_line_start": 174,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_path_no_archimedean",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path-no-archimedean/",
      "source_line_start": 178,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "orthodox_path_no_finite_witnesses",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path-no-finite-witnesses/",
      "source_line_start": 182,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_path_no_epsilon_delta",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path-no-epsilon-delta/",
      "source_line_start": 186,
      "source_line_end": 187,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "structural_incompatibility",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/structural-incompatibility/",
      "source_line_start": 191,
      "source_line_end": 194,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "paths_distinct",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/paths-distinct/",
      "source_line_start": 197,
      "source_line_end": 200,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_both_omega_and_archimedean_orthodox",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/no-both-omega-and-archimedean-orthodox/",
      "source_line_start": 204,
      "source_line_end": 209,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_both_omega_and_archimedean_tau",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/no-both-omega-and-archimedean-tau/",
      "source_line_start": 212,
      "source_line_end": 217,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
    },
    {
      "kind": "def",
      "name": "sign_level_index",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level-index/",
      "source_line_start": 224,
      "source_line_end": 236,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sign_indices_injective",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-indices-injective/",
      "source_line_start": 239,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sign_index_bound",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-index-bound/",
      "source_line_start": 244,
      "source_line_end": 246,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l255/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l268/",
      "source_line_start": 268,
      "source_line_end": 268,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sign_count_12",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-count-12/",
      "source_line_start": 275,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "theorem",
      "name": "orthodox_all_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-all-nonempty/",
      "source_line_start": 279,
      "source_line_end": 280,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D68"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_all_nonempty",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-all-nonempty/",
      "source_line_start": 282,
      "source_line_end": 283,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_differ",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/all-differ/",
      "source_line_start": 285,
      "source_line_end": 286,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_omega",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-omega/",
      "source_line_start": 289,
      "source_line_end": 290,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_archimedean",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-archimedean/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_epsilon",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-epsilon/",
      "source_line_start": 295,
      "source_line_end": 296,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_witnesses",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-witnesses/",
      "source_line_start": 298,
      "source_line_end": 299,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "incompatibility_native",
      "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/incompatibility-native/",
      "source_line_start": 302,
      "source_line_end": 307,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T43"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean",
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
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Mirror/SignClassification.lean`
- SHA-256: `d2972fa32cd6028fe8272118a5f70851e013e5288582e409090171a49d4d7583`

## Registry Links

- `II.D68` — Structural Sign Classification
- `II.D69` — The Infinity Trade-Off
- `II.T43` — Structural Incompatibility of Unique Omega and Archimedean Density

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Enrichment.EnrichmentLadder`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Mirror.WaveHolomorphy`

## Declaration Counts

- `def`: 9
- `eval`: 10
- `inductive`: 1
- `structure`: 1
- `theorem`: 23

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [SignLevel](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level/) | L47-L62 | defined | `II.D68` |
| `def` | [orthodox_property](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-property/) | L69-L81 | defined | `II.D68` |
| `def` | [tau_property](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-property/) | L84-L96 | defined | `II.D68` |
| `def` | [allSignLevels](/verify/taulib/docs/book-ii-mirror-sign-classification/all-sign-levels/) | L103-L106 | defined | — |
| `theorem` | [sign_level_count](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level-count/) | L109-L109 | formalized | `II.D68` |
| `def` | [orthodox_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-nonempty/) | L112-L113 | defined | — |
| `def` | [tau_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-nonempty/) | L116-L117 | defined | — |
| `theorem` | [all_orthodox_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/all-orthodox-nonempty/) | L120-L121 | formalized | — |
| `theorem` | [all_tau_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/all-tau-nonempty/) | L124-L125 | formalized | — |
| `def` | [descriptions_differ](/verify/taulib/docs/book-ii-mirror-sign-classification/descriptions-differ/) | L128-L129 | defined | — |
| `theorem` | [all_descriptions_differ](/verify/taulib/docs/book-ii-mirror-sign-classification/all-descriptions-differ/) | L132-L133 | formalized | `II.D68` |
| `structure` | [InfinityTradeOff](/verify/taulib/docs/book-ii-mirror-sign-classification/infinity-trade-off/) | L146-L151 | defined | `II.D69` |
| `def` | [orthodox_path](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path/) | L155-L159 | defined | `II.D69` |
| `def` | [tau_path](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path/) | L163-L167 | defined | `II.D69` |
| `theorem` | [orthodox_path_no_unique_omega](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path-no-unique-omega/) | L174-L175 | formalized | `II.T43` |
| `theorem` | [tau_path_no_archimedean](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path-no-archimedean/) | L178-L179 | formalized | `II.T43` |
| `theorem` | [orthodox_path_no_finite_witnesses](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path-no-finite-witnesses/) | L182-L183 | formalized | `II.T43` |
| `theorem` | [tau_path_no_epsilon_delta](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-path-no-epsilon-delta/) | L186-L187 | formalized | `II.T43` |
| `theorem` | [structural_incompatibility](/verify/taulib/docs/book-ii-mirror-sign-classification/structural-incompatibility/) | L191-L194 | formalized | `II.T43` |
| `theorem` | [paths_distinct](/verify/taulib/docs/book-ii-mirror-sign-classification/paths-distinct/) | L197-L200 | formalized | `II.T43` |
| `theorem` | [no_both_omega_and_archimedean_orthodox](/verify/taulib/docs/book-ii-mirror-sign-classification/no-both-omega-and-archimedean-orthodox/) | L204-L209 | formalized | `II.T43` |
| `theorem` | [no_both_omega_and_archimedean_tau](/verify/taulib/docs/book-ii-mirror-sign-classification/no-both-omega-and-archimedean-tau/) | L212-L217 | formalized | `II.T43` |
| `def` | [sign_level_index](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level-index/) | L224-L236 | defined | — |
| `theorem` | [sign_indices_injective](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-indices-injective/) | L239-L241 | formalized | — |
| `theorem` | [sign_index_bound](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-index-bound/) | L244-L246 | formalized | — |
| `eval` | [#eval L253](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l253/) | L253-L253 | computed | — |
| `eval` | [#eval L254](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l254/) | L254-L254 | computed | — |
| `eval` | [#eval L255](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l255/) | L255-L255 | computed | — |
| `eval` | [#eval L256](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l256/) | L256-L256 | computed | — |
| `eval` | [#eval L257](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l257/) | L257-L257 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L261](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l261/) | L261-L261 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l265/) | L265-L265 | computed | — |
| `eval` | [#eval L268](/verify/taulib/docs/book-ii-mirror-sign-classification/eval-l268/) | L268-L268 | computed | — |
| `theorem` | [sign_count_12](/verify/taulib/docs/book-ii-mirror-sign-classification/sign-count-12/) | L275-L276 | formalized | `II.D68` |
| `theorem` | [orthodox_all_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-all-nonempty/) | L279-L280 | formalized | `II.D68` |
| `theorem` | [tau_all_nonempty](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-all-nonempty/) | L282-L283 | formalized | — |
| `theorem` | [all_differ](/verify/taulib/docs/book-ii-mirror-sign-classification/all-differ/) | L285-L286 | formalized | — |
| `theorem` | [orthodox_omega](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-omega/) | L289-L290 | formalized | `II.D69` |
| `theorem` | [tau_archimedean](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-archimedean/) | L292-L293 | formalized | — |
| `theorem` | [orthodox_epsilon](/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-epsilon/) | L295-L296 | formalized | — |
| `theorem` | [tau_witnesses](/verify/taulib/docs/book-ii-mirror-sign-classification/tau-witnesses/) | L298-L299 | formalized | — |
| `theorem` | [incompatibility_native](/verify/taulib/docs/book-ii-mirror-sign-classification/incompatibility-native/) | L302-L307 | formalized | `II.T43` |
