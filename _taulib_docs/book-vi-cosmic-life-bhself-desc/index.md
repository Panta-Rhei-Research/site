---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "permalink": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_slug": "book-vi-cosmic-life-bhself-desc",
  "book": "BookVI",
  "family": "CosmicLife",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/CosmicLife/BHSelfDesc.lean",
  "sha256": "14371520f81456af3fa9c9d9981e3b79f9a7ee233b519a6667f6e28a24906225",
  "imports": [
    "TauLib.BookVI.CosmicLife.BHDist",
    "TauLib.BookV.Gravity.BHTopoModes"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.CosmicLife.CrossLimit"
  ],
  "registry_ids": [
    "V.D234",
    "V.T114",
    "V.T168",
    "VI.D58",
    "VI.D59",
    "VI.L09",
    "VI.L10",
    "VI.T30"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 4,
    "theorem": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BHDecodeTarget",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-target/",
      "source_line_start": 38,
      "source_line_end": 45,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D58"
      ]
    },
    {
      "kind": "def",
      "name": "bh_target",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-target/",
      "source_line_start": 47,
      "source_line_end": 47,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHDecodeHorizon",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-horizon/",
      "source_line_start": 55,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D59"
      ]
    },
    {
      "kind": "def",
      "name": "bh_horizon",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-horizon/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_uniqueness_lemma",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-uniqueness-lemma/",
      "source_line_start": 72,
      "source_line_end": 74,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VI.L09"
      ]
    },
    {
      "kind": "theorem",
      "name": "bh_constancy_lemma",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-constancy-lemma/",
      "source_line_start": 78,
      "source_line_end": 80,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VI.L10"
      ]
    },
    {
      "kind": "structure",
      "name": "BHEvaluator",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhevaluator/",
      "source_line_start": 89,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_evaluator",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-evaluator/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "evaluator_modes_consistent",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/evaluator-modes-consistent/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHSelfDescResult",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhself-desc-result/",
      "source_line_start": 113,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T30"
      ]
    },
    {
      "kind": "def",
      "name": "bh_sd",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-sd/",
      "source_line_start": 125,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_selfdesc_theorem",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-selfdesc-theorem/",
      "source_line_start": 130,
      "source_line_end": 136,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VI.T30"
      ]
    },
    {
      "kind": "theorem",
      "name": "selfdesc_uses_bookV_modes",
      "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/selfdesc-uses-book-v-modes/",
      "source_line_start": 139,
      "source_line_end": 144,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/CosmicLife/BHSelfDesc.lean`
- SHA-256: `14371520f81456af3fa9c9d9981e3b79f9a7ee233b519a6667f6e28a24906225`

## Registry Links

- `V.D234` — T² QNM Mode Structure
- `V.T114` — No-Shrink Theorem
- `V.T168` — QNM Fundamental Frequency Ratio = ι_τ⁻¹
- `VI.D58` — BH DecodeTarget
- `VI.D59` — BH DecodeHorizon
- `VI.L09` — BH Uniqueness Lemma
- `VI.L10` — BH Constancy Lemma
- `VI.T30` — BH SelfDesc Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.CosmicLife.BHDist`
- `TauLib.BookV.Gravity.BHTopoModes`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.CosmicLife.CrossLimit`

## Declaration Counts

- `def`: 4
- `structure`: 4
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BHDecodeTarget](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-target/) | L38-L45 | type/data schema | type/data schema | `VI.D58` |
| `def` | [bh_target](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-target/) | L47-L47 | definition | definition | — |
| `structure` | [BHDecodeHorizon](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-horizon/) | L55-L62 | type/data schema | type/data schema | `VI.D59` |
| `def` | [bh_horizon](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-horizon/) | L64-L64 | definition | definition | — |
| `theorem` | [bh_uniqueness_lemma](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-uniqueness-lemma/) | L72-L74 | proof obligation | formal proof obligation checked | `VI.L09` |
| `theorem` | [bh_constancy_lemma](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-constancy-lemma/) | L78-L80 | proof obligation | formal proof obligation checked | `VI.L10` |
| `structure` | [BHEvaluator](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhevaluator/) | L89-L96 | type/data schema | type/data schema | — |
| `def` | [bh_evaluator](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-evaluator/) | L98-L98 | definition | definition | — |
| `theorem` | [evaluator_modes_consistent](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/evaluator-modes-consistent/) | L101-L102 | proof obligation | formal proof obligation checked | — |
| `structure` | [BHSelfDescResult](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhself-desc-result/) | L113-L123 | type/data schema | type/data schema | `VI.T30` |
| `def` | [bh_sd](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-sd/) | L125-L127 | definition | definition | — |
| `theorem` | [bh_selfdesc_theorem](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-selfdesc-theorem/) | L130-L136 | proof obligation | formal proof obligation checked | `VI.T30` |
| `theorem` | [selfdesc_uses_bookV_modes](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/selfdesc-uses-book-v-modes/) | L139-L144 | proof obligation | formal proof obligation checked | — |
