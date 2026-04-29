---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Measure",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Measure`.",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_slug": "book-i-boundary-measure",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Measure.lean",
  "sha256": "69f95c1bdfbb7cf8840b12c81eac967cbc7050d27fd0c536b28bc9525b889ec9",
  "imports": [
    "TauLib.BookI.Boundary.Ring",
    "TauLib.BookI.Polarity.Polarity",
    "TauLib.BookI.Polarity.ModArith"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Integration"
  ],
  "registry_ids": [
    "I.D95",
    "I.D96",
    "I.P43",
    "I.T49"
  ],
  "declaration_counts": {
    "def": 13,
    "structure": 3,
    "theorem": 10,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "count_satisfying",
      "url": "/verify/taulib/docs/book-i-boundary-measure/count-satisfying/",
      "source_line_start": 51,
      "source_line_end": 57,
      "formal_status": "defined",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "structure",
      "name": "StageMeasure",
      "url": "/verify/taulib/docs/book-i-boundary-measure/stage-measure/",
      "source_line_start": 61,
      "source_line_end": 64,
      "formal_status": "defined",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "def",
      "name": "stage_measure",
      "url": "/verify/taulib/docs/book-i-boundary-measure/stage-measure-l67/",
      "source_line_start": 67,
      "source_line_end": 71,
      "formal_status": "defined",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "structure",
      "name": "TowerMeasurableSet",
      "url": "/verify/taulib/docs/book-i-boundary-measure/tower-measurable-set/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": [
        "I.D96"
      ]
    },
    {
      "kind": "def",
      "name": "tower_compatible_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/tower-compatible-check/",
      "source_line_start": 84,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": [
        "I.D96"
      ]
    },
    {
      "kind": "def",
      "name": "sigma_algebra_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/sigma-algebra-check/",
      "source_line_start": 97,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": [
        "I.D96"
      ]
    },
    {
      "kind": "def",
      "name": "disjoint_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/disjoint-check/",
      "source_line_start": 112,
      "source_line_end": 120,
      "formal_status": "defined",
      "registry_ids": [
        "I.T49"
      ]
    },
    {
      "kind": "def",
      "name": "countable_additivity_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/countable-additivity-check/",
      "source_line_start": 123,
      "source_line_end": 129,
      "formal_status": "defined",
      "registry_ids": [
        "I.T49"
      ]
    },
    {
      "kind": "def",
      "name": "measure_compatibility_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/measure-compatibility-check/",
      "source_line_start": 139,
      "source_line_end": 144,
      "formal_status": "defined",
      "registry_ids": [
        "I.P43"
      ]
    },
    {
      "kind": "def",
      "name": "measure_compatibility_full",
      "url": "/verify/taulib/docs/book-i-boundary-measure/measure-compatibility-full/",
      "source_line_start": 147,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": [
        "I.P43"
      ]
    },
    {
      "kind": "def",
      "name": "full_set",
      "url": "/verify/taulib/docs/book-i-boundary-measure/full-set/",
      "source_line_start": 161,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "empty_set",
      "url": "/verify/taulib/docs/book-i-boundary-measure/empty-set/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "even_set",
      "url": "/verify/taulib/docs/book-i-boundary-measure/even-set/",
      "source_line_start": 169,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "b_sector_set",
      "url": "/verify/taulib/docs/book-i-boundary-measure/b-sector-set/",
      "source_line_start": 173,
      "source_line_end": 174,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_pos_1",
      "url": "/verify/taulib/docs/book-i-boundary-measure/primorial-pos-1/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "theorem",
      "name": "primorial_pos_2",
      "url": "/verify/taulib/docs/book-i-boundary-measure/primorial-pos-2/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_pos_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/primorial-pos-3/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "additivity_even_odd_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/additivity-even-odd-3/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "additivity_bc_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/additivity-bc-3/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T49"
      ]
    },
    {
      "kind": "theorem",
      "name": "full_set_compatible_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/full-set-compatible-3/",
      "source_line_start": 196,
      "source_line_end": 197,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P43"
      ]
    },
    {
      "kind": "theorem",
      "name": "empty_set_compatible_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/empty-set-compatible-3/",
      "source_line_start": 200,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P43"
      ]
    },
    {
      "kind": "theorem",
      "name": "even_set_compatible_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/even-set-compatible-3/",
      "source_line_start": 204,
      "source_line_end": 205,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P43"
      ]
    },
    {
      "kind": "theorem",
      "name": "full_set_measure_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/full-set-measure-3/",
      "source_line_start": 208,
      "source_line_end": 209,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "theorem",
      "name": "empty_set_measure_3",
      "url": "/verify/taulib/docs/book-i-boundary-measure/empty-set-measure-3/",
      "source_line_start": 212,
      "source_line_end": 213,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "structure",
      "name": "TauMeasureSpace",
      "url": "/verify/taulib/docs/book-i-boundary-measure/tau-measure-space/",
      "source_line_start": 221,
      "source_line_end": 223,
      "formal_status": "defined",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "def",
      "name": "tau_measure_check",
      "url": "/verify/taulib/docs/book-i-boundary-measure/tau-measure-check/",
      "source_line_start": 226,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": [
        "I.D95"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l245/",
      "source_line_start": 245,
      "source_line_end": 245,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-measure/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 256,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Measure.lean`
- SHA-256: `69f95c1bdfbb7cf8840b12c81eac967cbc7050d27fd0c536b28bc9525b889ec9`

## Registry Links

- `I.D95` — τ-Measure Space
- `I.D96` — Tower σ-Algebra
- `I.P43` — Measure Compatibility
- `I.T49` — Countable Additivity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Ring`
- `TauLib.BookI.Polarity.Polarity`
- `TauLib.BookI.Polarity.ModArith`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Integration`

## Declaration Counts

- `def`: 13
- `eval`: 10
- `structure`: 3
- `theorem`: 10

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [count_satisfying](/verify/taulib/docs/book-i-boundary-measure/count-satisfying/) | L51-L57 | defined | `I.D95` |
| `structure` | [StageMeasure](/verify/taulib/docs/book-i-boundary-measure/stage-measure/) | L61-L64 | defined | `I.D95` |
| `def` | [stage_measure](/verify/taulib/docs/book-i-boundary-measure/stage-measure-l67/) | L67-L71 | defined | `I.D95` |
| `structure` | [TowerMeasurableSet](/verify/taulib/docs/book-i-boundary-measure/tower-measurable-set/) | L79-L80 | defined | `I.D96` |
| `def` | [tower_compatible_check](/verify/taulib/docs/book-i-boundary-measure/tower-compatible-check/) | L84-L94 | defined | `I.D96` |
| `def` | [sigma_algebra_check](/verify/taulib/docs/book-i-boundary-measure/sigma-algebra-check/) | L97-L104 | defined | `I.D96` |
| `def` | [disjoint_check](/verify/taulib/docs/book-i-boundary-measure/disjoint-check/) | L112-L120 | defined | `I.T49` |
| `def` | [countable_additivity_check](/verify/taulib/docs/book-i-boundary-measure/countable-additivity-check/) | L123-L129 | defined | `I.T49` |
| `def` | [measure_compatibility_check](/verify/taulib/docs/book-i-boundary-measure/measure-compatibility-check/) | L139-L144 | defined | `I.P43` |
| `def` | [measure_compatibility_full](/verify/taulib/docs/book-i-boundary-measure/measure-compatibility-full/) | L147-L154 | defined | `I.P43` |
| `def` | [full_set](/verify/taulib/docs/book-i-boundary-measure/full-set/) | L161-L162 | defined | — |
| `def` | [empty_set](/verify/taulib/docs/book-i-boundary-measure/empty-set/) | L165-L166 | defined | — |
| `def` | [even_set](/verify/taulib/docs/book-i-boundary-measure/even-set/) | L169-L170 | defined | — |
| `def` | [b_sector_set](/verify/taulib/docs/book-i-boundary-measure/b-sector-set/) | L173-L174 | defined | — |
| `theorem` | [primorial_pos_1](/verify/taulib/docs/book-i-boundary-measure/primorial-pos-1/) | L181-L181 | formalized | `I.D95` |
| `theorem` | [primorial_pos_2](/verify/taulib/docs/book-i-boundary-measure/primorial-pos-2/) | L182-L182 | formalized | — |
| `theorem` | [primorial_pos_3](/verify/taulib/docs/book-i-boundary-measure/primorial-pos-3/) | L183-L183 | formalized | — |
| `theorem` | [additivity_even_odd_3](/verify/taulib/docs/book-i-boundary-measure/additivity-even-odd-3/) | L186-L188 | formalized | `I.T49` |
| `theorem` | [additivity_bc_3](/verify/taulib/docs/book-i-boundary-measure/additivity-bc-3/) | L191-L193 | formalized | `I.T49` |
| `theorem` | [full_set_compatible_3](/verify/taulib/docs/book-i-boundary-measure/full-set-compatible-3/) | L196-L197 | formalized | `I.P43` |
| `theorem` | [empty_set_compatible_3](/verify/taulib/docs/book-i-boundary-measure/empty-set-compatible-3/) | L200-L201 | formalized | `I.P43` |
| `theorem` | [even_set_compatible_3](/verify/taulib/docs/book-i-boundary-measure/even-set-compatible-3/) | L204-L205 | formalized | `I.P43` |
| `theorem` | [full_set_measure_3](/verify/taulib/docs/book-i-boundary-measure/full-set-measure-3/) | L208-L209 | formalized | `I.D95` |
| `theorem` | [empty_set_measure_3](/verify/taulib/docs/book-i-boundary-measure/empty-set-measure-3/) | L212-L213 | formalized | `I.D95` |
| `structure` | [TauMeasureSpace](/verify/taulib/docs/book-i-boundary-measure/tau-measure-space/) | L221-L223 | defined | `I.D95` |
| `def` | [tau_measure_check](/verify/taulib/docs/book-i-boundary-measure/tau-measure-check/) | L226-L227 | defined | `I.D95` |
| `eval` | [#eval L234](/verify/taulib/docs/book-i-boundary-measure/eval-l234/) | L234-L234 | computed | — |
| `eval` | [#eval L235](/verify/taulib/docs/book-i-boundary-measure/eval-l235/) | L235-L235 | computed | — |
| `eval` | [#eval L236](/verify/taulib/docs/book-i-boundary-measure/eval-l236/) | L236-L236 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-i-boundary-measure/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L242](/verify/taulib/docs/book-i-boundary-measure/eval-l242/) | L242-L242 | computed | — |
| `eval` | [#eval L245](/verify/taulib/docs/book-i-boundary-measure/eval-l245/) | L245-L245 | computed | — |
| `eval` | [#eval L246](/verify/taulib/docs/book-i-boundary-measure/eval-l246/) | L246-L246 | computed | — |
| `eval` | [#eval L247](/verify/taulib/docs/book-i-boundary-measure/eval-l247/) | L247-L247 | computed | — |
| `eval` | [#eval L250](/verify/taulib/docs/book-i-boundary-measure/eval-l250/) | L250-L251 | computed | — |
| `eval` | [#eval L254](/verify/taulib/docs/book-i-boundary-measure/eval-l254/) | L254-L256 | computed | — |
