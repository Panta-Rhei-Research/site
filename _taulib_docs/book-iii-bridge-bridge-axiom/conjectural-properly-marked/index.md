---
{
  "projection_kind": "taulib_declaration",
  "title": "conjectural_properly_marked",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/conjectural-properly-marked/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::conjectural_properly_marked",
  "declaration_slug": "conjectural-properly-marked",
  "kind": "def",
  "name": "conjectural_properly_marked",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 277,
  "source_line_end": 279,
  "registry_ids": [
    "III.T47"
  ],
  "related_registry_items": [
    {
      "id": "III.T47",
      "title": "Honest Claim Theorem",
      "url": "/registry/object/III.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L277-L279",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L277-L279",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L277-L279)
- Source range: L277-L279
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T47` — Honest Claim Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T47] Conjectural claims are clearly marked: they depend on
    the bridge axiom and are NOT claimed as theorems. -/
```

## Source Excerpt

```lean
def conjectural_properly_marked : Bool :=
  ((bridge_ledger).filter (fun e => e.status == .conjectural)).all
    (fun e => e.scope == .conjectural)
```
