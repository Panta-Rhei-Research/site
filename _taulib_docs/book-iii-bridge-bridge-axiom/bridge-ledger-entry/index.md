---
{
  "projection_kind": "taulib_declaration",
  "title": "BridgeLedgerEntry",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::BridgeLedgerEntry",
  "declaration_slug": "bridge-ledger-entry",
  "kind": "structure",
  "name": "BridgeLedgerEntry",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 205,
  "source_line_end": 209,
  "registry_ids": [
    "III.T46"
  ],
  "related_registry_items": [
    {
      "id": "III.T46",
      "title": "Bridge Ledger",
      "url": "/registry/object/III.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L205-L209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L205-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/verify/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L205-L209)
- Source range: L205-L209
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.T46` — Bridge Ledger

## Immediate Comment / Docstring

```lean
/-- [III.T46] Bridge ledger entry: each Millennium Problem has a bridge
    status and a scope label. -/
```

## Source Excerpt

```lean
structure BridgeLedgerEntry where
  problem : MillenniumProblem
  status : BridgeStatus
  scope : ScopeLabel
  deriving Repr, DecidableEq, BEq
```
