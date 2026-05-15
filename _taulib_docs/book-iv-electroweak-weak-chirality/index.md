---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.WeakChirality",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.WeakChirality`.",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_slug": "book-iv-electroweak-weak-chirality",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/WeakChirality.lean",
  "sha256": "39131a0cd8f83da330d814b7f3fe3c4b45d36a8e81e1637022396d0856d97035",
  "imports": [
    "TauLib.BookIV.Electroweak.AlphaDerivation"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.WeakChirality2"
  ],
  "registry_ids": [
    "IV.D107",
    "IV.D108",
    "IV.D109",
    "IV.D110",
    "IV.D111",
    "IV.D112",
    "IV.D113",
    "IV.D114",
    "IV.L05",
    "IV.P52",
    "IV.P53",
    "IV.T51"
  ],
  "declaration_counts": {
    "structure": 6,
    "def": 21,
    "theorem": 6,
    "inductive": 1,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PolarityIndex",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/polarity-index/",
      "source_line_start": 40,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D107"
      ]
    },
    {
      "kind": "def",
      "name": "pol_D",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-d/",
      "source_line_start": 52,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pol_A",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-a/",
      "source_line_start": 56,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pol_B",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-b/",
      "source_line_start": 60,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pol_C",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-c/",
      "source_line_start": 64,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pol_Omega",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-omega/",
      "source_line_start": 68,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_sector_polarities",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/all-sector-polarities/",
      "source_line_start": 72,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.P52"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_sector_polarities_count",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/all-sector-polarities-count/",
      "source_line_start": 75,
      "source_line_end": 75,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ParityPreserving",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-preserving/",
      "source_line_start": 84,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D108"
      ]
    },
    {
      "kind": "def",
      "name": "parity_em",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-em/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "parity_strong",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-strong/",
      "source_line_start": 94,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "parity_gravity",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-gravity/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "parity_weak",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-weak/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "parity_higgs",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-higgs/",
      "source_line_start": 100,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ChiralityType",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/chirality-type/",
      "source_line_start": 109,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D111"
      ]
    },
    {
      "kind": "def",
      "name": "sigma_a_admissible",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-admissible/",
      "source_line_start": 123,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "sigma_a_iff_left",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-iff-left/",
      "source_line_start": 129,
      "source_line_end": 131,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.L05"
      ]
    },
    {
      "kind": "structure",
      "name": "WBosonMode",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/wboson-mode/",
      "source_line_start": 141,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D109"
      ]
    },
    {
      "kind": "def",
      "name": "w_plus",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-plus/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "w_minus",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-minus/",
      "source_line_start": 155,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ZBosonMode",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/zboson-mode/",
      "source_line_start": 163,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D110"
      ]
    },
    {
      "kind": "def",
      "name": "z_zero",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/z-zero/",
      "source_line_start": 175,
      "source_line_end": 180,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ParityTransformation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-transformation/",
      "source_line_start": 189,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D113"
      ]
    },
    {
      "kind": "def",
      "name": "parity_3d",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-3d/",
      "source_line_start": 199,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ParityViolation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-violation/",
      "source_line_start": 212,
      "source_line_end": 219,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D114"
      ]
    },
    {
      "kind": "def",
      "name": "pv_gravity",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-gravity/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pv_weak",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-weak/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pv_em",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-em/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pv_strong",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-strong/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pv_higgs",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-higgs/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weak_max_parity_violation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/weak-max-parity-violation/",
      "source_line_start": 236,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T51"
      ]
    },
    {
      "kind": "theorem",
      "name": "weak_unique_violator",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/weak-unique-violator/",
      "source_line_start": 245,
      "source_line_end": 251,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wz_massive_from_omega",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/wz-massive-from-omega/",
      "source_line_start": 261,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P53"
      ]
    },
    {
      "kind": "theorem",
      "name": "w_left_only",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-left-only/",
      "source_line_start": 268,
      "source_line_end": 270,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l276/",
      "source_line_start": 276,
      "source_line_end": 276,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l277/",
      "source_line_start": 277,
      "source_line_end": 277,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l281/",
      "source_line_start": 281,
      "source_line_end": 281,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l282/",
      "source_line_start": 282,
      "source_line_end": 282,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l284/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l285/",
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
      "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 288,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/WeakChirality.lean`
- SHA-256: `39131a0cd8f83da330d814b7f3fe3c4b45d36a8e81e1637022396d0856d97035`

## Registry Links

- `IV.D107` — Sector Polarity
- `IV.D108` — Polarity-Preserving Interaction
- `IV.D109` — Channel-Switching Defect Bundle
- `IV.D110` — W-pm Defect Bundles
- `IV.D111` — Z0 Defect Bundle
- `IV.D112` — Chirality
- `IV.D113` — A-Sector Sigma-Admissibility
- `IV.D114` — Parity Operator
- `IV.L05` — Sigma_A-Admissibility Selects Chirality
- `IV.P52` — Polarity Assignments
- `IV.P53` — Mass of Channel-Switching Defect Bundles
- `IV.T51` — Parity Violation in the A-Sector

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.AlphaDerivation`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.WeakChirality2`

## Declaration Counts

- `def`: 21
- `eval`: 11
- `inductive`: 1
- `structure`: 6
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [PolarityIndex](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/polarity-index/) | L40-L49 | type/data schema | type/data schema | `IV.D107` |
| `def` | [pol_D](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-d/) | L52-L53 | definition | definition | — |
| `def` | [pol_A](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-a/) | L56-L57 | definition | definition | — |
| `def` | [pol_B](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-b/) | L60-L61 | definition | definition | — |
| `def` | [pol_C](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-c/) | L64-L65 | definition | definition | — |
| `def` | [pol_Omega](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pol-omega/) | L68-L69 | definition | definition | — |
| `def` | [all_sector_polarities](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/all-sector-polarities/) | L72-L73 | data/computed value | data/computed value | `IV.P52` |
| `theorem` | [all_sector_polarities_count](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/all-sector-polarities-count/) | L75-L75 | proof obligation | formal proof obligation checked | — |
| `structure` | [ParityPreserving](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-preserving/) | L84-L89 | type/data schema | type/data schema | `IV.D108` |
| `def` | [parity_em](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-em/) | L92-L92 | definition | definition | — |
| `def` | [parity_strong](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-strong/) | L94-L94 | definition | definition | — |
| `def` | [parity_gravity](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-gravity/) | L96-L96 | definition | definition | — |
| `def` | [parity_weak](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-weak/) | L98-L98 | definition | definition | — |
| `def` | [parity_higgs](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-higgs/) | L100-L100 | definition | definition | — |
| `inductive` | [ChiralityType](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/chirality-type/) | L109-L114 | type/data schema | type/data schema | `IV.D111` |
| `def` | [sigma_a_admissible](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-admissible/) | L123-L126 | data/computed value | data/computed value | `IV.D112` |
| `theorem` | [sigma_a_iff_left](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-iff-left/) | L129-L131 | proof obligation | formal proof obligation checked | `IV.L05` |
| `structure` | [WBosonMode](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/wboson-mode/) | L141-L150 | type/data schema | type/data schema | `IV.D109` |
| `def` | [w_plus](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-plus/) | L153-L153 | definition | definition | — |
| `def` | [w_minus](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-minus/) | L155-L155 | definition | definition | — |
| `structure` | [ZBosonMode](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/zboson-mode/) | L163-L172 | type/data schema | type/data schema | `IV.D110` |
| `def` | [z_zero](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/z-zero/) | L175-L180 | definition | definition | — |
| `structure` | [ParityTransformation](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-transformation/) | L189-L196 | type/data schema | type/data schema | `IV.D113` |
| `def` | [parity_3d](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-3d/) | L199-L203 | definition | definition | — |
| `structure` | [ParityViolation](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/parity-violation/) | L212-L219 | type/data schema | type/data schema | `IV.D114` |
| `def` | [pv_gravity](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-gravity/) | L222-L222 | definition | definition | — |
| `def` | [pv_weak](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-weak/) | L223-L223 | definition | definition | — |
| `def` | [pv_em](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-em/) | L224-L224 | definition | definition | — |
| `def` | [pv_strong](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-strong/) | L225-L225 | definition | definition | — |
| `def` | [pv_higgs](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/pv-higgs/) | L226-L226 | definition | definition | — |
| `theorem` | [weak_max_parity_violation](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/weak-max-parity-violation/) | L236-L242 | proof obligation | formal proof obligation checked | `IV.T51` |
| `theorem` | [weak_unique_violator](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/weak-unique-violator/) | L245-L251 | proof obligation | formal proof obligation checked | — |
| `theorem` | [wz_massive_from_omega](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/wz-massive-from-omega/) | L261-L265 | proof obligation | formal proof obligation checked | `IV.P53` |
| `theorem` | [w_left_only](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/w-left-only/) | L268-L270 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L276](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l276/) | L276-L276 | computed check | computed check | — |
| `eval` | [#eval L277](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l277/) | L277-L277 | computed check | computed check | — |
| `eval` | [#eval L278](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l279/) | L279-L279 | computed check | computed check | — |
| `eval` | [#eval L280](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l280/) | L280-L280 | computed check | computed check | — |
| `eval` | [#eval L281](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l281/) | L281-L281 | computed check | computed check | — |
| `eval` | [#eval L282](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l282/) | L282-L282 | computed check | computed check | — |
| `eval` | [#eval L283](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l283/) | L283-L283 | computed check | computed check | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/eval-l286/) | L286-L288 | computed check | computed check | — |
