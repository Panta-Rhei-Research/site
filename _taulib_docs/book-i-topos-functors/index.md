---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Topos.Functors",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Topos.Functors`.",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_slug": "book-i-topos-functors",
  "book": "BookI",
  "family": "Topos",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Topos/Functors.lean",
  "sha256": "387c08b1253814846e6cd7df410024059afd08aecb72f33a2f28f5220c7a9507",
  "imports": [
    "TauLib.BookI.Topos.EarnedArrows",
    "TauLib.BookI.Polarity.ModArith"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Topos.LimitsSites"
  ],
  "registry_ids": [
    "I.D52",
    "I.D53",
    "I.D54",
    "I.T23"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 9,
    "theorem": 8,
    "example": 1,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauFunctor",
      "url": "/verify/taulib/docs/book-i-topos-functors/tau-functor/",
      "source_line_start": 45,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": [
        "I.D52"
      ]
    },
    {
      "kind": "def",
      "name": "TauFunctor.id",
      "url": "/verify/taulib/docs/book-i-topos-functors/id/",
      "source_line_start": 50,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauFunctor.comp",
      "url": "/verify/taulib/docs/book-i-topos-functors/comp/",
      "source_line_start": 53,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "functor_comp_assoc",
      "url": "/verify/taulib/docs/book-i-topos-functors/functor-comp-assoc/",
      "source_line_start": 57,
      "source_line_end": 58,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "functor_id_comp",
      "url": "/verify/taulib/docs/book-i-topos-functors/functor-id-comp/",
      "source_line_start": 61,
      "source_line_end": 63,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "functor_comp_id",
      "url": "/verify/taulib/docs/book-i-topos-functors/functor-comp-id/",
      "source_line_start": 66,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NatTrans",
      "url": "/verify/taulib/docs/book-i-topos-functors/nat-trans/",
      "source_line_start": 78,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": [
        "I.D53"
      ]
    },
    {
      "kind": "def",
      "name": "NatTrans.id",
      "url": "/verify/taulib/docs/book-i-topos-functors/id-l87/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "naturality_automatic",
      "url": "/verify/taulib/docs/book-i-topos-functors/naturality-automatic/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "forgetful_functor",
      "url": "/verify/taulib/docs/book-i-topos-functors/forgetful-functor/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "hom_predicate",
      "url": "/verify/taulib/docs/book-i-topos-functors/hom-predicate/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Presheaf",
      "url": "/verify/taulib/docs/book-i-topos-functors/presheaf/",
      "source_line_start": 117,
      "source_line_end": 119,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "yoneda",
      "url": "/verify/taulib/docs/book-i-topos-functors/yoneda/",
      "source_line_start": 123,
      "source_line_end": 124,
      "formal_status": "defined",
      "registry_ids": [
        "I.D54"
      ]
    },
    {
      "kind": "theorem",
      "name": "yoneda_constant",
      "url": "/verify/taulib/docs/book-i-topos-functors/yoneda-constant/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "yoneda_thin",
      "url": "/verify/taulib/docs/book-i-topos-functors/yoneda-thin/",
      "source_line_start": 146,
      "source_line_end": 148,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T23"
      ]
    },
    {
      "kind": "theorem",
      "name": "yoneda_faithful",
      "url": "/verify/taulib/docs/book-i-topos-functors/yoneda-faithful/",
      "source_line_start": 152,
      "source_line_end": 154,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Presheaf.representable",
      "url": "/verify/taulib/docs/book-i-topos-functors/representable/",
      "source_line_start": 161,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "representable_subterminal",
      "url": "/verify/taulib/docs/book-i-topos-functors/representable-subterminal/",
      "source_line_start": 166,
      "source_line_end": 170,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "double_functor",
      "url": "/verify/taulib/docs/book-i-topos-functors/double-functor/",
      "source_line_start": 177,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "succ_functor",
      "url": "/verify/taulib/docs/book-i-topos-functors/succ-functor/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-functors/example-l183/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-functors/eval-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-functors/eval-l191/",
      "source_line_start": 191,
      "source_line_end": 191,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-functors/eval-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-topos-functors/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 199,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean",
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
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Topos/Functors.lean`
- SHA-256: `387c08b1253814846e6cd7df410024059afd08aecb72f33a2f28f5220c7a9507`

## Registry Links

- `I.D52` — Tau-Functor
- `I.D53` — Natural Transformation
- `I.D54` — Yoneda Embedding
- `I.T23` — Yoneda Lemma

## Construction Spine Links

- [Internalize Self-Enrichment](/corpus/construction-spine/internalize-self-enrichment/)

## Imports

- `TauLib.BookI.Topos.EarnedArrows`
- `TauLib.BookI.Polarity.ModArith`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Topos.LimitsSites`

## Declaration Counts

- `def`: 9
- `eval`: 4
- `example`: 1
- `structure`: 3
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TauFunctor](/verify/taulib/docs/book-i-topos-functors/tau-functor/) | L45-L47 | defined | `I.D52` |
| `def` | [TauFunctor.id](/verify/taulib/docs/book-i-topos-functors/id/) | L50-L50 | defined | — |
| `def` | [TauFunctor.comp](/verify/taulib/docs/book-i-topos-functors/comp/) | L53-L54 | defined | — |
| `theorem` | [functor_comp_assoc](/verify/taulib/docs/book-i-topos-functors/functor-comp-assoc/) | L57-L58 | formalized | — |
| `theorem` | [functor_id_comp](/verify/taulib/docs/book-i-topos-functors/functor-id-comp/) | L61-L63 | formalized | — |
| `theorem` | [functor_comp_id](/verify/taulib/docs/book-i-topos-functors/functor-comp-id/) | L66-L68 | formalized | — |
| `structure` | [NatTrans](/verify/taulib/docs/book-i-topos-functors/nat-trans/) | L78-L84 | defined | `I.D53` |
| `def` | [NatTrans.id](/verify/taulib/docs/book-i-topos-functors/id-l87/) | L87-L88 | defined | — |
| `theorem` | [naturality_automatic](/verify/taulib/docs/book-i-topos-functors/naturality-automatic/) | L92-L93 | formalized | — |
| `def` | [forgetful_functor](/verify/taulib/docs/book-i-topos-functors/forgetful-functor/) | L101-L101 | defined | — |
| `def` | [hom_predicate](/verify/taulib/docs/book-i-topos-functors/hom-predicate/) | L106-L107 | defined | — |
| `structure` | [Presheaf](/verify/taulib/docs/book-i-topos-functors/presheaf/) | L117-L119 | defined | — |
| `def` | [yoneda](/verify/taulib/docs/book-i-topos-functors/yoneda/) | L123-L124 | defined | `I.D54` |
| `theorem` | [yoneda_constant](/verify/taulib/docs/book-i-topos-functors/yoneda-constant/) | L128-L129 | formalized | — |
| `theorem` | [yoneda_thin](/verify/taulib/docs/book-i-topos-functors/yoneda-thin/) | L146-L148 | formalized | `I.T23` |
| `theorem` | [yoneda_faithful](/verify/taulib/docs/book-i-topos-functors/yoneda-faithful/) | L152-L154 | formalized | — |
| `def` | [Presheaf.representable](/verify/taulib/docs/book-i-topos-functors/representable/) | L161-L162 | defined | — |
| `theorem` | [representable_subterminal](/verify/taulib/docs/book-i-topos-functors/representable-subterminal/) | L166-L170 | formalized | — |
| `def` | [double_functor](/verify/taulib/docs/book-i-topos-functors/double-functor/) | L177-L177 | defined | — |
| `def` | [succ_functor](/verify/taulib/docs/book-i-topos-functors/succ-functor/) | L180-L180 | defined | — |
| `example` | [#eval L183](/verify/taulib/docs/book-i-topos-functors/example-l183/) | L183-L183 | example | — |
| `eval` | [#eval L190](/verify/taulib/docs/book-i-topos-functors/eval-l190/) | L190-L190 | computed | — |
| `eval` | [#eval L191](/verify/taulib/docs/book-i-topos-functors/eval-l191/) | L191-L191 | computed | — |
| `eval` | [#eval L194](/verify/taulib/docs/book-i-topos-functors/eval-l194/) | L194-L194 | computed | — |
| `eval` | [#eval L197](/verify/taulib/docs/book-i-topos-functors/eval-l197/) | L197-L199 | computed | — |
