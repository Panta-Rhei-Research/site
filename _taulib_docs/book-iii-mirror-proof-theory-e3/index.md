---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "permalink": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_slug": "book-iii-mirror-proof-theory-e3",
  "book": "BookIII",
  "family": "Mirror",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Mirror/ProofTheoryE3.lean",
  "sha256": "cf708c4504d1737221ab4881088e58c6d866a9a72c7be244088c7f6d39d4d4ab",
  "imports": [
    "TauLib.BookIII.Bridge.BridgeAxiom"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Mirror.Saturation"
  ],
  "registry_ids": [
    "III.D73",
    "III.D74",
    "III.D75",
    "III.T48"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 12,
    "eval": 17,
    "theorem": 14
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "Paradox",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox/",
      "source_line_start": 55,
      "source_line_end": 60,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "def",
      "name": "Paradox.toNat",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/to-nat/",
      "source_line_start": 63,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Paradox.level",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/level/",
      "source_line_start": 71,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Paradox.resolution_level",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/resolution-level/",
      "source_line_start": 79,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Paradox.forbidden_move_idx",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-idx/",
      "source_line_start": 89,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "def",
      "name": "all_paradoxes",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes/",
      "source_line_start": 96,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D73"
      ]
    },
    {
      "kind": "def",
      "name": "proof_theory_e3_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/proof-theory-e3-check/",
      "source_line_start": 115,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D73",
        "III.D74"
      ]
    },
    {
      "kind": "def",
      "name": "self_model_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-check/",
      "source_line_start": 158,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D74"
      ]
    },
    {
      "kind": "def",
      "name": "self_model_invariant_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-invariant-check/",
      "source_line_start": 180,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D74",
        "III.D75"
      ]
    },
    {
      "kind": "def",
      "name": "paradox_single_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-single-check/",
      "source_line_start": 212,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "four_paradox_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/four-paradox-check/",
      "source_line_start": 236,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "def",
      "name": "forbidden_moves_distinct",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-moves-distinct/",
      "source_line_start": 243,
      "source_line_end": 251,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "def",
      "name": "paradox_resolution_check",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-resolution-check/",
      "source_line_start": 266,
      "source_line_end": 277,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T48"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l293/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l294/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proof_theory_e3_8_3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/proof-theory-e3-8-3/",
      "source_line_start": 317,
      "source_line_end": 318,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D73"
      ]
    },
    {
      "kind": "theorem",
      "name": "self_model_8_3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-8-3/",
      "source_line_start": 321,
      "source_line_end": 322,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D74"
      ]
    },
    {
      "kind": "theorem",
      "name": "self_model_inv_8_3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-inv-8-3/",
      "source_line_start": 325,
      "source_line_end": 326,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D74"
      ]
    },
    {
      "kind": "theorem",
      "name": "four_paradox_8_3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/four-paradox-8-3/",
      "source_line_start": 329,
      "source_line_end": 330,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "forbidden_moves_distinct_thm",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-moves-distinct-thm/",
      "source_line_start": 333,
      "source_line_end": 334,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "paradox_resolution_8_3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-resolution-8-3/",
      "source_line_start": 337,
      "source_line_end": 338,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T48"
      ]
    },
    {
      "kind": "theorem",
      "name": "e3_is_proof_theory",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/e3-is-proof-theory/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D73"
      ]
    },
    {
      "kind": "theorem",
      "name": "self_model_levels",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-levels/",
      "source_line_start": 348,
      "source_line_end": 349,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D74"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_paradoxes_at_e2",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes-at-e2/",
      "source_line_start": 352,
      "source_line_end": 353,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_paradoxes_resolve_e3",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes-resolve-e3/",
      "source_line_start": 356,
      "source_line_end": 357,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "exactly_four_paradoxes",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/exactly-four-paradoxes/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "forbidden_move_range",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-range/",
      "source_line_start": 363,
      "source_line_end": 364,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D75"
      ]
    },
    {
      "kind": "theorem",
      "name": "paradox_move_injective",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-move-injective/",
      "source_line_start": 367,
      "source_line_end": 374,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T48"
      ]
    },
    {
      "kind": "theorem",
      "name": "paradox_gap",
      "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-gap/",
      "source_line_start": 377,
      "source_line_end": 380,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T48"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Mirror/ProofTheoryE3.lean`
- SHA-256: `cf708c4504d1737221ab4881088e58c6d866a9a72c7be244088c7f6d39d4d4ab`

## Registry Links

- `III.D73` — Proof Theory as E₃
- `III.D74` — Diagrammatic Sector of E₃
- `III.D75` — E₂→E₃ Boundary Crossing
- `III.T48` — Four Paradox Diagnostic

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Bridge.BridgeAxiom`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Mirror.Saturation`

## Declaration Counts

- `def`: 12
- `eval`: 17
- `inductive`: 1
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [Paradox](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox/) | L55-L60 | type/data schema | type/data schema | `III.D75` |
| `def` | [Paradox.toNat](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/to-nat/) | L63-L67 | definition | definition | — |
| `def` | [Paradox.level](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/level/) | L71-L75 | definition | definition | — |
| `def` | [Paradox.resolution_level](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/resolution-level/) | L79-L83 | definition | definition | — |
| `def` | [Paradox.forbidden_move_idx](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-idx/) | L89-L93 | definition | definition | `III.D75` |
| `def` | [all_paradoxes](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes/) | L96-L107 | data/computed value | data/computed value | `III.D73` |
| `def` | [proof_theory_e3_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/proof-theory-e3-check/) | L115-L150 | data/computed value | data/computed value | `III.D73`, `III.D74` |
| `def` | [self_model_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-check/) | L158-L176 | data/computed value | data/computed value | `III.D74` |
| `def` | [self_model_invariant_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-invariant-check/) | L180-L209 | data/computed value | data/computed value | `III.D74`, `III.D75` |
| `def` | [paradox_single_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-single-check/) | L212-L226 | data/computed value | data/computed value | — |
| `def` | [four_paradox_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/four-paradox-check/) | L236-L240 | data/computed value | data/computed value | `III.D75` |
| `def` | [forbidden_moves_distinct](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-moves-distinct/) | L243-L251 | data/computed value | data/computed value | `III.D75` |
| `def` | [paradox_resolution_check](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-resolution-check/) | L266-L277 | data/computed value | data/computed value | `III.T48` |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l287/) | L287-L287 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l288/) | L288-L288 | computed check | computed check | — |
| `eval` | [#eval L291](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l291/) | L291-L291 | computed check | computed check | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l292/) | L292-L292 | computed check | computed check | — |
| `eval` | [#eval L293](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l293/) | L293-L293 | computed check | computed check | — |
| `eval` | [#eval L294](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l294/) | L294-L294 | computed check | computed check | — |
| `eval` | [#eval L295](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l295/) | L295-L295 | computed check | computed check | — |
| `eval` | [#eval L298](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l298/) | L298-L298 | computed check | computed check | — |
| `eval` | [#eval L301](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l301/) | L301-L301 | computed check | computed check | — |
| `eval` | [#eval L302](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l302/) | L302-L302 | computed check | computed check | — |
| `eval` | [#eval L305](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l305/) | L305-L305 | computed check | computed check | — |
| `eval` | [#eval L306](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l306/) | L306-L306 | computed check | computed check | — |
| `eval` | [#eval L307](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l307/) | L307-L307 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/eval-l310/) | L310-L310 | computed check | computed check | — |
| `theorem` | [proof_theory_e3_8_3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/proof-theory-e3-8-3/) | L317-L318 | proof obligation | formal proof obligation checked | `III.D73` |
| `theorem` | [self_model_8_3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-8-3/) | L321-L322 | proof obligation | formal proof obligation checked | `III.D74` |
| `theorem` | [self_model_inv_8_3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-inv-8-3/) | L325-L326 | proof obligation | formal proof obligation checked | `III.D74` |
| `theorem` | [four_paradox_8_3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/four-paradox-8-3/) | L329-L330 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [forbidden_moves_distinct_thm](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-moves-distinct-thm/) | L333-L334 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [paradox_resolution_8_3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-resolution-8-3/) | L337-L338 | proof obligation | formal proof obligation checked | `III.T48` |
| `theorem` | [e3_is_proof_theory](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/e3-is-proof-theory/) | L345-L345 | proof obligation | formal proof obligation checked | `III.D73` |
| `theorem` | [self_model_levels](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-levels/) | L348-L349 | proof obligation | formal proof obligation checked | `III.D74` |
| `theorem` | [all_paradoxes_at_e2](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes-at-e2/) | L352-L353 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [all_paradoxes_resolve_e3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes-resolve-e3/) | L356-L357 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [exactly_four_paradoxes](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/exactly-four-paradoxes/) | L360-L360 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [forbidden_move_range](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-range/) | L363-L364 | proof obligation | formal proof obligation checked | `III.D75` |
| `theorem` | [paradox_move_injective](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-move-injective/) | L367-L374 | proof obligation | formal proof obligation checked | `III.T48` |
| `theorem` | [paradox_gap](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-gap/) | L377-L380 | proof obligation | formal proof obligation checked | `III.T48` |
