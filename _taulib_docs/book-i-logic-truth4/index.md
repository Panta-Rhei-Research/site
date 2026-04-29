---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Logic.Truth4",
  "permalink": "/verify/taulib/docs/book-i-logic-truth4/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Logic.Truth4`.",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_slug": "book-i-logic-truth4",
  "book": "BookI",
  "family": "Logic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Logic/Truth4.lean",
  "sha256": "168260b726d78a310c50c93dcd17383c6204afbccb15d16a7ce9858a4d405ff6",
  "imports": [
    "TauLib.BookI.Polarity.BipolarAlgebra"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Logic.Explosion",
    "TauLib.BookI.MetaLogic.LinearDiscipline",
    "TauLib.BookI.Polarity.H4BoundaryAlgebra",
    "TauLib.Tour.GuidedTour.BookI"
  ],
  "registry_ids": [
    "I.D21"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 8,
    "theorem": 34,
    "eval": 32
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "Truth4",
      "url": "/verify/taulib/docs/book-i-logic-truth4/truth4/",
      "source_line_start": 41,
      "source_line_end": 48,
      "formal_status": "defined",
      "registry_ids": [
        "I.D21"
      ]
    },
    {
      "kind": "def",
      "name": "Truth4.le",
      "url": "/verify/taulib/docs/book-i-logic-truth4/le/",
      "source_line_start": 56,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.meet",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet/",
      "source_line_start": 68,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.join",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join/",
      "source_line_start": 83,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.neg",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg/",
      "source_line_start": 99,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.impl",
      "url": "/verify/taulib/docs/book-i-logic-truth4/impl/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.toBoolPair",
      "url": "/verify/taulib/docs/book-i-logic-truth4/to-bool-pair/",
      "source_line_start": 118,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.fromBoolPair",
      "url": "/verify/taulib/docs/book-i-logic-truth4/from-bool-pair/",
      "source_line_start": 125,
      "source_line_end": 129,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_comm",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-comm/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_comm",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-comm/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_assoc",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-assoc/",
      "source_line_start": 144,
      "source_line_end": 146,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_assoc",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-assoc/",
      "source_line_start": 149,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_idem",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-idem/",
      "source_line_start": 154,
      "source_line_end": 155,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_idem",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-idem/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.absorption_meet_join",
      "url": "/verify/taulib/docs/book-i-logic-truth4/absorption-meet-join/",
      "source_line_start": 162,
      "source_line_end": 164,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.absorption_join_meet",
      "url": "/verify/taulib/docs/book-i-logic-truth4/absorption-join-meet/",
      "source_line_start": 167,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_distrib_join",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-distrib-join/",
      "source_line_start": 172,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_distrib_meet",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-distrib-meet/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_F",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-f/",
      "source_line_start": 182,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_T",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-t/",
      "source_line_start": 186,
      "source_line_end": 187,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.meet_T",
      "url": "/verify/taulib/docs/book-i-logic-truth4/meet-t/",
      "source_line_start": 190,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.join_F",
      "url": "/verify/taulib/docs/book-i-logic-truth4/join-f/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.neg_involutive",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg-involutive/",
      "source_line_start": 202,
      "source_line_end": 203,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.neg_T",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg-t/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.neg_F",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg-f/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.neg_B",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg-b/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.neg_N",
      "url": "/verify/taulib/docs/book-i-logic-truth4/neg-n/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.complement_meet",
      "url": "/verify/taulib/docs/book-i-logic-truth4/complement-meet/",
      "source_line_start": 222,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.complement_join",
      "url": "/verify/taulib/docs/book-i-logic-truth4/complement-join/",
      "source_line_start": 226,
      "source_line_end": 227,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.de_morgan_meet",
      "url": "/verify/taulib/docs/book-i-logic-truth4/de-morgan-meet/",
      "source_line_start": 234,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.de_morgan_join",
      "url": "/verify/taulib/docs/book-i-logic-truth4/de-morgan-join/",
      "source_line_start": 239,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.toBoolPair_injective",
      "url": "/verify/taulib/docs/book-i-logic-truth4/to-bool-pair-injective/",
      "source_line_start": 248,
      "source_line_end": 250,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.fromBoolPair_roundtrip",
      "url": "/verify/taulib/docs/book-i-logic-truth4/from-bool-pair-roundtrip/",
      "source_line_start": 253,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.toBoolPair_roundtrip",
      "url": "/verify/taulib/docs/book-i-logic-truth4/to-bool-pair-roundtrip/",
      "source_line_start": 258,
      "source_line_end": 261,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Truth4.toSectorPair",
      "url": "/verify/taulib/docs/book-i-logic-truth4/to-sector-pair/",
      "source_line_start": 269,
      "source_line_end": 273,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.B_is_e_plus",
      "url": "/verify/taulib/docs/book-i-logic-truth4/b-is-e-plus/",
      "source_line_start": 276,
      "source_line_end": 277,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.N_is_e_minus",
      "url": "/verify/taulib/docs/book-i-logic-truth4/n-is-e-minus/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.B_meet_N_spectral",
      "url": "/verify/taulib/docs/book-i-logic-truth4/b-meet-n-spectral/",
      "source_line_start": 284,
      "source_line_end": 285,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.le_refl",
      "url": "/verify/taulib/docs/book-i-logic-truth4/le-refl/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.le_F",
      "url": "/verify/taulib/docs/book-i-logic-truth4/le-f/",
      "source_line_start": 296,
      "source_line_end": 297,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.le_T",
      "url": "/verify/taulib/docs/book-i-logic-truth4/le-t/",
      "source_line_start": 300,
      "source_line_end": 301,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.B_not_le_N",
      "url": "/verify/taulib/docs/book-i-logic-truth4/b-not-le-n/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Truth4.N_not_le_B",
      "url": "/verify/taulib/docs/book-i-logic-truth4/n-not-le-b/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 329,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l338/",
      "source_line_start": 338,
      "source_line_end": 338,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 358,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-logic-truth4/eval-l359/",
      "source_line_start": 359,
      "source_line_end": 361,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean",
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
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Logic/Truth4.lean`
- SHA-256: `168260b726d78a310c50c93dcd17383c6204afbccb15d16a7ce9858a4d405ff6`

## Registry Links

- `I.D21` — Truth4 Logic

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.BipolarAlgebra`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Logic.Explosion`
- `TauLib.BookI.MetaLogic.LinearDiscipline`
- `TauLib.BookI.Polarity.H4BoundaryAlgebra`
- `TauLib.Tour.GuidedTour.BookI`

## Declaration Counts

- `def`: 8
- `eval`: 32
- `inductive`: 1
- `theorem`: 34

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [Truth4](/verify/taulib/docs/book-i-logic-truth4/truth4/) | L41-L48 | defined | `I.D21` |
| `def` | [Truth4.le](/verify/taulib/docs/book-i-logic-truth4/le/) | L56-L61 | defined | — |
| `def` | [Truth4.meet](/verify/taulib/docs/book-i-logic-truth4/meet/) | L68-L76 | defined | — |
| `def` | [Truth4.join](/verify/taulib/docs/book-i-logic-truth4/join/) | L83-L91 | defined | — |
| `def` | [Truth4.neg](/verify/taulib/docs/book-i-logic-truth4/neg/) | L99-L103 | defined | — |
| `def` | [Truth4.impl](/verify/taulib/docs/book-i-logic-truth4/impl/) | L111-L111 | defined | — |
| `def` | [Truth4.toBoolPair](/verify/taulib/docs/book-i-logic-truth4/to-bool-pair/) | L118-L122 | defined | — |
| `def` | [Truth4.fromBoolPair](/verify/taulib/docs/book-i-logic-truth4/from-bool-pair/) | L125-L129 | defined | — |
| `theorem` | [Truth4.meet_comm](/verify/taulib/docs/book-i-logic-truth4/meet-comm/) | L136-L137 | formalized | — |
| `theorem` | [Truth4.join_comm](/verify/taulib/docs/book-i-logic-truth4/join-comm/) | L140-L141 | formalized | — |
| `theorem` | [Truth4.meet_assoc](/verify/taulib/docs/book-i-logic-truth4/meet-assoc/) | L144-L146 | formalized | — |
| `theorem` | [Truth4.join_assoc](/verify/taulib/docs/book-i-logic-truth4/join-assoc/) | L149-L151 | formalized | — |
| `theorem` | [Truth4.meet_idem](/verify/taulib/docs/book-i-logic-truth4/meet-idem/) | L154-L155 | formalized | — |
| `theorem` | [Truth4.join_idem](/verify/taulib/docs/book-i-logic-truth4/join-idem/) | L158-L159 | formalized | — |
| `theorem` | [Truth4.absorption_meet_join](/verify/taulib/docs/book-i-logic-truth4/absorption-meet-join/) | L162-L164 | formalized | — |
| `theorem` | [Truth4.absorption_join_meet](/verify/taulib/docs/book-i-logic-truth4/absorption-join-meet/) | L167-L169 | formalized | — |
| `theorem` | [Truth4.meet_distrib_join](/verify/taulib/docs/book-i-logic-truth4/meet-distrib-join/) | L172-L174 | formalized | — |
| `theorem` | [Truth4.join_distrib_meet](/verify/taulib/docs/book-i-logic-truth4/join-distrib-meet/) | L177-L179 | formalized | — |
| `theorem` | [Truth4.meet_F](/verify/taulib/docs/book-i-logic-truth4/meet-f/) | L182-L183 | formalized | — |
| `theorem` | [Truth4.join_T](/verify/taulib/docs/book-i-logic-truth4/join-t/) | L186-L187 | formalized | — |
| `theorem` | [Truth4.meet_T](/verify/taulib/docs/book-i-logic-truth4/meet-t/) | L190-L191 | formalized | — |
| `theorem` | [Truth4.join_F](/verify/taulib/docs/book-i-logic-truth4/join-f/) | L194-L195 | formalized | — |
| `theorem` | [Truth4.neg_involutive](/verify/taulib/docs/book-i-logic-truth4/neg-involutive/) | L202-L203 | formalized | — |
| `theorem` | [Truth4.neg_T](/verify/taulib/docs/book-i-logic-truth4/neg-t/) | L206-L206 | formalized | — |
| `theorem` | [Truth4.neg_F](/verify/taulib/docs/book-i-logic-truth4/neg-f/) | L209-L209 | formalized | — |
| `theorem` | [Truth4.neg_B](/verify/taulib/docs/book-i-logic-truth4/neg-b/) | L212-L212 | formalized | — |
| `theorem` | [Truth4.neg_N](/verify/taulib/docs/book-i-logic-truth4/neg-n/) | L215-L215 | formalized | — |
| `theorem` | [Truth4.complement_meet](/verify/taulib/docs/book-i-logic-truth4/complement-meet/) | L222-L223 | formalized | — |
| `theorem` | [Truth4.complement_join](/verify/taulib/docs/book-i-logic-truth4/complement-join/) | L226-L227 | formalized | — |
| `theorem` | [Truth4.de_morgan_meet](/verify/taulib/docs/book-i-logic-truth4/de-morgan-meet/) | L234-L236 | formalized | — |
| `theorem` | [Truth4.de_morgan_join](/verify/taulib/docs/book-i-logic-truth4/de-morgan-join/) | L239-L241 | formalized | — |
| `theorem` | [Truth4.toBoolPair_injective](/verify/taulib/docs/book-i-logic-truth4/to-bool-pair-injective/) | L248-L250 | formalized | — |
| `theorem` | [Truth4.fromBoolPair_roundtrip](/verify/taulib/docs/book-i-logic-truth4/from-bool-pair-roundtrip/) | L253-L255 | formalized | — |
| `theorem` | [Truth4.toBoolPair_roundtrip](/verify/taulib/docs/book-i-logic-truth4/to-bool-pair-roundtrip/) | L258-L261 | formalized | — |
| `def` | [Truth4.toSectorPair](/verify/taulib/docs/book-i-logic-truth4/to-sector-pair/) | L269-L273 | defined | — |
| `theorem` | [Truth4.B_is_e_plus](/verify/taulib/docs/book-i-logic-truth4/b-is-e-plus/) | L276-L277 | formalized | — |
| `theorem` | [Truth4.N_is_e_minus](/verify/taulib/docs/book-i-logic-truth4/n-is-e-minus/) | L280-L281 | formalized | — |
| `theorem` | [Truth4.B_meet_N_spectral](/verify/taulib/docs/book-i-logic-truth4/b-meet-n-spectral/) | L284-L285 | formalized | — |
| `theorem` | [Truth4.le_refl](/verify/taulib/docs/book-i-logic-truth4/le-refl/) | L292-L293 | formalized | — |
| `theorem` | [Truth4.le_F](/verify/taulib/docs/book-i-logic-truth4/le-f/) | L296-L297 | formalized | — |
| `theorem` | [Truth4.le_T](/verify/taulib/docs/book-i-logic-truth4/le-t/) | L300-L301 | formalized | — |
| `theorem` | [Truth4.B_not_le_N](/verify/taulib/docs/book-i-logic-truth4/b-not-le-n/) | L304-L304 | formalized | — |
| `theorem` | [Truth4.N_not_le_B](/verify/taulib/docs/book-i-logic-truth4/n-not-le-b/) | L307-L307 | formalized | — |
| `eval` | [#eval L314](/verify/taulib/docs/book-i-logic-truth4/eval-l314/) | L314-L314 | computed | — |
| `eval` | [#eval L315](/verify/taulib/docs/book-i-logic-truth4/eval-l315/) | L315-L315 | computed | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-i-logic-truth4/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-i-logic-truth4/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L320](/verify/taulib/docs/book-i-logic-truth4/eval-l320/) | L320-L320 | computed | — |
| `eval` | [#eval L321](/verify/taulib/docs/book-i-logic-truth4/eval-l321/) | L321-L321 | computed | — |
| `eval` | [#eval L322](/verify/taulib/docs/book-i-logic-truth4/eval-l322/) | L322-L322 | computed | — |
| `eval` | [#eval L323](/verify/taulib/docs/book-i-logic-truth4/eval-l323/) | L323-L323 | computed | — |
| `eval` | [#eval L326](/verify/taulib/docs/book-i-logic-truth4/eval-l326/) | L326-L326 | computed | — |
| `eval` | [#eval L327](/verify/taulib/docs/book-i-logic-truth4/eval-l327/) | L327-L327 | computed | — |
| `eval` | [#eval L328](/verify/taulib/docs/book-i-logic-truth4/eval-l328/) | L328-L328 | computed | — |
| `eval` | [#eval L329](/verify/taulib/docs/book-i-logic-truth4/eval-l329/) | L329-L329 | computed | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-i-logic-truth4/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L333](/verify/taulib/docs/book-i-logic-truth4/eval-l333/) | L333-L333 | computed | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-i-logic-truth4/eval-l334/) | L334-L334 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-i-logic-truth4/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L338](/verify/taulib/docs/book-i-logic-truth4/eval-l338/) | L338-L338 | computed | — |
| `eval` | [#eval L339](/verify/taulib/docs/book-i-logic-truth4/eval-l339/) | L339-L339 | computed | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-logic-truth4/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-i-logic-truth4/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L344](/verify/taulib/docs/book-i-logic-truth4/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-i-logic-truth4/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-i-logic-truth4/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-i-logic-truth4/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L350](/verify/taulib/docs/book-i-logic-truth4/eval-l350/) | L350-L350 | computed | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-i-logic-truth4/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-i-logic-truth4/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-i-logic-truth4/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L356](/verify/taulib/docs/book-i-logic-truth4/eval-l356/) | L356-L356 | computed | — |
| `eval` | [#eval L357](/verify/taulib/docs/book-i-logic-truth4/eval-l357/) | L357-L357 | computed | — |
| `eval` | [#eval L358](/verify/taulib/docs/book-i-logic-truth4/eval-l358/) | L358-L358 | computed | — |
| `eval` | [#eval L359](/verify/taulib/docs/book-i-logic-truth4/eval-l359/) | L359-L361 | computed | — |
