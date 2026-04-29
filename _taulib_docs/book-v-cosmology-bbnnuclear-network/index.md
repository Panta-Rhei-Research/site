---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_slug": "book-v-cosmology-bbnnuclear-network",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean",
  "sha256": "76d21831678be53b28f6b67c21fef90fadf6ecc91edc907776a9d12fd19dedd4",
  "imports": [
    "TauLib.BookV.Cosmology.HeliumFraction",
    "TauLib.BookV.Cosmology.BBNBaryogenesis",
    "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
  ],
  "imported_by": [
    "TauLib.BookV"
  ],
  "registry_ids": [
    "V.D301",
    "V.D302",
    "V.D303",
    "V.D304",
    "V.D305",
    "V.D306",
    "V.D307",
    "V.P166",
    "V.P167",
    "V.P168",
    "V.P169",
    "V.R427",
    "V.R428",
    "V.R429",
    "V.R430",
    "V.R431",
    "V.R432",
    "V.R433",
    "V.R434",
    "V.R435",
    "V.R436",
    "V.R437",
    "V.R438",
    "V.T241",
    "V.T242",
    "V.T243",
    "V.T244",
    "V.T245",
    "V.T246",
    "V.T247"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 11,
    "inductive": 3,
    "theorem": 19,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "DeuteriumBottleneck",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-bottleneck/",
      "source_line_start": 90,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": [
        "V.D301"
      ]
    },
    {
      "kind": "def",
      "name": "deuterium_bottleneck",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-bottleneck-l98/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "BBNNucleus",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnnucleus/",
      "source_line_start": 105,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": [
        "V.D302"
      ]
    },
    {
      "kind": "def",
      "name": "BBNNucleus.massNumber",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/mass-number/",
      "source_line_start": 117,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bbn_nucleus_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-nucleus-count/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "BBNReaction",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnreaction/",
      "source_line_start": 137,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": [
        "V.D303"
      ]
    },
    {
      "kind": "def",
      "name": "bbn_reactions",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-reactions/",
      "source_line_start": 153,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bbn_reaction_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-reaction-count/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "BBNSector",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnsector/",
      "source_line_start": 165,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "V.D304"
      ]
    },
    {
      "kind": "def",
      "name": "reaction_sector",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/reaction-sector/",
      "source_line_start": 172,
      "source_line_end": 184,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sector_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/sector-count/",
      "source_line_start": 187,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "a_sector_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/a-sector-count/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "b_sector_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/b-sector-count/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c_sector_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/c-sector-count/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_distribution_sum",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/sector-distribution-sum/",
      "source_line_start": 199,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T242"
      ]
    },
    {
      "kind": "theorem",
      "name": "reaction_9_is_B_sector",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/reaction-9-is-b-sector/",
      "source_line_start": 204,
      "source_line_end": 205,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FiberHolonomyCorrection",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/fiber-holonomy-correction/",
      "source_line_start": 214,
      "source_line_end": 223,
      "formal_status": "defined",
      "registry_ids": [
        "V.D305"
      ]
    },
    {
      "kind": "def",
      "name": "fiber_holonomy",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/fiber-holonomy/",
      "source_line_start": 226,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Be7SuppressionFactor",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/be7-suppression-factor/",
      "source_line_start": 236,
      "source_line_end": 245,
      "formal_status": "defined",
      "registry_ids": [
        "V.D306"
      ]
    },
    {
      "kind": "def",
      "name": "be7_suppression",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/be7-suppression/",
      "source_line_start": 248,
      "source_line_end": 250,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "suppression_is_one_third",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/suppression-is-one-third/",
      "source_line_start": 254,
      "source_line_end": 256,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T243"
      ]
    },
    {
      "kind": "theorem",
      "name": "suppression_den_matches_tau3_dim",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/suppression-den-matches-tau3-dim/",
      "source_line_start": 259,
      "source_line_end": 260,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LithiumResolution",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-resolution/",
      "source_line_start": 270,
      "source_line_end": 285,
      "formal_status": "defined",
      "registry_ids": [
        "V.T244"
      ]
    },
    {
      "kind": "def",
      "name": "lithium_resolution",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-resolution-l288/",
      "source_line_start": 288,
      "source_line_end": 290,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "lithium_within_1sigma",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-within-1sigma/",
      "source_line_start": 293,
      "source_line_end": 298,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DeuteriumPrediction",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-prediction/",
      "source_line_start": 307,
      "source_line_end": 316,
      "formal_status": "defined",
      "registry_ids": [
        "V.T241"
      ]
    },
    {
      "kind": "def",
      "name": "deuterium_prediction",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-prediction-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dh_in_range",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dh-in-range/",
      "source_line_start": 323,
      "source_line_end": 328,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P166"
      ]
    },
    {
      "kind": "structure",
      "name": "He3Prediction",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-prediction/",
      "source_line_start": 337,
      "source_line_end": 344,
      "formal_status": "defined",
      "registry_ids": [
        "V.T247"
      ]
    },
    {
      "kind": "def",
      "name": "he3_prediction",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-prediction-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "he3_in_range",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-in-range/",
      "source_line_start": 350,
      "source_line_end": 355,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T247"
      ]
    },
    {
      "kind": "theorem",
      "name": "yp_preserved",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/yp-preserved/",
      "source_line_start": 364,
      "source_line_end": 372,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T245"
      ]
    },
    {
      "kind": "theorem",
      "name": "dh_preserved",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dh-preserved/",
      "source_line_start": 378,
      "source_line_end": 383,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T246"
      ]
    },
    {
      "kind": "theorem",
      "name": "selectivity_threshold",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/selectivity-threshold/",
      "source_line_start": 388,
      "source_line_end": 400,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P168"
      ]
    },
    {
      "kind": "structure",
      "name": "CompleteBBNTable",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/complete-bbntable/",
      "source_line_start": 408,
      "source_line_end": 421,
      "formal_status": "defined",
      "registry_ids": [
        "V.D307"
      ]
    },
    {
      "kind": "def",
      "name": "complete_bbn_table",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/complete-bbn-table/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bbn_table_all_within_range",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-table-all-within-range/",
      "source_line_start": 428,
      "source_line_end": 434,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P169"
      ]
    },
    {
      "kind": "theorem",
      "name": "spite_plateau_consistent",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/spite-plateau-consistent/",
      "source_line_start": 441,
      "source_line_end": 447,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P167"
      ]
    },
    {
      "kind": "theorem",
      "name": "dim_tau3_universality",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dim-tau3-universality/",
      "source_line_start": 455,
      "source_line_end": 460,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bbn_species_standard",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-species-standard/",
      "source_line_start": 463,
      "source_line_end": 463,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l519/",
      "source_line_start": 519,
      "source_line_end": 519,
      "formal_status": "computed",
      "registry_ids": [
        "V.R427",
        "V.R428",
        "V.R429",
        "V.R430",
        "V.R431",
        "V.R432",
        "V.R433",
        "V.R434",
        "V.R435",
        "V.R436",
        "V.R437",
        "V.R438"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l520/",
      "source_line_start": 520,
      "source_line_end": 520,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l521/",
      "source_line_start": 521,
      "source_line_end": 521,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l522/",
      "source_line_start": 522,
      "source_line_end": 522,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l523/",
      "source_line_start": 523,
      "source_line_end": 523,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l524/",
      "source_line_start": 524,
      "source_line_end": 524,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l525/",
      "source_line_start": 525,
      "source_line_end": 525,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l526/",
      "source_line_start": 526,
      "source_line_end": 526,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l527/",
      "source_line_start": 527,
      "source_line_end": 527,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l528/",
      "source_line_start": 528,
      "source_line_end": 528,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l529/",
      "source_line_start": 529,
      "source_line_end": 529,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l530/",
      "source_line_start": 530,
      "source_line_end": 530,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l531/",
      "source_line_start": 531,
      "source_line_end": 531,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l532/",
      "source_line_start": 532,
      "source_line_end": 534,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`
- SHA-256: `76d21831678be53b28f6b67c21fef90fadf6ecc91edc907776a9d12fd19dedd4`

## Registry Links

- `V.D301` — Deuterium Bottleneck Temperature
- `V.D302` — BBN Network Light Elements
- `V.D303` — BBN Reaction Chain
- `V.D304` — Sector Assignment
- `V.D305` — T² Fiber Holonomy Correction
- `V.D306` — ⁷Be Suppression Factor
- `V.D307` — Complete BBN Abundance Table
- `V.P166` — D/H Observational Consistency
- `V.P167` — Spite Plateau Consistency
- `V.P168` — Selectivity: Only A ≥ 7 Suppressed
- `V.P169` — BBN Table Consistency
- `V.R427` — D/H Anti-correlation
- `V.R428` — N3 Status Upgrade
- `V.R429` — ⁷Be Production as B-Sector
- `V.R430` — EM Phase-Space Restriction
- `V.R431` — Voxel Packing Connection
- `V.R432` — Packing Threshold at A = 7
- `V.R433` — Stellar Depletion and Spite Plateau
- `V.R434` — All Four from Single η_B
- `V.R435` — N3 Falsification Update
- `V.R436` — N4 Falsification Update
- `V.R437` — Wave 25 BBN Prediction Table
- `V.R438` — Cross-Sprint Consistency
- `V.T241` — D/H from τ-native η_B
- `V.T242` — Sector Distribution {1,4,7}
- `V.T243` — Suppression = 1/dim(τ³) = 1/3
- `V.T244` — Li-7 Resolution
- `V.T245` — Y_p Preservation
- `V.T246` — D/H Preservation
- `V.T247` — He-3/H from τ-native η_B

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.HeliumFraction`
- `TauLib.BookV.Cosmology.BBNBaryogenesis`
- `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`

## Imported By

- `TauLib.BookV`

## Declaration Counts

- `def`: 11
- `eval`: 14
- `inductive`: 3
- `structure`: 7
- `theorem`: 19

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [DeuteriumBottleneck](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-bottleneck/) | L90-L95 | defined | `V.D301` |
| `def` | [deuterium_bottleneck](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-bottleneck-l98/) | L98-L98 | defined | — |
| `inductive` | [BBNNucleus](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnnucleus/) | L105-L114 | defined | `V.D302` |
| `def` | [BBNNucleus.massNumber](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/mass-number/) | L117-L125 | defined | — |
| `theorem` | [bbn_nucleus_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-nucleus-count/) | L128-L130 | formalized | — |
| `inductive` | [BBNReaction](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnreaction/) | L137-L150 | defined | `V.D303` |
| `def` | [bbn_reactions](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-reactions/) | L153-L155 | defined | — |
| `theorem` | [bbn_reaction_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-reaction-count/) | L158-L158 | formalized | — |
| `inductive` | [BBNSector](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnsector/) | L165-L169 | defined | `V.D304` |
| `def` | [reaction_sector](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/reaction-sector/) | L172-L184 | defined | — |
| `def` | [sector_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/sector-count/) | L187-L188 | defined | — |
| `theorem` | [a_sector_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/a-sector-count/) | L192-L192 | formalized | — |
| `theorem` | [b_sector_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/b-sector-count/) | L194-L194 | formalized | — |
| `theorem` | [c_sector_count](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/c-sector-count/) | L196-L196 | formalized | — |
| `theorem` | [sector_distribution_sum](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/sector-distribution-sum/) | L199-L201 | formalized | `V.T242` |
| `theorem` | [reaction_9_is_B_sector](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/reaction-9-is-b-sector/) | L204-L205 | formalized | — |
| `structure` | [FiberHolonomyCorrection](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/fiber-holonomy-correction/) | L214-L223 | defined | `V.D305` |
| `def` | [fiber_holonomy](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/fiber-holonomy/) | L226-L227 | defined | — |
| `structure` | [Be7SuppressionFactor](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/be7-suppression-factor/) | L236-L245 | defined | `V.D306` |
| `def` | [be7_suppression](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/be7-suppression/) | L248-L250 | defined | — |
| `theorem` | [suppression_is_one_third](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/suppression-is-one-third/) | L254-L256 | formalized | `V.T243` |
| `theorem` | [suppression_den_matches_tau3_dim](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/suppression-den-matches-tau3-dim/) | L259-L260 | formalized | — |
| `structure` | [LithiumResolution](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-resolution/) | L270-L285 | defined | `V.T244` |
| `def` | [lithium_resolution](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-resolution-l288/) | L288-L290 | defined | — |
| `theorem` | [lithium_within_1sigma](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-within-1sigma/) | L293-L298 | formalized | — |
| `structure` | [DeuteriumPrediction](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-prediction/) | L307-L316 | defined | `V.T241` |
| `def` | [deuterium_prediction](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-prediction-l319/) | L319-L319 | defined | — |
| `theorem` | [dh_in_range](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dh-in-range/) | L323-L328 | formalized | `V.P166` |
| `structure` | [He3Prediction](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-prediction/) | L337-L344 | defined | `V.T247` |
| `def` | [he3_prediction](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-prediction-l347/) | L347-L347 | defined | — |
| `theorem` | [he3_in_range](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-in-range/) | L350-L355 | formalized | `V.T247` |
| `theorem` | [yp_preserved](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/yp-preserved/) | L364-L372 | formalized | `V.T245` |
| `theorem` | [dh_preserved](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dh-preserved/) | L378-L383 | formalized | `V.T246` |
| `theorem` | [selectivity_threshold](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/selectivity-threshold/) | L388-L400 | formalized | `V.P168` |
| `structure` | [CompleteBBNTable](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/complete-bbntable/) | L408-L421 | defined | `V.D307` |
| `def` | [complete_bbn_table](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/complete-bbn-table/) | L424-L424 | defined | — |
| `theorem` | [bbn_table_all_within_range](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-table-all-within-range/) | L428-L434 | formalized | `V.P169` |
| `theorem` | [spite_plateau_consistent](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/spite-plateau-consistent/) | L441-L447 | formalized | `V.P167` |
| `theorem` | [dim_tau3_universality](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dim-tau3-universality/) | L455-L460 | formalized | — |
| `theorem` | [bbn_species_standard](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-species-standard/) | L463-L463 | formalized | — |
| `eval` | [#eval L519](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l519/) | L519-L519 | computed | `V.R427`, `V.R428`, `V.R429`, `V.R430`, `V.R431`, `V.R432`, `V.R433`, `V.R434`, `V.R435`, `V.R436`, `V.R437`, `V.R438` |
| `eval` | [#eval L520](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l520/) | L520-L520 | computed | — |
| `eval` | [#eval L521](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l521/) | L521-L521 | computed | — |
| `eval` | [#eval L522](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l522/) | L522-L522 | computed | — |
| `eval` | [#eval L523](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l523/) | L523-L523 | computed | — |
| `eval` | [#eval L524](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l524/) | L524-L524 | computed | — |
| `eval` | [#eval L525](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l525/) | L525-L525 | computed | — |
| `eval` | [#eval L526](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l526/) | L526-L526 | computed | — |
| `eval` | [#eval L527](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l527/) | L527-L527 | computed | — |
| `eval` | [#eval L528](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l528/) | L528-L528 | computed | — |
| `eval` | [#eval L529](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l529/) | L529-L529 | computed | — |
| `eval` | [#eval L530](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l530/) | L530-L530 | computed | — |
| `eval` | [#eval L531](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l531/) | L531-L531 | computed | — |
| `eval` | [#eval L532](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l532/) | L532-L534 | computed | — |
