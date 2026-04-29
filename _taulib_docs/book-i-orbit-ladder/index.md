---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Orbit.Ladder",
  "permalink": "/verify/taulib/docs/book-i-orbit-ladder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Orbit.Ladder`.",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_slug": "book-i-orbit-ladder",
  "book": "BookI",
  "family": "Orbit",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Orbit/Ladder.lean",
  "sha256": "ffb867eb4e9ff6971217dc956e14656888ac491f4042ef4e60cf342269167150",
  "imports": [
    "TauLib.BookI.Orbit.Closure",
    "TauLib.BookI.Kernel.Diagonal"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Denotation.Arithmetic",
    "TauLib.BookI.Orbit.Saturation",
    "TauLib.BookI.Orbit.TooFew",
    "TauLib.BookI.Orbit.TooMany",
    "TauLib.BookI.Sets.Counting"
  ],
  "registry_ids": [
    "I.D06",
    "I.L01",
    "I.T02"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 3,
    "theorem": 8
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "LadderLevel",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-level/",
      "source_line_start": 43,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": [
        "I.D06"
      ]
    },
    {
      "kind": "def",
      "name": "tetration",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/tetration/",
      "source_line_start": 52,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ladderOp",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-op/",
      "source_line_start": 57,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ladderChannel",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-channel/",
      "source_line_start": 67,
      "source_line_end": 72,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "add_injective",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/add-injective/",
      "source_line_start": 79,
      "source_line_end": 82,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mul_injective",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/mul-injective/",
      "source_line_start": 85,
      "source_line_end": 103,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exp_injective",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/exp-injective/",
      "source_line_start": 106,
      "source_line_end": 117,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "available_channels",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/available-channels/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pentation_channel_exhaustion",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/pentation-channel-exhaustion/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": [
        "I.L01"
      ]
    },
    {
      "kind": "theorem",
      "name": "ladder_saturation",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-saturation/",
      "source_line_start": 142,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T02"
      ]
    },
    {
      "kind": "theorem",
      "name": "ladder_channels_assigned",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-channels-assigned/",
      "source_line_start": 147,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladder_channels_distinct",
      "url": "/verify/taulib/docs/book-i-orbit-ladder/ladder-channels-distinct/",
      "source_line_start": 154,
      "source_line_end": 158,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean",
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
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Orbit/Ladder.lean`
- SHA-256: `ffb867eb4e9ff6971217dc956e14656888ac491f4042ef4e60cf342269167150`

## Registry Links

- `I.D06` — Iterator Ladder
- `I.L01` — Pentation Non-Injectivity
- `I.T02` — Iterator Ladder Saturation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Orbit.Closure`
- `TauLib.BookI.Kernel.Diagonal`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Denotation.Arithmetic`
- `TauLib.BookI.Orbit.Saturation`
- `TauLib.BookI.Orbit.TooFew`
- `TauLib.BookI.Orbit.TooMany`
- `TauLib.BookI.Sets.Counting`

## Declaration Counts

- `def`: 3
- `inductive`: 1
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [LadderLevel](/verify/taulib/docs/book-i-orbit-ladder/ladder-level/) | L43-L49 | defined | `I.D06` |
| `def` | [tetration](/verify/taulib/docs/book-i-orbit-ladder/tetration/) | L52-L54 | defined | — |
| `def` | [ladderOp](/verify/taulib/docs/book-i-orbit-ladder/ladder-op/) | L57-L62 | defined | — |
| `def` | [ladderChannel](/verify/taulib/docs/book-i-orbit-ladder/ladder-channel/) | L67-L72 | defined | — |
| `theorem` | [add_injective](/verify/taulib/docs/book-i-orbit-ladder/add-injective/) | L79-L82 | formalized | — |
| `theorem` | [mul_injective](/verify/taulib/docs/book-i-orbit-ladder/mul-injective/) | L85-L103 | formalized | — |
| `theorem` | [exp_injective](/verify/taulib/docs/book-i-orbit-ladder/exp-injective/) | L106-L117 | formalized | — |
| `theorem` | [available_channels](/verify/taulib/docs/book-i-orbit-ladder/available-channels/) | L124-L125 | formalized | — |
| `theorem` | [pentation_channel_exhaustion](/verify/taulib/docs/book-i-orbit-ladder/pentation-channel-exhaustion/) | L132-L134 | formalized | `I.L01` |
| `theorem` | [ladder_saturation](/verify/taulib/docs/book-i-orbit-ladder/ladder-saturation/) | L142-L144 | formalized | `I.T02` |
| `theorem` | [ladder_channels_assigned](/verify/taulib/docs/book-i-orbit-ladder/ladder-channels-assigned/) | L147-L151 | formalized | — |
| `theorem` | [ladder_channels_distinct](/verify/taulib/docs/book-i-orbit-ladder/ladder-channels-distinct/) | L154-L158 | formalized | — |
