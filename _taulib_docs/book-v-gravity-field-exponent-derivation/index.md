---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.ExponentDerivation",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.ExponentDerivation`.",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_slug": "book-v-gravity-field-exponent-derivation",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/ExponentDerivation.lean",
  "sha256": "1dda037f68250137daa799f92c43ac69c869a5fb8357d4eab37a87172579ad47",
  "imports": [
    "TauLib.BookV.GravityField.ClosingIdentity",
    "TauLib.BookIV.Physics.HolonomyCorrection",
    "TauLib.BookIV.Sectors.SpectralPage"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.BipolarHolonomy"
  ],
  "registry_ids": [
    "V.D100",
    "V.P110",
    "V.P111",
    "V.T145",
    "V.T80",
    "V.T81",
    "V.T82",
    "V.T83"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 2,
    "theorem": 15,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "ExponentFactors",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-factors/",
      "source_line_start": 89,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "V.D100"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_factors",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/canonical-factors/",
      "source_line_start": 101,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exponent_product",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-product/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T80"
      ]
    },
    {
      "kind": "theorem",
      "name": "product_matches_closing",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/product-matches-closing/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "betti_matches_tree_factor",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/betti-matches-tree-factor/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dim_matches_holonomy_circles",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/dim-matches-holonomy-circles/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "solenoidal_matches_kernel",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/solenoidal-matches-kernel/",
      "source_line_start": 139,
      "source_line_end": 141,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "factors_from_distinct_sources",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/factors-from-distinct-sources/",
      "source_line_start": 145,
      "source_line_end": 154,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "passage_count",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "V.T82"
      ]
    },
    {
      "kind": "theorem",
      "name": "passage_count_is_exponent",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count-is-exponent/",
      "source_line_start": 171,
      "source_line_end": 172,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "feynman_vertex_count",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/feynman-vertex-count/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "l3_template_extends",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/l3-template-extends/",
      "source_line_start": 189,
      "source_line_end": 196,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P110"
      ]
    },
    {
      "kind": "theorem",
      "name": "exponent_unique_even_match",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-unique-even-match/",
      "source_line_start": 214,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T83"
      ]
    },
    {
      "kind": "theorem",
      "name": "cf_anatomy",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/cf-anatomy/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_power_factorization",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/iota-power-factorization/",
      "source_line_start": 239,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "passage_uses_tensor_square",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-uses-tensor-square/",
      "source_line_start": 284,
      "source_line_end": 288,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T145"
      ]
    },
    {
      "kind": "theorem",
      "name": "total_iota_power",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/total-iota-power/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tensor_passage_cross_check",
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/tensor-passage-cross-check/",
      "source_line_start": 304,
      "source_line_end": 318,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P111"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 331,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean",
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
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/ExponentDerivation.lean`
- SHA-256: `1dda037f68250137daa799f92c43ac69c869a5fb8357d4eab37a87172579ad47`

## Registry Links

- `V.D100` — tau-enstrophy
- `V.P111` — Tensor-Square Connection
- `V.T80` — Correspondence Tower --- V.T32
- `V.T81` — Rotational Flux Conservation --- V.T33
- `V.T82` — Kepler's First Law --- V.T34
- `V.T83` — Kepler's Second Law --- V.T35

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.ClosingIdentity`
- `TauLib.BookIV.Physics.HolonomyCorrection`
- `TauLib.BookIV.Sectors.SpectralPage`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.BipolarHolonomy`

## Declaration Counts

- `def`: 2
- `eval`: 6
- `structure`: 1
- `theorem`: 15

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [ExponentFactors](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-factors/) | L89-L98 | defined | `V.D100` |
| `def` | [canonical_factors](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/canonical-factors/) | L101-L104 | defined | — |
| `theorem` | [exponent_product](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-product/) | L111-L111 | formalized | `V.T80` |
| `theorem` | [product_matches_closing](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/product-matches-closing/) | L114-L115 | formalized | — |
| `theorem` | [betti_matches_tree_factor](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/betti-matches-tree-factor/) | L128-L129 | formalized | — |
| `theorem` | [dim_matches_holonomy_circles](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/dim-matches-holonomy-circles/) | L134-L135 | formalized | — |
| `theorem` | [solenoidal_matches_kernel](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/solenoidal-matches-kernel/) | L139-L141 | formalized | — |
| `theorem` | [factors_from_distinct_sources](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/factors-from-distinct-sources/) | L145-L154 | formalized | — |
| `def` | [passage_count](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count/) | L169-L169 | defined | `V.T82` |
| `theorem` | [passage_count_is_exponent](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count-is-exponent/) | L171-L172 | formalized | — |
| `theorem` | [feynman_vertex_count](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/feynman-vertex-count/) | L176-L176 | formalized | — |
| `theorem` | [l3_template_extends](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/l3-template-extends/) | L189-L196 | formalized | `V.P110` |
| `theorem` | [exponent_unique_even_match](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-unique-even-match/) | L214-L223 | formalized | `V.T83` |
| `theorem` | [cf_anatomy](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/cf-anatomy/) | L236-L236 | formalized | — |
| `theorem` | [iota_power_factorization](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/iota-power-factorization/) | L239-L269 | formalized | — |
| `theorem` | [passage_uses_tensor_square](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-uses-tensor-square/) | L284-L288 | formalized | `V.T145` |
| `theorem` | [total_iota_power](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/total-iota-power/) | L292-L292 | formalized | — |
| `theorem` | [tensor_passage_cross_check](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/tensor-passage-cross-check/) | L304-L318 | formalized | `V.P111` |
| `eval` | [#eval L324](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l324/) | L324-L324 | computed | — |
| `eval` | [#eval L325](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l325/) | L325-L325 | computed | — |
| `eval` | [#eval L326](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l326/) | L326-L326 | computed | — |
| `eval` | [#eval L327](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l327/) | L327-L327 | computed | — |
| `eval` | [#eval L328](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l328/) | L328-L328 | computed | — |
| `eval` | [#eval L329](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l329/) | L329-L331 | computed | — |
