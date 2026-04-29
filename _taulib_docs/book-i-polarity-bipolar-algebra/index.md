---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.BipolarAlgebra",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_slug": "book-i-polarity-bipolar-algebra",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/BipolarAlgebra.lean",
  "sha256": "39f08922009110d77f82868c8d66eca08ea5fd27060947591cf975d7e474fd8e",
  "imports": [
    "TauLib.BookI.Polarity.PolarizedGerms",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.SplitComplex",
    "TauLib.BookI.Holomorphy.DHolomorphic",
    "TauLib.BookI.Logic.Explosion",
    "TauLib.BookI.Logic.Truth4",
    "TauLib.BookI.Polarity.Lemniscate",
    "TauLib.BookI.Polarity.SplitComplexCouplingLift",
    "TauLib.BookII.Geometry.CausalStructure",
    "TauLib.BookII.Interior.BipolarDecomposition",
    "TauLib.BookII.Interior.OmegaReadout",
    "TauLib.BookII.Prologue.SplitComplexInterior",
    "TauLib.BookIV.Electroweak.MajoranaStructure"
  ],
  "registry_ids": [
    "I.D27",
    "I.D28",
    "I.T10"
  ],
  "declaration_counts": {
    "def": 18,
    "structure": 3,
    "theorem": 19,
    "eval": 17
  },
  "declarations": [
    {
      "kind": "def",
      "name": "bdry_add",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-add/",
      "source_line_start": 43,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bdry_mul",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-mul/",
      "source_line_start": 44,
      "source_line_end": 44,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bdry_neg",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-neg/",
      "source_line_start": 45,
      "source_line_end": 45,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SplitComplex",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex/",
      "source_line_start": 53,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": [
        "I.D27"
      ]
    },
    {
      "kind": "def",
      "name": "SplitComplex.zero",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/zero/",
      "source_line_start": 61,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.one",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/one/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.j",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/j/",
      "source_line_start": 67,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.add",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/add/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.neg",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/neg/",
      "source_line_start": 74,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.mul",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.sub",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/sub/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "j_squared",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/j-squared/",
      "source_line_start": 91,
      "source_line_end": 92,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorPair",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/sector-pair/",
      "source_line_start": 100,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "I.D27"
      ]
    },
    {
      "kind": "def",
      "name": "to_sectors",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/to-sectors/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.add",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/add-l110/",
      "source_line_start": 110,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.mul",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul-l114/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sectors_add",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/sectors-add/",
      "source_line_start": 118,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sectors_mul",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/sectors-mul/",
      "source_line_start": 125,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_plus_sector",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-sector/",
      "source_line_start": 137,
      "source_line_end": 137,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_minus_sector",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-sector/",
      "source_line_start": 140,
      "source_line_end": 140,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_plus_idem",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-idem/",
      "source_line_start": 143,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_minus_idem",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-idem/",
      "source_line_start": 147,
      "source_line_end": 148,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_orthogonal",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-orthogonal/",
      "source_line_start": 151,
      "source_line_end": 153,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_partition",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-partition/",
      "source_line_start": 156,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GaussInt",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/gauss-int/",
      "source_line_start": 166,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GaussInt.mul",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul-l173/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "GaussInt.ext",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/ext/",
      "source_line_start": 177,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_no_zero_div",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/int-no-zero-div/",
      "source_line_start": 181,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_elliptic_idempotent",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/no-elliptic-idempotent/",
      "source_line_start": 201,
      "source_line_end": 224,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T10"
      ]
    },
    {
      "kind": "theorem",
      "name": "split_complex_forced",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex-forced/",
      "source_line_start": 229,
      "source_line_end": 237,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T10"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_inv",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv/",
      "source_line_start": 244,
      "source_line_end": 244,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_squared",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-squared/",
      "source_line_start": 247,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_fixes_real",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-fixes-real/",
      "source_line_start": 252,
      "source_line_end": 254,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_j",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-j/",
      "source_line_start": 257,
      "source_line_end": 259,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_swaps_sectors",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-swaps-sectors/",
      "source_line_start": 262,
      "source_line_end": 266,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_split",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split/",
      "source_line_start": 278,
      "source_line_end": 281,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_idempotent",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-idempotent/",
      "source_line_start": 284,
      "source_line_end": 291,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_of_b",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-b/",
      "source_line_start": 294,
      "source_line_end": 296,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_of_c",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-c/",
      "source_line_start": 299,
      "source_line_end": 301,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_orthogonal",
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-orthogonal/",
      "source_line_start": 305,
      "source_line_end": 309,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 344,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean",
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
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/BipolarAlgebra.lean`
- SHA-256: `39f08922009110d77f82868c8d66eca08ea5fd27060947591cf975d7e474fd8e`

## Registry Links

- `I.D27` — Bipolar Spectral Algebra
- `I.D28` — Boundary Local Ring
- `I.T10` — Split-Complex Forced

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.PolarizedGerms`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.SplitComplex`
- `TauLib.BookI.Holomorphy.DHolomorphic`
- `TauLib.BookI.Logic.Explosion`
- `TauLib.BookI.Logic.Truth4`
- `TauLib.BookI.Polarity.Lemniscate`
- `TauLib.BookI.Polarity.SplitComplexCouplingLift`
- `TauLib.BookII.Geometry.CausalStructure`
- `TauLib.BookII.Interior.BipolarDecomposition`
- `TauLib.BookII.Interior.OmegaReadout`
- `TauLib.BookII.Prologue.SplitComplexInterior`
- `TauLib.BookIV.Electroweak.MajoranaStructure`

## Declaration Counts

- `def`: 18
- `eval`: 17
- `structure`: 3
- `theorem`: 19

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [bdry_add](/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-add/) | L43-L43 | defined | — |
| `def` | [bdry_mul](/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-mul/) | L44-L44 | defined | — |
| `def` | [bdry_neg](/verify/taulib/docs/book-i-polarity-bipolar-algebra/bdry-neg/) | L45-L45 | defined | — |
| `structure` | [SplitComplex](/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex/) | L53-L58 | defined | `I.D27` |
| `def` | [SplitComplex.zero](/verify/taulib/docs/book-i-polarity-bipolar-algebra/zero/) | L61-L61 | defined | — |
| `def` | [SplitComplex.one](/verify/taulib/docs/book-i-polarity-bipolar-algebra/one/) | L64-L64 | defined | — |
| `def` | [SplitComplex.j](/verify/taulib/docs/book-i-polarity-bipolar-algebra/j/) | L67-L67 | defined | — |
| `def` | [SplitComplex.add](/verify/taulib/docs/book-i-polarity-bipolar-algebra/add/) | L70-L71 | defined | — |
| `def` | [SplitComplex.neg](/verify/taulib/docs/book-i-polarity-bipolar-algebra/neg/) | L74-L75 | defined | — |
| `def` | [SplitComplex.mul](/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul/) | L79-L80 | defined | — |
| `def` | [SplitComplex.sub](/verify/taulib/docs/book-i-polarity-bipolar-algebra/sub/) | L83-L84 | defined | — |
| `theorem` | [j_squared](/verify/taulib/docs/book-i-polarity-bipolar-algebra/j-squared/) | L91-L92 | formalized | — |
| `structure` | [SectorPair](/verify/taulib/docs/book-i-polarity-bipolar-algebra/sector-pair/) | L100-L103 | defined | `I.D27` |
| `def` | [to_sectors](/verify/taulib/docs/book-i-polarity-bipolar-algebra/to-sectors/) | L106-L107 | defined | — |
| `def` | [SectorPair.add](/verify/taulib/docs/book-i-polarity-bipolar-algebra/add-l110/) | L110-L111 | defined | — |
| `def` | [SectorPair.mul](/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul-l114/) | L114-L115 | defined | — |
| `theorem` | [sectors_add](/verify/taulib/docs/book-i-polarity-bipolar-algebra/sectors-add/) | L118-L122 | formalized | — |
| `theorem` | [sectors_mul](/verify/taulib/docs/book-i-polarity-bipolar-algebra/sectors-mul/) | L125-L129 | formalized | — |
| `def` | [e_plus_sector](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-sector/) | L137-L137 | defined | — |
| `def` | [e_minus_sector](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-sector/) | L140-L140 | defined | — |
| `theorem` | [e_plus_idem](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-idem/) | L143-L144 | formalized | — |
| `theorem` | [e_minus_idem](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-idem/) | L147-L148 | formalized | — |
| `theorem` | [e_orthogonal](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-orthogonal/) | L151-L153 | formalized | — |
| `theorem` | [e_partition](/verify/taulib/docs/book-i-polarity-bipolar-algebra/e-partition/) | L156-L158 | formalized | — |
| `structure` | [GaussInt](/verify/taulib/docs/book-i-polarity-bipolar-algebra/gauss-int/) | L166-L169 | defined | — |
| `def` | [GaussInt.mul](/verify/taulib/docs/book-i-polarity-bipolar-algebra/mul-l173/) | L173-L176 | defined | — |
| `theorem` | [GaussInt.ext](/verify/taulib/docs/book-i-polarity-bipolar-algebra/ext/) | L177-L178 | formalized | — |
| `theorem` | [int_no_zero_div](/verify/taulib/docs/book-i-polarity-bipolar-algebra/int-no-zero-div/) | L181-L191 | formalized | — |
| `theorem` | [no_elliptic_idempotent](/verify/taulib/docs/book-i-polarity-bipolar-algebra/no-elliptic-idempotent/) | L201-L224 | formalized | `I.T10` |
| `theorem` | [split_complex_forced](/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex-forced/) | L229-L237 | formalized | `I.T10` |
| `def` | [polarity_inv](/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv/) | L244-L244 | defined | — |
| `theorem` | [polarity_inv_squared](/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-squared/) | L247-L249 | formalized | — |
| `theorem` | [polarity_inv_fixes_real](/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-fixes-real/) | L252-L254 | formalized | — |
| `theorem` | [polarity_inv_j](/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-j/) | L257-L259 | formalized | — |
| `theorem` | [polarity_inv_swaps_sectors](/verify/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-swaps-sectors/) | L262-L266 | formalized | — |
| `def` | [chi_split](/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split/) | L278-L281 | defined | — |
| `theorem` | [chi_split_idempotent](/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-idempotent/) | L284-L291 | formalized | — |
| `theorem` | [chi_split_of_b](/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-b/) | L294-L296 | formalized | — |
| `theorem` | [chi_split_of_c](/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-c/) | L299-L301 | formalized | — |
| `theorem` | [chi_split_orthogonal](/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-orthogonal/) | L305-L309 | formalized | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L318](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l318/) | L318-L318 | computed | — |
| `eval` | [#eval L321](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l321/) | L321-L321 | computed | — |
| `eval` | [#eval L322](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l322/) | L322-L322 | computed | — |
| `eval` | [#eval L325](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l325/) | L325-L325 | computed | — |
| `eval` | [#eval L326](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l326/) | L326-L326 | computed | — |
| `eval` | [#eval L327](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l327/) | L327-L327 | computed | — |
| `eval` | [#eval L328](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l328/) | L328-L328 | computed | — |
| `eval` | [#eval L331](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l331/) | L331-L331 | computed | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L339](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l339/) | L339-L339 | computed | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-i-polarity-bipolar-algebra/eval-l342/) | L342-L344 | computed | — |
