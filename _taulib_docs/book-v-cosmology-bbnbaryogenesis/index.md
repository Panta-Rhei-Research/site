---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_slug": "book-v-cosmology-bbnbaryogenesis",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/BBNBaryogenesis.lean",
  "sha256": "2c67b9add7260f5a6a60bbaa2fe5b4df5b9b8543ed17a80551c7dde638bbb215",
  "imports": [
    "TauLib.BookV.Cosmology.ThresholdLadder",
    "TauLib.BookV.Cosmology.HeliumFraction"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.BBNNuclearNetwork",
    "TauLib.BookV.Cosmology.NeutrinoBackground"
  ],
  "registry_ids": [
    "V.D197",
    "V.D198",
    "V.D238",
    "V.P113",
    "V.P130",
    "V.R323",
    "V.R324",
    "V.R325",
    "V.R326",
    "V.R379",
    "V.T151",
    "V.T179",
    "V.T180"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 7,
    "def": 11,
    "theorem": 22,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "AdmissibilityCategory",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/admissibility-category/",
      "source_line_start": 66,
      "source_line_end": 71,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdDependentAdmissibility",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-dependent-admissibility/",
      "source_line_start": 81,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": [
        "V.D197"
      ]
    },
    {
      "kind": "def",
      "name": "threshold_admissibility",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-admissibility/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pre_confinement_admits_B_violation",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/pre-confinement-admits-b-violation/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "post_confinement_conserves_B",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/post-confinement-conserves-b/",
      "source_line_start": 102,
      "source_line_end": 104,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BaryogenesisWindow",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window/",
      "source_line_start": 116,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": [
        "V.D198"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_window",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window-l128/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_finite",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-finite/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleosynthesis_after_window",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/nucleosynthesis-after-window/",
      "source_line_start": 139,
      "source_line_end": 142,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_matches_ladder",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-matches-ladder/",
      "source_line_start": 146,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "n_gauge_generators",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-generators/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "n_total_generators",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-total-generators/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "n_gauge_from_total",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-from-total/",
      "source_line_start": 168,
      "source_line_end": 170,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "n_eff_eq_three",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-eq-three/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T151"
      ]
    },
    {
      "kind": "theorem",
      "name": "n_eff_upper_bound",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-upper-bound/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P113"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_dark_sector",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/no-dark-sector/",
      "source_line_start": 191,
      "source_line_end": 192,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_within_ladder",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-within-ladder/",
      "source_line_start": 200,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "clean_threshold_count",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/clean-threshold-count/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "registry_ids": [
        "V.R323",
        "V.R324",
        "V.R325",
        "V.R326"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BaryogenesisSAIMechanism",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-saimechanism/",
      "source_line_start": 257,
      "source_line_end": 272,
      "formal_status": "defined",
      "registry_ids": [
        "V.D238"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_sai_mechanism",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-mechanism/",
      "source_line_start": 275,
      "source_line_end": 280,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "baryogenesis_sai_thm",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-thm/",
      "source_line_start": 283,
      "source_line_end": 288,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fifteen_window_product",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/fifteen-window-product/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T179"
      ]
    },
    {
      "kind": "theorem",
      "name": "five_sixths_structure",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-structure/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T180"
      ]
    },
    {
      "kind": "structure",
      "name": "BaryogenesisFirstPrinciples",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles/",
      "source_line_start": 310,
      "source_line_end": 319,
      "formal_status": "defined",
      "registry_ids": [
        "V.P130"
      ]
    },
    {
      "kind": "def",
      "name": "baryogenesis_fp",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-fp/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "baryogenesis_first_principles",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles-l325/",
      "source_line_start": 325,
      "source_line_end": 330,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sai_mod_comparison",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-comparison/",
      "source_line_start": 333,
      "source_line_end": 335,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "vop2_status_sprint6c",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/vop2-status-sprint6c/",
      "source_line_start": 338,
      "source_line_end": 341,
      "formal_status": "defined",
      "registry_ids": [
        "V.R379"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeneratorOrbitSuppression",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression/",
      "source_line_start": 369,
      "source_line_end": 382,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "generator_orbit_suppression",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression-l384/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "generator_orbit_produces_15",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-produces-15/",
      "source_line_start": 388,
      "source_line_end": 393,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fiber_dimension_decomposition",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/fiber-dimension-decomposition/",
      "source_line_start": 396,
      "source_line_end": 397,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sai_mod_hierarchy",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-hierarchy/",
      "source_line_start": 402,
      "source_line_end": 403,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdUniquenessFiveSixths",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-five-sixths/",
      "source_line_start": 420,
      "source_line_end": 433,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "threshold_uniqueness_56",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-56/",
      "source_line_start": 435,
      "source_line_end": 437,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sixths_uniquely_forced",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-uniquely-forced/",
      "source_line_start": 440,
      "source_line_end": 445,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sixths_cross_check_yp",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-cross-check-yp/",
      "source_line_start": 448,
      "source_line_end": 449,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "threshold_uniqueness_matches_ladder",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-matches-ladder/",
      "source_line_start": 452,
      "source_line_end": 454,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CPAsymmetryFromPolarity",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cpasymmetry-from-polarity/",
      "source_line_start": 473,
      "source_line_end": 484,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cp_asymmetry_polarity",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-polarity/",
      "source_line_start": 486,
      "source_line_end": 486,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cp_asymmetry_structural",
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-structural/",
      "source_line_start": 489,
      "source_line_end": 493,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l496/",
      "source_line_start": 496,
      "source_line_end": 496,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l497/",
      "source_line_start": 497,
      "source_line_end": 497,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l498/",
      "source_line_start": 498,
      "source_line_end": 498,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l499/",
      "source_line_start": 499,
      "source_line_end": 501,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean",
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
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/BBNBaryogenesis.lean`
- SHA-256: `2c67b9add7260f5a6a60bbaa2fe5b4df5b9b8543ed17a80551c7dde638bbb215`

## Registry Links

- `V.D197` — Threshold-Dependent Admissibility
- `V.D198` — Baryogenesis Window
- `V.D238` — SA-i mod-W₃(4) Baryogenesis Mechanism: ι_τ¹⁵ = (ι_τ³)^W₃(4)
- `V.P113` — Dark Sector Closure
- `V.P130` — Baryogenesis First Principles: Generator Orbit + Threshold Uniqueness
- `V.R323` — Commutator Magnitude at omega-Crossing
- `V.R324` — eta_B Structural Candidate
- `V.R325` — Primorial-Confinement Bridge
- `V.R326` — Confinement Multiplicity Estimate
- `V.R379` — V.OP2 Status after Sprint 6C: SA-i mod-5 Mechanism Proposed
- `V.T151` — N_eff from Sector Exhaustion
- `V.T179` — ι_τ¹⁵ from Generator Orbit: 15 = dim(τ³) × |generators|
- `V.T180` — (5/6) Uniquely Forced from Threshold Topology

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.ThresholdLadder`
- `TauLib.BookV.Cosmology.HeliumFraction`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.BBNNuclearNetwork`
- `TauLib.BookV.Cosmology.NeutrinoBackground`

## Declaration Counts

- `def`: 11
- `eval`: 14
- `inductive`: 1
- `structure`: 7
- `theorem`: 22

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [AdmissibilityCategory](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/admissibility-category/) | L66-L71 | defined | — |
| `structure` | [ThresholdDependentAdmissibility](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-dependent-admissibility/) | L81-L90 | defined | `V.D197` |
| `def` | [threshold_admissibility](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-admissibility/) | L93-L94 | defined | — |
| `theorem` | [pre_confinement_admits_B_violation](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/pre-confinement-admits-b-violation/) | L97-L99 | formalized | — |
| `theorem` | [post_confinement_conserves_B](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/post-confinement-conserves-b/) | L102-L104 | formalized | — |
| `structure` | [BaryogenesisWindow](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window/) | L116-L125 | defined | `V.D198` |
| `def` | [baryogenesis_window](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window-l128/) | L128-L130 | defined | — |
| `theorem` | [window_finite](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-finite/) | L133-L135 | formalized | — |
| `theorem` | [nucleosynthesis_after_window](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/nucleosynthesis-after-window/) | L139-L142 | formalized | — |
| `theorem` | [window_matches_ladder](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-matches-ladder/) | L146-L151 | formalized | — |
| `def` | [n_gauge_generators](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-generators/) | L160-L160 | defined | — |
| `def` | [n_total_generators](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-total-generators/) | L163-L163 | defined | — |
| `theorem` | [n_gauge_from_total](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-gauge-from-total/) | L168-L170 | formalized | — |
| `theorem` | [n_eff_eq_three](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-eq-three/) | L176-L176 | formalized | `V.T151` |
| `theorem` | [n_eff_upper_bound](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-upper-bound/) | L188-L188 | formalized | `V.P113` |
| `theorem` | [no_dark_sector](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/no-dark-sector/) | L191-L192 | formalized | — |
| `theorem` | [window_within_ladder](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-within-ladder/) | L200-L204 | formalized | — |
| `theorem` | [clean_threshold_count](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/clean-threshold-count/) | L208-L210 | formalized | — |
| `eval` | [#eval L236](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l236/) | L236-L236 | computed | `V.R323`, `V.R324`, `V.R325`, `V.R326` |
| `eval` | [#eval L237](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l237/) | L237-L237 | computed | — |
| `eval` | [#eval L238](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l238/) | L238-L238 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L240](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l240/) | L240-L240 | computed | — |
| `structure` | [BaryogenesisSAIMechanism](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-saimechanism/) | L257-L272 | defined | `V.D238` |
| `def` | [baryogenesis_sai_mechanism](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-mechanism/) | L275-L280 | defined | — |
| `theorem` | [baryogenesis_sai_thm](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-thm/) | L283-L288 | formalized | — |
| `theorem` | [fifteen_window_product](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/fifteen-window-product/) | L291-L291 | formalized | `V.T179` |
| `theorem` | [five_sixths_structure](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-structure/) | L294-L294 | formalized | `V.T180` |
| `structure` | [BaryogenesisFirstPrinciples](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles/) | L310-L319 | defined | `V.P130` |
| `def` | [baryogenesis_fp](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-fp/) | L322-L322 | defined | — |
| `theorem` | [baryogenesis_first_principles](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles-l325/) | L325-L330 | formalized | — |
| `def` | [sai_mod_comparison](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-comparison/) | L333-L335 | defined | — |
| `def` | [vop2_status_sprint6c](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/vop2-status-sprint6c/) | L338-L341 | defined | `V.R379` |
| `eval` | [#eval L344](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l346/) | L346-L346 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l348/) | L348-L348 | computed | — |
| `structure` | [GeneratorOrbitSuppression](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression/) | L369-L382 | defined | — |
| `def` | [generator_orbit_suppression](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression-l384/) | L384-L385 | defined | — |
| `theorem` | [generator_orbit_produces_15](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-produces-15/) | L388-L393 | formalized | — |
| `theorem` | [fiber_dimension_decomposition](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/fiber-dimension-decomposition/) | L396-L397 | formalized | — |
| `theorem` | [sai_mod_hierarchy](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/sai-mod-hierarchy/) | L402-L403 | formalized | — |
| `structure` | [ThresholdUniquenessFiveSixths](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-five-sixths/) | L420-L433 | defined | — |
| `def` | [threshold_uniqueness_56](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-56/) | L435-L437 | defined | — |
| `theorem` | [five_sixths_uniquely_forced](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-uniquely-forced/) | L440-L445 | formalized | — |
| `theorem` | [five_sixths_cross_check_yp](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-cross-check-yp/) | L448-L449 | formalized | — |
| `theorem` | [threshold_uniqueness_matches_ladder](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-matches-ladder/) | L452-L454 | formalized | — |
| `structure` | [CPAsymmetryFromPolarity](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cpasymmetry-from-polarity/) | L473-L484 | defined | — |
| `def` | [cp_asymmetry_polarity](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-polarity/) | L486-L486 | defined | — |
| `theorem` | [cp_asymmetry_structural](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-structural/) | L489-L493 | formalized | — |
| `eval` | [#eval L496](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l496/) | L496-L496 | computed | — |
| `eval` | [#eval L497](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l497/) | L497-L497 | computed | — |
| `eval` | [#eval L498](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l498/) | L498-L498 | computed | — |
| `eval` | [#eval L499](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l499/) | L499-L501 | computed | — |
