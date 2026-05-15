---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Integration",
  "permalink": "/corpus/taulib/docs/book-i-boundary-integration/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Integration`.",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_slug": "book-i-boundary-integration",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Integration.lean",
  "sha256": "4706793127cdbbcf885f8287166bc0ba7d803fb4bd98e8579d8a1fd5e5ddbb7a",
  "imports": [
    "TauLib.BookI.Boundary.Measure"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookII.Hartogs.L2Space"
  ],
  "registry_ids": [
    "I.D99",
    "I.P45",
    "I.T51"
  ],
  "declaration_counts": {
    "def": 8,
    "structure": 1,
    "theorem": 4,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "stage_sum",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/stage-sum/",
      "source_line_start": 39,
      "source_line_end": 45,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "structure",
      "name": "TauIntegral",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/tau-integral/",
      "source_line_start": 49,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "def",
      "name": "tau_integral",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/tau-integral-l55/",
      "source_line_start": 55,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "def",
      "name": "integral_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/integral-equiv/",
      "source_line_start": 61,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "def",
      "name": "integral_linearity_check",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/integral-linearity-check/",
      "source_line_start": 69,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "I.T51"
      ]
    },
    {
      "kind": "def",
      "name": "monotone_convergence_check_step",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/monotone-convergence-check-step/",
      "source_line_start": 85,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "I.P45"
      ]
    },
    {
      "kind": "def",
      "name": "const_one",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/const-one/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ident_fn",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/ident-fn/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "even_indicator",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/even-indicator/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "integral_const_one_3",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/integral-const-one-3/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "theorem",
      "name": "linearity_2f_3g_stage2",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/linearity-2f-3g-stage2/",
      "source_line_start": 115,
      "source_line_end": 116,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T51"
      ]
    },
    {
      "kind": "theorem",
      "name": "linearity_identity_stage2",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/linearity-identity-stage2/",
      "source_line_start": 119,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T51"
      ]
    },
    {
      "kind": "theorem",
      "name": "integral_even_2",
      "url": "/corpus/taulib/docs/book-i-boundary-integration/integral-even-2/",
      "source_line_start": 123,
      "source_line_end": 124,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.D99"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l130/",
      "source_line_start": 130,
      "source_line_end": 130,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l131/",
      "source_line_start": 131,
      "source_line_end": 131,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l132/",
      "source_line_start": 132,
      "source_line_end": 132,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l133/",
      "source_line_start": 133,
      "source_line_end": 133,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l134/",
      "source_line_start": 134,
      "source_line_end": 134,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-integration/eval-l135/",
      "source_line_start": 135,
      "source_line_end": 137,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean",
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
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Integration.lean`
- SHA-256: `4706793127cdbbcf885f8287166bc0ba7d803fb4bd98e8579d8a1fd5e5ddbb7a`

## Registry Links

- `I.D99` — τ-Integral
- `I.P45` — Monotone Convergence
- `I.T51` — Linearity of Integration

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Measure`

## Imported By

- `TauLib.BookI`
- `TauLib.BookII.Hartogs.L2Space`

## Declaration Counts

- `def`: 8
- `eval`: 6
- `structure`: 1
- `theorem`: 4

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [stage_sum](/corpus/taulib/docs/book-i-boundary-integration/stage-sum/) | L39-L45 | data/computed value | data/computed value | `I.D99` |
| `structure` | [TauIntegral](/corpus/taulib/docs/book-i-boundary-integration/tau-integral/) | L49-L52 | type/data schema | type/data schema | `I.D99` |
| `def` | [tau_integral](/corpus/taulib/docs/book-i-boundary-integration/tau-integral-l55/) | L55-L57 | data/computed value | data/computed value | `I.D99` |
| `def` | [integral_equiv](/corpus/taulib/docs/book-i-boundary-integration/integral-equiv/) | L61-L62 | data/computed value | data/computed value | `I.D99` |
| `def` | [integral_linearity_check](/corpus/taulib/docs/book-i-boundary-integration/integral-linearity-check/) | L69-L77 | data/computed value | data/computed value | `I.T51` |
| `def` | [monotone_convergence_check_step](/corpus/taulib/docs/book-i-boundary-integration/monotone-convergence-check-step/) | L85-L91 | data/computed value | data/computed value | `I.P45` |
| `def` | [const_one](/corpus/taulib/docs/book-i-boundary-integration/const-one/) | L98-L98 | data/computed value | data/computed value | — |
| `def` | [ident_fn](/corpus/taulib/docs/book-i-boundary-integration/ident-fn/) | L101-L101 | data/computed value | data/computed value | — |
| `def` | [even_indicator](/corpus/taulib/docs/book-i-boundary-integration/even-indicator/) | L104-L104 | data/computed value | data/computed value | — |
| `theorem` | [integral_const_one_3](/corpus/taulib/docs/book-i-boundary-integration/integral-const-one-3/) | L111-L112 | proof obligation | formal proof obligation checked | `I.D99` |
| `theorem` | [linearity_2f_3g_stage2](/corpus/taulib/docs/book-i-boundary-integration/linearity-2f-3g-stage2/) | L115-L116 | proof obligation | formal proof obligation checked | `I.T51` |
| `theorem` | [linearity_identity_stage2](/corpus/taulib/docs/book-i-boundary-integration/linearity-identity-stage2/) | L119-L120 | proof obligation | formal proof obligation checked | `I.T51` |
| `theorem` | [integral_even_2](/corpus/taulib/docs/book-i-boundary-integration/integral-even-2/) | L123-L124 | proof obligation | formal proof obligation checked | `I.D99` |
| `eval` | [#eval L130](/corpus/taulib/docs/book-i-boundary-integration/eval-l130/) | L130-L130 | computed check | computed check | — |
| `eval` | [#eval L131](/corpus/taulib/docs/book-i-boundary-integration/eval-l131/) | L131-L131 | computed check | computed check | — |
| `eval` | [#eval L132](/corpus/taulib/docs/book-i-boundary-integration/eval-l132/) | L132-L132 | computed check | computed check | — |
| `eval` | [#eval L133](/corpus/taulib/docs/book-i-boundary-integration/eval-l133/) | L133-L133 | computed check | computed check | — |
| `eval` | [#eval L134](/corpus/taulib/docs/book-i-boundary-integration/eval-l134/) | L134-L134 | computed check | computed check | — |
| `eval` | [#eval L135](/corpus/taulib/docs/book-i-boundary-integration/eval-l135/) | L135-L137 | computed check | computed check | — |
