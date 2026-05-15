---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Hartogs.CanonicalBasis",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_slug": "book-ii-hartogs-canonical-basis",
  "book": "BookII",
  "family": "Hartogs",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Hartogs/CanonicalBasis.lean",
  "sha256": "2df6b1e14d05092416310a47b0804eb53cba556cbf8ee3be95db84095e39f0ad",
  "imports": [
    "TauLib.BookII.Hartogs.EvolutionOperator"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Hartogs.L2Space",
    "TauLib.BookII.Hartogs.SheafCoherence"
  ],
  "registry_ids": [
    "II.D45",
    "II.D46",
    "II.P09",
    "II.T31"
  ],
  "declaration_counts": {
    "def": 18,
    "eval": 28,
    "theorem": 9
  },
  "declarations": [
    {
      "kind": "def",
      "name": "cylinder_gen",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/cylinder-gen/",
      "source_line_start": 52,
      "source_line_end": 56,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D46"
      ]
    },
    {
      "kind": "def",
      "name": "cylinder_gen_indicator",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/cylinder-gen-indicator/",
      "source_line_start": 59,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ortho_pair",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/ortho-pair/",
      "source_line_start": 70,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "basis_orthogonality_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-orthogonality-check/",
      "source_line_start": 85,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gen_sum",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/gen-sum/",
      "source_line_start": 108,
      "source_line_end": 120,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "basis_completeness_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-completeness-check/",
      "source_line_start": 124,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "indep_witness",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/indep-witness/",
      "source_line_start": 142,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "basis_independence_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-independence-check/",
      "source_line_start": 157,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_basis_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/canonical-basis-check/",
      "source_line_start": 175,
      "source_line_end": 178,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D45"
      ]
    },
    {
      "kind": "def",
      "name": "count_nonzero_generators",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/count-nonzero-generators/",
      "source_line_start": 186,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T31"
      ]
    },
    {
      "kind": "def",
      "name": "prime_sum",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/prime-sum/",
      "source_line_start": 199,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "finite_spectral_support_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/finite-spectral-support-check/",
      "source_line_start": 211,
      "source_line_end": 222,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T31"
      ]
    },
    {
      "kind": "def",
      "name": "proj_coeff",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-coeff/",
      "source_line_start": 230,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P09"
      ]
    },
    {
      "kind": "def",
      "name": "projection_delta_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/projection-delta-check/",
      "source_line_start": 243,
      "source_line_end": 259,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P09"
      ]
    },
    {
      "kind": "def",
      "name": "projection_recovery_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/projection-recovery-check/",
      "source_line_start": 263,
      "source_line_end": 279,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P09"
      ]
    },
    {
      "kind": "def",
      "name": "bipolar_cylinder_gen",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-cylinder-gen/",
      "source_line_start": 287,
      "source_line_end": 292,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bipolar_channel_orthogonality",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-channel-orthogonality/",
      "source_line_start": 296,
      "source_line_end": 309,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "full_canonical_basis_check",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/full-canonical-basis-check/",
      "source_line_start": 317,
      "source_line_end": 322,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 329,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l330/",
      "source_line_start": 330,
      "source_line_end": 330,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l331/",
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
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l332/",
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
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l335/",
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
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l338/",
      "source_line_start": 338,
      "source_line_end": 338,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l341/",
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
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l350/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l356/",
      "source_line_start": 356,
      "source_line_end": 356,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l360/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l363/",
      "source_line_start": 363,
      "source_line_end": 363,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l364/",
      "source_line_start": 364,
      "source_line_end": 364,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l367/",
      "source_line_start": 367,
      "source_line_end": 367,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l368/",
      "source_line_start": 368,
      "source_line_end": 368,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l369/",
      "source_line_start": 369,
      "source_line_end": 369,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l370/",
      "source_line_start": 370,
      "source_line_end": 370,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l373/",
      "source_line_start": 373,
      "source_line_end": 373,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 374,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l377/",
      "source_line_start": 377,
      "source_line_end": 377,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 380,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "basis_ortho_3_30",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-ortho-3-30/",
      "source_line_start": 387,
      "source_line_end": 388,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D45"
      ]
    },
    {
      "kind": "theorem",
      "name": "basis_complete_3_30",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-complete-3-30/",
      "source_line_start": 391,
      "source_line_end": 392,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D45"
      ]
    },
    {
      "kind": "theorem",
      "name": "basis_indep_4",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-indep-4/",
      "source_line_start": 395,
      "source_line_end": 396,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D45"
      ]
    },
    {
      "kind": "theorem",
      "name": "basis_3_30",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-3-30/",
      "source_line_start": 399,
      "source_line_end": 400,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D45"
      ]
    },
    {
      "kind": "theorem",
      "name": "spectral_support_3_30",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/spectral-support-3-30/",
      "source_line_start": 403,
      "source_line_end": 404,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T31"
      ]
    },
    {
      "kind": "theorem",
      "name": "proj_delta_3",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-delta-3/",
      "source_line_start": 407,
      "source_line_end": 408,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.P09"
      ]
    },
    {
      "kind": "theorem",
      "name": "proj_recovery_3",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-recovery-3/",
      "source_line_start": 411,
      "source_line_end": 412,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.P09"
      ]
    },
    {
      "kind": "theorem",
      "name": "bipolar_ortho_20",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-ortho-20/",
      "source_line_start": 415,
      "source_line_end": 416,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "full_basis_3_20",
      "url": "/corpus/taulib/docs/book-ii-hartogs-canonical-basis/full-basis-3-20/",
      "source_line_start": 419,
      "source_line_end": 422,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean",
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
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Hartogs/CanonicalBasis.lean`
- SHA-256: `2df6b1e14d05092416310a47b0804eb53cba556cbf8ee3be95db84095e39f0ad`

## Registry Links

- `II.D45` — Canonical Holomorphic Basis
- `II.D46` — Cylinder Generator
- `II.P09` — Decomposition Functoriality
- `II.T31` — Finite Spectral Support

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Hartogs.EvolutionOperator`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Hartogs.L2Space`
- `TauLib.BookII.Hartogs.SheafCoherence`

## Declaration Counts

- `def`: 18
- `eval`: 28
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [cylinder_gen](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/cylinder-gen/) | L52-L56 | data/computed value | data/computed value | `II.D46` |
| `def` | [cylinder_gen_indicator](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/cylinder-gen-indicator/) | L59-L62 | data/computed value | data/computed value | — |
| `def` | [ortho_pair](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/ortho-pair/) | L70-L80 | data/computed value | data/computed value | — |
| `def` | [basis_orthogonality_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-orthogonality-check/) | L85-L100 | data/computed value | data/computed value | — |
| `def` | [gen_sum](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/gen-sum/) | L108-L120 | data/computed value | data/computed value | — |
| `def` | [basis_completeness_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-completeness-check/) | L124-L135 | data/computed value | data/computed value | — |
| `def` | [indep_witness](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/indep-witness/) | L142-L153 | data/computed value | data/computed value | — |
| `def` | [basis_independence_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-independence-check/) | L157-L167 | data/computed value | data/computed value | — |
| `def` | [canonical_basis_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/canonical-basis-check/) | L175-L178 | data/computed value | data/computed value | `II.D45` |
| `def` | [count_nonzero_generators](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/count-nonzero-generators/) | L186-L196 | data/computed value | data/computed value | `II.T31` |
| `def` | [prime_sum](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/prime-sum/) | L199-L206 | data/computed value | data/computed value | — |
| `def` | [finite_spectral_support_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/finite-spectral-support-check/) | L211-L222 | data/computed value | data/computed value | `II.T31` |
| `def` | [proj_coeff](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-coeff/) | L230-L239 | data/computed value | data/computed value | `II.P09` |
| `def` | [projection_delta_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/projection-delta-check/) | L243-L259 | data/computed value | data/computed value | `II.P09` |
| `def` | [projection_recovery_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/projection-recovery-check/) | L263-L279 | data/computed value | data/computed value | `II.P09` |
| `def` | [bipolar_cylinder_gen](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-cylinder-gen/) | L287-L292 | data/computed value | data/computed value | — |
| `def` | [bipolar_channel_orthogonality](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-channel-orthogonality/) | L296-L309 | data/computed value | data/computed value | — |
| `def` | [full_canonical_basis_check](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/full-canonical-basis-check/) | L317-L322 | data/computed value | data/computed value | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l329/) | L329-L329 | computed check | computed check | — |
| `eval` | [#eval L330](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l330/) | L330-L330 | computed check | computed check | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l331/) | L331-L331 | computed check | computed check | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l332/) | L332-L332 | computed check | computed check | — |
| `eval` | [#eval L333](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l334/) | L334-L334 | computed check | computed check | — |
| `eval` | [#eval L335](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l335/) | L335-L335 | computed check | computed check | — |
| `eval` | [#eval L338](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l338/) | L338-L338 | computed check | computed check | — |
| `eval` | [#eval L341](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l341/) | L341-L341 | computed check | computed check | — |
| `eval` | [#eval L344](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l344/) | L344-L344 | computed check | computed check | — |
| `eval` | [#eval L347](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l347/) | L347-L347 | computed check | computed check | — |
| `eval` | [#eval L350](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l350/) | L350-L350 | computed check | computed check | — |
| `eval` | [#eval L351](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l351/) | L351-L351 | computed check | computed check | — |
| `eval` | [#eval L352](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l352/) | L352-L352 | computed check | computed check | — |
| `eval` | [#eval L355](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l355/) | L355-L355 | computed check | computed check | — |
| `eval` | [#eval L356](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l356/) | L356-L356 | computed check | computed check | — |
| `eval` | [#eval L357](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l357/) | L357-L357 | computed check | computed check | — |
| `eval` | [#eval L360](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l360/) | L360-L360 | computed check | computed check | — |
| `eval` | [#eval L363](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l363/) | L363-L363 | computed check | computed check | — |
| `eval` | [#eval L364](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l364/) | L364-L364 | computed check | computed check | — |
| `eval` | [#eval L367](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l367/) | L367-L367 | computed check | computed check | — |
| `eval` | [#eval L368](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l368/) | L368-L368 | computed check | computed check | — |
| `eval` | [#eval L369](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l369/) | L369-L369 | computed check | computed check | — |
| `eval` | [#eval L370](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l370/) | L370-L370 | computed check | computed check | — |
| `eval` | [#eval L373](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l373/) | L373-L373 | computed check | computed check | — |
| `eval` | [#eval L374](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l374/) | L374-L374 | computed check | computed check | — |
| `eval` | [#eval L377](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l377/) | L377-L377 | computed check | computed check | — |
| `eval` | [#eval L380](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/eval-l380/) | L380-L380 | computed check | computed check | — |
| `theorem` | [basis_ortho_3_30](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-ortho-3-30/) | L387-L388 | proof obligation | formal proof obligation checked | `II.D45` |
| `theorem` | [basis_complete_3_30](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-complete-3-30/) | L391-L392 | proof obligation | formal proof obligation checked | `II.D45` |
| `theorem` | [basis_indep_4](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-indep-4/) | L395-L396 | proof obligation | formal proof obligation checked | `II.D45` |
| `theorem` | [basis_3_30](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/basis-3-30/) | L399-L400 | proof obligation | formal proof obligation checked | `II.D45` |
| `theorem` | [spectral_support_3_30](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/spectral-support-3-30/) | L403-L404 | proof obligation | formal proof obligation checked | `II.T31` |
| `theorem` | [proj_delta_3](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-delta-3/) | L407-L408 | proof obligation | formal proof obligation checked | `II.P09` |
| `theorem` | [proj_recovery_3](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/proj-recovery-3/) | L411-L412 | proof obligation | formal proof obligation checked | `II.P09` |
| `theorem` | [bipolar_ortho_20](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/bipolar-ortho-20/) | L415-L416 | proof obligation | formal proof obligation checked | — |
| `theorem` | [full_basis_3_20](/corpus/taulib/docs/book-ii-hartogs-canonical-basis/full-basis-3-20/) | L419-L422 | proof obligation | formal proof obligation checked | — |
