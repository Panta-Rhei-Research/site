---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.BipolarAlgebra",
  "permalink": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/",
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
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-add/",
      "source_line_start": 43,
      "source_line_end": 43,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bdry_mul",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-mul/",
      "source_line_start": 44,
      "source_line_end": 44,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bdry_neg",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-neg/",
      "source_line_start": 45,
      "source_line_end": 45,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SplitComplex",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/split-complex/",
      "source_line_start": 53,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D27"
      ]
    },
    {
      "kind": "def",
      "name": "SplitComplex.zero",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/zero/",
      "source_line_start": 61,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.one",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/one/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.j",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/j/",
      "source_line_start": 67,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.add",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/add/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.neg",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/neg/",
      "source_line_start": 74,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.mul",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SplitComplex.sub",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sub/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "j_squared",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/j-squared/",
      "source_line_start": 91,
      "source_line_end": 92,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorPair",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sector-pair/",
      "source_line_start": 100,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D27"
      ]
    },
    {
      "kind": "def",
      "name": "to_sectors",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/to-sectors/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.add",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/add-l110/",
      "source_line_start": 110,
      "source_line_end": 111,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.mul",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul-l114/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sectors_add",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sectors-add/",
      "source_line_start": 118,
      "source_line_end": 122,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sectors_mul",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sectors-mul/",
      "source_line_start": 125,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_plus_sector",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-sector/",
      "source_line_start": 137,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_minus_sector",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-sector/",
      "source_line_start": 140,
      "source_line_end": 140,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_plus_idem",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-idem/",
      "source_line_start": 143,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_minus_idem",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-idem/",
      "source_line_start": 147,
      "source_line_end": 148,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_orthogonal",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-orthogonal/",
      "source_line_start": 151,
      "source_line_end": 153,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e_partition",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-partition/",
      "source_line_start": 156,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GaussInt",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/gauss-int/",
      "source_line_start": 166,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GaussInt.mul",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul-l173/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "GaussInt.ext",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/ext/",
      "source_line_start": 177,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_no_zero_div",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/int-no-zero-div/",
      "source_line_start": 181,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_elliptic_idempotent",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/no-elliptic-idempotent/",
      "source_line_start": 201,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T10"
      ]
    },
    {
      "kind": "theorem",
      "name": "split_complex_forced",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/split-complex-forced/",
      "source_line_start": 229,
      "source_line_end": 237,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T10"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_inv",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv/",
      "source_line_start": 244,
      "source_line_end": 244,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_squared",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-squared/",
      "source_line_start": 247,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_fixes_real",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-fixes-real/",
      "source_line_start": 252,
      "source_line_end": 254,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_j",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-j/",
      "source_line_start": 257,
      "source_line_end": 259,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_inv_swaps_sectors",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-swaps-sectors/",
      "source_line_start": 262,
      "source_line_end": 266,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_split",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split/",
      "source_line_start": 278,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_idempotent",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-idempotent/",
      "source_line_start": 284,
      "source_line_end": 291,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_of_b",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-b/",
      "source_line_start": 294,
      "source_line_end": 296,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_of_c",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-c/",
      "source_line_start": 299,
      "source_line_end": 301,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_orthogonal",
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-orthogonal/",
      "source_line_start": 305,
      "source_line_end": 309,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 344,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [bdry_add](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-add/) | L43-L43 | definition | definition | — |
| `def` | [bdry_mul](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-mul/) | L44-L44 | definition | definition | — |
| `def` | [bdry_neg](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/bdry-neg/) | L45-L45 | definition | definition | — |
| `structure` | [SplitComplex](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/split-complex/) | L53-L58 | type/data schema | type/data schema | `I.D27` |
| `def` | [SplitComplex.zero](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/zero/) | L61-L61 | definition | definition | — |
| `def` | [SplitComplex.one](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/one/) | L64-L64 | definition | definition | — |
| `def` | [SplitComplex.j](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/j/) | L67-L67 | definition | definition | — |
| `def` | [SplitComplex.add](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/add/) | L70-L71 | definition | definition | — |
| `def` | [SplitComplex.neg](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/neg/) | L74-L75 | definition | definition | — |
| `def` | [SplitComplex.mul](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul/) | L79-L80 | definition | definition | — |
| `def` | [SplitComplex.sub](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sub/) | L83-L84 | definition | definition | — |
| `theorem` | [j_squared](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/j-squared/) | L91-L92 | proof obligation | formal proof obligation checked | — |
| `structure` | [SectorPair](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sector-pair/) | L100-L103 | type/data schema | type/data schema | `I.D27` |
| `def` | [to_sectors](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/to-sectors/) | L106-L107 | definition | definition | — |
| `def` | [SectorPair.add](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/add-l110/) | L110-L111 | definition | definition | — |
| `def` | [SectorPair.mul](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul-l114/) | L114-L115 | definition | definition | — |
| `theorem` | [sectors_add](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sectors-add/) | L118-L122 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sectors_mul](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/sectors-mul/) | L125-L129 | proof obligation | formal proof obligation checked | — |
| `def` | [e_plus_sector](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-sector/) | L137-L137 | definition | definition | — |
| `def` | [e_minus_sector](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-sector/) | L140-L140 | definition | definition | — |
| `theorem` | [e_plus_idem](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-plus-idem/) | L143-L144 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e_minus_idem](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-idem/) | L147-L148 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e_orthogonal](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-orthogonal/) | L151-L153 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e_partition](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-partition/) | L156-L158 | proof obligation | formal proof obligation checked | — |
| `structure` | [GaussInt](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/gauss-int/) | L166-L169 | type/data schema | type/data schema | — |
| `def` | [GaussInt.mul](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/mul-l173/) | L173-L176 | definition | definition | — |
| `theorem` | [GaussInt.ext](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/ext/) | L177-L178 | proof obligation | formal proof obligation checked | — |
| `theorem` | [int_no_zero_div](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/int-no-zero-div/) | L181-L191 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_elliptic_idempotent](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/no-elliptic-idempotent/) | L201-L224 | proof obligation | formal proof obligation checked | `I.T10` |
| `theorem` | [split_complex_forced](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/split-complex-forced/) | L229-L237 | proof obligation | formal proof obligation checked | `I.T10` |
| `def` | [polarity_inv](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv/) | L244-L244 | definition | definition | — |
| `theorem` | [polarity_inv_squared](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-squared/) | L247-L249 | proof obligation | formal proof obligation checked | — |
| `theorem` | [polarity_inv_fixes_real](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-fixes-real/) | L252-L254 | proof obligation | formal proof obligation checked | — |
| `theorem` | [polarity_inv_j](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-j/) | L257-L259 | proof obligation | formal proof obligation checked | — |
| `theorem` | [polarity_inv_swaps_sectors](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/polarity-inv-swaps-sectors/) | L262-L266 | proof obligation | formal proof obligation checked | — |
| `def` | [chi_split](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split/) | L278-L281 | definition | definition | — |
| `theorem` | [chi_split_idempotent](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-idempotent/) | L284-L291 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_split_of_b](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-b/) | L294-L296 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_split_of_c](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-of-c/) | L299-L301 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_split_orthogonal](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/chi-split-orthogonal/) | L305-L309 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L317](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l317/) | L317-L317 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l318/) | L318-L318 | computed check | computed check | — |
| `eval` | [#eval L321](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l321/) | L321-L321 | computed check | computed check | — |
| `eval` | [#eval L322](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l322/) | L322-L322 | computed check | computed check | — |
| `eval` | [#eval L325](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l325/) | L325-L325 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l327/) | L327-L327 | computed check | computed check | — |
| `eval` | [#eval L328](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l328/) | L328-L328 | computed check | computed check | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l331/) | L331-L331 | computed check | computed check | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l332/) | L332-L332 | computed check | computed check | — |
| `eval` | [#eval L335](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l335/) | L335-L335 | computed check | computed check | — |
| `eval` | [#eval L336](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l336/) | L336-L336 | computed check | computed check | — |
| `eval` | [#eval L339](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l339/) | L339-L339 | computed check | computed check | — |
| `eval` | [#eval L340](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l340/) | L340-L340 | computed check | computed check | — |
| `eval` | [#eval L341](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l341/) | L341-L341 | computed check | computed check | — |
| `eval` | [#eval L342](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/eval-l342/) | L342-L344 | computed check | computed check | — |
