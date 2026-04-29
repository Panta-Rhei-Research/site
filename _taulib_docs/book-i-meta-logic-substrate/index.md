---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.Substrate",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-substrate/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.MetaLogic.Substrate`.",
  "module_name": "TauLib.BookI.MetaLogic.Substrate",
  "module_slug": "book-i-meta-logic-substrate",
  "book": "BookI",
  "family": "MetaLogic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/MetaLogic/Substrate.lean",
  "sha256": "f66906649acca7181bb2a91fb748938e99155ac0e902dbe35025e08c69a0806a",
  "imports": [
    "TauLib.BookI.Kernel.Diagonal"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.MetaLogic.LinearDiscipline",
    "TauLib.BookI.MetaLogic.StructuralExclusion"
  ],
  "registry_ids": [
    "I.D77",
    "I.R15"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 4,
    "theorem": 13,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "StructuralRule",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/structural-rule/",
      "source_line_start": 29,
      "source_line_end": 35,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ObjectLevelStatus",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/object-level-status/",
      "source_line_start": 42,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "k5_status",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/k5-status/",
      "source_line_start": 51,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "contraction_refused",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/contraction-refused/",
      "source_line_start": 61,
      "source_line_end": 61,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weakening_refused",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/weakening-refused/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exchange_preserved",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/exchange-preserved/",
      "source_line_start": 67,
      "source_line_end": 67,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allRules",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/all-rules/",
      "source_line_start": 74,
      "source_line_end": 74,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "allRules_length",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/all-rules-length/",
      "source_line_start": 77,
      "source_line_end": 77,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "refusedRules",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/refused-rules/",
      "source_line_start": 80,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "preservedRules",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/preserved-rules/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refused_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/refused-count/",
      "source_line_start": 88,
      "source_line_end": 88,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "preserved_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/preserved-count/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refused_are",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/refused-are/",
      "source_line_start": 94,
      "source_line_end": 94,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "preserved_is",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/preserved-is/",
      "source_line_start": 97,
      "source_line_end": 97,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "count_partition",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/count-partition/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_discipline_refuses_contraction",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/diagonal-discipline-refuses-contraction/",
      "source_line_start": 113,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_discipline_refuses_weakening",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/diagonal-discipline-refuses-weakening/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "scaffold_invariant",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/scaffold-invariant/",
      "source_line_start": 126,
      "source_line_end": 126,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rewiring_budget",
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/rewiring-budget/",
      "source_line_start": 131,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l139/",
      "source_line_start": 139,
      "source_line_end": 139,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l140/",
      "source_line_start": 140,
      "source_line_end": 140,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l141/",
      "source_line_start": 141,
      "source_line_end": 141,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l142/",
      "source_line_start": 142,
      "source_line_end": 142,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l143/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l144/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-substrate/eval-l145/",
      "source_line_start": 145,
      "source_line_end": 147,
      "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean",
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
- Source path: [`TauLib/BookI/MetaLogic/Substrate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/MetaLogic/Substrate.lean`
- SHA-256: `f66906649acca7181bb2a91fb748938e99155ac0e902dbe35025e08c69a0806a`

## Registry Links

- `I.D77` — Meta-Logical Substrate
- `I.R15` — Structural Rules Inventory

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Kernel.Diagonal`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.MetaLogic.LinearDiscipline`
- `TauLib.BookI.MetaLogic.StructuralExclusion`

## Declaration Counts

- `def`: 4
- `eval`: 7
- `inductive`: 2
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [StructuralRule](/verify/taulib/docs/book-i-meta-logic-substrate/structural-rule/) | L29-L35 | defined | — |
| `inductive` | [ObjectLevelStatus](/verify/taulib/docs/book-i-meta-logic-substrate/object-level-status/) | L42-L47 | defined | — |
| `def` | [k5_status](/verify/taulib/docs/book-i-meta-logic-substrate/k5-status/) | L51-L54 | defined | — |
| `theorem` | [contraction_refused](/verify/taulib/docs/book-i-meta-logic-substrate/contraction-refused/) | L61-L61 | formalized | — |
| `theorem` | [weakening_refused](/verify/taulib/docs/book-i-meta-logic-substrate/weakening-refused/) | L64-L64 | formalized | — |
| `theorem` | [exchange_preserved](/verify/taulib/docs/book-i-meta-logic-substrate/exchange-preserved/) | L67-L67 | formalized | — |
| `def` | [allRules](/verify/taulib/docs/book-i-meta-logic-substrate/all-rules/) | L74-L74 | defined | — |
| `theorem` | [allRules_length](/verify/taulib/docs/book-i-meta-logic-substrate/all-rules-length/) | L77-L77 | formalized | — |
| `def` | [refusedRules](/verify/taulib/docs/book-i-meta-logic-substrate/refused-rules/) | L80-L81 | defined | — |
| `def` | [preservedRules](/verify/taulib/docs/book-i-meta-logic-substrate/preserved-rules/) | L84-L85 | defined | — |
| `theorem` | [refused_count](/verify/taulib/docs/book-i-meta-logic-substrate/refused-count/) | L88-L88 | formalized | — |
| `theorem` | [preserved_count](/verify/taulib/docs/book-i-meta-logic-substrate/preserved-count/) | L91-L91 | formalized | — |
| `theorem` | [refused_are](/verify/taulib/docs/book-i-meta-logic-substrate/refused-are/) | L94-L94 | formalized | — |
| `theorem` | [preserved_is](/verify/taulib/docs/book-i-meta-logic-substrate/preserved-is/) | L97-L97 | formalized | — |
| `theorem` | [count_partition](/verify/taulib/docs/book-i-meta-logic-substrate/count-partition/) | L100-L101 | formalized | — |
| `theorem` | [diagonal_discipline_refuses_contraction](/verify/taulib/docs/book-i-meta-logic-substrate/diagonal-discipline-refuses-contraction/) | L113-L115 | formalized | — |
| `theorem` | [diagonal_discipline_refuses_weakening](/verify/taulib/docs/book-i-meta-logic-substrate/diagonal-discipline-refuses-weakening/) | L120-L122 | formalized | — |
| `theorem` | [scaffold_invariant](/verify/taulib/docs/book-i-meta-logic-substrate/scaffold-invariant/) | L126-L126 | formalized | — |
| `theorem` | [rewiring_budget](/verify/taulib/docs/book-i-meta-logic-substrate/rewiring-budget/) | L131-L133 | formalized | — |
| `eval` | [#eval L139](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l139/) | L139-L139 | computed | — |
| `eval` | [#eval L140](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l140/) | L140-L140 | computed | — |
| `eval` | [#eval L141](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l141/) | L141-L141 | computed | — |
| `eval` | [#eval L142](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l142/) | L142-L142 | computed | — |
| `eval` | [#eval L143](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l143/) | L143-L143 | computed | — |
| `eval` | [#eval L144](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l144/) | L144-L144 | computed | — |
| `eval` | [#eval L145](/verify/taulib/docs/book-i-meta-logic-substrate/eval-l145/) | L145-L147 | computed | — |
