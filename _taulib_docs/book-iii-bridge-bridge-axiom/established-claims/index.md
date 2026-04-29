---
{
  "projection_kind": "taulib_declaration",
  "title": "established_claims",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/established-claims/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::established_claims",
  "declaration_slug": "established-claims",
  "kind": "def",
  "name": "established_claims",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 249,
  "source_line_end": 256,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L249-L256",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L249-L256",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L249-L256)
- Source range: L249-L256
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T47` — Honest Claim Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T47] The established claims: these pass checks and have scope
    "established" or "tau-effective". No bridge axiom needed. -/
```

## Source Excerpt

```lean
def established_claims : List ClaimRecord :=
  [ ⟨"ZFC_VM",           .tau_effective, zfc_vm_check⟩
  , ⟨"axiom_encoding",   .tau_effective, axiom_encoding_check⟩
  , ⟨"set_universe",     .tau_effective, set_universe_check⟩
  , ⟨"forbidden_moves",  .tau_effective, forbidden_moves_check⟩
  , ⟨"move_bridge",      .tau_effective, move_bridge_check⟩
  , ⟨"incompleteness",   .tau_effective, incompleteness_vm_check⟩
  ]
```
