---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Arena.FiveSectors",
  "permalink": "/corpus/taulib/docs/book-iv-arena-five-sectors/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Arena.FiveSectors`.",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_slug": "book-iv-arena-five-sectors",
  "book": "BookIV",
  "family": "Arena",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Arena/FiveSectors.lean",
  "sha256": "7ebf88b7c9c2a7bb4383bb54a3cba5e190584d7d835345513305d90c4496ebea",
  "imports": [
    "TauLib.BookIV.Arena.BoundaryHolonomy",
    "TauLib.BookIV.Sectors.CouplingFormulas"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.ActorsDynamics",
    "TauLib.BookV.Prologue.HermeticPrinciple",
    "TauLib.BookV.Temporal.HighEnergy",
    "TauLib.BookVI.LifeCore.ParityBridge"
  ],
  "registry_ids": [
    "IV.D264",
    "IV.D265",
    "IV.D266",
    "IV.P154",
    "IV.P155",
    "IV.P156",
    "IV.R225",
    "IV.R226",
    "IV.T100",
    "IV.T101",
    "IV.T98",
    "IV.T99"
  ],
  "declaration_counts": {
    "theorem": 5,
    "structure": 4,
    "def": 2,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "phi_unique",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/phi-unique/",
      "source_line_start": 48,
      "source_line_end": 52,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T98"
      ]
    },
    {
      "kind": "structure",
      "name": "CouplingEntry",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/coupling-entry/",
      "source_line_start": 59,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D265"
      ]
    },
    {
      "kind": "structure",
      "name": "CouplingLedger",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/coupling-ledger/",
      "source_line_start": 73,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D265"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_complement",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/temporal-complement/",
      "source_line_start": 88,
      "source_line_end": 90,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.R225",
        "IV.T99"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_mult_closure",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/temporal-mult-closure/",
      "source_line_start": 98,
      "source_line_end": 101,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P154"
      ]
    },
    {
      "kind": "theorem",
      "name": "power_hier",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/power-hier/",
      "source_line_start": 113,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P156"
      ]
    },
    {
      "kind": "structure",
      "name": "NoRunning",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/no-running/",
      "source_line_start": 132,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T100"
      ]
    },
    {
      "kind": "def",
      "name": "no_running",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/no-running-l142/",
      "source_line_start": 142,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolonomyGenerator",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/holonomy-generator/",
      "source_line_start": 154,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D266"
      ]
    },
    {
      "kind": "def",
      "name": "holonomy_generators",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/holonomy-generators/",
      "source_line_start": 164,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "generator_adequacy",
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/generator-adequacy/",
      "source_line_start": 175,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T101"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l186/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l187/",
      "source_line_start": 187,
      "source_line_end": 189,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean",
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
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Arena/FiveSectors.lean`
- SHA-256: `7ebf88b7c9c2a7bb4383bb54a3cba5e190584d7d835345513305d90c4496ebea`

## Registry Links

- `IV.D264` — Generator--Sector Correspondence
- `IV.D265` — Coupling Ledger
- `IV.D266` — Boundary holonomy generators
- `IV.P154` — Temporal Multiplicative Closure
- `IV.P155` — Multiplicative Closure
- `IV.P156` — Power Hierarchy
- `IV.R225` — Physical meaning
- `IV.R226` — Power structure
- `IV.T100` — No-Running Principle
- `IV.T101` — Generator Adequacy
- `IV.T98` — Uniqueness of Phi
- `IV.T99` — Temporal Complement

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.BoundaryHolonomy`
- `TauLib.BookIV.Sectors.CouplingFormulas`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.ActorsDynamics`
- `TauLib.BookV.Prologue.HermeticPrinciple`
- `TauLib.BookV.Temporal.HighEnergy`
- `TauLib.BookVI.LifeCore.ParityBridge`

## Declaration Counts

- `def`: 2
- `eval`: 3
- `structure`: 4
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `theorem` | [phi_unique](/corpus/taulib/docs/book-iv-arena-five-sectors/phi-unique/) | L48-L52 | proof obligation | formal proof obligation checked | `IV.T98` |
| `structure` | [CouplingEntry](/corpus/taulib/docs/book-iv-arena-five-sectors/coupling-entry/) | L59-L69 | type/data schema | type/data schema | `IV.D265` |
| `structure` | [CouplingLedger](/corpus/taulib/docs/book-iv-arena-five-sectors/coupling-ledger/) | L73-L79 | type/data schema | type/data schema | `IV.D265` |
| `theorem` | [temporal_complement](/corpus/taulib/docs/book-iv-arena-five-sectors/temporal-complement/) | L88-L90 | proof obligation | formal proof obligation checked | `IV.R225`, `IV.T99` |
| `theorem` | [temporal_mult_closure](/corpus/taulib/docs/book-iv-arena-five-sectors/temporal-mult-closure/) | L98-L101 | proof obligation | formal proof obligation checked | `IV.P154` |
| `theorem` | [power_hier](/corpus/taulib/docs/book-iv-arena-five-sectors/power-hier/) | L113-L120 | proof obligation | formal proof obligation checked | `IV.P156` |
| `structure` | [NoRunning](/corpus/taulib/docs/book-iv-arena-five-sectors/no-running/) | L132-L139 | type/data schema | type/data schema | `IV.T100` |
| `def` | [no_running](/corpus/taulib/docs/book-iv-arena-five-sectors/no-running-l142/) | L142-L146 | definition | definition | — |
| `structure` | [HolonomyGenerator](/corpus/taulib/docs/book-iv-arena-five-sectors/holonomy-generator/) | L154-L161 | type/data schema | type/data schema | `IV.D266` |
| `def` | [holonomy_generators](/corpus/taulib/docs/book-iv-arena-five-sectors/holonomy-generators/) | L164-L166 | data/computed value | data/computed value | — |
| `theorem` | [generator_adequacy](/corpus/taulib/docs/book-iv-arena-five-sectors/generator-adequacy/) | L175-L179 | proof obligation | formal proof obligation checked | `IV.T101` |
| `eval` | [#eval L185](/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l185/) | L185-L185 | computed check | computed check | — |
| `eval` | [#eval L186](/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l186/) | L186-L186 | computed check | computed check | — |
| `eval` | [#eval L187](/corpus/taulib/docs/book-iv-arena-five-sectors/eval-l187/) | L187-L189 | computed check | computed check | — |
