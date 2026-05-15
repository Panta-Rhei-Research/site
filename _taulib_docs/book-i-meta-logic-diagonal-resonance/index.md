---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_slug": "book-i-meta-logic-diagonal-resonance",
  "book": "BookI",
  "family": "MetaLogic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/MetaLogic/DiagonalResonance.lean",
  "sha256": "18d84d3f70ac085da37c6d75d7a4878e0feff05bdfd8800a235bb8da2fe5ec01",
  "imports": [
    "TauLib.BookI.MetaLogic.StructuralExclusion"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
    "TauLib.BookI.MetaLogic.OnticInvariance"
  ],
  "registry_ids": [
    "I.D89",
    "I.D90",
    "I.D91",
    "I.R24",
    "I.R25"
  ],
  "declaration_counts": {
    "inductive": 4,
    "structure": 3,
    "def": 7,
    "theorem": 9,
    "eval": 13
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ResonanceComponent",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component/",
      "source_line_start": 32,
      "source_line_end": 36,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D89"
      ]
    },
    {
      "kind": "structure",
      "name": "DiagonalResonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/diagonal-resonance/",
      "source_line_start": 39,
      "source_line_end": 43,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D89"
      ]
    },
    {
      "kind": "def",
      "name": "DiagonalResonance.isFullResonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/is-full-resonance/",
      "source_line_start": 46,
      "source_line_end": 47,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allResonanceComponents",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-resonance-components/",
      "source_line_start": 50,
      "source_line_end": 50,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resonance_component_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component-count/",
      "source_line_start": 53,
      "source_line_end": 53,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_resonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-resonance/",
      "source_line_start": 60,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_full_resonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-full-resonance/",
      "source_line_start": 66,
      "source_line_end": 66,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IdentitySlippage",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/identity-slippage/",
      "source_line_start": 75,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D90"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_no_slippage",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-slippage/",
      "source_line_start": 81,
      "source_line_end": 85,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ShadowIdentityType",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity-type/",
      "source_line_start": 92,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D91"
      ]
    },
    {
      "kind": "def",
      "name": "shadowRequires",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-requires/",
      "source_line_start": 99,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ShadowIdentity",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity/",
      "source_line_start": 106,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D91"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_equivalence",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-equivalence/",
      "source_line_start": 116,
      "source_line_end": 121,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_substitution",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-substitution/",
      "source_line_start": 124,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_diagonal",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-diagonal/",
      "source_line_start": 132,
      "source_line_end": 137,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "BugHidingReason",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason/",
      "source_line_start": 144,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.R24"
      ]
    },
    {
      "kind": "def",
      "name": "allBugHidingReasons",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-bug-hiding-reasons/",
      "source_line_start": 153,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bug_hiding_reason_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason-count/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "OrthodoxFoundation",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-foundation/",
      "source_line_start": 164,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.R25"
      ]
    },
    {
      "kind": "def",
      "name": "orthodox_resonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-resonance/",
      "source_line_start": 171,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_full_resonance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-full-resonance/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allOrthodoxFoundations",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-orthodox-foundations/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-count/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l192/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 197,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l198/",
      "source_line_start": 198,
      "source_line_end": 198,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l201/",
      "source_line_start": 201,
      "source_line_end": 201,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l202/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l206/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l209/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l210/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l211/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 214,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean",
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
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/MetaLogic/DiagonalResonance.lean`
- SHA-256: `18d84d3f70ac085da37c6d75d7a4878e0feff05bdfd8800a235bb8da2fe5ec01`

## Registry Links

- `I.D89` — Diagonal Resonance
- `I.D90` — Identity Slippage
- `I.D91` — Shadow Identity
- `I.R24` — Five Reasons Why The Bug Hides
- `I.R25` — Orthodox Foundations Under the Lens

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.MetaLogic.StructuralExclusion`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.KernelFoundation.H8KernelSynthesis`
- `TauLib.BookI.MetaLogic.OnticInvariance`

## Declaration Counts

- `def`: 7
- `eval`: 13
- `inductive`: 4
- `structure`: 3
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ResonanceComponent](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component/) | L32-L36 | type/data schema | type/data schema | `I.D89` |
| `structure` | [DiagonalResonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/diagonal-resonance/) | L39-L43 | type/data schema | type/data schema | `I.D89` |
| `def` | [DiagonalResonance.isFullResonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/is-full-resonance/) | L46-L47 | data/computed value | data/computed value | — |
| `def` | [allResonanceComponents](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-resonance-components/) | L50-L50 | data/computed value | data/computed value | — |
| `theorem` | [resonance_component_count](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component-count/) | L53-L53 | proof obligation | formal proof obligation checked | — |
| `def` | [tau_resonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-resonance/) | L60-L63 | definition | definition | — |
| `theorem` | [tau_no_full_resonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-full-resonance/) | L66-L66 | proof obligation | formal proof obligation checked | — |
| `structure` | [IdentitySlippage](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/identity-slippage/) | L75-L77 | type/data schema | type/data schema | `I.D90` |
| `theorem` | [tau_no_slippage](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-slippage/) | L81-L85 | proof obligation | formal proof obligation checked | — |
| `inductive` | [ShadowIdentityType](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity-type/) | L92-L96 | type/data schema | type/data schema | `I.D91` |
| `def` | [shadowRequires](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-requires/) | L99-L102 | definition | definition | — |
| `structure` | [ShadowIdentity](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity/) | L106-L113 | type/data schema | type/data schema | `I.D91` |
| `theorem` | [tau_no_shadow_equivalence](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-equivalence/) | L116-L121 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_no_shadow_substitution](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-substitution/) | L124-L129 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_no_shadow_diagonal](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-diagonal/) | L132-L137 | proof obligation | formal proof obligation checked | — |
| `inductive` | [BugHidingReason](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason/) | L144-L150 | type/data schema | type/data schema | `I.R24` |
| `def` | [allBugHidingReasons](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-bug-hiding-reasons/) | L153-L154 | data/computed value | data/computed value | — |
| `theorem` | [bug_hiding_reason_count](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason-count/) | L157-L157 | proof obligation | formal proof obligation checked | — |
| `inductive` | [OrthodoxFoundation](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-foundation/) | L164-L168 | type/data schema | type/data schema | `I.R25` |
| `def` | [orthodox_resonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-resonance/) | L171-L174 | definition | definition | — |
| `theorem` | [orthodox_full_resonance](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-full-resonance/) | L177-L179 | proof obligation | formal proof obligation checked | — |
| `def` | [allOrthodoxFoundations](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/all-orthodox-foundations/) | L182-L182 | data/computed value | data/computed value | — |
| `theorem` | [orthodox_count](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-count/) | L185-L185 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L192](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l192/) | L192-L192 | computed check | computed check | — |
| `eval` | [#eval L195](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l195/) | L195-L195 | computed check | computed check | — |
| `eval` | [#eval L196](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l196/) | L196-L196 | computed check | computed check | — |
| `eval` | [#eval L197](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l197/) | L197-L197 | computed check | computed check | — |
| `eval` | [#eval L198](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l198/) | L198-L198 | computed check | computed check | — |
| `eval` | [#eval L201](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l201/) | L201-L201 | computed check | computed check | — |
| `eval` | [#eval L202](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l202/) | L202-L202 | computed check | computed check | — |
| `eval` | [#eval L203](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l203/) | L203-L203 | computed check | computed check | — |
| `eval` | [#eval L206](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l206/) | L206-L206 | computed check | computed check | — |
| `eval` | [#eval L209](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l209/) | L209-L209 | computed check | computed check | — |
| `eval` | [#eval L210](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l210/) | L210-L210 | computed check | computed check | — |
| `eval` | [#eval L211](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l211/) | L211-L211 | computed check | computed check | — |
| `eval` | [#eval L212](/corpus/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l212/) | L212-L214 | computed check | computed check | — |
