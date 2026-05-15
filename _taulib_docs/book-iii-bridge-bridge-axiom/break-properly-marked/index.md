---
{
  "projection_kind": "taulib_declaration",
  "title": "break_properly_marked",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/break-properly-marked/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::break_properly_marked",
  "declaration_slug": "break-properly-marked",
  "kind": "def",
  "name": "break_properly_marked",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 283,
  "source_line_end": 285,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L283-L285",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L283-L285",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L283-L285)
- Source range: L283-L285
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T47` — Honest Claim Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T47] Bridge breaks are clearly marked: P vs NP is tau_effective
    internally but the bridge degenerates. -/
```

## Source Excerpt

```lean
def break_properly_marked : Bool :=
  ((bridge_ledger).filter (fun e => e.status == .bridge_break)).all
    (fun e => e.scope == .tau_effective)
```
