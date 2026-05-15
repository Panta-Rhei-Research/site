---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Hinge.DependencyChain",
  "permalink": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Hinge.DependencyChain`.",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_slug": "book-iii-hinge-dependency-chain",
  "book": "BookIII",
  "family": "Hinge",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Hinge/DependencyChain.lean",
  "sha256": "018f8c7ab3ec4d1a32ecf6809d3d050d99b7cca538ac611afae9f9dc97624333",
  "imports": [
    "TauLib.BookIII.Arithmetic.TowerAssembly"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Hinge.HingeTheorem",
    "TauLib.Tour.GuidedTour.BookIII"
  ],
  "registry_ids": [
    "III.D66",
    "III.P29",
    "III.P30"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 16,
    "eval": 16,
    "theorem": 20
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ChainLink",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-link/",
      "source_line_start": 48,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ChainLink.toNat",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/to-nat/",
      "source_line_start": 66,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chain_links",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-links/",
      "source_line_start": 83,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ChainLink.toEnrLevel",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/to-enr-level/",
      "source_line_start": 88,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ChainLink.succ",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/succ/",
      "source_line_start": 95,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chain_strict_order_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-strict-order-check/",
      "source_line_start": 117,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "def",
      "name": "chain_layer_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-layer-check/",
      "source_line_start": 130,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "def",
      "name": "chain_tower_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-tower-check/",
      "source_line_start": 145,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "def",
      "name": "dependency_chain_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/dependency-chain-check/",
      "source_line_start": 153,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "def",
      "name": "chain_linearity_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-check/",
      "source_line_start": 165,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P29"
      ]
    },
    {
      "kind": "def",
      "name": "chain_no_duplicates_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-no-duplicates-check/",
      "source_line_start": 180,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P29"
      ]
    },
    {
      "kind": "def",
      "name": "chain_linearity_full_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-full-check/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P29"
      ]
    },
    {
      "kind": "def",
      "name": "terminal_completeness_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-check/",
      "source_line_start": 203,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "def",
      "name": "chain_length_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-length-check/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "def",
      "name": "chain_terminal_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-terminal-check/",
      "source_line_start": 224,
      "source_line_end": 227,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "def",
      "name": "chain_saturation_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-saturation-check/",
      "source_line_start": 230,
      "source_line_end": 231,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "def",
      "name": "terminal_completeness_full_check",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-full-check/",
      "source_line_start": 235,
      "source_line_end": 239,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l255/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l269/",
      "source_line_start": 269,
      "source_line_end": 269,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l270/",
      "source_line_start": 270,
      "source_line_end": 270,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l271/",
      "source_line_start": 271,
      "source_line_end": 271,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l272/",
      "source_line_start": 272,
      "source_line_end": 272,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "dependency_chain_8_3",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/dependency-chain-8-3/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_strict_order",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-strict-order/",
      "source_line_start": 283,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_layer_8_3",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-layer-8-3/",
      "source_line_start": 286,
      "source_line_end": 287,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_tower_10_3",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-tower-10-3/",
      "source_line_start": 289,
      "source_line_end": 290,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_linearity",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity/",
      "source_line_start": 293,
      "source_line_end": 294,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P29"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_no_duplicates",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-no-duplicates/",
      "source_line_start": 296,
      "source_line_end": 297,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_linearity_full",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-full/",
      "source_line_start": 299,
      "source_line_end": 300,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "terminal_completeness",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness/",
      "source_line_start": 303,
      "source_line_end": 304,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_length",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-length/",
      "source_line_start": 306,
      "source_line_end": 307,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_terminal",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-terminal/",
      "source_line_start": 309,
      "source_line_end": 310,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_saturation",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-saturation/",
      "source_line_start": 312,
      "source_line_end": 313,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "terminal_completeness_full",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-full/",
      "source_line_start": 315,
      "source_line_end": 316,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_has_14_links",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-has-14-links/",
      "source_line_start": 323,
      "source_line_end": 324,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "theorem",
      "name": "k0_is_first",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/k0-is-first/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "theorem",
      "name": "e3p_is_last",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/e3p-is-last/",
      "source_line_start": 330,
      "source_line_end": 330,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "theorem",
      "name": "axiom_to_enrichment",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/axiom-to-enrichment/",
      "source_line_start": 333,
      "source_line_end": 334,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
      ]
    },
    {
      "kind": "theorem",
      "name": "succ_monotone",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/succ-monotone/",
      "source_line_start": 337,
      "source_line_end": 339,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P29"
      ]
    },
    {
      "kind": "theorem",
      "name": "e3p_saturates",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/e3p-saturates/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_links_have_level",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/all-links-have-level/",
      "source_line_start": 345,
      "source_line_end": 350,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P30"
      ]
    },
    {
      "kind": "theorem",
      "name": "seven_plus_seven",
      "url": "/corpus/taulib/docs/book-iii-hinge-dependency-chain/seven-plus-seven/",
      "source_line_start": 353,
      "source_line_end": 356,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D66"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Hinge/DependencyChain.lean`
