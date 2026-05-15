---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
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
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-is-cauchy/",
      "source_line_start": 53,
      "source_line_end": 61,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauReal.one_isCauchy",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-is-cauchy/",
      "source_line_start": 63,
      "source_line_end": 71,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CauchyTauReal",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/cauchy-tau-real/",
      "source_line_start": 81,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "zero",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero/",
      "source_line_start": 90,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "one",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "add",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neg",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg/",
      "source_line_start": 96,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mul",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv/",
      "source_line_start": 103,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-refl/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-symm/",
      "source_line_start": 107,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-trans/",
      "source_line_start": 110,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "setoid",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/setoid/",
      "source_line_start": 115,
      "source_line_end": 131,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CauchyTauReal.toQ",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/to-q/",
      "source_line_start": 133,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.add_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-respects-equiv/",
      "source_line_start": 144,
      "source_line_end": 147,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.mul_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-respects-equiv/",
      "source_line_start": 149,
      "source_line_end": 153,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CauchyTauReal.neg_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-respects-equiv/",
      "source_line_start": 155,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.add",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-l160/",
      "source_line_start": 160,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-l165/",
      "source_line_start": 165,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.neg",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-l170/",
      "source_line_start": 170,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-l174/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRealQ.one",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-l175/",
      "source_line_start": 175,
      "source_line_end": 192,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRealQ.from_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/from-equiv/",
      "source_line_start": 200,
      "source_line_end": 297,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h8_taureal_mathlib_commring_bridge_synthesis",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/h8-taureal-mathlib-commring-bridge-synthesis/",
      "source_line_start": 320,
      "source_line_end": 339,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `theorem` | [TauReal.zero_isCauchy](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-is-cauchy/) | L53-L61 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauReal.one_isCauchy](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-is-cauchy/) | L63-L71 | proof obligation | formal proof obligation checked | — |
| `structure` | [CauchyTauReal](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/cauchy-tau-real/) | L81-L88 | type/data schema | type/data schema | — |
| `def` | [zero](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero/) | L90-L90 | definition | definition | — |
| `def` | [one](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one/) | L91-L91 | definition | definition | — |
| `def` | [add](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add/) | L93-L94 | definition | definition | — |
| `def` | [neg](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg/) | L96-L97 | definition | definition | — |
| `def` | [mul](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul/) | L99-L100 | definition | definition | — |
| `def` | [equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv/) | L103-L103 | definition | definition | — |
| `theorem` | [equiv_refl](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-refl/) | L105-L105 | proof obligation | formal proof obligation checked | — |
| `theorem` | [equiv_symm](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-symm/) | L107-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [equiv_trans](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/equiv-trans/) | L110-L112 | proof obligation | formal proof obligation checked | — |
| `def` | [setoid](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/setoid/) | L115-L131 | definition | definition | — |
| `def` | [CauchyTauReal.toQ](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/to-q/) | L133-L138 | definition | definition | — |
| `theorem` | [CauchyTauReal.add_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-respects-equiv/) | L144-L147 | proof obligation | formal proof obligation checked | — |
| `theorem` | [CauchyTauReal.mul_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-respects-equiv/) | L149-L153 | proof obligation | formal proof obligation checked | — |
| `theorem` | [CauchyTauReal.neg_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-respects-equiv/) | L155-L158 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRealQ.add](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/add-l160/) | L160-L163 | definition | definition | — |
| `def` | [TauRealQ.mul](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-l165/) | L165-L168 | definition | definition | — |
| `def` | [TauRealQ.neg](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/neg-l170/) | L170-L172 | definition | definition | — |
| `def` | [TauRealQ.zero](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-l174/) | L174-L174 | definition | definition | — |
| `def` | [TauRealQ.one](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-l175/) | L175-L192 | definition | definition | — |
| `theorem` | [TauRealQ.from_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/from-equiv/) | L200-L297 | proof obligation | formal proof obligation checked | — |
| `theorem` | [h8_taureal_mathlib_commring_bridge_synthesis](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/h8-taureal-mathlib-commring-bridge-synthesis/) | L320-L339 | proof obligation | formal proof obligation checked | — |
