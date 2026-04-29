---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.SplitComplex",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.SplitComplex`.",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_slug": "book-i-boundary-split-complex",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/SplitComplex.lean",
  "sha256": "85d58abbeffd44a2166367786faf3b127dd450fe6c6fbec305a14cf43b5d4452",
  "imports": [
    "TauLib.BookI.Polarity.BipolarAlgebra",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Characters",
    "TauLib.BookI.Boundary.ComplexField",
    "TauLib.BookI.Boundary.Iota",
    "TauLib.BookI.Holomorphy.DHolomorphic",
    "TauLib.BookII.Geometry.CausalStructure",
    "TauLib.BookII.Interior.BipolarDecomposition",
    "TauLib.BookII.Prologue.SplitComplexInterior",
    "TauLib.BookII.Transcendentals.JReplacesI",
    "TauLib.Tour.CentralTheorem",
    "TauLib.Tour.GuidedTour.BookI",
    "TauLib.Tour.GuidedTour.BookII"
  ],
  "registry_ids": [
    "I.D27",
    "I.T10"
  ],
  "declaration_counts": {
    "theorem": 31,
    "def": 4,
    "example": 9,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "SplitComplex.ext",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/ext/",
      "source_line_start": 37,
      "source_line_end": 39,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_add_comm",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-add-comm/",
      "source_line_start": 46,
      "source_line_end": 48,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_add_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-add-assoc/",
      "source_line_start": 51,
      "source_line_end": 54,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_add_zero",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-add-zero/",
      "source_line_start": 57,
      "source_line_end": 59,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_add_neg",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-add-neg/",
      "source_line_start": 62,
      "source_line_end": 64,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_mul_comm",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-comm/",
      "source_line_start": 67,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_mul_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-assoc/",
      "source_line_start": 72,
      "source_line_end": 75,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_mul_one",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-one/",
      "source_line_start": 78,
      "source_line_end": 80,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_left_distrib",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-left-distrib/",
      "source_line_start": 83,
      "source_line_end": 86,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sc_ring_axioms",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sc-ring-axioms/",
      "source_line_start": 89,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "SectorPair.ext",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/ext-l109/",
      "source_line_start": 109,
      "source_line_end": 112,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.zero",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/zero/",
      "source_line_start": 119,
      "source_line_end": 119,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.one",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/one/",
      "source_line_start": 122,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPair.neg",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/neg/",
      "source_line_start": 125,
      "source_line_end": 126,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_add_comm",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-add-comm/",
      "source_line_start": 129,
      "source_line_end": 131,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_add_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-add-assoc/",
      "source_line_start": 134,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_add_zero",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-add-zero/",
      "source_line_start": 140,
      "source_line_end": 142,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_add_neg",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-add-neg/",
      "source_line_start": 145,
      "source_line_end": 147,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_mul_comm",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-comm/",
      "source_line_start": 150,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_mul_assoc",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-assoc/",
      "source_line_start": 155,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_mul_one",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-one/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_left_distrib",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-left-distrib/",
      "source_line_start": 166,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_ring_axioms",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/sp-ring-axioms/",
      "source_line_start": 172,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "from_sectors",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/from-sectors/",
      "source_line_start": 196,
      "source_line_end": 197,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_injective",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-injective/",
      "source_line_start": 200,
      "source_line_end": 206,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "from_sectors_left_inv",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/from-sectors-left-inv/",
      "source_line_start": 209,
      "source_line_end": 212,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_surj_on_image",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-surj-on-image/",
      "source_line_start": 216,
      "source_line_end": 224,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_parity",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-parity/",
      "source_line_start": 227,
      "source_line_end": 233,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_zero",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-zero/",
      "source_line_start": 240,
      "source_line_end": 242,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_one",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-one/",
      "source_line_start": 245,
      "source_line_end": 247,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "to_sectors_neg",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-neg/",
      "source_line_start": 250,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_divisor_sector",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-sector/",
      "source_line_start": 267,
      "source_line_end": 278,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_divisor_witness_b",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-witness-b/",
      "source_line_start": 282,
      "source_line_end": 286,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_divisor_witness_c",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-witness-c/",
      "source_line_start": 288,
      "source_line_end": 292,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_divisors_iff",
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisors-iff/",
      "source_line_start": 295,
      "source_line_end": 314,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/example-l333/",
      "source_line_start": 333,
      "source_line_end": 334,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-split-complex/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 348,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean",
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
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/SplitComplex.lean`
- SHA-256: `85d58abbeffd44a2166367786faf3b127dd450fe6c6fbec305a14cf43b5d4452`

## Registry Links

- `I.D27` — Bipolar Spectral Algebra
- `I.T10` — Split-Complex Forced

## Construction Spine Links

- [Build the τ-Kernel](/corpus/construction-spine/build-the-kernel/)

## Imports

- `TauLib.BookI.Polarity.BipolarAlgebra`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Characters`
- `TauLib.BookI.Boundary.ComplexField`
- `TauLib.BookI.Boundary.Iota`
- `TauLib.BookI.Holomorphy.DHolomorphic`
- `TauLib.BookII.Geometry.CausalStructure`
- `TauLib.BookII.Interior.BipolarDecomposition`
- `TauLib.BookII.Prologue.SplitComplexInterior`
- `TauLib.BookII.Transcendentals.JReplacesI`
- `TauLib.Tour.CentralTheorem`
- `TauLib.Tour.GuidedTour.BookI`
- `TauLib.Tour.GuidedTour.BookII`

## Declaration Counts

- `def`: 4
- `eval`: 7
- `example`: 9
- `theorem`: 31

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [SplitComplex.ext](/verify/taulib/docs/book-i-boundary-split-complex/ext/) | L37-L39 | formalized | — |
| `theorem` | [sc_add_comm](/verify/taulib/docs/book-i-boundary-split-complex/sc-add-comm/) | L46-L48 | formalized | — |
| `theorem` | [sc_add_assoc](/verify/taulib/docs/book-i-boundary-split-complex/sc-add-assoc/) | L51-L54 | formalized | — |
| `theorem` | [sc_add_zero](/verify/taulib/docs/book-i-boundary-split-complex/sc-add-zero/) | L57-L59 | formalized | — |
| `theorem` | [sc_add_neg](/verify/taulib/docs/book-i-boundary-split-complex/sc-add-neg/) | L62-L64 | formalized | — |
| `theorem` | [sc_mul_comm](/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-comm/) | L67-L69 | formalized | — |
| `theorem` | [sc_mul_assoc](/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-assoc/) | L72-L75 | formalized | — |
| `theorem` | [sc_mul_one](/verify/taulib/docs/book-i-boundary-split-complex/sc-mul-one/) | L78-L80 | formalized | — |
| `theorem` | [sc_left_distrib](/verify/taulib/docs/book-i-boundary-split-complex/sc-left-distrib/) | L83-L86 | formalized | — |
| `theorem` | [sc_ring_axioms](/verify/taulib/docs/book-i-boundary-split-complex/sc-ring-axioms/) | L89-L108 | formalized | — |
| `theorem` | [SectorPair.ext](/verify/taulib/docs/book-i-boundary-split-complex/ext-l109/) | L109-L112 | formalized | — |
| `def` | [SectorPair.zero](/verify/taulib/docs/book-i-boundary-split-complex/zero/) | L119-L119 | defined | — |
| `def` | [SectorPair.one](/verify/taulib/docs/book-i-boundary-split-complex/one/) | L122-L122 | defined | — |
| `def` | [SectorPair.neg](/verify/taulib/docs/book-i-boundary-split-complex/neg/) | L125-L126 | defined | — |
| `theorem` | [sp_add_comm](/verify/taulib/docs/book-i-boundary-split-complex/sp-add-comm/) | L129-L131 | formalized | — |
| `theorem` | [sp_add_assoc](/verify/taulib/docs/book-i-boundary-split-complex/sp-add-assoc/) | L134-L137 | formalized | — |
| `theorem` | [sp_add_zero](/verify/taulib/docs/book-i-boundary-split-complex/sp-add-zero/) | L140-L142 | formalized | — |
| `theorem` | [sp_add_neg](/verify/taulib/docs/book-i-boundary-split-complex/sp-add-neg/) | L145-L147 | formalized | — |
| `theorem` | [sp_mul_comm](/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-comm/) | L150-L152 | formalized | — |
| `theorem` | [sp_mul_assoc](/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-assoc/) | L155-L158 | formalized | — |
| `theorem` | [sp_mul_one](/verify/taulib/docs/book-i-boundary-split-complex/sp-mul-one/) | L161-L163 | formalized | — |
| `theorem` | [sp_left_distrib](/verify/taulib/docs/book-i-boundary-split-complex/sp-left-distrib/) | L166-L169 | formalized | — |
| `theorem` | [sp_ring_axioms](/verify/taulib/docs/book-i-boundary-split-complex/sp-ring-axioms/) | L172-L185 | formalized | — |
| `def` | [from_sectors](/verify/taulib/docs/book-i-boundary-split-complex/from-sectors/) | L196-L197 | defined | — |
| `theorem` | [to_sectors_injective](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-injective/) | L200-L206 | formalized | — |
| `theorem` | [from_sectors_left_inv](/verify/taulib/docs/book-i-boundary-split-complex/from-sectors-left-inv/) | L209-L212 | formalized | — |
| `theorem` | [to_sectors_surj_on_image](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-surj-on-image/) | L216-L224 | formalized | — |
| `theorem` | [to_sectors_parity](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-parity/) | L227-L233 | formalized | — |
| `theorem` | [to_sectors_zero](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-zero/) | L240-L242 | formalized | — |
| `theorem` | [to_sectors_one](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-one/) | L245-L247 | formalized | — |
| `theorem` | [to_sectors_neg](/verify/taulib/docs/book-i-boundary-split-complex/to-sectors-neg/) | L250-L253 | formalized | — |
| `theorem` | [zero_divisor_sector](/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-sector/) | L267-L278 | formalized | — |
| `theorem` | [zero_divisor_witness_b](/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-witness-b/) | L282-L286 | formalized | — |
| `theorem` | [zero_divisor_witness_c](/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-witness-c/) | L288-L292 | formalized | — |
| `theorem` | [zero_divisors_iff](/verify/taulib/docs/book-i-boundary-split-complex/zero-divisors-iff/) | L295-L314 | formalized | — |
| `example` | [#eval L321](/verify/taulib/docs/book-i-boundary-split-complex/example-l321/) | L321-L321 | example | — |
| `example` | [#eval L322](/verify/taulib/docs/book-i-boundary-split-complex/example-l322/) | L322-L322 | example | — |
| `example` | [#eval L323](/verify/taulib/docs/book-i-boundary-split-complex/example-l323/) | L323-L323 | example | — |
| `example` | [#eval L324](/verify/taulib/docs/book-i-boundary-split-complex/example-l324/) | L324-L324 | example | — |
| `example` | [#eval L327](/verify/taulib/docs/book-i-boundary-split-complex/example-l327/) | L327-L327 | example | — |
| `example` | [#eval L328](/verify/taulib/docs/book-i-boundary-split-complex/example-l328/) | L328-L328 | example | — |
| `example` | [#eval L331](/verify/taulib/docs/book-i-boundary-split-complex/example-l331/) | L331-L331 | example | — |
| `example` | [#eval L332](/verify/taulib/docs/book-i-boundary-split-complex/example-l332/) | L332-L332 | example | — |
| `example` | [#eval L333](/verify/taulib/docs/book-i-boundary-split-complex/example-l333/) | L333-L334 | example | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-boundary-split-complex/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-i-boundary-split-complex/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-i-boundary-split-complex/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-i-boundary-split-complex/eval-l343/) | L343-L343 | computed | — |
| `eval` | [#eval L344](/verify/taulib/docs/book-i-boundary-split-complex/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L345](/verify/taulib/docs/book-i-boundary-split-complex/eval-l345/) | L345-L345 | computed | — |
| `eval` | [#eval L346](/verify/taulib/docs/book-i-boundary-split-complex/eval-l346/) | L346-L348 | computed | — |
