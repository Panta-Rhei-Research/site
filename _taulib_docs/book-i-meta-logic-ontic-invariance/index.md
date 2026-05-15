---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.OnticInvariance",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_slug": "book-i-meta-logic-ontic-invariance",
  "book": "BookI",
  "family": "MetaLogic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/MetaLogic/OnticInvariance.lean",
  "sha256": "ac4fb5827f830a4317d1dda055a43510e7ab69bc1e6b9aacbf300aea587f69bc",
  "imports": [
    "TauLib.BookI.MetaLogic.DiagonalResonance"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
    "TauLib.BookI.MetaLogic.ReceptionCriterion"
  ],
  "registry_ids": [
    "I.C03",
    "I.T46",
    "I.T47"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 5,
    "theorem": 9,
    "structure": 2,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "BlockingMechanism",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism/",
      "source_line_start": 30,
      "source_line_end": 34,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.T46"
      ]
    },
    {
      "kind": "def",
      "name": "blocking_targets",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets/",
      "source_line_start": 37,
      "source_line_end": 40,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "blocking_targets_injective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets-injective/",
      "source_line_start": 43,
      "source_line_end": 45,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "blocking_targets_surjective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets-surjective/",
      "source_line_start": 48,
      "source_line_end": 53,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allBlockingMechanisms",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/all-blocking-mechanisms/",
      "source_line_start": 56,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "blocking_mechanism_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism-count/",
      "source_line_start": 60,
      "source_line_end": 60,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OnticIdentityInvariance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance/",
      "source_line_start": 74,
      "source_line_end": 86,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.T46"
      ]
    },
    {
      "kind": "def",
      "name": "ontic_identity_invariance",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance-l89/",
      "source_line_start": 89,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "identityCoherenceLevel",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/identity-coherence-level/",
      "source_line_start": 102,
      "source_line_end": 106,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_identity_coherence_100",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/tau-identity-coherence-100/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_identity_coherence_0",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/orthodox-identity-coherence-0/",
      "source_line_start": 112,
      "source_line_end": 114,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_identity_decoherence",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/no-identity-decoherence/",
      "source_line_start": 122,
      "source_line_end": 123,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.C03"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_partial_decoherence",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/no-partial-decoherence/",
      "source_line_start": 126,
      "source_line_end": 130,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UniqueOmegaCapability",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/unique-omega-capability/",
      "source_line_start": 137,
      "source_line_end": 140,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "slippage_breaks_omega",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/slippage-breaks-omega/",
      "source_line_start": 151,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T47"
      ]
    },
    {
      "kind": "def",
      "name": "tau_omega_capability",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/tau-omega-capability/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_no_omega",
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/orthodox-no-omega/",
      "source_line_start": 166,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l175/",
      "source_line_start": 175,
      "source_line_end": 175,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l178/",
      "source_line_start": 178,
      "source_line_end": 178,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l179/",
      "source_line_start": 179,
      "source_line_end": 179,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l180/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l181/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l184/",
      "source_line_start": 184,
      "source_line_end": 184,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l186/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l189/",
      "source_line_start": 189,
      "source_line_end": 191,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean",
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
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/MetaLogic/OnticInvariance.lean`
- SHA-256: `ac4fb5827f830a4317d1dda055a43510e7ab69bc1e6b9aacbf300aea587f69bc`

## Registry Links

- `I.C03` — No Identity Decoherence
- `I.T46` — Ontic Identity Invariance
- `I.T47` — Slippage Breaks Unique Omega

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.MetaLogic.DiagonalResonance`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.KernelFoundation.H8KernelSynthesis`
- `TauLib.BookI.MetaLogic.ReceptionCriterion`

## Declaration Counts

- `def`: 5
- `eval`: 9
- `inductive`: 1
- `structure`: 2
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [BlockingMechanism](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism/) | L30-L34 | type/data schema | type/data schema | `I.T46` |
| `def` | [blocking_targets](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets/) | L37-L40 | definition | definition | — |
| `theorem` | [blocking_targets_injective](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets-injective/) | L43-L45 | proof obligation | formal proof obligation checked | — |
| `theorem` | [blocking_targets_surjective](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets-surjective/) | L48-L53 | proof obligation | formal proof obligation checked | — |
| `def` | [allBlockingMechanisms](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/all-blocking-mechanisms/) | L56-L57 | data/computed value | data/computed value | — |
| `theorem` | [blocking_mechanism_count](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism-count/) | L60-L60 | proof obligation | formal proof obligation checked | — |
| `structure` | [OnticIdentityInvariance](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance/) | L74-L86 | type/data schema | type/data schema | `I.T46` |
| `def` | [ontic_identity_invariance](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance-l89/) | L89-L95 | definition | definition | — |
| `def` | [identityCoherenceLevel](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/identity-coherence-level/) | L102-L106 | data/computed value | data/computed value | — |
| `theorem` | [tau_identity_coherence_100](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/tau-identity-coherence-100/) | L109-L109 | proof obligation | formal proof obligation checked | — |
| `theorem` | [orthodox_identity_coherence_0](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/orthodox-identity-coherence-0/) | L112-L114 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_identity_decoherence](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/no-identity-decoherence/) | L122-L123 | proof obligation | formal proof obligation checked | `I.C03` |
| `theorem` | [no_partial_decoherence](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/no-partial-decoherence/) | L126-L130 | proof obligation | formal proof obligation checked | — |
| `structure` | [UniqueOmegaCapability](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/unique-omega-capability/) | L137-L140 | type/data schema | type/data schema | — |
| `theorem` | [slippage_breaks_omega](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/slippage-breaks-omega/) | L151-L158 | proof obligation | formal proof obligation checked | `I.T47` |
| `def` | [tau_omega_capability](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/tau-omega-capability/) | L161-L163 | definition | definition | — |
| `theorem` | [orthodox_no_omega](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/orthodox-no-omega/) | L166-L168 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L175](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l175/) | L175-L175 | computed check | computed check | — |
| `eval` | [#eval L178](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l178/) | L178-L178 | computed check | computed check | — |
| `eval` | [#eval L179](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l179/) | L179-L179 | computed check | computed check | — |
| `eval` | [#eval L180](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l180/) | L180-L180 | computed check | computed check | — |
| `eval` | [#eval L181](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l181/) | L181-L181 | computed check | computed check | — |
| `eval` | [#eval L184](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l184/) | L184-L184 | computed check | computed check | — |
| `eval` | [#eval L185](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l185/) | L185-L185 | computed check | computed check | — |
| `eval` | [#eval L186](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l186/) | L186-L186 | computed check | computed check | — |
| `eval` | [#eval L189](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/eval-l189/) | L189-L191 | computed check | computed check | — |
