---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Topos.EarnedArrows",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-arrows/",
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
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/tau-arrow/",
      "source_line_start": 47,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": [
        "I.D50"
      ]
    },
    {
      "kind": "def",
      "name": "TauArrow.ext_agree",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/ext-agree/",
      "source_line_start": 53,
      "source_line_end": 55,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_arrow",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/id-arrow/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "arrow_comp_stage",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/arrow-comp-stage/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CatTau",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "I.D51"
      ]
    },
    {
      "kind": "def",
      "name": "cat_tau",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-l76/",
      "source_line_start": 76,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_src",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-src/",
      "source_line_start": 79,
      "source_line_end": 79,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_tgt",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-tgt/",
      "source_line_start": 82,
      "source_line_end": 82,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_left_stage",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-left-stage/",
      "source_line_start": 90,
      "source_line_end": 92,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_id_right_stage",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-right-stage/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_assoc",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-assoc/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_gt_assoc",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-gt-assoc/",
      "source_line_start": 105,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cat_tau_thin",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-thin/",
      "source_line_start": 117,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P25"
      ]
    },
    {
      "kind": "theorem",
      "name": "cat_tau_self_agree",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-self-agree/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_holfun_coherent",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/id-holfun-coherent/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_idempotent",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/chi-plus-idempotent/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_idempotent",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/chi-minus-idempotent/",
      "source_line_start": 141,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "at_least_three_holfuns",
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/at-least-three-holfuns/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/eval-l159/",
      "source_line_start": 159,
      "source_line_end": 159,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/eval-l160/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/eval-l163/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/eval-l164/",
      "source_line_start": 164,
      "source_line_end": 164,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-earned-arrows/eval-l167/",
      "source_line_start": 167,
      "source_line_end": 169,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TauArrow](/verify/taulib/docs/book-i-topos-earned-arrows/tau-arrow/) | L47-L50 | defined | `I.D50` |
| `def` | [TauArrow.ext_agree](/verify/taulib/docs/book-i-topos-earned-arrows/ext-agree/) | L53-L55 | defined | — |
| `def` | [id_arrow](/verify/taulib/docs/book-i-topos-earned-arrows/id-arrow/) | L62-L63 | defined | — |
| `def` | [arrow_comp_stage](/verify/taulib/docs/book-i-topos-earned-arrows/arrow-comp-stage/) | L66-L67 | defined | — |
| `structure` | [CatTau](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau/) | L71-L73 | defined | `I.D51` |
| `def` | [cat_tau](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-l76/) | L76-L76 | defined | — |
| `theorem` | [cat_tau_id_src](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-src/) | L79-L79 | formalized | — |
| `theorem` | [cat_tau_id_tgt](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-tgt/) | L82-L82 | formalized | — |
| `theorem` | [cat_tau_id_left_stage](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-left-stage/) | L90-L92 | formalized | — |
| `theorem` | [cat_tau_id_right_stage](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-right-stage/) | L95-L97 | formalized | — |
| `theorem` | [cat_tau_assoc](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-assoc/) | L100-L102 | formalized | — |
| `theorem` | [cat_tau_gt_assoc](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-gt-assoc/) | L105-L108 | formalized | — |
| `theorem` | [cat_tau_thin](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-thin/) | L117-L121 | formalized | `I.P25` |
| `theorem` | [cat_tau_self_agree](/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-self-agree/) | L124-L125 | formalized | — |
| `theorem` | [id_holfun_coherent](/verify/taulib/docs/book-i-topos-earned-arrows/id-holfun-coherent/) | L132-L133 | formalized | — |
| `theorem` | [chi_plus_idempotent](/verify/taulib/docs/book-i-topos-earned-arrows/chi-plus-idempotent/) | L136-L138 | formalized | — |
| `theorem` | [chi_minus_idempotent](/verify/taulib/docs/book-i-topos-earned-arrows/chi-minus-idempotent/) | L141-L143 | formalized | — |
| `theorem` | [at_least_three_holfuns](/verify/taulib/docs/book-i-topos-earned-arrows/at-least-three-holfuns/) | L151-L152 | formalized | — |
| `eval` | [#eval L159](/verify/taulib/docs/book-i-topos-earned-arrows/eval-l159/) | L159-L159 | computed | — |
| `eval` | [#eval L160](/verify/taulib/docs/book-i-topos-earned-arrows/eval-l160/) | L160-L160 | computed | — |
| `eval` | [#eval L163](/verify/taulib/docs/book-i-topos-earned-arrows/eval-l163/) | L163-L163 | computed | — |
| `eval` | [#eval L164](/verify/taulib/docs/book-i-topos-earned-arrows/eval-l164/) | L164-L164 | computed | — |
| `eval` | [#eval L167](/verify/taulib/docs/book-i-topos-earned-arrows/eval-l167/) | L167-L169 | computed | — |
