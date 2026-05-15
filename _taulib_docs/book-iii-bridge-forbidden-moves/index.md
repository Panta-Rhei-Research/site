---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_slug": "book-iii-bridge-forbidden-moves",
  "book": "BookIII",
  "family": "Bridge",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Bridge/ForbiddenMoves.lean",
  "sha256": "969e7bf28d360e32b81663640139b04234e36b44c6436794968bd7a1d78735d2",
  "imports": [
    "TauLib.BookIII.Bridge.ZFCasVM"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Bridge.ConjectureGaps",
    "TauLib.BookIII.Bridge.Incompleteness"
  ],
  "registry_ids": [
    "III.D69",
    "III.T43"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 11,
    "eval": 12,
    "theorem": 12
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ForbiddenMove",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-move/",
      "source_line_start": 43,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "forbidden_move_count",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-move-count/",
      "source_line_start": 52,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "ForbiddenMove.toNat",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/to-nat/",
      "source_line_start": 55,
      "source_line_end": 60,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "all_forbidden_moves",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/all-forbidden-moves/",
      "source_line_start": 63,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "violated_axiom",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/violated-axiom/",
      "source_line_start": 69,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "move_threshold",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-threshold/",
      "source_line_start": 79,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "forbidden_witness",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-witness/",
      "source_line_start": 90,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "forbidden_moves_check",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-moves-check/",
      "source_line_start": 118,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "def",
      "name": "bridge_damage",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/bridge-damage/",
      "source_line_start": 145,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "def",
      "name": "move_bridge_check",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-bridge-check/",
      "source_line_start": 156,
      "source_line_end": 182,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "def",
      "name": "move_correspondence_exhaustive",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-correspondence-exhaustive/",
      "source_line_start": 186,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "def",
      "name": "pvsnp_forbidden_count",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/pvsnp-forbidden-count/",
      "source_line_start": 201,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l217/",
      "source_line_start": 217,
      "source_line_end": 217,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "forbidden_moves_8_3",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-moves-8-3/",
      "source_line_start": 233,
      "source_line_end": 234,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "move_bridge_8_3",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-bridge-8-3/",
      "source_line_start": 237,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "move_correspondence",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-correspondence/",
      "source_line_start": 241,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "five_forbidden",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/five-forbidden/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "move_index_0",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-index-0/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "move_index_4",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-index-4/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fanout_violates_K3",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/fanout-violates-k3/",
      "source_line_start": 256,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "equality_violates_K5",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/equality-violates-k5/",
      "source_line_start": 260,
      "source_line_end": 261,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
      ]
    },
    {
      "kind": "theorem",
      "name": "circuits_break_bridge",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/circuits-break-bridge/",
      "source_line_start": 264,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "pvsnp_uses_3_moves",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/pvsnp-uses-3-moves/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "max_damage_is_3",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/max-damage-is-3/",
      "source_line_start": 272,
      "source_line_end": 274,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T43"
      ]
    },
    {
      "kind": "theorem",
      "name": "threshold_exceeds",
      "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/threshold-exceeds/",
      "source_line_start": 278,
      "source_line_end": 282,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D69"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean",
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
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Bridge/ForbiddenMoves.lean`
- SHA-256: `969e7bf28d360e32b81663640139b04234e36b44c6436794968bd7a1d78735d2`

## Registry Links

- `III.D69` — Five Forbidden Moves
- `III.T43` — Move-Bridge Correspondence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Bridge.ZFCasVM`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Bridge.ConjectureGaps`
- `TauLib.BookIII.Bridge.Incompleteness`

## Declaration Counts

- `def`: 11
- `eval`: 12
- `inductive`: 1
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ForbiddenMove](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-move/) | L43-L49 | type/data schema | type/data schema | `III.D69` |
| `def` | [forbidden_move_count](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-move-count/) | L52-L52 | data/computed value | data/computed value | `III.D69` |
| `def` | [ForbiddenMove.toNat](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/to-nat/) | L55-L60 | definition | definition | `III.D69` |
| `def` | [all_forbidden_moves](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/all-forbidden-moves/) | L63-L65 | data/computed value | data/computed value | — |
| `def` | [violated_axiom](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/violated-axiom/) | L69-L74 | definition | definition | `III.D69` |
| `def` | [move_threshold](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-threshold/) | L79-L85 | definition | definition | `III.D69` |
| `def` | [forbidden_witness](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-witness/) | L90-L113 | data/computed value | data/computed value | `III.D69` |
| `def` | [forbidden_moves_check](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-moves-check/) | L118-L133 | data/computed value | data/computed value | `III.D69` |
| `def` | [bridge_damage](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/bridge-damage/) | L145-L150 | definition | definition | `III.T43` |
| `def` | [move_bridge_check](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-bridge-check/) | L156-L182 | data/computed value | data/computed value | `III.T43` |
| `def` | [move_correspondence_exhaustive](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-correspondence-exhaustive/) | L186-L197 | data/computed value | data/computed value | `III.T43` |
| `def` | [pvsnp_forbidden_count](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/pvsnp-forbidden-count/) | L201-L202 | data/computed value | data/computed value | `III.T43` |
| `eval` | [#eval L209](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l209/) | L209-L209 | computed check | computed check | — |
| `eval` | [#eval L210](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l210/) | L210-L210 | computed check | computed check | — |
| `eval` | [#eval L211](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l211/) | L211-L211 | computed check | computed check | — |
| `eval` | [#eval L212](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l212/) | L212-L212 | computed check | computed check | — |
| `eval` | [#eval L215](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l215/) | L215-L215 | computed check | computed check | — |
| `eval` | [#eval L216](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l216/) | L216-L216 | computed check | computed check | — |
| `eval` | [#eval L217](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l217/) | L217-L217 | computed check | computed check | — |
| `eval` | [#eval L220](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l220/) | L220-L220 | computed check | computed check | — |
| `eval` | [#eval L221](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l221/) | L221-L221 | computed check | computed check | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l224/) | L224-L224 | computed check | computed check | — |
| `eval` | [#eval L225](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l225/) | L225-L225 | computed check | computed check | — |
| `eval` | [#eval L226](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/eval-l226/) | L226-L226 | computed check | computed check | — |
| `theorem` | [forbidden_moves_8_3](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-moves-8-3/) | L233-L234 | proof obligation | formal proof obligation checked | `III.D69` |
| `theorem` | [move_bridge_8_3](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-bridge-8-3/) | L237-L238 | proof obligation | formal proof obligation checked | `III.T43` |
| `theorem` | [move_correspondence](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-correspondence/) | L241-L242 | proof obligation | formal proof obligation checked | `III.T43` |
| `theorem` | [five_forbidden](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/five-forbidden/) | L249-L249 | proof obligation | formal proof obligation checked | `III.D69` |
| `theorem` | [move_index_0](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-index-0/) | L252-L252 | proof obligation | formal proof obligation checked | `III.D69` |
| `theorem` | [move_index_4](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-index-4/) | L253-L253 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fanout_violates_K3](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/fanout-violates-k3/) | L256-L257 | proof obligation | formal proof obligation checked | `III.D69` |
| `theorem` | [equality_violates_K5](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/equality-violates-k5/) | L260-L261 | proof obligation | formal proof obligation checked | `III.D69` |
| `theorem` | [circuits_break_bridge](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/circuits-break-bridge/) | L264-L265 | proof obligation | formal proof obligation checked | `III.T43` |
| `theorem` | [pvsnp_uses_3_moves](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/pvsnp-uses-3-moves/) | L268-L269 | proof obligation | formal proof obligation checked | `III.T43` |
| `theorem` | [max_damage_is_3](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/max-damage-is-3/) | L272-L274 | proof obligation | formal proof obligation checked | `III.T43` |
| `theorem` | [threshold_exceeds](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/threshold-exceeds/) | L278-L282 | proof obligation | formal proof obligation checked | `III.D69` |
