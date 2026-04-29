---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Mirror.WaveHolomorphy",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_slug": "book-ii-mirror-wave-holomorphy",
  "book": "BookII",
  "family": "Mirror",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Mirror/WaveHolomorphy.lean",
  "sha256": "689363a5674a9b6dbe44455d4268ff7c5a639604979df326379b263a09ae0cb0",
  "imports": [
    "TauLib.BookII.Mirror.SignClassification"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Mirror.Inventory"
  ],
  "registry_ids": [
    "II.D70",
    "II.D71",
    "II.T44",
    "II.T45"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 4,
    "def": 10,
    "theorem": 26,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "PDEType",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pdetype/",
      "source_line_start": 57,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "structure",
      "name": "PDEClassification",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pdeclassification/",
      "source_line_start": 65,
      "source_line_end": 71,
      "formal_status": "defined",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "def",
      "name": "elliptic_classification",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/elliptic-classification/",
      "source_line_start": 74,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "def",
      "name": "hyperbolic_classification",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hyperbolic-classification/",
      "source_line_start": 82,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "theorem",
      "name": "hyperbolic_hartogs_natural",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hyperbolic-hartogs-natural/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "elliptic_hartogs_not_natural",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/elliptic-hartogs-not-natural/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "asymmetric_determination",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/asymmetric-determination/",
      "source_line_start": 103,
      "source_line_end": 106,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "max_principle_asymmetry",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-principle-asymmetry/",
      "source_line_start": 110,
      "source_line_end": 113,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "pde_classifications_distinct",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pde-classifications-distinct/",
      "source_line_start": 116,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "characteristics_iff_hyperbolic",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/characteristics-iff-hyperbolic/",
      "source_line_start": 124,
      "source_line_end": 127,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "structure",
      "name": "StageGeometry",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-geometry/",
      "source_line_start": 135,
      "source_line_end": 139,
      "formal_status": "defined",
      "registry_ids": [
        "II.D71"
      ]
    },
    {
      "kind": "def",
      "name": "default_stage_geometry",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/default-stage-geometry/",
      "source_line_start": 142,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "stage_euclidean_check",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean-check/",
      "source_line_start": 149,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": [
        "II.D71"
      ]
    },
    {
      "kind": "def",
      "name": "all_stages_euclidean",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/all-stages-euclidean/",
      "source_line_start": 154,
      "source_line_end": 161,
      "formal_status": "defined",
      "registry_ids": [
        "II.D71"
      ]
    },
    {
      "kind": "theorem",
      "name": "stage_no_light_cones",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-no-light-cones/",
      "source_line_start": 168,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "stage_euclidean",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean/",
      "source_line_start": 172,
      "source_line_end": 173,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "stage_euclidean_check_true",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean-check-true/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_stages_euclidean_5",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/all-stages-euclidean-5/",
      "source_line_start": 181,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "stage_size_is_primorial",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-size-is-primorial/",
      "source_line_start": 185,
      "source_line_end": 186,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "structure",
      "name": "SCFun",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/scfun/",
      "source_line_start": 193,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SCFun.b_sector",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/b-sector/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SCFun.c_sector",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector/",
      "source_line_start": 202,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "wave_decompose_check",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-decompose-check/",
      "source_line_start": 209,
      "source_line_end": 212,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SCFun.wave_check",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-check/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wave_decompose_exact",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-decompose-exact/",
      "source_line_start": 219,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wave_check_always_true",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-check-always-true/",
      "source_line_start": 225,
      "source_line_end": 229,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_additive",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/sector-additive/",
      "source_line_start": 233,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "theorem",
      "name": "c_sector_additive",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector-additive/",
      "source_line_start": 239,
      "source_line_end": 242,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "b_sector_multiplicative",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/b-sector-multiplicative/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D70"
      ]
    },
    {
      "kind": "theorem",
      "name": "c_sector_multiplicative",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector-multiplicative/",
      "source_line_start": 252,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MirrorSummary",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/mirror-summary/",
      "source_line_start": 262,
      "source_line_end": 266,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mirror_summary",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/mirror-summary-l269/",
      "source_line_start": 269,
      "source_line_end": 272,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "both_unique_continuation",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/both-unique-continuation/",
      "source_line_start": 275,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l289/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l290/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l297/",
      "source_line_start": 297,
      "source_line_end": 297,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l304/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "hartogs_natural_hyp",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hartogs-natural-hyp/",
      "source_line_start": 311,
      "source_line_end": 312,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "hartogs_not_natural_ell",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hartogs-not-natural-ell/",
      "source_line_start": 314,
      "source_line_end": 315,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chars_hyp",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/chars-hyp/",
      "source_line_start": 318,
      "source_line_end": 319,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "chars_ell",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/chars-ell/",
      "source_line_start": 321,
      "source_line_end": 322,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "max_hyp",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-hyp/",
      "source_line_start": 325,
      "source_line_end": 326,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T44"
      ]
    },
    {
      "kind": "theorem",
      "name": "max_ell",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-ell/",
      "source_line_start": 328,
      "source_line_end": 329,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "stages_euclidean_5",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stages-euclidean-5/",
      "source_line_start": 332,
      "source_line_end": 333,
      "formal_status": "formalized",
      "registry_ids": [
        "II.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "pde_distinct",
      "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pde-distinct/",
      "source_line_start": 336,
      "source_line_end": 342,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D70"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean",
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
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Mirror/WaveHolomorphy.lean`
- SHA-256: `689363a5674a9b6dbe44455d4268ff7c5a639604979df326379b263a09ae0cb0`

## Registry Links

- `II.D70` — PDE Type Classification
- `II.D71` — Stage-Finite Euclidean Geometry
- `II.T44` — Asymmetric Determination
- `II.T45` — Parallel Preservation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Mirror.SignClassification`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Mirror.Inventory`

## Declaration Counts

- `def`: 10
- `eval`: 14
- `inductive`: 1
- `structure`: 4
- `theorem`: 26

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [PDEType](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pdetype/) | L57-L62 | defined | `II.D70` |
| `structure` | [PDEClassification](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pdeclassification/) | L65-L71 | defined | `II.D70` |
| `def` | [elliptic_classification](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/elliptic-classification/) | L74-L79 | defined | `II.D70` |
| `def` | [hyperbolic_classification](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hyperbolic-classification/) | L82-L87 | defined | `II.D70` |
| `theorem` | [hyperbolic_hartogs_natural](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hyperbolic-hartogs-natural/) | L94-L95 | formalized | `II.T44` |
| `theorem` | [elliptic_hartogs_not_natural](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/elliptic-hartogs-not-natural/) | L98-L99 | formalized | `II.T44` |
| `theorem` | [asymmetric_determination](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/asymmetric-determination/) | L103-L106 | formalized | `II.T44` |
| `theorem` | [max_principle_asymmetry](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-principle-asymmetry/) | L110-L113 | formalized | `II.T44` |
| `theorem` | [pde_classifications_distinct](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pde-classifications-distinct/) | L116-L121 | formalized | `II.T44` |
| `theorem` | [characteristics_iff_hyperbolic](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/characteristics-iff-hyperbolic/) | L124-L127 | formalized | `II.T44` |
| `structure` | [StageGeometry](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-geometry/) | L135-L139 | defined | `II.D71` |
| `def` | [default_stage_geometry](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/default-stage-geometry/) | L142-L145 | defined | — |
| `def` | [stage_euclidean_check](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean-check/) | L149-L151 | defined | `II.D71` |
| `def` | [all_stages_euclidean](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/all-stages-euclidean/) | L154-L161 | defined | `II.D71` |
| `theorem` | [stage_no_light_cones](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-no-light-cones/) | L168-L169 | formalized | `II.T45` |
| `theorem` | [stage_euclidean](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean/) | L172-L173 | formalized | `II.T45` |
| `theorem` | [stage_euclidean_check_true](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean-check-true/) | L176-L178 | formalized | `II.T45` |
| `theorem` | [all_stages_euclidean_5](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/all-stages-euclidean-5/) | L181-L182 | formalized | `II.T45` |
| `theorem` | [stage_size_is_primorial](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-size-is-primorial/) | L185-L186 | formalized | `II.T45` |
| `structure` | [SCFun](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/scfun/) | L193-L195 | defined | — |
| `def` | [SCFun.b_sector](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/b-sector/) | L198-L199 | defined | — |
| `def` | [SCFun.c_sector](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector/) | L202-L203 | defined | — |
| `def` | [wave_decompose_check](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-decompose-check/) | L209-L212 | defined | — |
| `def` | [SCFun.wave_check](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-check/) | L215-L216 | defined | — |
| `theorem` | [wave_decompose_exact](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-decompose-exact/) | L219-L222 | formalized | — |
| `theorem` | [wave_check_always_true](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/wave-check-always-true/) | L225-L229 | formalized | — |
| `theorem` | [sector_additive](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/sector-additive/) | L233-L236 | formalized | `II.D70` |
| `theorem` | [c_sector_additive](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector-additive/) | L239-L242 | formalized | — |
| `theorem` | [b_sector_multiplicative](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/b-sector-multiplicative/) | L246-L249 | formalized | `II.D70` |
| `theorem` | [c_sector_multiplicative](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/c-sector-multiplicative/) | L252-L255 | formalized | — |
| `structure` | [MirrorSummary](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/mirror-summary/) | L262-L266 | defined | — |
| `def` | [mirror_summary](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/mirror-summary-l269/) | L269-L272 | defined | — |
| `theorem` | [both_unique_continuation](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/both-unique-continuation/) | L275-L276 | formalized | — |
| `eval` | [#eval L283](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l283/) | L283-L283 | computed | — |
| `eval` | [#eval L284](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l284/) | L284-L284 | computed | — |
| `eval` | [#eval L287](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l287/) | L287-L287 | computed | — |
| `eval` | [#eval L288](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l288/) | L288-L288 | computed | — |
| `eval` | [#eval L289](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l289/) | L289-L289 | computed | — |
| `eval` | [#eval L290](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l290/) | L290-L290 | computed | — |
| `eval` | [#eval L291](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l291/) | L291-L291 | computed | — |
| `eval` | [#eval L292](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l292/) | L292-L292 | computed | — |
| `eval` | [#eval L295](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l295/) | L295-L295 | computed | — |
| `eval` | [#eval L296](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l296/) | L296-L296 | computed | — |
| `eval` | [#eval L297](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l297/) | L297-L297 | computed | — |
| `eval` | [#eval L300](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l300/) | L300-L300 | computed | — |
| `eval` | [#eval L301](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l301/) | L301-L301 | computed | — |
| `eval` | [#eval L304](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/eval-l304/) | L304-L304 | computed | — |
| `theorem` | [hartogs_natural_hyp](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hartogs-natural-hyp/) | L311-L312 | formalized | `II.T44` |
| `theorem` | [hartogs_not_natural_ell](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/hartogs-not-natural-ell/) | L314-L315 | formalized | — |
| `theorem` | [chars_hyp](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/chars-hyp/) | L318-L319 | formalized | `II.T44` |
| `theorem` | [chars_ell](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/chars-ell/) | L321-L322 | formalized | — |
| `theorem` | [max_hyp](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-hyp/) | L325-L326 | formalized | `II.T44` |
| `theorem` | [max_ell](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/max-ell/) | L328-L329 | formalized | — |
| `theorem` | [stages_euclidean_5](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stages-euclidean-5/) | L332-L333 | formalized | `II.T45` |
| `theorem` | [pde_distinct](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pde-distinct/) | L336-L342 | formalized | `II.D70` |
