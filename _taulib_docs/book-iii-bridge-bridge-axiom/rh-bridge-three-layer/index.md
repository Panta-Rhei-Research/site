---
{
  "projection_kind": "taulib_declaration",
  "title": "rh_bridge_three_layer",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/rh-bridge-three-layer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::rh_bridge_three_layer",
  "declaration_slug": "rh-bridge-three-layer",
  "kind": "def",
  "name": "rh_bridge_three_layer",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 186,
  "source_line_end": 191,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L186-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L186-L191",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L186-L191)
- Source range: L186-L191
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T45` — RH Bridge Three-Layer Structure

## Immediate Comment / Docstring

```lean
/-- [III.T45] RH bridge three-layer structure:
    Layer 1: tau-internal spectral purity on H_L (tau-effective)
    Layer 2: Connes-Consani Weil positivity Q_W(g) >= 0 (established)
    Layer 3: identification of tau spectral data with zeta zeros (conjectural) -/
```

## Source Excerpt

```lean
def rh_bridge_three_layer (bound db : TauIdx) (h : bridge_functor_check bound db = true)
    : BridgeStatus :=
  -- Layer 1: tau-internal result passes (by assumption, bridge_functor_check = true)
  -- Layer 2: Weil positivity is classical (established)
  -- Layer 3: identification is the conjectural gap
  .conjectural
```
