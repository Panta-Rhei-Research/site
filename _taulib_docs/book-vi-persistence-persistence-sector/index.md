---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Persistence.PersistenceSector",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Persistence.PersistenceSector`.",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_slug": "book-vi-persistence-persistence-sector",
  "book": "BookVI",
  "family": "Persistence",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Persistence/PersistenceSector.lean",
  "sha256": "db13bfc5dd2d517b5a2c555c2f72ef3cb2df96c1cb2d73919d0db89362712776",
  "imports": [
    "TauLib.BookVI.Sectors.FourPlusOne"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.Persistence.TemporalLemniscate"
  ],
  "registry_ids": [
    "VI.D24",
    "VI.D25",
    "VI.D26",
    "VI.D74",
    "VI.D75",
    "VI.D76",
    "VI.D77",
    "VI.L15",
    "VI.L16",
    "VI.P08",
    "VI.R27",
    "VI.R28",
    "VI.T16",
    "VI.T44",
    "VI.T45",
    "VI.T46"
  ],
  "declaration_counts": {
    "structure": 16,
    "def": 11,
    "theorem": 12
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PersistenceSectorDef",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-sector-def/",
      "source_line_start": 51,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D24"
      ]
    },
    {
      "kind": "def",
      "name": "persistence_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-def/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "persistence_generator_match",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-generator-match/",
      "source_line_start": 67,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TemporalStabilityPredicate",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-predicate/",
      "source_line_start": 79,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D25"
      ]
    },
    {
      "kind": "def",
      "name": "temporal_stability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_stability_three_conditions",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-three-conditions/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_stability_all_hold",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-all-hold/",
      "source_line_start": 100,
      "source_line_end": 104,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PersistenceStability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-stability/",
      "source_line_start": 114,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T16"
      ]
    },
    {
      "kind": "def",
      "name": "pers_stability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/pers-stability/",
      "source_line_start": 125,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "persistence_is_alpha_stability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-is-alpha-stability/",
      "source_line_start": 129,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AbiogenesisDef",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-def/",
      "source_line_start": 141,
      "source_line_end": 148,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D26"
      ]
    },
    {
      "kind": "structure",
      "name": "ThermodynamicInevitability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/thermodynamic-inevitability/",
      "source_line_start": 159,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": [
        "VI.P08"
      ]
    },
    {
      "kind": "def",
      "name": "thermo_inev",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/thermo-inev/",
      "source_line_start": 174,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "thermodynamic_inevitability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/thermodynamic-inevitability-l178/",
      "source_line_start": 178,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FarFromEquilibriumRegime",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium-regime/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D74"
      ]
    },
    {
      "kind": "def",
      "name": "far_from_equilibrium",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium/",
      "source_line_start": 204,
      "source_line_end": 204,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "far_from_equilibrium_conditions",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium-conditions/",
      "source_line_start": 206,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ComplexityBudget",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-budget/",
      "source_line_start": 220,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D75"
      ]
    },
    {
      "kind": "structure",
      "name": "ComplexityMonotone",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone/",
      "source_line_start": 237,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": [
        "VI.L15"
      ]
    },
    {
      "kind": "def",
      "name": "complexity_monotone_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone-def/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "complexity_monotone",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone-l250/",
      "source_line_start": 250,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DistinctionThreshold",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/distinction-threshold/",
      "source_line_start": 263,
      "source_line_end": 274,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D76"
      ]
    },
    {
      "kind": "def",
      "name": "distinction_threshold",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/distinction-threshold-l276/",
      "source_line_start": 276,
      "source_line_end": 278,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "threshold_is_sum",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/threshold-is-sum/",
      "source_line_start": 280,
      "source_line_end": 283,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AttractorExistence",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence/",
      "source_line_start": 296,
      "source_line_end": 311,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T44"
      ]
    },
    {
      "kind": "def",
      "name": "attractor_existence_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence-def/",
      "source_line_start": 313,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "attractor_existence",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence-l317/",
      "source_line_start": 317,
      "source_line_end": 323,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BasinAbsorbing",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-absorbing/",
      "source_line_start": 333,
      "source_line_end": 342,
      "formal_status": "defined",
      "registry_ids": [
        "VI.L16"
      ]
    },
    {
      "kind": "def",
      "name": "basin_absorbing_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-absorbing-def/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "basin_is_absorbing",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-is-absorbing/",
      "source_line_start": 346,
      "source_line_end": 350,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AbiogenesisTimescaleBound",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-timescale-bound/",
      "source_line_start": 361,
      "source_line_end": 370,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D77"
      ]
    },
    {
      "kind": "structure",
      "name": "TimescaleFromHalfLife",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-from-half-life/",
      "source_line_start": 381,
      "source_line_end": 390,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T45"
      ]
    },
    {
      "kind": "def",
      "name": "timescale_half_life_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-half-life-def/",
      "source_line_start": 392,
      "source_line_end": 392,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "timescale_from_half_life",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-from-half-life-l394/",
      "source_line_start": 394,
      "source_line_end": 396,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TimescaleGeologicalConsistency",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-geological-consistency/",
      "source_line_start": 407,
      "source_line_end": 416,
      "formal_status": "defined",
      "registry_ids": [
        "VI.R27"
      ]
    },
    {
      "kind": "structure",
      "name": "AbiogenesisInevitability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability/",
      "source_line_start": 431,
      "source_line_end": 446,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T46"
      ]
    },
    {
      "kind": "def",
      "name": "abiogenesis_inevitability_def",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability-def/",
      "source_line_start": 448,
      "source_line_end": 450,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "abiogenesis_inevitability",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability-l452/",
      "source_line_start": 452,
      "source_line_end": 458,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AbiogenesisNotContingent",
      "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-not-contingent/",
      "source_line_start": 469,
      "source_line_end": 480,
      "formal_status": "defined",
      "registry_ids": [
        "VI.R28"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Persistence/PersistenceSector.lean`
- SHA-256: `db13bfc5dd2d517b5a2c555c2f72ef3cb2df96c1cb2d73919d0db89362712776`

## Registry Links

- `VI.D24` — Persistence Sector
- `VI.D25` — Temporal Stability Predicate
- `VI.D26` — Abiogenesis as First Persistence Event
- `VI.D74` — Far-From-Equilibrium Regime
- `VI.D75` — Complexity Budget
- `VI.D76` — Distinction Threshold
- `VI.D77` — Abiogenesis Timescale Bound
- `VI.L15` — Complexity Monotone
- `VI.L16` — Basin Is Absorbing
- `VI.P08` — Thermodynamic Inevitability of Life
- `VI.R27` — Geological Consistency
- `VI.R28` — Abiogenesis is not contingent
- `VI.T16` — Persistence as α-Base Stability
- `VI.T44` — Attractor Existence
- `VI.T45` — Timescale From Half-Life
- `VI.T46` — Abiogenesis Inevitability

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.Sectors.FourPlusOne`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.Persistence.TemporalLemniscate`

## Declaration Counts

- `def`: 11
- `structure`: 16
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [PersistenceSectorDef](/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-sector-def/) | L51-L62 | defined | `VI.D24` |
| `def` | [persistence_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-def/) | L64-L64 | defined | — |
| `theorem` | [persistence_generator_match](/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-generator-match/) | L67-L69 | formalized | — |
| `structure` | [TemporalStabilityPredicate](/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-predicate/) | L79-L90 | defined | `VI.D25` |
| `def` | [temporal_stability](/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability/) | L92-L94 | defined | — |
| `theorem` | [temporal_stability_three_conditions](/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-three-conditions/) | L96-L98 | formalized | — |
| `theorem` | [temporal_stability_all_hold](/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-all-hold/) | L100-L104 | formalized | — |
| `structure` | [PersistenceStability](/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-stability/) | L114-L123 | defined | `VI.T16` |
| `def` | [pers_stability](/verify/taulib/docs/book-vi-persistence-persistence-sector/pers-stability/) | L125-L127 | defined | — |
| `theorem` | [persistence_is_alpha_stability](/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-is-alpha-stability/) | L129-L133 | formalized | — |
| `structure` | [AbiogenesisDef](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-def/) | L141-L148 | defined | `VI.D26` |
| `structure` | [ThermodynamicInevitability](/verify/taulib/docs/book-vi-persistence-persistence-sector/thermodynamic-inevitability/) | L159-L172 | defined | `VI.P08` |
| `def` | [thermo_inev](/verify/taulib/docs/book-vi-persistence-persistence-sector/thermo-inev/) | L174-L176 | defined | — |
| `theorem` | [thermodynamic_inevitability](/verify/taulib/docs/book-vi-persistence-persistence-sector/thermodynamic-inevitability-l178/) | L178-L183 | formalized | — |
| `structure` | [FarFromEquilibriumRegime](/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium-regime/) | L193-L202 | defined | `VI.D74` |
| `def` | [far_from_equilibrium](/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium/) | L204-L204 | defined | — |
| `theorem` | [far_from_equilibrium_conditions](/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium-conditions/) | L206-L210 | formalized | — |
| `structure` | [ComplexityBudget](/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-budget/) | L220-L227 | defined | `VI.D75` |
| `structure` | [ComplexityMonotone](/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone/) | L237-L246 | defined | `VI.L15` |
| `def` | [complexity_monotone_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone-def/) | L248-L248 | defined | — |
| `theorem` | [complexity_monotone](/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone-l250/) | L250-L253 | formalized | — |
| `structure` | [DistinctionThreshold](/verify/taulib/docs/book-vi-persistence-persistence-sector/distinction-threshold/) | L263-L274 | defined | `VI.D76` |
| `def` | [distinction_threshold](/verify/taulib/docs/book-vi-persistence-persistence-sector/distinction-threshold-l276/) | L276-L278 | defined | — |
| `theorem` | [threshold_is_sum](/verify/taulib/docs/book-vi-persistence-persistence-sector/threshold-is-sum/) | L280-L283 | formalized | — |
| `structure` | [AttractorExistence](/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence/) | L296-L311 | defined | `VI.T44` |
| `def` | [attractor_existence_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence-def/) | L313-L315 | defined | — |
| `theorem` | [attractor_existence](/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence-l317/) | L317-L323 | formalized | — |
| `structure` | [BasinAbsorbing](/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-absorbing/) | L333-L342 | defined | `VI.L16` |
| `def` | [basin_absorbing_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-absorbing-def/) | L344-L344 | defined | — |
| `theorem` | [basin_is_absorbing](/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-is-absorbing/) | L346-L350 | formalized | — |
| `structure` | [AbiogenesisTimescaleBound](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-timescale-bound/) | L361-L370 | defined | `VI.D77` |
| `structure` | [TimescaleFromHalfLife](/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-from-half-life/) | L381-L390 | defined | `VI.T45` |
| `def` | [timescale_half_life_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-half-life-def/) | L392-L392 | defined | — |
| `theorem` | [timescale_from_half_life](/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-from-half-life-l394/) | L394-L396 | formalized | — |
| `structure` | [TimescaleGeologicalConsistency](/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-geological-consistency/) | L407-L416 | defined | `VI.R27` |
| `structure` | [AbiogenesisInevitability](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability/) | L431-L446 | defined | `VI.T46` |
| `def` | [abiogenesis_inevitability_def](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability-def/) | L448-L450 | defined | — |
| `theorem` | [abiogenesis_inevitability](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability-l452/) | L452-L458 | formalized | — |
| `structure` | [AbiogenesisNotContingent](/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-not-contingent/) | L469-L480 | defined | `VI.R28` |
