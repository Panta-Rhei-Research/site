---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_slug": "book-ii-regularity-idempotent-decomposition",
  "book": "BookII",
  "family": "Regularity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Regularity/IdempotentDecomposition.lean",
  "sha256": "2c59431a5f7496384f22188b8659374970e6e5a835b108da2520d300edcab1e1",
  "imports": [
    "TauLib.BookII.Hartogs.SheafCoherence"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Regularity.ThreeLemmaChain"
  ],
  "registry_ids": [
    "II.D48",
    "II.L07",
    "II.P10"
  ],
  "declaration_counts": {
    "def": 9,
    "theorem": 13,
    "eval": 13
  },
  "declarations": [
    {
      "kind": "def",
      "name": "idempotent_decompose",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/idempotent-decompose/",
      "source_line_start": 54,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D48"
      ]
    },
    {
      "kind": "def",
      "name": "proj_plus",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "proj_minus",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_plus_kills_c",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-kills-c/",
      "source_line_start": 70,
      "source_line_end": 72,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_minus_kills_b",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-kills-b/",
      "source_line_start": 75,
      "source_line_end": 77,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_plus_preserves_b",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-preserves-b/",
      "source_line_start": 80,
      "source_line_end": 82,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_minus_preserves_c",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-preserves-c/",
      "source_line_start": 85,
      "source_line_end": 87,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "decompose_recovery",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery/",
      "source_line_start": 99,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.L07"
      ]
    },
    {
      "kind": "theorem",
      "name": "proj_orthogonal",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-orthogonal/",
      "source_line_start": 106,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_plus_idem",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-idem/",
      "source_line_start": 111,
      "source_line_end": 113,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proj_minus_idem",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-idem/",
      "source_line_start": 116,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decompose_recovery_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery-check/",
      "source_line_start": 126,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.L07"
      ]
    },
    {
      "kind": "def",
      "name": "stagefun_decompose",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose/",
      "source_line_start": 157,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D48"
      ]
    },
    {
      "kind": "def",
      "name": "stagefun_decompose_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose-check/",
      "source_line_start": 167,
      "source_line_end": 186,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decompose_functorial_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-check/",
      "source_line_start": 201,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P10"
      ]
    },
    {
      "kind": "def",
      "name": "decompose_functorial_extended",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-extended/",
      "source_line_start": 228,
      "source_line_end": 255,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P10"
      ]
    },
    {
      "kind": "def",
      "name": "full_idempotent_check",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/full-idempotent-check/",
      "source_line_start": 262,
      "source_line_end": 266,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l275/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l282/",
      "source_line_start": 282,
      "source_line_end": 282,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recovery_30",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/recovery-30/",
      "source_line_start": 309,
      "source_line_end": 310,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.L07"
      ]
    },
    {
      "kind": "theorem",
      "name": "stagefun_decompose_12_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose-12-4/",
      "source_line_start": 313,
      "source_line_end": 314,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.D48"
      ]
    },
    {
      "kind": "theorem",
      "name": "functorial_12_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/functorial-12-4/",
      "source_line_start": 317,
      "source_line_end": 318,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "II.P10"
      ]
    },
    {
      "kind": "theorem",
      "name": "functorial_ext_12_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/functorial-ext-12-4/",
      "source_line_start": 320,
      "source_line_end": 321,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "full_idempotent_12_4",
      "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/full-idempotent-12-4/",
      "source_line_start": 324,
      "source_line_end": 327,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean",
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
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Regularity/IdempotentDecomposition.lean`
- SHA-256: `2c59431a5f7496384f22188b8659374970e6e5a835b108da2520d300edcab1e1`

## Registry Links

- `II.D48` — Canonical Decomposition
- `II.L07` — Idempotent Decomposition Lemma
- `II.P10` — Functions as Tau-Objects

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Hartogs.SheafCoherence`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Regularity.ThreeLemmaChain`

## Declaration Counts

- `def`: 9
- `eval`: 13
- `theorem`: 13

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [idempotent_decompose](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/idempotent-decompose/) | L54-L55 | definition | definition | `II.D48` |
| `def` | [proj_plus](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus/) | L58-L59 | definition | definition | — |
| `def` | [proj_minus](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus/) | L62-L63 | definition | definition | — |
| `theorem` | [proj_plus_kills_c](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-kills-c/) | L70-L72 | proof obligation | formal proof obligation checked | — |
| `theorem` | [proj_minus_kills_b](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-kills-b/) | L75-L77 | proof obligation | formal proof obligation checked | — |
| `theorem` | [proj_plus_preserves_b](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-preserves-b/) | L80-L82 | proof obligation | formal proof obligation checked | — |
| `theorem` | [proj_minus_preserves_c](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-preserves-c/) | L85-L87 | proof obligation | formal proof obligation checked | — |
| `theorem` | [decompose_recovery](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery/) | L99-L102 | proof obligation | formal proof obligation checked | `II.L07` |
| `theorem` | [proj_orthogonal](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-orthogonal/) | L106-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [proj_plus_idem](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-plus-idem/) | L111-L113 | proof obligation | formal proof obligation checked | — |
| `theorem` | [proj_minus_idem](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/proj-minus-idem/) | L116-L118 | proof obligation | formal proof obligation checked | — |
| `def` | [decompose_recovery_check](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery-check/) | L126-L146 | data/computed value | data/computed value | `II.L07` |
| `def` | [stagefun_decompose](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose/) | L157-L162 | definition | definition | `II.D48` |
| `def` | [stagefun_decompose_check](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose-check/) | L167-L186 | data/computed value | data/computed value | — |
| `def` | [decompose_functorial_check](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-check/) | L201-L225 | data/computed value | data/computed value | `II.P10` |
| `def` | [decompose_functorial_extended](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-extended/) | L228-L255 | data/computed value | data/computed value | `II.P10` |
| `def` | [full_idempotent_check](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/full-idempotent-check/) | L262-L266 | data/computed value | data/computed value | — |
| `eval` | [#eval L273](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l273/) | L273-L273 | computed check | computed check | — |
| `eval` | [#eval L274](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l274/) | L274-L274 | computed check | computed check | — |
| `eval` | [#eval L275](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l275/) | L275-L275 | computed check | computed check | — |
| `eval` | [#eval L278](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l279/) | L279-L279 | computed check | computed check | — |
| `eval` | [#eval L282](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l282/) | L282-L282 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l288/) | L288-L288 | computed check | computed check | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l292/) | L292-L292 | computed check | computed check | — |
| `eval` | [#eval L295](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l295/) | L295-L295 | computed check | computed check | — |
| `eval` | [#eval L298](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l298/) | L298-L298 | computed check | computed check | — |
| `eval` | [#eval L299](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l299/) | L299-L299 | computed check | computed check | — |
| `eval` | [#eval L302](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/eval-l302/) | L302-L302 | computed check | computed check | — |
| `theorem` | [recovery_30](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/recovery-30/) | L309-L310 | proof obligation | formal proof obligation checked | `II.L07` |
| `theorem` | [stagefun_decompose_12_4](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose-12-4/) | L313-L314 | proof obligation | formal proof obligation checked | `II.D48` |
| `theorem` | [functorial_12_4](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/functorial-12-4/) | L317-L318 | proof obligation | formal proof obligation checked | `II.P10` |
| `theorem` | [functorial_ext_12_4](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/functorial-ext-12-4/) | L320-L321 | proof obligation | formal proof obligation checked | — |
| `theorem` | [full_idempotent_12_4](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/full-idempotent-12-4/) | L324-L327 | proof obligation | formal proof obligation checked | — |
