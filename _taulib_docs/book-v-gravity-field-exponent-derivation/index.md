---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.ExponentDerivation",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-factors/",
      "source_line_start": 89,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D100"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_factors",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/canonical-factors/",
      "source_line_start": 101,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exponent_product",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-product/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T80"
      ]
    },
    {
      "kind": "theorem",
      "name": "product_matches_closing",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/product-matches-closing/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "betti_matches_tree_factor",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/betti-matches-tree-factor/",
      "source_line_start": 128,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dim_matches_holonomy_circles",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/dim-matches-holonomy-circles/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "solenoidal_matches_kernel",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/solenoidal-matches-kernel/",
      "source_line_start": 139,
      "source_line_end": 141,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "factors_from_distinct_sources",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/factors-from-distinct-sources/",
      "source_line_start": 145,
      "source_line_end": 154,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "passage_count",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.T82"
      ]
    },
    {
      "kind": "theorem",
      "name": "passage_count_is_exponent",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count-is-exponent/",
      "source_line_start": 171,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "feynman_vertex_count",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/feynman-vertex-count/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "l3_template_extends",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/l3-template-extends/",
      "source_line_start": 189,
      "source_line_end": 196,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P110"
      ]
    },
    {
      "kind": "theorem",
      "name": "exponent_unique_even_match",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-unique-even-match/",
      "source_line_start": 214,
      "source_line_end": 223,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T83"
      ]
    },
    {
      "kind": "theorem",
      "name": "cf_anatomy",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/cf-anatomy/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_power_factorization",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/iota-power-factorization/",
      "source_line_start": 239,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "passage_uses_tensor_square",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-uses-tensor-square/",
      "source_line_start": 284,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T145"
      ]
    },
    {
      "kind": "theorem",
      "name": "total_iota_power",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/total-iota-power/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tensor_passage_cross_check",
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/tensor-passage-cross-check/",
      "source_line_start": 304,
      "source_line_end": 318,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P111"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l325/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l326/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l327/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l328/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 331,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [ExponentFactors](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-factors/) | L89-L98 | type/data schema | type/data schema | `V.D100` |
| `def` | [canonical_factors](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/canonical-factors/) | L101-L104 | definition | definition | — |
| `theorem` | [exponent_product](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-product/) | L111-L111 | proof obligation | formal proof obligation checked | `V.T80` |
| `theorem` | [product_matches_closing](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/product-matches-closing/) | L114-L115 | proof obligation | formal proof obligation checked | — |
| `theorem` | [betti_matches_tree_factor](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/betti-matches-tree-factor/) | L128-L129 | proof obligation | formal proof obligation checked | — |
| `theorem` | [dim_matches_holonomy_circles](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/dim-matches-holonomy-circles/) | L134-L135 | proof obligation | formal proof obligation checked | — |
| `theorem` | [solenoidal_matches_kernel](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/solenoidal-matches-kernel/) | L139-L141 | proof obligation | formal proof obligation checked | — |
| `theorem` | [factors_from_distinct_sources](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/factors-from-distinct-sources/) | L145-L154 | proof obligation | formal proof obligation checked | — |
| `def` | [passage_count](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count/) | L169-L169 | data/computed value | data/computed value | `V.T82` |
| `theorem` | [passage_count_is_exponent](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count-is-exponent/) | L171-L172 | proof obligation | formal proof obligation checked | — |
| `theorem` | [feynman_vertex_count](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/feynman-vertex-count/) | L176-L176 | proof obligation | formal proof obligation checked | — |
| `theorem` | [l3_template_extends](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/l3-template-extends/) | L189-L196 | proof obligation | formal proof obligation checked | `V.P110` |
| `theorem` | [exponent_unique_even_match](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-unique-even-match/) | L214-L223 | proof obligation | formal proof obligation checked | `V.T83` |
| `theorem` | [cf_anatomy](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/cf-anatomy/) | L236-L236 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota_power_factorization](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/iota-power-factorization/) | L239-L269 | proof obligation | formal proof obligation checked | — |
| `theorem` | [passage_uses_tensor_square](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/passage-uses-tensor-square/) | L284-L288 | proof obligation | formal proof obligation checked | `V.T145` |
| `theorem` | [total_iota_power](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/total-iota-power/) | L292-L292 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tensor_passage_cross_check](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/tensor-passage-cross-check/) | L304-L318 | proof obligation | formal proof obligation checked | `V.P111` |
| `eval` | [#eval L324](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l324/) | L324-L324 | computed check | computed check | — |
| `eval` | [#eval L325](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l325/) | L325-L325 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l327/) | L327-L327 | computed check | computed check | — |
| `eval` | [#eval L328](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l328/) | L328-L328 | computed check | computed check | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-v-gravity-field-exponent-derivation/eval-l329/) | L329-L331 | computed check | computed check | — |
