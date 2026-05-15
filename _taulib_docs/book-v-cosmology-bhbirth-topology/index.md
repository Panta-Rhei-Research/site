---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.BHBirthTopology",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_slug": "book-v-cosmology-bhbirth-topology",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/BHBirthTopology.lean",
  "sha256": "14e1456a764677fb0be857410642b281731d01836b6b817f6ee4c4bdc4535c1f",
  "imports": [
    "TauLib.BookV.Cosmology.ThresholdLadder"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.BHBipolarFusion",
    "TauLib.Tour.GuidedTour.BookV"
  ],
  "registry_ids": [
    "V.C18",
    "V.D163",
    "V.D164",
    "V.D165",
    "V.D166",
    "V.D167",
    "V.P93",
    "V.R222",
    "V.T109",
    "V.T110"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 5,
    "inductive": 1,
    "theorem": 8,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "GravitationalTension",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/gravitational-tension/",
      "source_line_start": 64,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D163"
      ]
    },
    {
      "kind": "def",
      "name": "GravitationalTension.toFloat",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/to-float/",
      "source_line_start": 76,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SphericalCapacity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/spherical-capacity/",
      "source_line_start": 88,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D164"
      ]
    },
    {
      "kind": "structure",
      "name": "LinkingClass",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/linking-class/",
      "source_line_start": 110,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D165"
      ]
    },
    {
      "kind": "def",
      "name": "unit_linking",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/unit-linking/",
      "source_line_start": 120,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "HorizonTopology",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/horizon-topology/",
      "source_line_start": 130,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BlackHoleTopologicalEvent",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/black-hole-topological-event/",
      "source_line_start": 143,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D166"
      ]
    },
    {
      "kind": "theorem",
      "name": "bh_threshold_theorem",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-threshold-theorem/",
      "source_line_start": 166,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T109"
      ]
    },
    {
      "kind": "theorem",
      "name": "bh_toroidal_topology",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-topology/",
      "source_line_start": 179,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T110"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_interior_singularity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/no-interior-singularity/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P93"
      ]
    },
    {
      "kind": "theorem",
      "name": "information_preservation",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/information-preservation/",
      "source_line_start": 204,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C18"
      ]
    },
    {
      "kind": "structure",
      "name": "CanonicalBHNeighborhood",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/canonical-bhneighborhood/",
      "source_line_start": 217,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D167"
      ]
    },
    {
      "kind": "def",
      "name": "example_bh",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/example-bh/",
      "source_line_start": 242,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l247/",
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
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l248/",
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
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l249/",
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
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FiberShapeRatio",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio/",
      "source_line_start": 274,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "fiber_shape_ratio",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fiber_shape_ratio_structural",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio-structural/",
      "source_line_start": 290,
      "source_line_end": 294,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bh_toroidal_structural",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-structural/",
      "source_line_start": 310,
      "source_line_end": 311,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_singularity_from_linking",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/no-singularity-from-linking/",
      "source_line_start": 316,
      "source_line_end": 321,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InformationPreservationStructural",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/information-preservation-structural/",
      "source_line_start": 327,
      "source_line_end": 334,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "info_preservation_structural",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/info-preservation-structural/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "info_preservation_thm",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/info-preservation-thm/",
      "source_line_start": 338,
      "source_line_end": 341,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l344/",
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
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l345/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 348,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/BHBirthTopology.lean`
- SHA-256: `14e1456a764677fb0be857410642b281731d01836b6b817f6ee4c4bdc4535c1f`

## Registry Links

- `V.C18` — Information Preservation
- `V.D163` — Gravitational Tension
- `V.D164` — Spherical Capacity
- `V.D165` — Linking Class
- `V.D166` — Black Hole (Topological Event)
- `V.D167` — Canonical BH Neighborhood
- `V.P93` — No Interior Singularity
- `V.R222` — Event horizon as linking boundary
- `V.T109` — BH Threshold Theorem
- `V.T110` — BH Toroidal Topology

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.ThresholdLadder`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.BHBipolarFusion`
- `TauLib.Tour.GuidedTour.BookV`

## Declaration Counts

- `def`: 5
- `eval`: 8
- `inductive`: 1
- `structure`: 7
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [GravitationalTension](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/gravitational-tension/) | L64-L73 | type/data schema | type/data schema | `V.D163` |
| `def` | [GravitationalTension.toFloat](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/to-float/) | L76-L77 | data/computed value | data/computed value | — |
| `structure` | [SphericalCapacity](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/spherical-capacity/) | L88-L99 | type/data schema | type/data schema | `V.D164` |
| `structure` | [LinkingClass](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/linking-class/) | L110-L117 | type/data schema | type/data schema | `V.D165` |
| `def` | [unit_linking](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/unit-linking/) | L120-L123 | definition | definition | — |
| `inductive` | [HorizonTopology](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/horizon-topology/) | L130-L135 | type/data schema | type/data schema | — |
| `structure` | [BlackHoleTopologicalEvent](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/black-hole-topological-event/) | L143-L154 | type/data schema | type/data schema | `V.D166` |
| `theorem` | [bh_threshold_theorem](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-threshold-theorem/) | L166-L168 | proof obligation | formal proof obligation checked | `V.T109` |
| `theorem` | [bh_toroidal_topology](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-topology/) | L179-L181 | proof obligation | formal proof obligation checked | `V.T110` |
| `theorem` | [no_interior_singularity](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/no-interior-singularity/) | L191-L193 | proof obligation | formal proof obligation checked | `V.P93` |
| `theorem` | [information_preservation](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/information-preservation/) | L204-L206 | proof obligation | formal proof obligation checked | `V.C18` |
| `structure` | [CanonicalBHNeighborhood](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/canonical-bhneighborhood/) | L217-L226 | type/data schema | type/data schema | `V.D167` |
| `def` | [example_bh](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/example-bh/) | L242-L245 | definition | definition | — |
| `eval` | [#eval L247](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l247/) | L247-L247 | computed check | computed check | — |
| `eval` | [#eval L248](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l248/) | L248-L248 | computed check | computed check | — |
| `eval` | [#eval L249](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l249/) | L249-L249 | computed check | computed check | — |
| `eval` | [#eval L250](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l250/) | L250-L250 | computed check | computed check | — |
| `eval` | [#eval L251](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l251/) | L251-L251 | computed check | computed check | — |
| `structure` | [FiberShapeRatio](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio/) | L274-L285 | type/data schema | type/data schema | — |
| `def` | [fiber_shape_ratio](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio-l287/) | L287-L287 | definition | definition | — |
| `theorem` | [fiber_shape_ratio_structural](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio-structural/) | L290-L294 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bh_toroidal_structural](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-structural/) | L310-L311 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_singularity_from_linking](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/no-singularity-from-linking/) | L316-L321 | proof obligation | formal proof obligation checked | — |
| `structure` | [InformationPreservationStructural](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/information-preservation-structural/) | L327-L334 | type/data schema | type/data schema | — |
| `def` | [info_preservation_structural](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/info-preservation-structural/) | L336-L336 | definition | definition | — |
| `theorem` | [info_preservation_thm](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/info-preservation-thm/) | L338-L341 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L344](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l344/) | L344-L344 | computed check | computed check | — |
| `eval` | [#eval L345](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l345/) | L345-L345 | computed check | computed check | — |
| `eval` | [#eval L346](/corpus/taulib/docs/book-v-cosmology-bhbirth-topology/eval-l346/) | L346-L348 | computed check | computed check | — |
