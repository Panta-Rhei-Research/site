---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.TickUnits",
  "permalink": "/corpus/taulib/docs/book-iv-physics-tick-units/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.TickUnits`.",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_slug": "book-iv-physics-tick-units",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/TickUnits.lean",
  "sha256": "eb4896891ba2afab2cdb14fd35546524702432b27085255c12d4ab20494a31df",
  "imports": [
    "TauLib.BookIV.Physics.QuantityFramework"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Physics.InternalEquations"
  ],
  "registry_ids": [
    "IV.D321",
    "IV.D322",
    "IV.T125",
    "IV.T126"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 2,
    "def": 6,
    "theorem": 5,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "TickKind",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/tick-kind/",
      "source_line_start": 54,
      "source_line_end": 70,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D322"
      ]
    },
    {
      "kind": "structure",
      "name": "TickMorphism",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/tick-morphism/",
      "source_line_start": 82,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D321"
      ]
    },
    {
      "kind": "def",
      "name": "TickMorphism.identity",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/identity/",
      "source_line_start": 91,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickMorphism.compose",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/compose/",
      "source_line_start": 96,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.sector",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/sector/",
      "source_line_start": 106,
      "source_line_end": 111,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.carrier",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/carrier/",
      "source_line_start": 114,
      "source_line_end": 119,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.measuredInvariant",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/measured-invariant/",
      "source_line_start": 122,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tick_sector_bijection",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/tick-sector-bijection/",
      "source_line_start": 135,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T125"
      ]
    },
    {
      "kind": "theorem",
      "name": "tick_exhaustion",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/tick-exhaustion/",
      "source_line_start": 149,
      "source_line_end": 152,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T126"
      ]
    },
    {
      "kind": "theorem",
      "name": "tick_sector_consistent_with_invariant",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/tick-sector-consistent-with-invariant/",
      "source_line_start": 155,
      "source_line_end": 157,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "identity_count",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/identity-count/",
      "source_line_start": 160,
      "source_line_end": 161,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_count",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/compose-count/",
      "source_line_start": 164,
      "source_line_end": 165,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InternalRatio",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/internal-ratio/",
      "source_line_start": 174,
      "source_line_end": 185,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "InternalRatio.isDimensionless",
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/is-dimensionless/",
      "source_line_start": 188,
      "source_line_end": 189,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/eval-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-tick-units/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 199,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean",
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
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/TickUnits.lean`
- SHA-256: `eb4896891ba2afab2cdb14fd35546524702432b27085255c12d4ab20494a31df`

## Registry Links

- `IV.D321` — Tick Morphism
- `IV.D322` — Tick Kind
- `IV.T125` — Tick-Sector Bijection
- `IV.T126` — Tick Exhaustion

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.QuantityFramework`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Physics.InternalEquations`

## Declaration Counts

- `def`: 6
- `eval`: 3
- `inductive`: 1
- `structure`: 2
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [TickKind](/corpus/taulib/docs/book-iv-physics-tick-units/tick-kind/) | L54-L70 | type/data schema | type/data schema | `IV.D322` |
| `structure` | [TickMorphism](/corpus/taulib/docs/book-iv-physics-tick-units/tick-morphism/) | L82-L88 | type/data schema | type/data schema | `IV.D321` |
| `def` | [TickMorphism.identity](/corpus/taulib/docs/book-iv-physics-tick-units/identity/) | L91-L93 | definition | definition | — |
| `def` | [TickMorphism.compose](/corpus/taulib/docs/book-iv-physics-tick-units/compose/) | L96-L99 | definition | definition | — |
| `def` | [TickKind.sector](/corpus/taulib/docs/book-iv-physics-tick-units/sector/) | L106-L111 | definition | definition | — |
| `def` | [TickKind.carrier](/corpus/taulib/docs/book-iv-physics-tick-units/carrier/) | L114-L119 | definition | definition | — |
| `def` | [TickKind.measuredInvariant](/corpus/taulib/docs/book-iv-physics-tick-units/measured-invariant/) | L122-L127 | definition | definition | — |
| `theorem` | [tick_sector_bijection](/corpus/taulib/docs/book-iv-physics-tick-units/tick-sector-bijection/) | L135-L146 | proof obligation | formal proof obligation checked | `IV.T125` |
| `theorem` | [tick_exhaustion](/corpus/taulib/docs/book-iv-physics-tick-units/tick-exhaustion/) | L149-L152 | proof obligation | formal proof obligation checked | `IV.T126` |
| `theorem` | [tick_sector_consistent_with_invariant](/corpus/taulib/docs/book-iv-physics-tick-units/tick-sector-consistent-with-invariant/) | L155-L157 | proof obligation | formal proof obligation checked | — |
| `theorem` | [identity_count](/corpus/taulib/docs/book-iv-physics-tick-units/identity-count/) | L160-L161 | proof obligation | formal proof obligation checked | — |
| `theorem` | [compose_count](/corpus/taulib/docs/book-iv-physics-tick-units/compose-count/) | L164-L165 | proof obligation | formal proof obligation checked | — |
| `structure` | [InternalRatio](/corpus/taulib/docs/book-iv-physics-tick-units/internal-ratio/) | L174-L185 | type/data schema | type/data schema | — |
| `def` | [InternalRatio.isDimensionless](/corpus/taulib/docs/book-iv-physics-tick-units/is-dimensionless/) | L188-L189 | data/computed value | data/computed value | — |
| `eval` | [#eval L195](/corpus/taulib/docs/book-iv-physics-tick-units/eval-l195/) | L195-L195 | computed check | computed check | — |
| `eval` | [#eval L196](/corpus/taulib/docs/book-iv-physics-tick-units/eval-l196/) | L196-L196 | computed check | computed check | — |
| `eval` | [#eval L197](/corpus/taulib/docs/book-iv-physics-tick-units/eval-l197/) | L197-L199 | computed check | computed check | — |
