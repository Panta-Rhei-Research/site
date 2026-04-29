---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Logic.BooleanRecovery",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Logic.BooleanRecovery`.",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_slug": "book-i-logic-boolean-recovery",
  "book": "BookI",
  "family": "Logic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Logic/BooleanRecovery.lean",
  "sha256": "33e453dcf97140930d6eea111ee2ac5db1c0584630abc0864864e1362efa3f53",
  "imports": [
    "TauLib.BookI.Logic.Explosion"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Topos.EarnedTopos"
  ],
  "registry_ids": [
    "I.D41",
    "I.P13"
  ],
  "declaration_counts": {
    "def": 8,
    "theorem": 25,
    "eval": 33
  },
  "declarations": [
    {
      "kind": "def",
      "name": "forget",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget/",
      "source_line_start": 49,
      "source_line_end": 53,
      "formal_status": "defined",
      "registry_ids": [
        "I.P13"
      ]
    },
    {
      "kind": "theorem",
      "name": "forget_preserves_meet",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-meet/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_preserves_join",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-join/",
      "source_line_start": 65,
      "source_line_end": 67,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_conflates_T_B",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-conflates-t-b/",
      "source_line_start": 78,
      "source_line_end": 78,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_conflates_F_N",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-conflates-f-n/",
      "source_line_start": 81,
      "source_line_end": 81,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_not_injective",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-not-injective/",
      "source_line_start": 84,
      "source_line_end": 87,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_preserves_neg",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-neg/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "forget_pessimistic",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic/",
      "source_line_start": 99,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_pessimistic_preserves_meet",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-meet/",
      "source_line_start": 106,
      "source_line_end": 109,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_pessimistic_preserves_join",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-join/",
      "source_line_start": 112,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_pessimistic_preserves_neg",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-neg/",
      "source_line_start": 118,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dual_forget_injective",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/dual-forget-injective/",
      "source_line_start": 124,
      "source_line_end": 127,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dual_forget_is_toBoolPair",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/dual-forget-is-to-bool-pair/",
      "source_line_start": 130,
      "source_line_end": 132,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "boolean_recovery",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/boolean-recovery/",
      "source_line_start": 143,
      "source_line_end": 145,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P13"
      ]
    },
    {
      "kind": "theorem",
      "name": "forget_fiber_T_B",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber-t-b/",
      "source_line_start": 148,
      "source_line_end": 148,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_fiber_F_N",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber-f-n/",
      "source_line_start": 150,
      "source_line_end": 150,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_never_injective",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-never-injective/",
      "source_line_start": 153,
      "source_line_end": 159,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forget_fiber",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber/",
      "source_line_start": 163,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D41"
      ]
    },
    {
      "kind": "def",
      "name": "omega_true",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/omega-true/",
      "source_line_start": 179,
      "source_line_end": 179,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_false",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/omega-false/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_both",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/omega-both/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_neither",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/omega-neither/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.heyting_impl",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-impl/",
      "source_line_start": 204,
      "source_line_end": 214,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "heyting_eq_material",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-eq-material/",
      "source_line_start": 219,
      "source_line_end": 221,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "heyting_adjunction",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-adjunction/",
      "source_line_start": 225,
      "source_line_end": 227,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "heyting_maximality",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-maximality/",
      "source_line_start": 230,
      "source_line_end": 234,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.heyting_neg",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-neg/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "heyting_neg_eq_neg",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-neg-eq-neg/",
      "source_line_start": 240,
      "source_line_end": 242,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "excluded_middle",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/excluded-middle/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "double_negation",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/double-negation/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "non_contradiction",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/non-contradiction/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth4_is_boolean",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/truth4-is-boolean/",
      "source_line_start": 270,
      "source_line_end": 280,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "explosion_is_semantic",
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/explosion-is-semantic/",
      "source_line_start": 291,
      "source_line_end": 297,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l304/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l337/",
      "source_line_start": 337,
      "source_line_end": 337,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 356,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Logic/BooleanRecovery.lean`
- SHA-256: `33e453dcf97140930d6eea111ee2ac5db1c0584630abc0864864e1362efa3f53`

## Registry Links

- `I.D41` — Subobject Classifier Preview
- `I.P13` — Boolean Recovery

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Logic.Explosion`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Topos.EarnedTopos`

## Declaration Counts

- `def`: 8
- `eval`: 33
- `theorem`: 25

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [forget](/verify/taulib/docs/book-i-logic-boolean-recovery/forget/) | L49-L53 | defined | `I.P13` |
| `theorem` | [forget_preserves_meet](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-meet/) | L60-L62 | formalized | — |
| `theorem` | [forget_preserves_join](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-join/) | L65-L67 | formalized | — |
| `theorem` | [forget_conflates_T_B](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-conflates-t-b/) | L78-L78 | formalized | — |
| `theorem` | [forget_conflates_F_N](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-conflates-f-n/) | L81-L81 | formalized | — |
| `theorem` | [forget_not_injective](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-not-injective/) | L84-L87 | formalized | — |
| `theorem` | [forget_preserves_neg](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-preserves-neg/) | L90-L91 | formalized | — |
| `def` | [forget_pessimistic](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic/) | L99-L103 | defined | — |
| `theorem` | [forget_pessimistic_preserves_meet](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-meet/) | L106-L109 | formalized | — |
| `theorem` | [forget_pessimistic_preserves_join](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-join/) | L112-L115 | formalized | — |
| `theorem` | [forget_pessimistic_preserves_neg](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-pessimistic-preserves-neg/) | L118-L120 | formalized | — |
| `theorem` | [dual_forget_injective](/verify/taulib/docs/book-i-logic-boolean-recovery/dual-forget-injective/) | L124-L127 | formalized | — |
| `theorem` | [dual_forget_is_toBoolPair](/verify/taulib/docs/book-i-logic-boolean-recovery/dual-forget-is-to-bool-pair/) | L130-L132 | formalized | — |
| `theorem` | [boolean_recovery](/verify/taulib/docs/book-i-logic-boolean-recovery/boolean-recovery/) | L143-L145 | formalized | `I.P13` |
| `theorem` | [forget_fiber_T_B](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber-t-b/) | L148-L148 | formalized | — |
| `theorem` | [forget_fiber_F_N](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber-f-n/) | L150-L150 | formalized | — |
| `theorem` | [forget_never_injective](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-never-injective/) | L153-L159 | formalized | — |
| `theorem` | [forget_fiber](/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber/) | L163-L176 | formalized | `I.D41` |
| `def` | [omega_true](/verify/taulib/docs/book-i-logic-boolean-recovery/omega-true/) | L179-L179 | defined | — |
| `def` | [omega_false](/verify/taulib/docs/book-i-logic-boolean-recovery/omega-false/) | L182-L182 | defined | — |
| `def` | [omega_both](/verify/taulib/docs/book-i-logic-boolean-recovery/omega-both/) | L185-L185 | defined | — |
| `def` | [omega_neither](/verify/taulib/docs/book-i-logic-boolean-recovery/omega-neither/) | L188-L188 | defined | — |
| `def` | [Truth4.heyting_impl](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-impl/) | L204-L214 | defined | — |
| `theorem` | [heyting_eq_material](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-eq-material/) | L219-L221 | formalized | — |
| `theorem` | [heyting_adjunction](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-adjunction/) | L225-L227 | formalized | — |
| `theorem` | [heyting_maximality](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-maximality/) | L230-L234 | formalized | — |
| `def` | [Truth4.heyting_neg](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-neg/) | L237-L237 | defined | — |
| `theorem` | [heyting_neg_eq_neg](/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-neg-eq-neg/) | L240-L242 | formalized | — |
| `theorem` | [excluded_middle](/verify/taulib/docs/book-i-logic-boolean-recovery/excluded-middle/) | L250-L251 | formalized | — |
| `theorem` | [double_negation](/verify/taulib/docs/book-i-logic-boolean-recovery/double-negation/) | L254-L255 | formalized | — |
| `theorem` | [non_contradiction](/verify/taulib/docs/book-i-logic-boolean-recovery/non-contradiction/) | L258-L259 | formalized | — |
| `theorem` | [truth4_is_boolean](/verify/taulib/docs/book-i-logic-boolean-recovery/truth4-is-boolean/) | L270-L280 | formalized | — |
| `theorem` | [explosion_is_semantic](/verify/taulib/docs/book-i-logic-boolean-recovery/explosion-is-semantic/) | L291-L297 | formalized | — |
| `eval` | [#eval L304](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l304/) | L304-L304 | computed | — |
| `eval` | [#eval L305](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l305/) | L305-L305 | computed | — |
| `eval` | [#eval L306](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l306/) | L306-L306 | computed | — |
| `eval` | [#eval L307](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l307/) | L307-L307 | computed | — |
| `eval` | [#eval L310](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l310/) | L310-L310 | computed | — |
| `eval` | [#eval L311](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l311/) | L311-L311 | computed | — |
| `eval` | [#eval L314](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l314/) | L314-L314 | computed | — |
| `eval` | [#eval L315](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l315/) | L315-L315 | computed | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L320](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l320/) | L320-L320 | computed | — |
| `eval` | [#eval L321](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l321/) | L321-L321 | computed | — |
| `eval` | [#eval L322](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l322/) | L322-L322 | computed | — |
| `eval` | [#eval L325](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l325/) | L325-L325 | computed | — |
| `eval` | [#eval L326](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l326/) | L326-L326 | computed | — |
| `eval` | [#eval L327](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l327/) | L327-L327 | computed | — |
| `eval` | [#eval L328](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l328/) | L328-L328 | computed | — |
| `eval` | [#eval L331](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l331/) | L331-L331 | computed | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L337](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l337/) | L337-L337 | computed | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l343/) | L343-L343 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-i-logic-boolean-recovery/eval-l354/) | L354-L356 | computed | — |
