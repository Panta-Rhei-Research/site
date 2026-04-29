---
{
  "projection_kind": "taulib_declaration",
  "title": "rh_bridge_conjectural",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-conjectural/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::rh_bridge_conjectural",
  "declaration_slug": "rh-bridge-conjectural",
  "kind": "theorem",
  "name": "rh_bridge_conjectural",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 363,
  "source_line_end": 365,
  "registry_ids": [
    "III.T45"
  ],
  "related_registry_items": [
    {
      "id": "III.T45",
      "title": "RH Bridge Three-Layer Structure",
      "url": "/registry/object/III.T45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L363-L365",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L363-L365",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L363-L365)
- Source range: L363-L365
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T45` — RH Bridge Three-Layer Structure

## Immediate Comment / Docstring

```lean
/-- [III.T45] RH bridge is conjectural (conditional on bridge axiom). -/
```

## Source Excerpt

```lean
theorem rh_bridge_conjectural (bound db : TauIdx) :
    rh_bridge_three_layer bound db (bridge_functor_exists bound db) = .conjectural :=
  rfl
```
