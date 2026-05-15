---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Enrichment.LayerTemplate",
  "permalink": "/corpus/taulib/docs/book-iii-enrichment-layer-template/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_slug": "book-iii-enrichment-layer-template",
  "book": "BookIII",
  "family": "Enrichment",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Enrichment/LayerTemplate.lean",
  "sha256": "cf44cf29c6d0ef0c8be37baf3dafad02ceab5a1570098a88d9a2cb757b4f4877",
  "imports": [
    "TauLib.BookIII.Prologue.HartogsBulk",
    "TauLib.BookII.Enrichment.SelfEnrichment"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Enrichment.Functor"
  ],
  "registry_ids": [
    "III.D05",
    "III.D06",
    "III.D07",
    "III.D08",
    "III.D09"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 13,
    "structure": 1,
    "eval": 23,
    "theorem": 12
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "EnrLevel",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/enr-level/",
      "source_line_start": 49,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EnrLevel.ofBookII",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/of-book-ii/",
      "source_line_start": 57,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EnrLevel.toNat",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/to-nat/",
      "source_line_start": 62,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EnrLevel.lt",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/lt/",
      "source_line_start": 69,
      "source_line_end": 70,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EnrLevel.le",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/le/",
      "source_line_start": 73,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EnrLevel.succ",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/succ/",
      "source_line_start": 77,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LayerTemplate",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-template/",
      "source_line_start": 98,
      "source_line_end": 106,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "III.D05"
      ]
    },
    {
      "kind": "def",
      "name": "layer_template_check",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-template-check/",
      "source_line_start": 110,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D05"
      ]
    },
    {
      "kind": "def",
      "name": "e0_layer",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-layer/",
      "source_line_start": 141,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D06"
      ]
    },
    {
      "kind": "def",
      "name": "e1_layer_book3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-layer-book3/",
      "source_line_start": 164,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D07"
      ]
    },
    {
      "kind": "def",
      "name": "e2_layer",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-layer/",
      "source_line_start": 202,
      "source_line_end": 228,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D08",
        "III.D09"
      ]
    },
    {
      "kind": "def",
      "name": "e3_layer",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-layer/",
      "source_line_start": 239,
      "source_line_end": 267,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D09"
      ]
    },
    {
      "kind": "def",
      "name": "layer_of",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-of/",
      "source_line_start": 274,
      "source_line_end": 279,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "layer_valid_at",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-valid-at/",
      "source_line_start": 282,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_layers_valid",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/all-layers-valid/",
      "source_line_start": 286,
      "source_line_end": 290,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l297/",
      "source_line_start": 297,
      "source_line_end": 297,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l312/",
      "source_line_start": 312,
      "source_line_end": 312,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l316/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l324/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l327/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l328/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l329/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l330/",
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
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_layer_valid_8_3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-layer-valid-8-3/",
      "source_line_start": 338,
      "source_line_end": 339,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D06"
      ]
    },
    {
      "kind": "theorem",
      "name": "e1_layer_valid_8_3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-layer-valid-8-3/",
      "source_line_start": 342,
      "source_line_end": 343,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D07"
      ]
    },
    {
      "kind": "theorem",
      "name": "e2_layer_valid_8_3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-layer-valid-8-3/",
      "source_line_start": 346,
      "source_line_end": 347,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D08"
      ]
    },
    {
      "kind": "theorem",
      "name": "e3_layer_valid_8_3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-layer-valid-8-3/",
      "source_line_start": 350,
      "source_line_end": 351,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D09"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_layers_8_3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/all-layers-8-3/",
      "source_line_start": 354,
      "source_line_end": 355,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D05"
      ]
    },
    {
      "kind": "theorem",
      "name": "enr_le_total",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/enr-le-total/",
      "source_line_start": 362,
      "source_line_end": 364,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e3_saturates",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-saturates/",
      "source_line_start": 367,
      "source_line_end": 367,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_ne_e1",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-ne-e1/",
      "source_line_start": 370,
      "source_line_end": 370,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e1_ne_e2",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-ne-e2/",
      "source_line_start": 371,
      "source_line_end": 371,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e2_ne_e3",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-ne-e3/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coercion_preserves_order",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/coercion-preserves-order/",
      "source_line_start": 375,
      "source_line_end": 377,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_carrier_small",
      "url": "/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-carrier-small/",
      "source_line_start": 380,
      "source_line_end": 385,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Enrichment/LayerTemplate.lean`
- SHA-256: `cf44cf29c6d0ef0c8be37baf3dafad02ceab5a1570098a88d9a2cb757b4f4877`

## Registry Links

- `III.D05` — Layer Template
- `III.D06` — E₀ Layer (Mathematics)
- `III.D07` — E₁ Layer (Physics)
- `III.D08` — E₂ Layer (Computation)
- `III.D09` — E₃ Layer (Metaphysics)

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Prologue.HartogsBulk`
- `TauLib.BookII.Enrichment.SelfEnrichment`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Enrichment.Functor`

## Declaration Counts

- `def`: 13
- `eval`: 23
- `inductive`: 1
- `structure`: 1
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [EnrLevel](/corpus/taulib/docs/book-iii-enrichment-layer-template/enr-level/) | L49-L54 | type/data schema | type/data schema | — |
| `def` | [EnrLevel.ofBookII](/corpus/taulib/docs/book-iii-enrichment-layer-template/of-book-ii/) | L57-L59 | definition | definition | — |
| `def` | [EnrLevel.toNat](/corpus/taulib/docs/book-iii-enrichment-layer-template/to-nat/) | L62-L66 | definition | definition | — |
| `def` | [EnrLevel.lt](/corpus/taulib/docs/book-iii-enrichment-layer-template/lt/) | L69-L70 | data/computed value | data/computed value | — |
| `def` | [EnrLevel.le](/corpus/taulib/docs/book-iii-enrichment-layer-template/le/) | L73-L74 | data/computed value | data/computed value | — |
| `def` | [EnrLevel.succ](/corpus/taulib/docs/book-iii-enrichment-layer-template/succ/) | L77-L81 | definition | definition | — |
| `structure` | [LayerTemplate](/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-template/) | L98-L106 | type/data schema | type/data schema | `III.D05` |
| `def` | [layer_template_check](/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-template-check/) | L110-L130 | data/computed value | data/computed value | `III.D05` |
| `def` | [e0_layer](/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-layer/) | L141-L151 | definition | definition | `III.D06` |
| `def` | [e1_layer_book3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-layer-book3/) | L164-L188 | definition | definition | `III.D07` |
| `def` | [e2_layer](/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-layer/) | L202-L228 | definition | definition | `III.D08`, `III.D09` |
| `def` | [e3_layer](/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-layer/) | L239-L267 | definition | definition | `III.D09` |
| `def` | [layer_of](/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-of/) | L274-L279 | definition | definition | — |
| `def` | [layer_valid_at](/corpus/taulib/docs/book-iii-enrichment-layer-template/layer-valid-at/) | L282-L283 | data/computed value | data/computed value | — |
| `def` | [all_layers_valid](/corpus/taulib/docs/book-iii-enrichment-layer-template/all-layers-valid/) | L286-L290 | data/computed value | data/computed value | — |
| `eval` | [#eval L297](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l297/) | L297-L297 | computed check | computed check | — |
| `eval` | [#eval L298](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l298/) | L298-L298 | computed check | computed check | — |
| `eval` | [#eval L299](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l299/) | L299-L299 | computed check | computed check | — |
| `eval` | [#eval L300](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l300/) | L300-L300 | computed check | computed check | — |
| `eval` | [#eval L301](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l301/) | L301-L301 | computed check | computed check | — |
| `eval` | [#eval L302](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l302/) | L302-L302 | computed check | computed check | — |
| `eval` | [#eval L305](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l305/) | L305-L305 | computed check | computed check | — |
| `eval` | [#eval L306](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l306/) | L306-L306 | computed check | computed check | — |
| `eval` | [#eval L309](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l309/) | L309-L309 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l310/) | L310-L310 | computed check | computed check | — |
| `eval` | [#eval L311](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l311/) | L311-L311 | computed check | computed check | — |
| `eval` | [#eval L312](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l312/) | L312-L312 | computed check | computed check | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L319](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l319/) | L319-L319 | computed check | computed check | — |
| `eval` | [#eval L320](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l320/) | L320-L320 | computed check | computed check | — |
| `eval` | [#eval L323](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l323/) | L323-L323 | computed check | computed check | — |
| `eval` | [#eval L324](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l324/) | L324-L324 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l327/) | L327-L327 | computed check | computed check | — |
| `eval` | [#eval L328](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l328/) | L328-L328 | computed check | computed check | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l329/) | L329-L329 | computed check | computed check | — |
| `eval` | [#eval L330](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l330/) | L330-L330 | computed check | computed check | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-iii-enrichment-layer-template/eval-l331/) | L331-L331 | computed check | computed check | — |
| `theorem` | [e0_layer_valid_8_3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-layer-valid-8-3/) | L338-L339 | proof obligation | formal proof obligation checked | `III.D06` |
| `theorem` | [e1_layer_valid_8_3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-layer-valid-8-3/) | L342-L343 | proof obligation | formal proof obligation checked | `III.D07` |
| `theorem` | [e2_layer_valid_8_3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-layer-valid-8-3/) | L346-L347 | proof obligation | formal proof obligation checked | `III.D08` |
| `theorem` | [e3_layer_valid_8_3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-layer-valid-8-3/) | L350-L351 | proof obligation | formal proof obligation checked | `III.D09` |
| `theorem` | [all_layers_8_3](/corpus/taulib/docs/book-iii-enrichment-layer-template/all-layers-8-3/) | L354-L355 | proof obligation | formal proof obligation checked | `III.D05` |
| `theorem` | [enr_le_total](/corpus/taulib/docs/book-iii-enrichment-layer-template/enr-le-total/) | L362-L364 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e3_saturates](/corpus/taulib/docs/book-iii-enrichment-layer-template/e3-saturates/) | L367-L367 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e0_ne_e1](/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-ne-e1/) | L370-L370 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e1_ne_e2](/corpus/taulib/docs/book-iii-enrichment-layer-template/e1-ne-e2/) | L371-L371 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e2_ne_e3](/corpus/taulib/docs/book-iii-enrichment-layer-template/e2-ne-e3/) | L372-L372 | proof obligation | formal proof obligation checked | — |
| `theorem` | [coercion_preserves_order](/corpus/taulib/docs/book-iii-enrichment-layer-template/coercion-preserves-order/) | L375-L377 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e0_carrier_small](/corpus/taulib/docs/book-iii-enrichment-layer-template/e0-carrier-small/) | L380-L385 | proof obligation | formal proof obligation checked | — |
