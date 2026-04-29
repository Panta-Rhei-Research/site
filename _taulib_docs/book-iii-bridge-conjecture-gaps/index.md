---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Bridge.ConjectureGaps",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_slug": "book-iii-bridge-conjecture-gaps",
  "book": "BookIII",
  "family": "Bridge",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Bridge/ConjectureGaps.lean",
  "sha256": "9a939779b5df40fea673d1d92bbf33c232e8d8700660d043b45548f140167404",
  "imports": [
    "TauLib.BookIII.Bridge.BridgeAxiom",
    "TauLib.BookIII.Bridge.ForbiddenMoves"
  ],
  "imported_by": [
    "TauLib.BookIII"
  ],
  "registry_ids": [
    "III.D111",
    "III.D112",
    "III.D113",
    "III.R47",
    "III.R48",
    "III.T79",
    "III.T80"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 12,
    "theorem": 13,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "GapType",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-type/",
      "source_line_start": 85,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "def",
      "name": "GapType.toNat",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/to-nat/",
      "source_line_start": 92,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "def",
      "name": "GapType.name",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/name/",
      "source_line_start": 98,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "inductive",
      "name": "AdditiveConjecture",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/additive-conjecture/",
      "source_line_start": 108,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_conjectures",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-conjectures/",
      "source_line_start": 115,
      "source_line_end": 116,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "conjecture_gap_type",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/conjecture-gap-type/",
      "source_line_start": 119,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "def",
      "name": "gap_forbidden_move",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-forbidden-move/",
      "source_line_start": 132,
      "source_line_end": 135,
      "formal_status": "defined",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "def",
      "name": "gap_violated_axiom",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-violated-axiom/",
      "source_line_start": 138,
      "source_line_end": 139,
      "formal_status": "defined",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "def",
      "name": "conjecture_scope",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/conjecture-scope/",
      "source_line_start": 146,
      "source_line_end": 149,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "full_conjecture_scope",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/full-conjecture-scope/",
      "source_line_start": 152,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "scope_discipline_check",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/scope-discipline-check/",
      "source_line_start": 159,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tower_decidable_check",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-decidable-check/",
      "source_line_start": 173,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": [
        "III.D111"
      ]
    },
    {
      "kind": "def",
      "name": "bridge_necessary_check",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-check/",
      "source_line_start": 193,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": [
        "III.T80"
      ]
    },
    {
      "kind": "def",
      "name": "gap_taxonomy_complete",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-taxonomy-complete/",
      "source_line_start": 201,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": [
        "III.T80"
      ]
    },
    {
      "kind": "theorem",
      "name": "tower_finite_decidable",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-finite-decidable/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T79"
      ]
    },
    {
      "kind": "theorem",
      "name": "bridge_necessary_insufficient",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-insufficient/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T80"
      ]
    },
    {
      "kind": "theorem",
      "name": "gap_taxonomy",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-taxonomy/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_gaps_exponential",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-gaps-exponential/",
      "source_line_start": 225,
      "source_line_end": 228,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "scope_check",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/scope-check/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "parity_ne_density",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/parity-ne-density/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "gap_indices",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-indices/",
      "source_line_start": 243,
      "source_line_end": 247,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "goldbach_gap_parity",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/goldbach-gap-parity/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_gap_density",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/twin-gap-density/",
      "source_line_start": 254,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "abc_gap_structural",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/abc-gap-structural/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_gaps_K4",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-gaps-k4/",
      "source_line_start": 262,
      "source_line_end": 266,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D113"
      ]
    },
    {
      "kind": "theorem",
      "name": "exponential_damage",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/exponential-damage/",
      "source_line_start": 269,
      "source_line_end": 270,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T80"
      ]
    },
    {
      "kind": "theorem",
      "name": "three_conjectures",
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/three-conjectures/",
      "source_line_start": 273,
      "source_line_end": 274,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l281/",
      "source_line_start": 281,
      "source_line_end": 281,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l282/",
      "source_line_start": 282,
      "source_line_end": 282,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 290,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean",
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
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Bridge/ConjectureGaps.lean`
- SHA-256: `9a939779b5df40fea673d1d92bbf33c232e8d8700660d043b45548f140167404`

## Registry Links

- `III.D111` — Tower Decidable Check
- `III.D112` — Gap Type
- `III.D113` — Forbidden Move Mapping
- `III.R47` — Classical Comparison
- `III.R48` — Honest Conclusion
- `III.T79` — Tower Finite Decidable
- `III.T80` — Bridge Necessary Insufficient

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Bridge.BridgeAxiom`
- `TauLib.BookIII.Bridge.ForbiddenMoves`

## Imported By

- `TauLib.BookIII`

## Declaration Counts

- `def`: 12
- `eval`: 9
- `inductive`: 2
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [GapType](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-type/) | L85-L89 | defined | `III.D112` |
| `def` | [GapType.toNat](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/to-nat/) | L92-L95 | defined | `III.D112` |
| `def` | [GapType.name](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/name/) | L98-L101 | defined | `III.D112` |
| `inductive` | [AdditiveConjecture](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/additive-conjecture/) | L108-L112 | defined | — |
| `def` | [all_conjectures](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-conjectures/) | L115-L116 | defined | — |
| `def` | [conjecture_gap_type](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/conjecture-gap-type/) | L119-L122 | defined | `III.D112` |
| `def` | [gap_forbidden_move](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-forbidden-move/) | L132-L135 | defined | `III.D113` |
| `def` | [gap_violated_axiom](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-violated-axiom/) | L138-L139 | defined | `III.D113` |
| `def` | [conjecture_scope](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/conjecture-scope/) | L146-L149 | defined | — |
| `def` | [full_conjecture_scope](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/full-conjecture-scope/) | L152-L155 | defined | — |
| `def` | [scope_discipline_check](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/scope-discipline-check/) | L159-L162 | defined | — |
| `def` | [tower_decidable_check](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-decidable-check/) | L173-L182 | defined | `III.D111` |
| `def` | [bridge_necessary_check](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-check/) | L193-L198 | defined | `III.T80` |
| `def` | [gap_taxonomy_complete](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-taxonomy-complete/) | L201-L205 | defined | `III.T80` |
| `theorem` | [tower_finite_decidable](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-finite-decidable/) | L213-L214 | formalized | `III.T79` |
| `theorem` | [bridge_necessary_insufficient](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-insufficient/) | L217-L218 | formalized | `III.T80` |
| `theorem` | [gap_taxonomy](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-taxonomy/) | L221-L222 | formalized | `III.D112` |
| `theorem` | [all_gaps_exponential](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-gaps-exponential/) | L225-L228 | formalized | `III.D113` |
| `theorem` | [scope_check](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/scope-check/) | L231-L232 | formalized | — |
| `theorem` | [parity_ne_density](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/parity-ne-density/) | L239-L240 | formalized | `III.D112` |
| `theorem` | [gap_indices](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-indices/) | L243-L247 | formalized | `III.D112` |
| `theorem` | [goldbach_gap_parity](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/goldbach-gap-parity/) | L250-L251 | formalized | `III.D113` |
| `theorem` | [twin_gap_density](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/twin-gap-density/) | L254-L255 | formalized | `III.D113` |
| `theorem` | [abc_gap_structural](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/abc-gap-structural/) | L258-L259 | formalized | `III.D113` |
| `theorem` | [all_gaps_K4](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-gaps-k4/) | L262-L266 | formalized | `III.D113` |
| `theorem` | [exponential_damage](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/exponential-damage/) | L269-L270 | formalized | `III.T80` |
| `theorem` | [three_conjectures](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/three-conjectures/) | L273-L274 | formalized | — |
| `eval` | [#eval L280](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l280/) | L280-L280 | computed | — |
| `eval` | [#eval L281](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l281/) | L281-L281 | computed | — |
| `eval` | [#eval L282](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l282/) | L282-L282 | computed | — |
| `eval` | [#eval L283](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l283/) | L283-L283 | computed | — |
| `eval` | [#eval L284](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l284/) | L284-L284 | computed | — |
| `eval` | [#eval L285](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l285/) | L285-L285 | computed | — |
| `eval` | [#eval L286](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l286/) | L286-L286 | computed | — |
| `eval` | [#eval L287](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l287/) | L287-L287 | computed | — |
| `eval` | [#eval L288](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/eval-l288/) | L288-L290 | computed | — |
