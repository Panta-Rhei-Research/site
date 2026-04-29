---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Characters",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Characters`.",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_slug": "book-i-boundary-characters",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Characters.lean",
  "sha256": "2c293e1fe0cf0b0f3e6f48e689dffeda1d29ae00932cf5efd4b876689d02bc5a",
  "imports": [
    "TauLib.BookI.Boundary.SplitComplex",
    "TauLib.BookI.Polarity.Lemniscate",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Spectral",
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.KernelFoundation.ScalarBridges",
    "TauLib.BookIV.Electroweak.MajoranaStructure",
    "TauLib.Tour.GuidedTour.BookI",
    "TauLib.Tour.GuidedTour.BookII"
  ],
  "registry_ids": [
    "I.D37",
    "I.D38"
  ],
  "declaration_counts": {
    "def": 4,
    "theorem": 29,
    "example": 10,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "chi_plus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus/",
      "source_line_start": 48,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": [
        "I.D37"
      ]
    },
    {
      "kind": "def",
      "name": "chi_minus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus/",
      "source_line_start": 53,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": [
        "I.D37"
      ]
    },
    {
      "kind": "def",
      "name": "chi_plus_val",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-val/",
      "source_line_start": 57,
      "source_line_end": 57,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_val",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-val/",
      "source_line_start": 60,
      "source_line_end": 60,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_eq",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-eq/",
      "source_line_start": 63,
      "source_line_end": 64,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_eq",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-eq/",
      "source_line_start": 67,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_add",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-add/",
      "source_line_start": 75,
      "source_line_end": 79,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_mul",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-mul/",
      "source_line_start": 82,
      "source_line_end": 88,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_one",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-one/",
      "source_line_start": 91,
      "source_line_end": 93,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_zero",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-zero/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_neg",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-neg/",
      "source_line_start": 101,
      "source_line_end": 104,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_add",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-add/",
      "source_line_start": 111,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_mul",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-mul/",
      "source_line_start": 118,
      "source_line_end": 124,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_one",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-one/",
      "source_line_start": 127,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_zero",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-zero/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_neg",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-neg/",
      "source_line_start": 137,
      "source_line_end": 140,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_complete",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-complete/",
      "source_line_start": 148,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D38"
      ]
    },
    {
      "kind": "theorem",
      "name": "to_sectors_eq_chi",
      "url": "/verify/taulib/docs/book-i-boundary-characters/to-sectors-eq-chi/",
      "source_line_start": 154,
      "source_line_end": 156,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_orthogonal",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-orthogonal/",
      "source_line_start": 164,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D38"
      ]
    },
    {
      "kind": "theorem",
      "name": "chi_orthogonal'",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-orthogonal-l169/",
      "source_line_start": 169,
      "source_line_end": 171,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_idempotent",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-idempotent/",
      "source_line_start": 178,
      "source_line_end": 181,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_of_e_plus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-of-e-plus/",
      "source_line_start": 184,
      "source_line_end": 186,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_of_e_minus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-of-e-minus/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_of_e_minus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-of-e-minus/",
      "source_line_start": 194,
      "source_line_end": 196,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_of_e_plus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-of-e-plus/",
      "source_line_start": 199,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma_swaps_chi_plus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi-plus/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma_swaps_chi_minus",
      "url": "/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi-minus/",
      "source_line_start": 213,
      "source_line_end": 215,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigma_swaps_chi",
      "url": "/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi/",
      "source_line_start": 218,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_b_sector",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-split-b-sector/",
      "source_line_start": 231,
      "source_line_end": 233,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_split_c_sector",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-split-c-sector/",
      "source_line_start": 237,
      "source_line_end": 239,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_j",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-j/",
      "source_line_start": 246,
      "source_line_end": 247,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_j",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-minus-j/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_vals_one",
      "url": "/verify/taulib/docs/book-i-boundary-characters/chi-vals-one/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l268/",
      "source_line_start": 268,
      "source_line_end": 268,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l269/",
      "source_line_start": 269,
      "source_line_end": 269,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l272/",
      "source_line_start": 272,
      "source_line_end": 272,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l276/",
      "source_line_start": 276,
      "source_line_end": 277,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/example-l278/",
      "source_line_start": 278,
      "source_line_end": 279,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-characters/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 302,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean",
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
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Characters.lean`
- SHA-256: `2c293e1fe0cf0b0f3e6f48e689dffeda1d29ae00932cf5efd4b876689d02bc5a`

## Registry Links

- `I.D37` — Lemniscate Characters
- `I.D38` — Character Group

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.SplitComplex`
- `TauLib.BookI.Polarity.Lemniscate`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Spectral`
- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.KernelFoundation.ScalarBridges`
- `TauLib.BookIV.Electroweak.MajoranaStructure`
- `TauLib.Tour.GuidedTour.BookI`
- `TauLib.Tour.GuidedTour.BookII`

## Declaration Counts

- `def`: 4
- `eval`: 10
- `example`: 10
- `theorem`: 29

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [chi_plus](/verify/taulib/docs/book-i-boundary-characters/chi-plus/) | L48-L49 | defined | `I.D37` |
| `def` | [chi_minus](/verify/taulib/docs/book-i-boundary-characters/chi-minus/) | L53-L54 | defined | `I.D37` |
| `def` | [chi_plus_val](/verify/taulib/docs/book-i-boundary-characters/chi-plus-val/) | L57-L57 | defined | — |
| `def` | [chi_minus_val](/verify/taulib/docs/book-i-boundary-characters/chi-minus-val/) | L60-L60 | defined | — |
| `theorem` | [chi_plus_eq](/verify/taulib/docs/book-i-boundary-characters/chi-plus-eq/) | L63-L64 | formalized | — |
| `theorem` | [chi_minus_eq](/verify/taulib/docs/book-i-boundary-characters/chi-minus-eq/) | L67-L68 | formalized | — |
| `theorem` | [chi_plus_add](/verify/taulib/docs/book-i-boundary-characters/chi-plus-add/) | L75-L79 | formalized | — |
| `theorem` | [chi_plus_mul](/verify/taulib/docs/book-i-boundary-characters/chi-plus-mul/) | L82-L88 | formalized | — |
| `theorem` | [chi_plus_one](/verify/taulib/docs/book-i-boundary-characters/chi-plus-one/) | L91-L93 | formalized | — |
| `theorem` | [chi_plus_zero](/verify/taulib/docs/book-i-boundary-characters/chi-plus-zero/) | L96-L98 | formalized | — |
| `theorem` | [chi_plus_neg](/verify/taulib/docs/book-i-boundary-characters/chi-plus-neg/) | L101-L104 | formalized | — |
| `theorem` | [chi_minus_add](/verify/taulib/docs/book-i-boundary-characters/chi-minus-add/) | L111-L115 | formalized | — |
| `theorem` | [chi_minus_mul](/verify/taulib/docs/book-i-boundary-characters/chi-minus-mul/) | L118-L124 | formalized | — |
| `theorem` | [chi_minus_one](/verify/taulib/docs/book-i-boundary-characters/chi-minus-one/) | L127-L129 | formalized | — |
| `theorem` | [chi_minus_zero](/verify/taulib/docs/book-i-boundary-characters/chi-minus-zero/) | L132-L134 | formalized | — |
| `theorem` | [chi_minus_neg](/verify/taulib/docs/book-i-boundary-characters/chi-minus-neg/) | L137-L140 | formalized | — |
| `theorem` | [chi_complete](/verify/taulib/docs/book-i-boundary-characters/chi-complete/) | L148-L151 | formalized | `I.D38` |
| `theorem` | [to_sectors_eq_chi](/verify/taulib/docs/book-i-boundary-characters/to-sectors-eq-chi/) | L154-L156 | formalized | — |
| `theorem` | [chi_orthogonal](/verify/taulib/docs/book-i-boundary-characters/chi-orthogonal/) | L164-L166 | formalized | `I.D38` |
| `theorem` | [chi_orthogonal'](/verify/taulib/docs/book-i-boundary-characters/chi-orthogonal-l169/) | L169-L171 | formalized | — |
| `theorem` | [chi_plus_idempotent](/verify/taulib/docs/book-i-boundary-characters/chi-plus-idempotent/) | L178-L181 | formalized | — |
| `theorem` | [chi_plus_of_e_plus](/verify/taulib/docs/book-i-boundary-characters/chi-plus-of-e-plus/) | L184-L186 | formalized | — |
| `theorem` | [chi_minus_of_e_minus](/verify/taulib/docs/book-i-boundary-characters/chi-minus-of-e-minus/) | L189-L191 | formalized | — |
| `theorem` | [chi_plus_of_e_minus](/verify/taulib/docs/book-i-boundary-characters/chi-plus-of-e-minus/) | L194-L196 | formalized | — |
| `theorem` | [chi_minus_of_e_plus](/verify/taulib/docs/book-i-boundary-characters/chi-minus-of-e-plus/) | L199-L201 | formalized | — |
| `theorem` | [sigma_swaps_chi_plus](/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi-plus/) | L208-L210 | formalized | — |
| `theorem` | [sigma_swaps_chi_minus](/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi-minus/) | L213-L215 | formalized | — |
| `theorem` | [sigma_swaps_chi](/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi/) | L218-L223 | formalized | — |
| `theorem` | [chi_split_b_sector](/verify/taulib/docs/book-i-boundary-characters/chi-split-b-sector/) | L231-L233 | formalized | — |
| `theorem` | [chi_split_c_sector](/verify/taulib/docs/book-i-boundary-characters/chi-split-c-sector/) | L237-L239 | formalized | — |
| `theorem` | [chi_plus_j](/verify/taulib/docs/book-i-boundary-characters/chi-plus-j/) | L246-L247 | formalized | — |
| `theorem` | [chi_minus_j](/verify/taulib/docs/book-i-boundary-characters/chi-minus-j/) | L250-L251 | formalized | — |
| `theorem` | [chi_vals_one](/verify/taulib/docs/book-i-boundary-characters/chi-vals-one/) | L254-L255 | formalized | — |
| `example` | [#eval L262](/verify/taulib/docs/book-i-boundary-characters/example-l262/) | L262-L262 | example | — |
| `example` | [#eval L263](/verify/taulib/docs/book-i-boundary-characters/example-l263/) | L263-L263 | example | — |
| `example` | [#eval L264](/verify/taulib/docs/book-i-boundary-characters/example-l264/) | L264-L264 | example | — |
| `example` | [#eval L265](/verify/taulib/docs/book-i-boundary-characters/example-l265/) | L265-L265 | example | — |
| `example` | [#eval L268](/verify/taulib/docs/book-i-boundary-characters/example-l268/) | L268-L268 | example | — |
| `example` | [#eval L269](/verify/taulib/docs/book-i-boundary-characters/example-l269/) | L269-L269 | example | — |
| `example` | [#eval L272](/verify/taulib/docs/book-i-boundary-characters/example-l272/) | L272-L272 | example | — |
| `example` | [#eval L273](/verify/taulib/docs/book-i-boundary-characters/example-l273/) | L273-L273 | example | — |
| `example` | [#eval L276](/verify/taulib/docs/book-i-boundary-characters/example-l276/) | L276-L277 | example | — |
| `example` | [#eval L278](/verify/taulib/docs/book-i-boundary-characters/example-l278/) | L278-L279 | example | — |
| `eval` | [#eval L285](/verify/taulib/docs/book-i-boundary-characters/eval-l285/) | L285-L285 | computed | — |
| `eval` | [#eval L286](/verify/taulib/docs/book-i-boundary-characters/eval-l286/) | L286-L286 | computed | — |
| `eval` | [#eval L287](/verify/taulib/docs/book-i-boundary-characters/eval-l287/) | L287-L287 | computed | — |
| `eval` | [#eval L288](/verify/taulib/docs/book-i-boundary-characters/eval-l288/) | L288-L288 | computed | — |
| `eval` | [#eval L291](/verify/taulib/docs/book-i-boundary-characters/eval-l291/) | L291-L291 | computed | — |
| `eval` | [#eval L292](/verify/taulib/docs/book-i-boundary-characters/eval-l292/) | L292-L292 | computed | — |
| `eval` | [#eval L295](/verify/taulib/docs/book-i-boundary-characters/eval-l295/) | L295-L295 | computed | — |
| `eval` | [#eval L296](/verify/taulib/docs/book-i-boundary-characters/eval-l296/) | L296-L296 | computed | — |
| `eval` | [#eval L299](/verify/taulib/docs/book-i-boundary-characters/eval-l299/) | L299-L299 | computed | — |
| `eval` | [#eval L300](/verify/taulib/docs/book-i-boundary-characters/eval-l300/) | L300-L302 | computed | — |
