---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Topos.EarnedArrows",
  "permalink": "/corpus/taulib/docs/book-i-topos-earned-arrows/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Topos.EarnedArrows`.",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_slug": "book-i-topos-earned-arrows",
  "book": "BookI",
  "family": "Topos",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Topos/EarnedArrows.lean",
  "sha256": "1e4d4d6a1a915ed1de9777b2a67e454cde0f6523827095ad27c9f070f8851e18",
  "imports": [
    "TauLib.BookI.Holomorphy.DiagonalProtection",
    "TauLib.BookI.Holomorphy.IdentityTheorem"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Topos.Functors",
    "TauLib.BookI.Topos.H6EarnedCategoricalMachine"
  ],
  "registry_ids": [
    "I.D50",
    "I.D51",
    "I.P25",
    "I.T22"
  ],
  "declaration_counts": {
    "structure": 2,
    "def": 4,
    "theorem": 12,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauArrow",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/tau-arrow/",
      "source_line_start": 47,
      "source_line_end": 50,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D50"
      ]
    },
    {
      "kind": "def",
      "name": "TauArrow.ext_agree",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/ext-agree/",
      "source_line_start": 53,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_arrow",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/id-arrow/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "arrow_comp_stage",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/arrow-comp-stage/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CatTau",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D51"
      ]
    },
    {
      "kind": "def",
      "name": "cat_tau",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-l76/",
      "source_line_start": 76,
      "source_line_end": 76,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_src",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-src/",
      "source_line_start": 79,
      "source_line_end": 79,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_tgt",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-tgt/",
      "source_line_start": 82,
      "source_line_end": 82,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_left_stage",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-left-stage/",
      "source_line_start": 90,
      "source_line_end": 92,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_right_stage",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-right-stage/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_assoc",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-assoc/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_gt_assoc",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-gt-assoc/",
      "source_line_start": 105,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_thin",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-thin/",
      "source_line_start": 117,
      "source_line_end": 121,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.P25"
      ]
    },
    {
      "kind": "theorem",
      "name": "cat_tau_self_agree",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-self-agree/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_holfun_coherent",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/id-holfun-coherent/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_idempotent",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/chi-plus-idempotent/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_idempotent",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/chi-minus-idempotent/",
      "source_line_start": 141,
      "source_line_end": 143,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "at_least_three_holfuns",
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/at-least-three-holfuns/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l159/",
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
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l160/",
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
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l163/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l164/",
      "source_line_start": 164,
      "source_line_end": 164,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l167/",
      "source_line_start": 167,
      "source_line_end": 169,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean",
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
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Topos/EarnedArrows.lean`
- SHA-256: `1e4d4d6a1a915ed1de9777b2a67e454cde0f6523827095ad27c9f070f8851e18`

## Registry Links

- `I.D50` — Tau-Arrow
- `I.D51` — Cat_tau
- `I.P25` — Thin Category
- `I.T22` — Category Axioms

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Holomorphy.DiagonalProtection`
- `TauLib.BookI.Holomorphy.IdentityTheorem`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Topos.Functors`
- `TauLib.BookI.Topos.H6EarnedCategoricalMachine`

## Declaration Counts

- `def`: 4
- `eval`: 5
- `structure`: 2
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauArrow](/corpus/taulib/docs/book-i-topos-earned-arrows/tau-arrow/) | L47-L50 | type/data schema | type/data schema | `I.D50` |
| `def` | [TauArrow.ext_agree](/corpus/taulib/docs/book-i-topos-earned-arrows/ext-agree/) | L53-L55 | definition | definition | — |
| `def` | [id_arrow](/corpus/taulib/docs/book-i-topos-earned-arrows/id-arrow/) | L62-L63 | definition | definition | — |
| `def` | [arrow_comp_stage](/corpus/taulib/docs/book-i-topos-earned-arrows/arrow-comp-stage/) | L66-L67 | definition | definition | — |
| `structure` | [CatTau](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau/) | L71-L73 | type/data schema | type/data schema | `I.D51` |
| `def` | [cat_tau](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-l76/) | L76-L76 | definition | definition | — |
| `theorem` | [cat_tau_id_src](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-src/) | L79-L79 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_id_tgt](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-tgt/) | L82-L82 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_id_left_stage](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-left-stage/) | L90-L92 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_id_right_stage](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-right-stage/) | L95-L97 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_assoc](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-assoc/) | L100-L102 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_gt_assoc](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-gt-assoc/) | L105-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cat_tau_thin](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-thin/) | L117-L121 | proof obligation | formal proof obligation checked | `I.P25` |
| `theorem` | [cat_tau_self_agree](/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-self-agree/) | L124-L125 | proof obligation | formal proof obligation checked | — |
| `theorem` | [id_holfun_coherent](/corpus/taulib/docs/book-i-topos-earned-arrows/id-holfun-coherent/) | L132-L133 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_plus_idempotent](/corpus/taulib/docs/book-i-topos-earned-arrows/chi-plus-idempotent/) | L136-L138 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_minus_idempotent](/corpus/taulib/docs/book-i-topos-earned-arrows/chi-minus-idempotent/) | L141-L143 | proof obligation | formal proof obligation checked | — |
| `theorem` | [at_least_three_holfuns](/corpus/taulib/docs/book-i-topos-earned-arrows/at-least-three-holfuns/) | L151-L152 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L159](/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l159/) | L159-L159 | computed check | computed check | — |
| `eval` | [#eval L160](/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l160/) | L160-L160 | computed check | computed check | — |
| `eval` | [#eval L163](/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l163/) | L163-L163 | computed check | computed check | — |
| `eval` | [#eval L164](/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l164/) | L164-L164 | computed check | computed check | — |
| `eval` | [#eval L167](/corpus/taulib/docs/book-i-topos-earned-arrows/eval-l167/) | L167-L169 | computed check | computed check | — |
