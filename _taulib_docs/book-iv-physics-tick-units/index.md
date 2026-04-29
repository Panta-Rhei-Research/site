---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.TickUnits",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/",
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
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/tick-kind/",
      "source_line_start": 54,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D322"
      ]
    },
    {
      "kind": "structure",
      "name": "TickMorphism",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/tick-morphism/",
      "source_line_start": 82,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D321"
      ]
    },
    {
      "kind": "def",
      "name": "TickMorphism.identity",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/identity/",
      "source_line_start": 91,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickMorphism.compose",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/compose/",
      "source_line_start": 96,
      "source_line_end": 99,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.sector",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/sector/",
      "source_line_start": 106,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.carrier",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/carrier/",
      "source_line_start": 114,
      "source_line_end": 119,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TickKind.measuredInvariant",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/measured-invariant/",
      "source_line_start": 122,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tick_sector_bijection",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/tick-sector-bijection/",
      "source_line_start": 135,
      "source_line_end": 146,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T125"
      ]
    },
    {
      "kind": "theorem",
      "name": "tick_exhaustion",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/tick-exhaustion/",
      "source_line_start": 149,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T126"
      ]
    },
    {
      "kind": "theorem",
      "name": "tick_sector_consistent_with_invariant",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/tick-sector-consistent-with-invariant/",
      "source_line_start": 155,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "identity_count",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/identity-count/",
      "source_line_start": 160,
      "source_line_end": 161,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_count",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/compose-count/",
      "source_line_start": 164,
      "source_line_end": 165,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InternalRatio",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/internal-ratio/",
      "source_line_start": 174,
      "source_line_end": 185,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "InternalRatio.isDimensionless",
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/is-dimensionless/",
      "source_line_start": 188,
      "source_line_end": 189,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/eval-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-tick-units/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 199,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [TickKind](/verify/taulib/docs/book-iv-physics-tick-units/tick-kind/) | L54-L70 | defined | `IV.D322` |
| `structure` | [TickMorphism](/verify/taulib/docs/book-iv-physics-tick-units/tick-morphism/) | L82-L88 | defined | `IV.D321` |
| `def` | [TickMorphism.identity](/verify/taulib/docs/book-iv-physics-tick-units/identity/) | L91-L93 | defined | — |
| `def` | [TickMorphism.compose](/verify/taulib/docs/book-iv-physics-tick-units/compose/) | L96-L99 | defined | — |
| `def` | [TickKind.sector](/verify/taulib/docs/book-iv-physics-tick-units/sector/) | L106-L111 | defined | — |
| `def` | [TickKind.carrier](/verify/taulib/docs/book-iv-physics-tick-units/carrier/) | L114-L119 | defined | — |
| `def` | [TickKind.measuredInvariant](/verify/taulib/docs/book-iv-physics-tick-units/measured-invariant/) | L122-L127 | defined | — |
| `theorem` | [tick_sector_bijection](/verify/taulib/docs/book-iv-physics-tick-units/tick-sector-bijection/) | L135-L146 | formalized | `IV.T125` |
| `theorem` | [tick_exhaustion](/verify/taulib/docs/book-iv-physics-tick-units/tick-exhaustion/) | L149-L152 | formalized | `IV.T126` |
| `theorem` | [tick_sector_consistent_with_invariant](/verify/taulib/docs/book-iv-physics-tick-units/tick-sector-consistent-with-invariant/) | L155-L157 | formalized | — |
| `theorem` | [identity_count](/verify/taulib/docs/book-iv-physics-tick-units/identity-count/) | L160-L161 | formalized | — |
| `theorem` | [compose_count](/verify/taulib/docs/book-iv-physics-tick-units/compose-count/) | L164-L165 | formalized | — |
| `structure` | [InternalRatio](/verify/taulib/docs/book-iv-physics-tick-units/internal-ratio/) | L174-L185 | defined | — |
| `def` | [InternalRatio.isDimensionless](/verify/taulib/docs/book-iv-physics-tick-units/is-dimensionless/) | L188-L189 | defined | — |
| `eval` | [#eval L195](/verify/taulib/docs/book-iv-physics-tick-units/eval-l195/) | L195-L195 | computed | — |
| `eval` | [#eval L196](/verify/taulib/docs/book-iv-physics-tick-units/eval-l196/) | L196-L196 | computed | — |
| `eval` | [#eval L197](/verify/taulib/docs/book-iv-physics-tick-units/eval-l197/) | L197-L199 | computed | — |
