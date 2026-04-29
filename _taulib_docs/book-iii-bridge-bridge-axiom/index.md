---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Bridge.BridgeAxiom",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_slug": "book-iii-bridge-bridge-axiom",
  "book": "BookIII",
  "family": "Bridge",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Bridge/BridgeAxiom.lean",
  "sha256": "c0179eee1a19258396fa53cb4b94265f836a79a7487f852423812efe135eed45",
  "imports": [
    "TauLib.BookIII.Bridge.Incompleteness"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Bridge.ConjectureGaps",
    "TauLib.BookIII.Mirror.ProofTheoryE3",
    "TauLib.Meta.PrintAxioms",
    "TauLib.Tour.GuidedTour.BookIII",
    "TauLib.Tour.MillenniumProblems",
    "TauLib.Tour.VerifyItYourself"
  ],
  "registry_ids": [
    "III.D71",
    "III.D72",
    "III.T45",
    "III.T46",
    "III.T47"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 15,
    "axiom": 1,
    "structure": 2,
    "eval": 15,
    "theorem": 16
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ScopeLabel",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/scope-label/",
      "source_line_start": 58,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ScopeLabel.toNat",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/to-nat/",
      "source_line_start": 66,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bridge_functor_check",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-check/",
      "source_line_start": 79,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "III.D71"
      ]
    },
    {
      "kind": "axiom",
      "name": "bridge_functor_exists",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-exists/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "axiom",
      "registry_ids": [
        "III.D71"
      ]
    },
    {
      "kind": "def",
      "name": "shadow_diagram_check",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/shadow-diagram-check/",
      "source_line_start": 148,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "III.D72"
      ]
    },
    {
      "kind": "inductive",
      "name": "BridgeStatus",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-status/",
      "source_line_start": 176,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rh_bridge_three_layer",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-three-layer/",
      "source_line_start": 186,
      "source_line_end": 191,
      "formal_status": "defined",
      "registry_ids": [
        "III.T45"
      ]
    },
    {
      "kind": "def",
      "name": "rh_bridge_layer_count",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-layer-count/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": [
        "III.T45"
      ]
    },
    {
      "kind": "def",
      "name": "rh_conjectural_layer",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-conjectural-layer/",
      "source_line_start": 197,
      "source_line_end": 197,
      "formal_status": "defined",
      "registry_ids": [
        "III.T45"
      ]
    },
    {
      "kind": "structure",
      "name": "BridgeLedgerEntry",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-entry/",
      "source_line_start": 205,
      "source_line_end": 209,
      "formal_status": "defined",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "def",
      "name": "bridge_ledger",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger/",
      "source_line_start": 212,
      "source_line_end": 221,
      "formal_status": "defined",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "def",
      "name": "bridge_ledger_len",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-len/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "defined",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "def",
      "name": "ledger_status_count",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-status-count/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "defined",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "def",
      "name": "bridge_ledger_check",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-check/",
      "source_line_start": 231,
      "source_line_end": 235,
      "formal_status": "defined",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "structure",
      "name": "ClaimRecord",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/claim-record/",
      "source_line_start": 242,
      "source_line_end": 245,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "def",
      "name": "established_claims",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/established-claims/",
      "source_line_start": 249,
      "source_line_end": 256,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "def",
      "name": "honest_claim_check",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-check/",
      "source_line_start": 261,
      "source_line_end": 273,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "def",
      "name": "conjectural_properly_marked",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/conjectural-properly-marked/",
      "source_line_start": 277,
      "source_line_end": 279,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "def",
      "name": "break_properly_marked",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/break-properly-marked/",
      "source_line_start": 283,
      "source_line_end": 285,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "def",
      "name": "honest_claim_full",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-full/",
      "source_line_start": 289,
      "source_line_end": 293,
      "formal_status": "defined",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l313/",
      "source_line_start": 313,
      "source_line_end": 313,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bridge_functor_8_3",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-8-3/",
      "source_line_start": 331,
      "source_line_end": 332,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D71"
      ]
    },
    {
      "kind": "theorem",
      "name": "shadow_diagram_8_3",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/shadow-diagram-8-3/",
      "source_line_start": 335,
      "source_line_end": 336,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D72"
      ]
    },
    {
      "kind": "theorem",
      "name": "honest_claim_8_3",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-8-3/",
      "source_line_start": 339,
      "source_line_end": 340,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "conjectural_marked",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/conjectural-marked/",
      "source_line_start": 343,
      "source_line_end": 344,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "break_marked",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/break-marked/",
      "source_line_start": 347,
      "source_line_end": 348,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "honest_claim_full_8_3",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-full-8-3/",
      "source_line_start": 351,
      "source_line_end": 352,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "bridge_ledger_consistent",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-consistent/",
      "source_line_start": 355,
      "source_line_end": 356,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "theorem",
      "name": "rh_bridge_conjectural",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-conjectural/",
      "source_line_start": 363,
      "source_line_end": 365,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "one_axiom",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/one-axiom/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D71"
      ]
    },
    {
      "kind": "theorem",
      "name": "rh_layers",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-layers/",
      "source_line_start": 375,
      "source_line_end": 375,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "ledger_count",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-count/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "theorem",
      "name": "poincare_established",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/poincare-established/",
      "source_line_start": 381,
      "source_line_end": 382,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "theorem",
      "name": "pvsnp_bridge_break",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/pvsnp-bridge-break/",
      "source_line_start": 385,
      "source_line_end": 386,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T46"
      ]
    },
    {
      "kind": "theorem",
      "name": "scope_order",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/scope-order/",
      "source_line_start": 389,
      "source_line_end": 393,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "established_not_conjectural",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/established-not-conjectural/",
      "source_line_start": 396,
      "source_line_end": 399,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "ledger_partition",
      "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-partition/",
      "source_line_start": 402,
      "source_line_end": 408,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T47"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Bridge/BridgeAxiom.lean`
- SHA-256: `c0179eee1a19258396fa53cb4b94265f836a79a7487f852423812efe135eed45`

## Registry Links

- `III.D71` — Bridge Axiom
- `III.D72` — Shadow Diagram
- `III.T45` — RH Bridge Three-Layer Structure
- `III.T46` — Bridge Ledger
- `III.T47` — Honest Claim Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Bridge.Incompleteness`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Bridge.ConjectureGaps`
- `TauLib.BookIII.Mirror.ProofTheoryE3`
- `TauLib.Meta.PrintAxioms`
- `TauLib.Tour.GuidedTour.BookIII`
- `TauLib.Tour.MillenniumProblems`
- `TauLib.Tour.VerifyItYourself`

## Declaration Counts

- `axiom`: 1
- `def`: 15
- `eval`: 15
- `inductive`: 2
- `structure`: 2
- `theorem`: 16

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [ScopeLabel](/verify/taulib/docs/book-iii-bridge-bridge-axiom/scope-label/) | L58-L63 | defined | — |
| `def` | [ScopeLabel.toNat](/verify/taulib/docs/book-iii-bridge-bridge-axiom/to-nat/) | L66-L70 | defined | — |
| `def` | [bridge_functor_check](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-check/) | L79-L98 | defined | `III.D71` |
| `axiom` | [bridge_functor_exists](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-exists/) | L134-L135 | axiom | `III.D71` |
| `def` | [shadow_diagram_check](/verify/taulib/docs/book-iii-bridge-bridge-axiom/shadow-diagram-check/) | L148-L169 | defined | `III.D72` |
| `inductive` | [BridgeStatus](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-status/) | L176-L180 | defined | — |
| `def` | [rh_bridge_three_layer](/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-three-layer/) | L186-L191 | defined | `III.T45` |
| `def` | [rh_bridge_layer_count](/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-layer-count/) | L194-L194 | defined | `III.T45` |
| `def` | [rh_conjectural_layer](/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-conjectural-layer/) | L197-L197 | defined | `III.T45` |
| `structure` | [BridgeLedgerEntry](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-entry/) | L205-L209 | defined | `III.T46` |
| `def` | [bridge_ledger](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger/) | L212-L221 | defined | `III.T46` |
| `def` | [bridge_ledger_len](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-len/) | L224-L224 | defined | `III.T46` |
| `def` | [ledger_status_count](/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-status-count/) | L227-L228 | defined | `III.T46` |
| `def` | [bridge_ledger_check](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-check/) | L231-L235 | defined | `III.T46` |
| `structure` | [ClaimRecord](/verify/taulib/docs/book-iii-bridge-bridge-axiom/claim-record/) | L242-L245 | defined | `III.T47` |
| `def` | [established_claims](/verify/taulib/docs/book-iii-bridge-bridge-axiom/established-claims/) | L249-L256 | defined | `III.T47` |
| `def` | [honest_claim_check](/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-check/) | L261-L273 | defined | `III.T47` |
| `def` | [conjectural_properly_marked](/verify/taulib/docs/book-iii-bridge-bridge-axiom/conjectural-properly-marked/) | L277-L279 | defined | `III.T47` |
| `def` | [break_properly_marked](/verify/taulib/docs/book-iii-bridge-bridge-axiom/break-properly-marked/) | L283-L285 | defined | `III.T47` |
| `def` | [honest_claim_full](/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-full/) | L289-L293 | defined | `III.T47` |
| `eval` | [#eval L300](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l300/) | L300-L300 | computed | — |
| `eval` | [#eval L303](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l303/) | L303-L303 | computed | — |
| `eval` | [#eval L306](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l306/) | L306-L306 | computed | — |
| `eval` | [#eval L307](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l307/) | L307-L307 | computed | — |
| `eval` | [#eval L308](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l308/) | L308-L308 | computed | — |
| `eval` | [#eval L309](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l309/) | L309-L309 | computed | — |
| `eval` | [#eval L310](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l310/) | L310-L310 | computed | — |
| `eval` | [#eval L313](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l313/) | L313-L313 | computed | — |
| `eval` | [#eval L314](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l314/) | L314-L314 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L318](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l318/) | L318-L318 | computed | — |
| `eval` | [#eval L319](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l319/) | L319-L319 | computed | — |
| `eval` | [#eval L320](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l320/) | L320-L320 | computed | — |
| `eval` | [#eval L323](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l323/) | L323-L323 | computed | — |
| `eval` | [#eval L324](/verify/taulib/docs/book-iii-bridge-bridge-axiom/eval-l324/) | L324-L324 | computed | — |
| `theorem` | [bridge_functor_8_3](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-8-3/) | L331-L332 | formalized | `III.D71` |
| `theorem` | [shadow_diagram_8_3](/verify/taulib/docs/book-iii-bridge-bridge-axiom/shadow-diagram-8-3/) | L335-L336 | formalized | `III.D72` |
| `theorem` | [honest_claim_8_3](/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-8-3/) | L339-L340 | formalized | `III.T47` |
| `theorem` | [conjectural_marked](/verify/taulib/docs/book-iii-bridge-bridge-axiom/conjectural-marked/) | L343-L344 | formalized | `III.T47` |
| `theorem` | [break_marked](/verify/taulib/docs/book-iii-bridge-bridge-axiom/break-marked/) | L347-L348 | formalized | `III.T47` |
| `theorem` | [honest_claim_full_8_3](/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-full-8-3/) | L351-L352 | formalized | `III.T47` |
| `theorem` | [bridge_ledger_consistent](/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-consistent/) | L355-L356 | formalized | `III.T46` |
| `theorem` | [rh_bridge_conjectural](/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-conjectural/) | L363-L365 | formalized | `III.T45` |
| `theorem` | [one_axiom](/verify/taulib/docs/book-iii-bridge-bridge-axiom/one-axiom/) | L372-L372 | formalized | `III.D71` |
| `theorem` | [rh_layers](/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-layers/) | L375-L375 | formalized | `III.T45` |
| `theorem` | [ledger_count](/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-count/) | L378-L378 | formalized | `III.T46` |
| `theorem` | [poincare_established](/verify/taulib/docs/book-iii-bridge-bridge-axiom/poincare-established/) | L381-L382 | formalized | `III.T46` |
| `theorem` | [pvsnp_bridge_break](/verify/taulib/docs/book-iii-bridge-bridge-axiom/pvsnp-bridge-break/) | L385-L386 | formalized | `III.T46` |
| `theorem` | [scope_order](/verify/taulib/docs/book-iii-bridge-bridge-axiom/scope-order/) | L389-L393 | formalized | `III.T47` |
| `theorem` | [established_not_conjectural](/verify/taulib/docs/book-iii-bridge-bridge-axiom/established-not-conjectural/) | L396-L399 | formalized | `III.T47` |
| `theorem` | [ledger_partition](/verify/taulib/docs/book-iii-bridge-bridge-axiom/ledger-partition/) | L402-L408 | formalized | `III.T47` |
