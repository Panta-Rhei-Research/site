---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_slug": "book-v-astrophysics-sector-exhaustion",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/SectorExhaustion.lean",
  "sha256": "4d9feb6e0d64ea9ffae9fe31ae4e89fa50e3d9fe6784e9c1e9df382ae8275aa4",
  "imports": [
    "TauLib.BookV.Astrophysics.BulletClusterLSS"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.H0TensionLCDM"
  ],
  "registry_ids": [
    "V.C14",
    "V.C15",
    "V.C16",
    "V.D144",
    "V.D145",
    "V.D146",
    "V.D147",
    "V.P86",
    "V.P87",
    "V.R202",
    "V.R203",
    "V.R204",
    "V.T100",
    "V.T99"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 4,
    "theorem": 7,
    "structure": 3,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "AstroPhenomenon",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/astro-phenomenon/",
      "source_line_start": 71,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D144"
      ]
    },
    {
      "kind": "inductive",
      "name": "SectorLabel",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-label/",
      "source_line_start": 103,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primarySectors",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/primary-sectors/",
      "source_line_start": 112,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_assignment",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-assignment/",
      "source_line_start": 127,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P86"
      ]
    },
    {
      "kind": "structure",
      "name": "SectorExhaustionMap",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-exhaustion-map/",
      "source_line_start": 137,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D145"
      ]
    },
    {
      "kind": "theorem",
      "name": "exhaustion_theorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/exhaustion-theorem/",
      "source_line_start": 158,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T99"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_orphan_phenomenon",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/no-orphan-phenomenon/",
      "source_line_start": 171,
      "source_line_end": 173,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T100"
      ]
    },
    {
      "kind": "theorem",
      "name": "d_covers_gravity",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/d-covers-gravity/",
      "source_line_start": 180,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C14"
      ]
    },
    {
      "kind": "theorem",
      "name": "b_covers_em",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/b-covers-em/",
      "source_line_start": 185,
      "source_line_end": 187,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C15"
      ]
    },
    {
      "kind": "theorem",
      "name": "c_covers_nuclear",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/c-covers-nuclear/",
      "source_line_start": 190,
      "source_line_end": 192,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C16"
      ]
    },
    {
      "kind": "structure",
      "name": "MultiSectorPhenomenon",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/multi-sector-phenomenon/",
      "source_line_start": 200,
      "source_line_end": 205,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D146"
      ]
    },
    {
      "kind": "def",
      "name": "stellar_multi",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/stellar-multi/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bbn_multi",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/bbn-multi/",
      "source_line_start": 213,
      "source_line_end": 215,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorCoverageSummary",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-coverage-summary/",
      "source_line_start": 223,
      "source_line_end": 236,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D147"
      ]
    },
    {
      "kind": "def",
      "name": "coverage_summary",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/coverage-summary/",
      "source_line_start": 239,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_bsm_astro",
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/no-bsm-astro/",
      "source_line_start": 259,
      "source_line_end": 261,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P87"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R202",
        "V.R203",
        "V.R204"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 290,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/SectorExhaustion.lean`
- SHA-256: `4d9feb6e0d64ea9ffae9fe31ae4e89fa50e3d9fe6784e9c1e9df382ae8275aa4`

## Registry Links

- `V.C14` — No Dark Matter Particle
- `V.C15` — No Dark Energy Field
- `V.C16` — No Fifth Force
- `V.D144` — Sector Budget
- `V.D145` — Sector Exhaustion Decomposition
- `V.D146` — Dark Sector Hypothesis
- `V.D147` — Readout Artifact
- `V.P86` — Coupling Budget Completeness
- `V.P87` — LCDM Budget Translation
- `V.R202` — Minimal Alphabet and Sector Count
- `V.R203` — From "Not Needed" to "Not Possible"
- `V.R204` — What 68% and 27% Actually Are
- `V.T100` — No Fifth Sector
- `V.T99` — Sector Exhaustion Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.BulletClusterLSS`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.H0TensionLCDM`

## Declaration Counts

- `def`: 4
- `eval`: 4
- `inductive`: 2
- `structure`: 3
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [AstroPhenomenon](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/astro-phenomenon/) | L71-L96 | type/data schema | type/data schema | `V.D144` |
| `inductive` | [SectorLabel](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-label/) | L103-L109 | type/data schema | type/data schema | — |
| `def` | [primarySectors](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/primary-sectors/) | L112-L124 | definition | definition | — |
| `theorem` | [sector_assignment](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-assignment/) | L127-L129 | proof obligation | formal proof obligation checked | `V.P86` |
| `structure` | [SectorExhaustionMap](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-exhaustion-map/) | L137-L146 | type/data schema | type/data schema | `V.D145` |
| `theorem` | [exhaustion_theorem](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/exhaustion-theorem/) | L158-L160 | proof obligation | formal proof obligation checked | `V.T99` |
| `theorem` | [no_orphan_phenomenon](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/no-orphan-phenomenon/) | L171-L173 | proof obligation | formal proof obligation checked | `V.T100` |
| `theorem` | [d_covers_gravity](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/d-covers-gravity/) | L180-L182 | proof obligation | formal proof obligation checked | `V.C14` |
| `theorem` | [b_covers_em](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/b-covers-em/) | L185-L187 | proof obligation | formal proof obligation checked | `V.C15` |
| `theorem` | [c_covers_nuclear](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/c-covers-nuclear/) | L190-L192 | proof obligation | formal proof obligation checked | `V.C16` |
| `structure` | [MultiSectorPhenomenon](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/multi-sector-phenomenon/) | L200-L205 | type/data schema | type/data schema | `V.D146` |
| `def` | [stellar_multi](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/stellar-multi/) | L208-L210 | definition | definition | — |
| `def` | [bbn_multi](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/bbn-multi/) | L213-L215 | definition | definition | — |
| `structure` | [SectorCoverageSummary](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-coverage-summary/) | L223-L236 | type/data schema | type/data schema | `V.D147` |
| `def` | [coverage_summary](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/coverage-summary/) | L239-L245 | definition | definition | — |
| `theorem` | [no_bsm_astro](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/no-bsm-astro/) | L259-L261 | proof obligation | formal proof obligation checked | `V.P87` |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l285/) | L285-L285 | computed check | computed check | `V.R202`, `V.R203`, `V.R204` |
| `eval` | [#eval L286](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l287/) | L287-L287 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l288/) | L288-L290 | computed check | computed check | — |
