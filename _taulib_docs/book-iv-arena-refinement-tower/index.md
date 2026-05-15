---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Arena.RefinementTower",
  "permalink": "/corpus/taulib/docs/book-iv-arena-refinement-tower/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Arena.RefinementTower`.",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_slug": "book-iv-arena-refinement-tower",
  "book": "BookIV",
  "family": "Arena",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Arena/RefinementTower.lean",
  "sha256": "8d66328bdcb395bc1123e14436f49c09952902ab895ac919c7ad66d116ec0f67",
  "imports": [
    "TauLib.BookIV.Arena.CoherenceKernel"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.Tau3Arena",
    "TauLib.BookV.Temporal.BaseCircle"
  ],
  "registry_ids": [
    "IV.D249",
    "IV.D250",
    "IV.D251",
    "IV.P147",
    "IV.P148",
    "IV.T95"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 3,
    "theorem": 5,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TowerLevel",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/tower-level/",
      "source_line_start": 38,
      "source_line_end": 43,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D249"
      ]
    },
    {
      "kind": "structure",
      "name": "RefinementTower",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/refinement-tower/",
      "source_line_start": 47,
      "source_line_end": 51,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D249"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_tower",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/canonical-tower/",
      "source_line_start": 54,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ProfiniteLimit",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/profinite-limit/",
      "source_line_start": 66,
      "source_line_end": 72,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D250"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_profinite",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/alpha-profinite/",
      "source_line_start": 75,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "subsystem_horizon",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/subsystem-horizon/",
      "source_line_start": 87,
      "source_line_end": 87,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P147"
      ]
    },
    {
      "kind": "structure",
      "name": "ProtoTime",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/proto-time/",
      "source_line_start": 96,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D251"
      ]
    },
    {
      "kind": "def",
      "name": "prototime_to_nat",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/prototime-to-nat/",
      "source_line_start": 116,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.P148"
      ]
    },
    {
      "kind": "theorem",
      "name": "nno_from_alpha",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/nno-from-alpha/",
      "source_line_start": 119,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_arrow",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/structural-arrow/",
      "source_line_start": 129,
      "source_line_end": 130,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T95"
      ]
    },
    {
      "kind": "theorem",
      "name": "arrow_transitive",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/arrow-transitive/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "arrow_irreflexive",
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/arrow-irreflexive/",
      "source_line_start": 138,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l144/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l145/",
      "source_line_start": 145,
      "source_line_end": 145,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l146/",
      "source_line_start": 146,
      "source_line_end": 146,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l147/",
      "source_line_start": 147,
      "source_line_end": 149,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean",
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Arena/RefinementTower.lean`
- SHA-256: `8d66328bdcb395bc1123e14436f49c09952902ab895ac919c7ad66d116ec0f67`

## Registry Links

- `IV.D249` — Refinement Tower mathcalR
- `IV.D250` — Profinite Limit hatalpha
- `IV.D251` — Proto-Time t_p
- `IV.P147` — Subsystem Horizon
- `IV.P148` — NNO from the alpha-Orbit
- `IV.T95` — Structural Arrow of Time

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.CoherenceKernel`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.Tau3Arena`
- `TauLib.BookV.Temporal.BaseCircle`

## Declaration Counts

- `def`: 3
- `eval`: 4
- `structure`: 4
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TowerLevel](/corpus/taulib/docs/book-iv-arena-refinement-tower/tower-level/) | L38-L43 | type/data schema | type/data schema | `IV.D249` |
| `structure` | [RefinementTower](/corpus/taulib/docs/book-iv-arena-refinement-tower/refinement-tower/) | L47-L51 | type/data schema | type/data schema | `IV.D249` |
| `def` | [canonical_tower](/corpus/taulib/docs/book-iv-arena-refinement-tower/canonical-tower/) | L54-L57 | definition | definition | — |
| `structure` | [ProfiniteLimit](/corpus/taulib/docs/book-iv-arena-refinement-tower/profinite-limit/) | L66-L72 | type/data schema | type/data schema | `IV.D250` |
| `def` | [alpha_profinite](/corpus/taulib/docs/book-iv-arena-refinement-tower/alpha-profinite/) | L75-L78 | definition | definition | — |
| `theorem` | [subsystem_horizon](/corpus/taulib/docs/book-iv-arena-refinement-tower/subsystem-horizon/) | L87-L87 | proof obligation | formal proof obligation checked | `IV.P147` |
| `structure` | [ProtoTime](/corpus/taulib/docs/book-iv-arena-refinement-tower/proto-time/) | L96-L108 | type/data schema | type/data schema | `IV.D251` |
| `def` | [prototime_to_nat](/corpus/taulib/docs/book-iv-arena-refinement-tower/prototime-to-nat/) | L116-L116 | data/computed value | data/computed value | `IV.P148` |
| `theorem` | [nno_from_alpha](/corpus/taulib/docs/book-iv-arena-refinement-tower/nno-from-alpha/) | L119-L120 | proof obligation | formal proof obligation checked | — |
| `theorem` | [structural_arrow](/corpus/taulib/docs/book-iv-arena-refinement-tower/structural-arrow/) | L129-L130 | proof obligation | formal proof obligation checked | `IV.T95` |
| `theorem` | [arrow_transitive](/corpus/taulib/docs/book-iv-arena-refinement-tower/arrow-transitive/) | L133-L135 | proof obligation | formal proof obligation checked | — |
| `theorem` | [arrow_irreflexive](/corpus/taulib/docs/book-iv-arena-refinement-tower/arrow-irreflexive/) | L138-L138 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L144](/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l144/) | L144-L144 | computed check | computed check | — |
| `eval` | [#eval L145](/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l145/) | L145-L145 | computed check | computed check | — |
| `eval` | [#eval L146](/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l146/) | L146-L146 | computed check | computed check | — |
| `eval` | [#eval L147](/corpus/taulib/docs/book-iv-arena-refinement-tower/eval-l147/) | L147-L149 | computed check | computed check | — |
