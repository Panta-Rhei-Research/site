---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
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
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component/",
      "source_line_start": 32,
      "source_line_end": 36,
      "formal_status": "defined",
      "registry_ids": [
        "I.D89"
      ]
    },
    {
      "kind": "structure",
      "name": "DiagonalResonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/diagonal-resonance/",
      "source_line_start": 39,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": [
        "I.D89"
      ]
    },
    {
      "kind": "def",
      "name": "DiagonalResonance.isFullResonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/is-full-resonance/",
      "source_line_start": 46,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allResonanceComponents",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-resonance-components/",
      "source_line_start": 50,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resonance_component_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component-count/",
      "source_line_start": 53,
      "source_line_end": 53,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_resonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-resonance/",
      "source_line_start": 60,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_full_resonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-full-resonance/",
      "source_line_start": 66,
      "source_line_end": 66,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IdentitySlippage",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/identity-slippage/",
      "source_line_start": 75,
      "source_line_end": 77,
      "formal_status": "defined",
      "registry_ids": [
        "I.D90"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_no_slippage",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-slippage/",
      "source_line_start": 81,
      "source_line_end": 85,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ShadowIdentityType",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity-type/",
      "source_line_start": 92,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": [
        "I.D91"
      ]
    },
    {
      "kind": "def",
      "name": "shadowRequires",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-requires/",
      "source_line_start": 99,
      "source_line_end": 102,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ShadowIdentity",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity/",
      "source_line_start": 106,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": [
        "I.D91"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_equivalence",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-equivalence/",
      "source_line_start": 116,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_substitution",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-substitution/",
      "source_line_start": 124,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_shadow_diagonal",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-diagonal/",
      "source_line_start": 132,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "BugHidingReason",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason/",
      "source_line_start": 144,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": [
        "I.R24"
      ]
    },
    {
      "kind": "def",
      "name": "allBugHidingReasons",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-bug-hiding-reasons/",
      "source_line_start": 153,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bug_hiding_reason_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason-count/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "OrthodoxFoundation",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-foundation/",
      "source_line_start": 164,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": [
        "I.R25"
      ]
    },
    {
      "kind": "def",
      "name": "orthodox_resonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-resonance/",
      "source_line_start": 171,
      "source_line_end": 174,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_full_resonance",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-full-resonance/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allOrthodoxFoundations",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-orthodox-foundations/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-count/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l192/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 197,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l198/",
      "source_line_start": 198,
      "source_line_end": 198,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l201/",
      "source_line_start": 201,
      "source_line_end": 201,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l202/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l206/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 214,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [ResonanceComponent](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component/) | L32-L36 | defined | `I.D89` |
| `structure` | [DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/diagonal-resonance/) | L39-L43 | defined | `I.D89` |
| `def` | [DiagonalResonance.isFullResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/is-full-resonance/) | L46-L47 | defined | — |
| `def` | [allResonanceComponents](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-resonance-components/) | L50-L50 | defined | — |
| `theorem` | [resonance_component_count](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component-count/) | L53-L53 | formalized | — |
| `def` | [tau_resonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-resonance/) | L60-L63 | defined | — |
| `theorem` | [tau_no_full_resonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-full-resonance/) | L66-L66 | formalized | — |
| `structure` | [IdentitySlippage](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/identity-slippage/) | L75-L77 | defined | `I.D90` |
| `theorem` | [tau_no_slippage](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-slippage/) | L81-L85 | formalized | — |
| `inductive` | [ShadowIdentityType](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity-type/) | L92-L96 | defined | `I.D91` |
| `def` | [shadowRequires](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-requires/) | L99-L102 | defined | — |
| `structure` | [ShadowIdentity](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity/) | L106-L113 | defined | `I.D91` |
| `theorem` | [tau_no_shadow_equivalence](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-equivalence/) | L116-L121 | formalized | — |
| `theorem` | [tau_no_shadow_substitution](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-substitution/) | L124-L129 | formalized | — |
| `theorem` | [tau_no_shadow_diagonal](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-shadow-diagonal/) | L132-L137 | formalized | — |
| `inductive` | [BugHidingReason](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason/) | L144-L150 | defined | `I.R24` |
| `def` | [allBugHidingReasons](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-bug-hiding-reasons/) | L153-L154 | defined | — |
| `theorem` | [bug_hiding_reason_count](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason-count/) | L157-L157 | formalized | — |
| `inductive` | [OrthodoxFoundation](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-foundation/) | L164-L168 | defined | `I.R25` |
| `def` | [orthodox_resonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-resonance/) | L171-L174 | defined | — |
| `theorem` | [orthodox_full_resonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-full-resonance/) | L177-L179 | formalized | — |
| `def` | [allOrthodoxFoundations](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/all-orthodox-foundations/) | L182-L182 | defined | — |
| `theorem` | [orthodox_count](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-count/) | L185-L185 | formalized | — |
| `eval` | [#eval L192](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l192/) | L192-L192 | computed | — |
| `eval` | [#eval L195](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l195/) | L195-L195 | computed | — |
| `eval` | [#eval L196](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l196/) | L196-L196 | computed | — |
| `eval` | [#eval L197](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l197/) | L197-L197 | computed | — |
| `eval` | [#eval L198](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l198/) | L198-L198 | computed | — |
| `eval` | [#eval L201](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l201/) | L201-L201 | computed | — |
| `eval` | [#eval L202](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l202/) | L202-L202 | computed | — |
| `eval` | [#eval L203](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l203/) | L203-L203 | computed | — |
| `eval` | [#eval L206](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l206/) | L206-L206 | computed | — |
| `eval` | [#eval L209](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l209/) | L209-L209 | computed | — |
| `eval` | [#eval L210](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l210/) | L210-L210 | computed | — |
| `eval` | [#eval L211](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l211/) | L211-L211 | computed | — |
| `eval` | [#eval L212](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/eval-l212/) | L212-L214 | computed | — |
