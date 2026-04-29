---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Consumer.Evolution",
  "permalink": "/verify/taulib/docs/book-vi-consumer-evolution/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Consumer.Evolution`.",
  "module_name": "TauLib.BookVI.Consumer.Evolution",
  "module_slug": "book-vi-consumer-evolution",
  "book": "BookVI",
  "family": "Consumer",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Consumer/Evolution.lean",
  "sha256": "41c199ad9c33ff5113cf843351e3c64f37928371697e0758805313ee0fd2ee20",
  "imports": [
    "TauLib.BookVI.Consumer.Reproduction"
  ],
  "imported_by": [
    "TauLib.BookVI"
  ],
  "registry_ids": [
    "VI.D50",
    "VI.R20",
    "VI.T27"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 3,
    "theorem": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PPASFitness",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/ppasfitness/",
      "source_line_start": 35,
      "source_line_end": 44,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D50"
      ]
    },
    {
      "kind": "def",
      "name": "ppas_fit",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/ppas-fit/",
      "source_line_start": 46,
      "source_line_end": 46,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EvolutionOptimization",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/evolution-optimization/",
      "source_line_start": 56,
      "source_line_end": 71,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T27"
      ]
    },
    {
      "kind": "def",
      "name": "evo_opt",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/evo-opt/",
      "source_line_start": 73,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "evolution_is_ppas",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/evolution-is-ppas/",
      "source_line_start": 77,
      "source_line_end": 81,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ppas_polynomial_convergence",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/ppas-polynomial-convergence/",
      "source_line_start": 83,
      "source_line_end": 86,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FitnessLandscapeTopology",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-topology/",
      "source_line_start": 96,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "VI.R20"
      ]
    },
    {
      "kind": "def",
      "name": "fitness_topo",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/fitness-topo/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fitness_landscape_rugged",
      "url": "/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-rugged/",
      "source_line_start": 107,
      "source_line_end": 113,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean",
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
- Source path: [`TauLib/BookVI/Consumer/Evolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Consumer/Evolution.lean`
- SHA-256: `41c199ad9c33ff5113cf843351e3c64f37928371697e0758805313ee0fd2ee20`

## Registry Links

- `VI.D50` — PPAS Algorithm on Fitness Landscapes
- `VI.R20` — Fitness Landscape Topology
- `VI.T27` — Evolution as Optimization

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.Consumer.Reproduction`

## Imported By

- `TauLib.BookVI`

## Declaration Counts

- `def`: 3
- `structure`: 3
- `theorem`: 3

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [PPASFitness](/verify/taulib/docs/book-vi-consumer-evolution/ppasfitness/) | L35-L44 | defined | `VI.D50` |
| `def` | [ppas_fit](/verify/taulib/docs/book-vi-consumer-evolution/ppas-fit/) | L46-L46 | defined | — |
| `structure` | [EvolutionOptimization](/verify/taulib/docs/book-vi-consumer-evolution/evolution-optimization/) | L56-L71 | defined | `VI.T27` |
| `def` | [evo_opt](/verify/taulib/docs/book-vi-consumer-evolution/evo-opt/) | L73-L75 | defined | — |
| `theorem` | [evolution_is_ppas](/verify/taulib/docs/book-vi-consumer-evolution/evolution-is-ppas/) | L77-L81 | formalized | — |
| `theorem` | [ppas_polynomial_convergence](/verify/taulib/docs/book-vi-consumer-evolution/ppas-polynomial-convergence/) | L83-L86 | formalized | — |
| `structure` | [FitnessLandscapeTopology](/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-topology/) | L96-L103 | defined | `VI.R20` |
| `def` | [fitness_topo](/verify/taulib/docs/book-vi-consumer-evolution/fitness-topo/) | L105-L105 | defined | — |
| `theorem` | [fitness_landscape_rugged](/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-rugged/) | L107-L113 | formalized | — |
