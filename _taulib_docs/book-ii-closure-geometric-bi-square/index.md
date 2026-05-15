---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Closure.GeometricBiSquare",
  "permalink": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Closure.GeometricBiSquare`.",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_slug": "book-ii-closure-geometric-bi-square",
  "book": "BookII",
  "family": "Closure",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Closure/GeometricBiSquare.lean",
  "sha256": "063526d702345297f81ce0fac23139a1e8b69fb8199b4347566f423bac29542e",
  "imports": [
    "TauLib.BookII.Closure.ForwardBook3",
    "TauLib.BookI.Holomorphy.PresheafEssence",
    "TauLib.BookII.Topology.TorusDegeneration",
    "TauLib.BookII.Geometry.PaschParallel",
    "TauLib.BookII.Domains.HolImpliesCont"
  ],
  "imported_by": [
    "TauLib.BookII"
  ],
  "registry_ids": [
    "II.D77",
    "II.R33",
    "II.R34",
    "II.T49"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 10,
    "theorem": 20,
    "inductive": 1,
    "eval": 15
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "GeometricBiSquareData",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bi-square-data/",
      "source_line_start": 65,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D77"
      ]
    },
    {
      "kind": "def",
      "name": "compute_geometric_bisquare",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/compute-geometric-bisquare/",
      "source_line_start": 91,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D77"
      ]
    },
    {
      "kind": "def",
      "name": "geometric_bisquare_complete",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-complete/",
      "source_line_start": 104,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D77"
      ]
    },
    {
      "kind": "def",
      "name": "geometric_bisquare_check",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-check/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "def",
      "name": "geometric_component_count",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-component-count/",
      "source_line_start": 124,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "def",
      "name": "algebraic_geometric_audit",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/algebraic-geometric-audit/",
      "source_line_start": 142,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.R33"
      ]
    },
    {
      "kind": "def",
      "name": "algebraic_core",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/algebraic-core/",
      "source_line_start": 154,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compatibility_with_algebraic",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/compatibility-with-algebraic/",
      "source_line_start": 158,
      "source_line_end": 162,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geometric_preserves_limit",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-preserves-limit/",
      "source_line_start": 165,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geometric_preserves_right_auto",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-preserves-right-auto/",
      "source_line_start": 172,
      "source_line_end": 177,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ScalingLevel",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level/",
      "source_line_start": 187,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "def",
      "name": "scaling_level_index",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level-index/",
      "source_line_start": 195,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "def",
      "name": "scaling_chain_check",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-chain-check/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "def",
      "name": "book2_scaling_level",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/book2-scaling-level/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "def",
      "name": "e2_not_yet_earned",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e2-not-yet-earned/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l218/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l231/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 247,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geometric_bisquare_3_15",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-3-15/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "geometric_all_eight",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-all-eight/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "geo_topology",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-topology/",
      "source_line_start": 262,
      "source_line_end": 263,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D77"
      ]
    },
    {
      "kind": "theorem",
      "name": "geo_continuity",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-continuity/",
      "source_line_start": 265,
      "source_line_end": 266,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_geometry",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-geometry/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_torus_degeneration",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-torus-degeneration/",
      "source_line_start": 271,
      "source_line_end": 272,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_calibration",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-calibration/",
      "source_line_start": 274,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_spectral_algebra",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-spectral-algebra/",
      "source_line_start": 277,
      "source_line_end": 278,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_central_theorem",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-central-theorem/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "geo_hartogs",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-hartogs/",
      "source_line_start": 283,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "audit_3_15_3",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/audit-3-15-3/",
      "source_line_start": 287,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R33"
      ]
    },
    {
      "kind": "theorem",
      "name": "scaling_chain_valid",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-chain-valid/",
      "source_line_start": 291,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "theorem",
      "name": "e2_not_earned",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e2-not-earned/",
      "source_line_start": 294,
      "source_line_end": 295,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "complete_means_eight",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/complete-means-eight/",
      "source_line_start": 303,
      "source_line_end": 318,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "geometric_implies_central",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-implies-central/",
      "source_line_start": 322,
      "source_line_end": 329,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "e0_ne_e1",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e0-ne-e1/",
      "source_line_start": 332,
      "source_line_end": 333,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R34"
      ]
    },
    {
      "kind": "theorem",
      "name": "e1_ne_e2",
      "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e1-ne-e2/",
      "source_line_start": 336,
      "source_line_end": 339,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.R34"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean",
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
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Closure/GeometricBiSquare.lean`
- SHA-256: `063526d702345297f81ce0fac23139a1e8b69fb8199b4347566f423bac29542e`

## Registry Links

