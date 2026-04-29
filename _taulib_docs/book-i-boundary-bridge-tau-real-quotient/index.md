---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_slug": "book-i-boundary-bridge-tau-real-quotient",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean",
  "sha256": "0a9df9f1170926704a2a7db25d32385d79a6ab8119418251e0a9c08e063d3072",
  "imports": [
    "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
    "Mathlib.Algebra.Ring.Defs",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.Linarith"
  ],
  "imported_by": [],
  "registry_ids": [
    "I.D146",
    "I.T223",
    "I.T224"
  ],
  "declaration_counts": {
    "theorem": 10,
    "structure": 1,
    "def": 13
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "TauReal.zero_isCauchy",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-is-cauchy/",
      "source_line_start": 53,
      "source_line_end": 61,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.one_isCauchy",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-is-cauchy/",
      "source_line_start": 63,
      "source_line_end": 71,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CauchyTauReal",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/cauchy-tau-real/",
      "source_line_start": 81,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "zero",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero/",
      "source_line_start": 90,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "one",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "add",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neg",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg/",
      "source_line_start": 96,
      "source_line_end": 97,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mul",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv/",
      "source_line_start": 103,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_refl",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-refl/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_symm",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-symm/",
      "source_line_start": 107,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_trans",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-trans/",
      "source_line_start": 110,
      "source_line_end": 112,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "setoid",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/setoid/",
      "source_line_start": 115,
      "source_line_end": 131,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CauchyTauReal.toQ",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/to-q/",
      "source_line_start": 133,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.add_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-respects-equiv/",
      "source_line_start": 144,
      "source_line_end": 147,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.mul_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-respects-equiv/",
      "source_line_start": 149,
      "source_line_end": 153,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.neg_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-respects-equiv/",
      "source_line_start": 155,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.add",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-l160/",
      "source_line_start": 160,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.mul",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-l165/",
      "source_line_start": 165,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.neg",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-l170/",
      "source_line_start": 170,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.zero",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-l174/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.one",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-l175/",
      "source_line_start": 175,
      "source_line_end": 192,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRealQ.from_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/from-equiv/",
      "source_line_start": 200,
      "source_line_end": 297,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h8_taureal_mathlib_commring_bridge_synthesis",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/h8-taureal-mathlib-commring-bridge-synthesis/",
      "source_line_start": 320,
      "source_line_end": 339,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`
- SHA-256: `0a9df9f1170926704a2a7db25d32385d79a6ab8119418251e0a9c08e063d3072`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Bridge.TauRealCongruence`
- `Mathlib.Algebra.Ring.Defs`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.Linarith`

## Imported By

- No TauLib module in the snapshot imports this module.

## Declaration Counts

- `def`: 13
- `structure`: 1
- `theorem`: 10

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [TauReal.zero_isCauchy](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-is-cauchy/) | L53-L61 | formalized | — |
| `theorem` | [TauReal.one_isCauchy](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-is-cauchy/) | L63-L71 | formalized | — |
| `structure` | [CauchyTauReal](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/cauchy-tau-real/) | L81-L88 | defined | — |
| `def` | [zero](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero/) | L90-L90 | defined | — |
| `def` | [one](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one/) | L91-L91 | defined | — |
| `def` | [add](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add/) | L93-L94 | defined | — |
| `def` | [neg](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg/) | L96-L97 | defined | — |
| `def` | [mul](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul/) | L99-L100 | defined | — |
| `def` | [equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv/) | L103-L103 | defined | — |
| `theorem` | [equiv_refl](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-refl/) | L105-L105 | formalized | — |
| `theorem` | [equiv_symm](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-symm/) | L107-L108 | formalized | — |
| `theorem` | [equiv_trans](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-trans/) | L110-L112 | formalized | — |
| `def` | [setoid](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/setoid/) | L115-L131 | defined | — |
| `def` | [CauchyTauReal.toQ](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/to-q/) | L133-L138 | defined | — |
| `theorem` | [CauchyTauReal.add_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-respects-equiv/) | L144-L147 | formalized | — |
| `theorem` | [CauchyTauReal.mul_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-respects-equiv/) | L149-L153 | formalized | — |
| `theorem` | [CauchyTauReal.neg_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-respects-equiv/) | L155-L158 | formalized | — |
| `def` | [TauRealQ.add](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-l160/) | L160-L163 | defined | — |
| `def` | [TauRealQ.mul](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-l165/) | L165-L168 | defined | — |
| `def` | [TauRealQ.neg](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-l170/) | L170-L172 | defined | — |
| `def` | [TauRealQ.zero](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-l174/) | L174-L174 | defined | — |
| `def` | [TauRealQ.one](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-l175/) | L175-L192 | defined | — |
| `theorem` | [TauRealQ.from_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/from-equiv/) | L200-L297 | formalized | — |
| `theorem` | [h8_taureal_mathlib_commring_bridge_synthesis](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/h8-taureal-mathlib-commring-bridge-synthesis/) | L320-L339 | formalized | — |
