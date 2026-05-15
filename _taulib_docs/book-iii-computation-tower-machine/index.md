---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Computation.TowerMachine",
  "permalink": "/corpus/taulib/docs/book-iii-computation-tower-machine/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Computation.TowerMachine`.",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_slug": "book-iii-computation-tower-machine",
  "book": "BookIII",
  "family": "Computation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Computation/TowerMachine.lean",
  "sha256": "d1e8f017faa1816e14cf5d84dd01745bd6254c0d5348281de225f2b899a0937b",
  "imports": [
    "TauLib.BookIII.Computation.E2Agent"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Computation.Admissibility",
    "TauLib.BookIII.Computation.E2Witness"
  ],
  "registry_ids": [
    "III.D51",
    "III.D52",
    "III.T30"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 6,
    "eval": 5,
    "theorem": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TTMConfig",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttmconfig/",
      "source_line_start": 43,
      "source_line_end": 48,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "def",
      "name": "ttm_step",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-step/",
      "source_line_start": 52,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "def",
      "name": "ttm_run",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-run/",
      "source_line_start": 68,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "def",
      "name": "ttm_check",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-check/",
      "source_line_start": 78,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "def",
      "name": "ttm_nativity_check",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-nativity-check/",
      "source_line_start": 108,
      "source_line_end": 131,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T30"
      ]
    },
    {
      "kind": "def",
      "name": "observable_width",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/observable-width/",
      "source_line_start": 139,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D52"
      ]
    },
    {
      "kind": "def",
      "name": "observable_transition_check",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/observable-transition-check/",
      "source_line_start": 143,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D52"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l171/",
      "source_line_start": 171,
      "source_line_end": 171,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l172/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l173/",
      "source_line_start": 173,
      "source_line_end": 173,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l174/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l175/",
      "source_line_start": 175,
      "source_line_end": 175,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ttm_5_3",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-5-3/",
      "source_line_start": 181,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ttm_nativity_10_3",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-nativity-10-3/",
      "source_line_start": 184,
      "source_line_end": 185,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "observable_10_3",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/observable-10-3/",
      "source_line_start": 187,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ttm_preserves_depth",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-preserves-depth/",
      "source_line_start": 195,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "theorem",
      "name": "ttm_depth_0",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-depth-0/",
      "source_line_start": 201,
      "source_line_end": 202,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D51"
      ]
    },
    {
      "kind": "theorem",
      "name": "code_is_data",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/code-is-data/",
      "source_line_start": 205,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T30"
      ]
    },
    {
      "kind": "theorem",
      "name": "obs_width",
      "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/obs-width/",
      "source_line_start": 209,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D52"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Computation/TowerMachine.lean`
- SHA-256: `d1e8f017faa1816e14cf5d84dd01745bd6254c0d5348281de225f2b899a0937b`

## Registry Links

- `III.D51` — τ-Tower Machine
- `III.D52` — Observable Transition
- `III.T30` — TTM τ-Nativity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Computation.E2Agent`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Computation.Admissibility`
- `TauLib.BookIII.Computation.E2Witness`

## Declaration Counts

- `def`: 6
- `eval`: 5
- `structure`: 1
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TTMConfig](/corpus/taulib/docs/book-iii-computation-tower-machine/ttmconfig/) | L43-L48 | type/data schema | type/data schema | `III.D51` |
| `def` | [ttm_step](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-step/) | L52-L65 | definition | definition | `III.D51` |
| `def` | [ttm_run](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-run/) | L68-L74 | definition | definition | `III.D51` |
| `def` | [ttm_check](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-check/) | L78-L99 | data/computed value | data/computed value | `III.D51` |
| `def` | [ttm_nativity_check](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-nativity-check/) | L108-L131 | data/computed value | data/computed value | `III.T30` |
| `def` | [observable_width](/corpus/taulib/docs/book-iii-computation-tower-machine/observable-width/) | L139-L139 | definition | definition | `III.D52` |
| `def` | [observable_transition_check](/corpus/taulib/docs/book-iii-computation-tower-machine/observable-transition-check/) | L143-L165 | data/computed value | data/computed value | `III.D52` |
| `eval` | [#eval L171](/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l171/) | L171-L171 | computed check | computed check | — |
| `eval` | [#eval L172](/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l172/) | L172-L172 | computed check | computed check | — |
| `eval` | [#eval L173](/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l173/) | L173-L173 | computed check | computed check | — |
| `eval` | [#eval L174](/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l174/) | L174-L174 | computed check | computed check | — |
| `eval` | [#eval L175](/corpus/taulib/docs/book-iii-computation-tower-machine/eval-l175/) | L175-L175 | computed check | computed check | — |
| `theorem` | [ttm_5_3](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-5-3/) | L181-L182 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ttm_nativity_10_3](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-nativity-10-3/) | L184-L185 | proof obligation | formal proof obligation checked | — |
| `theorem` | [observable_10_3](/corpus/taulib/docs/book-iii-computation-tower-machine/observable-10-3/) | L187-L188 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ttm_preserves_depth](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-preserves-depth/) | L195-L198 | proof obligation | formal proof obligation checked | `III.D51` |
| `theorem` | [ttm_depth_0](/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-depth-0/) | L201-L202 | proof obligation | formal proof obligation checked | `III.D51` |
| `theorem` | [code_is_data](/corpus/taulib/docs/book-iii-computation-tower-machine/code-is-data/) | L205-L206 | proof obligation | formal proof obligation checked | `III.T30` |
| `theorem` | [obs_width](/corpus/taulib/docs/book-iii-computation-tower-machine/obs-width/) | L209-L211 | proof obligation | formal proof obligation checked | `III.D52` |