- SHA-256: `018f8c7ab3ec4d1a32ecf6809d3d050d99b7cca538ac611afae9f9dc97624333`

## Registry Links

- `III.D66` — Complete Dependency Chain
- `III.P29` — Chain Verification Protocol
- `III.P30` — Sector Instantiation Lemma

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Arithmetic.TowerAssembly`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Hinge.HingeTheorem`
- `TauLib.Tour.GuidedTour.BookIII`

## Declaration Counts

- `def`: 16
- `eval`: 16
- `inductive`: 1
- `theorem`: 20

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ChainLink](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-link/) | L48-L63 | type/data schema | type/data schema | — |
| `def` | [ChainLink.toNat](/corpus/taulib/docs/book-iii-hinge-dependency-chain/to-nat/) | L66-L80 | definition | definition | — |
| `def` | [chain_links](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-links/) | L83-L85 | data/computed value | data/computed value | — |
| `def` | [ChainLink.toEnrLevel](/corpus/taulib/docs/book-iii-hinge-dependency-chain/to-enr-level/) | L88-L92 | definition | definition | — |
| `def` | [ChainLink.succ](/corpus/taulib/docs/book-iii-hinge-dependency-chain/succ/) | L95-L109 | definition | definition | — |
| `def` | [chain_strict_order_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-strict-order-check/) | L117-L125 | data/computed value | data/computed value | `III.D66` |
| `def` | [chain_layer_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-layer-check/) | L130-L141 | data/computed value | data/computed value | `III.D66` |
| `def` | [chain_tower_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-tower-check/) | L145-L149 | data/computed value | data/computed value | `III.D66` |
| `def` | [dependency_chain_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/dependency-chain-check/) | L153-L156 | data/computed value | data/computed value | `III.D66` |
| `def` | [chain_linearity_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-check/) | L165-L177 | data/computed value | data/computed value | `III.P29` |
| `def` | [chain_no_duplicates_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-no-duplicates-check/) | L180-L191 | data/computed value | data/computed value | `III.P29` |
| `def` | [chain_linearity_full_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-full-check/) | L194-L195 | data/computed value | data/computed value | `III.P29` |
| `def` | [terminal_completeness_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-check/) | L203-L217 | data/computed value | data/computed value | `III.P30` |
| `def` | [chain_length_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-length-check/) | L220-L221 | data/computed value | data/computed value | `III.P30` |
| `def` | [chain_terminal_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-terminal-check/) | L224-L227 | data/computed value | data/computed value | `III.P30` |
| `def` | [chain_saturation_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-saturation-check/) | L230-L231 | data/computed value | data/computed value | `III.P30` |
| `def` | [terminal_completeness_full_check](/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-full-check/) | L235-L239 | data/computed value | data/computed value | `III.P30` |
| `eval` | [#eval L246](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l246/) | L246-L246 | computed check | computed check | — |
| `eval` | [#eval L247](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l247/) | L247-L247 | computed check | computed check | — |
| `eval` | [#eval L248](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l248/) | L248-L248 | computed check | computed check | — |
| `eval` | [#eval L249](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l249/) | L249-L249 | computed check | computed check | — |
| `eval` | [#eval L252](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l252/) | L252-L252 | computed check | computed check | — |
| `eval` | [#eval L255](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l255/) | L255-L255 | computed check | computed check | — |
| `eval` | [#eval L258](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l258/) | L258-L258 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l264/) | L264-L264 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l265/) | L265-L265 | computed check | computed check | — |
| `eval` | [#eval L266](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l266/) | L266-L266 | computed check | computed check | — |
| `eval` | [#eval L269](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l269/) | L269-L269 | computed check | computed check | — |
| `eval` | [#eval L270](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l270/) | L270-L270 | computed check | computed check | — |
| `eval` | [#eval L271](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l271/) | L271-L271 | computed check | computed check | — |
| `eval` | [#eval L272](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l272/) | L272-L272 | computed check | computed check | — |
| `eval` | [#eval L273](/corpus/taulib/docs/book-iii-hinge-dependency-chain/eval-l273/) | L273-L273 | computed check | computed check | — |
| `theorem` | [dependency_chain_8_3](/corpus/taulib/docs/book-iii-hinge-dependency-chain/dependency-chain-8-3/) | L280-L281 | proof obligation | formal proof obligation checked | `III.D66` |
| `theorem` | [chain_strict_order](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-strict-order/) | L283-L284 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_layer_8_3](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-layer-8-3/) | L286-L287 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_tower_10_3](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-tower-10-3/) | L289-L290 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_linearity](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity/) | L293-L294 | proof obligation | formal proof obligation checked | `III.P29` |
| `theorem` | [chain_no_duplicates](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-no-duplicates/) | L296-L297 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_linearity_full](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-full/) | L299-L300 | proof obligation | formal proof obligation checked | — |
| `theorem` | [terminal_completeness](/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness/) | L303-L304 | proof obligation | formal proof obligation checked | `III.P30` |
| `theorem` | [chain_length](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-length/) | L306-L307 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_terminal](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-terminal/) | L309-L310 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_saturation](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-saturation/) | L312-L313 | proof obligation | formal proof obligation checked | — |
| `theorem` | [terminal_completeness_full](/corpus/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-full/) | L315-L316 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chain_has_14_links](/corpus/taulib/docs/book-iii-hinge-dependency-chain/chain-has-14-links/) | L323-L324 | proof obligation | formal proof obligation checked | `III.D66` |
| `theorem` | [k0_is_first](/corpus/taulib/docs/book-iii-hinge-dependency-chain/k0-is-first/) | L327-L327 | proof obligation | formal proof obligation checked | `III.D66` |
| `theorem` | [e3p_is_last](/corpus/taulib/docs/book-iii-hinge-dependency-chain/e3p-is-last/) | L330-L330 | proof obligation | formal proof obligation checked | `III.D66` |
| `theorem` | [axiom_to_enrichment](/corpus/taulib/docs/book-iii-hinge-dependency-chain/axiom-to-enrichment/) | L333-L334 | proof obligation | formal proof obligation checked | `III.D66` |
| `theorem` | [succ_monotone](/corpus/taulib/docs/book-iii-hinge-dependency-chain/succ-monotone/) | L337-L339 | proof obligation | formal proof obligation checked | `III.P29` |
| `theorem` | [e3p_saturates](/corpus/taulib/docs/book-iii-hinge-dependency-chain/e3p-saturates/) | L342-L342 | proof obligation | formal proof obligation checked | `III.P30` |
| `theorem` | [all_links_have_level](/corpus/taulib/docs/book-iii-hinge-dependency-chain/all-links-have-level/) | L345-L350 | proof obligation | formal proof obligation checked | `III.P30` |
| `theorem` | [seven_plus_seven](/corpus/taulib/docs/book-iii-hinge-dependency-chain/seven-plus-seven/) | L353-L356 | proof obligation | formal proof obligation checked | `III.D66` |