- `II.D77` — Geometric Bi-Square
- `II.R33` — Algebraic-to-Geometric Audit
- `II.R34` — Scaling Chain Forward
- `II.T49` — Geometric Bi-Square Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Closure.ForwardBook3`
- `TauLib.BookI.Holomorphy.PresheafEssence`
- `TauLib.BookII.Topology.TorusDegeneration`
- `TauLib.BookII.Geometry.PaschParallel`
- `TauLib.BookII.Domains.HolImpliesCont`

## Imported By

- `TauLib.BookII`

## Declaration Counts

- `def`: 10
- `eval`: 15
- `inductive`: 1
- `structure`: 1
- `theorem`: 20

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [GeometricBiSquareData](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bi-square-data/) | L65-L82 | type/data schema | type/data schema | `II.D77` |
| `def` | [compute_geometric_bisquare](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/compute-geometric-bisquare/) | L91-L101 | definition | definition | `II.D77` |
| `def` | [geometric_bisquare_complete](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-complete/) | L104-L112 | data/computed value | data/computed value | `II.D77` |
| `def` | [geometric_bisquare_check](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-check/) | L120-L121 | data/computed value | data/computed value | `II.T49` |
| `def` | [geometric_component_count](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-component-count/) | L124-L132 | data/computed value | data/computed value | `II.T49` |
| `def` | [algebraic_geometric_audit](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/algebraic-geometric-audit/) | L142-L144 | data/computed value | data/computed value | `II.R33` |
| `def` | [algebraic_core](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/algebraic-core/) | L154-L154 | definition | definition | — |
| `theorem` | [compatibility_with_algebraic](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/compatibility-with-algebraic/) | L158-L162 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geometric_preserves_limit](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-preserves-limit/) | L165-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geometric_preserves_right_auto](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-preserves-right-auto/) | L172-L177 | proof obligation | formal proof obligation checked | — |
| `inductive` | [ScalingLevel](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level/) | L187-L191 | type/data schema | type/data schema | `II.R34` |
| `def` | [scaling_level_index](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-level-index/) | L195-L198 | definition | definition | `II.R34` |
| `def` | [scaling_chain_check](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-chain-check/) | L201-L203 | data/computed value | data/computed value | `II.R34` |
| `def` | [book2_scaling_level](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/book2-scaling-level/) | L206-L206 | definition | definition | `II.R34` |
| `def` | [e2_not_yet_earned](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e2-not-yet-earned/) | L210-L211 | data/computed value | data/computed value | `II.R34` |
| `eval` | [#eval L218](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l218/) | L218-L218 | computed check | computed check | — |
| `eval` | [#eval L221](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l221/) | L221-L221 | computed check | computed check | — |
| `eval` | [#eval L222](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l222/) | L222-L222 | computed check | computed check | — |
| `eval` | [#eval L223](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l223/) | L223-L223 | computed check | computed check | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l224/) | L224-L224 | computed check | computed check | — |
| `eval` | [#eval L225](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l225/) | L225-L225 | computed check | computed check | — |
| `eval` | [#eval L226](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l226/) | L226-L226 | computed check | computed check | — |
| `eval` | [#eval L227](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l227/) | L227-L227 | computed check | computed check | — |
| `eval` | [#eval L228](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l228/) | L228-L228 | computed check | computed check | — |
| `eval` | [#eval L231](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l231/) | L231-L231 | computed check | computed check | — |
| `eval` | [#eval L234](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l234/) | L234-L234 | computed check | computed check | — |
| `eval` | [#eval L237](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l237/) | L237-L237 | computed check | computed check | — |
| `eval` | [#eval L240](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l240/) | L240-L240 | computed check | computed check | — |
| `eval` | [#eval L241](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l241/) | L241-L241 | computed check | computed check | — |
| `eval` | [#eval L242](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/eval-l242/) | L242-L247 | computed check | computed check | — |
| `theorem` | [geometric_bisquare_3_15](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-bisquare-3-15/) | L254-L255 | proof obligation | formal proof obligation checked | `II.T49` |
| `theorem` | [geometric_all_eight](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-all-eight/) | L258-L259 | proof obligation | formal proof obligation checked | `II.T49` |
| `theorem` | [geo_topology](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-topology/) | L262-L263 | proof obligation | formal proof obligation checked | `II.D77` |
| `theorem` | [geo_continuity](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-continuity/) | L265-L266 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_geometry](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-geometry/) | L268-L269 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_torus_degeneration](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-torus-degeneration/) | L271-L272 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_calibration](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-calibration/) | L274-L275 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_spectral_algebra](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-spectral-algebra/) | L277-L278 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_central_theorem](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-central-theorem/) | L280-L281 | proof obligation | formal proof obligation checked | — |
| `theorem` | [geo_hartogs](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geo-hartogs/) | L283-L284 | proof obligation | formal proof obligation checked | — |
| `theorem` | [audit_3_15_3](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/audit-3-15-3/) | L287-L288 | proof obligation | formal proof obligation checked | `II.R33` |
| `theorem` | [scaling_chain_valid](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/scaling-chain-valid/) | L291-L292 | proof obligation | formal proof obligation checked | `II.R34` |
| `theorem` | [e2_not_earned](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e2-not-earned/) | L294-L295 | proof obligation | formal proof obligation checked | — |
| `theorem` | [complete_means_eight](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/complete-means-eight/) | L303-L318 | proof obligation | formal proof obligation checked | `II.T49` |
| `theorem` | [geometric_implies_central](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/geometric-implies-central/) | L322-L329 | proof obligation | formal proof obligation checked | `II.T49` |
| `theorem` | [e0_ne_e1](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e0-ne-e1/) | L332-L333 | proof obligation | formal proof obligation checked | `II.R34` |
| `theorem` | [e1_ne_e2](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/e1-ne-e2/) | L336-L339 | proof obligation | formal proof obligation checked | `II.R34` |
