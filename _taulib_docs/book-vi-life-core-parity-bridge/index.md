---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.LifeCore.ParityBridge",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.LifeCore.ParityBridge`.",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_slug": "book-vi-life-core-parity-bridge",
  "book": "BookVI",
  "family": "LifeCore",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/LifeCore/ParityBridge.lean",
  "sha256": "8d615e75a3d0ea36d3502daaef3cf70338efc86a338428e1bc8d8edc84a87809",
  "imports": [
    "TauLib.BookIV.Arena.FiveSectors"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.LifeCore.Distinction"
  ],
  "registry_ids": [
    "VI.D01",
    "VI.D02",
    "VI.D03",
    "VI.D71",
    "VI.D72",
    "VI.L01",
    "VI.L14",
    "VI.P01",
    "VI.T01",
    "VI.T41"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 7,
    "theorem": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PolarityFunctional",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-functional/",
      "source_line_start": 28,
      "source_line_end": 33,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D01"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_functional",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-functional-l35/",
      "source_line_start": 35,
      "source_line_end": 39,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TwoPointObject",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/two-point-object/",
      "source_line_start": 43,
      "source_line_end": 48,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D02"
      ]
    },
    {
      "kind": "def",
      "name": "two_point",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/two-point/",
      "source_line_start": 50,
      "source_line_end": 52,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThreePolarityTerms",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/three-polarity-terms/",
      "source_line_start": 55,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D03"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_terms",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-terms/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weak_sector_uniqueness",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/weak-sector-uniqueness/",
      "source_line_start": 66,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": [
        "VI.L01"
      ]
    },
    {
      "kind": "structure",
      "name": "ParityBridgeTheorem",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge-theorem/",
      "source_line_start": 73,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T01"
      ]
    },
    {
      "kind": "def",
      "name": "parity_bridge",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge/",
      "source_line_start": 81,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "parity_bridge_theorem",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge-theorem-l85/",
      "source_line_start": 85,
      "source_line_end": 87,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LowNoiseCarrierCondition",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise-carrier-condition/",
      "source_line_start": 90,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": [
        "VI.P01"
      ]
    },
    {
      "kind": "def",
      "name": "low_noise",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "low_noise_carrier_condition",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise-carrier-condition-l99/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PolarityPropagation",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-propagation/",
      "source_line_start": 111,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D71"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_propagation",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-propagation-l123/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChiralitySeed",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/chirality-seed/",
      "source_line_start": 135,
      "source_line_end": 143,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D72"
      ]
    },
    {
      "kind": "def",
      "name": "chirality_seed",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/chirality-seed-l145/",
      "source_line_start": 145,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "propagation_preserves_chirality",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-preserves-chirality/",
      "source_line_start": 158,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": [
        "VI.T41"
      ]
    },
    {
      "kind": "theorem",
      "name": "propagation_uniqueness",
      "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-uniqueness/",
      "source_line_start": 172,
      "source_line_end": 177,
      "formal_status": "formalized",
      "registry_ids": [
        "VI.L14"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/LifeCore/ParityBridge.lean`
- SHA-256: `8d615e75a3d0ea36d3502daaef3cf70338efc86a338428e1bc8d8edc84a87809`

## Registry Links

- `VI.D01` — Polarity Functional
- `VI.D02` — Polarity-Typed Two-Point Object (2_τ)
- `VI.D03` — Three Polarity Terms
- `VI.D71` — Polarity Propagation
- `VI.D72` — Chirality Seed
- `VI.L01` — Weak-Sector Uniqueness
- `VI.L14` — Propagation Uniqueness
- `VI.P01` — Low-Noise Carrier Condition
- `VI.T01` — Parity Bridge Theorem
- `VI.T41` — Propagation Preserves Chirality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.FiveSectors`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.LifeCore.Distinction`

## Declaration Counts

- `def`: 7
- `structure`: 7
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [PolarityFunctional](/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-functional/) | L28-L33 | defined | `VI.D01` |
| `def` | [polarity_functional](/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-functional-l35/) | L35-L39 | defined | — |
| `structure` | [TwoPointObject](/verify/taulib/docs/book-vi-life-core-parity-bridge/two-point-object/) | L43-L48 | defined | `VI.D02` |
| `def` | [two_point](/verify/taulib/docs/book-vi-life-core-parity-bridge/two-point/) | L50-L52 | defined | — |
| `structure` | [ThreePolarityTerms](/verify/taulib/docs/book-vi-life-core-parity-bridge/three-polarity-terms/) | L55-L58 | defined | `VI.D03` |
| `def` | [polarity_terms](/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-terms/) | L60-L62 | defined | — |
| `theorem` | [weak_sector_uniqueness](/verify/taulib/docs/book-vi-life-core-parity-bridge/weak-sector-uniqueness/) | L66-L69 | formalized | `VI.L01` |
| `structure` | [ParityBridgeTheorem](/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge-theorem/) | L73-L79 | defined | `VI.T01` |
| `def` | [parity_bridge](/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge/) | L81-L83 | defined | — |
| `theorem` | [parity_bridge_theorem](/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge-theorem-l85/) | L85-L87 | formalized | — |
| `structure` | [LowNoiseCarrierCondition](/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise-carrier-condition/) | L90-L93 | defined | `VI.P01` |
| `def` | [low_noise](/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise/) | L95-L97 | defined | — |
| `theorem` | [low_noise_carrier_condition](/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise-carrier-condition-l99/) | L99-L100 | formalized | — |
| `structure` | [PolarityPropagation](/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-propagation/) | L111-L121 | defined | `VI.D71` |
| `def` | [polarity_propagation](/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-propagation-l123/) | L123-L125 | defined | — |
| `structure` | [ChiralitySeed](/verify/taulib/docs/book-vi-life-core-parity-bridge/chirality-seed/) | L135-L143 | defined | `VI.D72` |
| `def` | [chirality_seed](/verify/taulib/docs/book-vi-life-core-parity-bridge/chirality-seed-l145/) | L145-L147 | defined | — |
| `theorem` | [propagation_preserves_chirality](/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-preserves-chirality/) | L158-L163 | formalized | `VI.T41` |
| `theorem` | [propagation_uniqueness](/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-uniqueness/) | L172-L177 | formalized | `VI.L14` |
