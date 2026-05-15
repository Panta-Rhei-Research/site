---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_ledger",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/bridge-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::bridge_ledger",
  "declaration_slug": "bridge-ledger",
  "kind": "def",
  "name": "bridge_ledger",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 212,
  "source_line_end": 221,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L212-L221",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L212-L221",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/corpus/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L212-L221)
- Source range: L212-L221
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T46` — Bridge Ledger

## Immediate Comment / Docstring

```lean
/-- [III.T46] The complete bridge ledger. -/
```

## Source Excerpt

```lean
def bridge_ledger : List BridgeLedgerEntry :=
  [ ⟨.RH,        .conjectural,   .conjectural⟩
  , ⟨.Poincare,  .established,   .established⟩
  , ⟨.NS,        .conjectural,   .conjectural⟩
  , ⟨.YM,        .conjectural,   .conjectural⟩
  , ⟨.Hodge,     .conjectural,   .conjectural⟩
  , ⟨.BSD,       .conjectural,   .conjectural⟩
  , ⟨.Langlands, .conjectural,   .conjectural⟩
  , ⟨.PvsNP,     .bridge_break,  .tau_effective⟩
  ]
```
