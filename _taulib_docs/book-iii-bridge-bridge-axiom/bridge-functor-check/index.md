---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_functor_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::bridge_functor_check",
  "declaration_slug": "bridge-functor-check",
  "kind": "def",
  "name": "bridge_functor_check",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 79,
  "source_line_end": 98,
  "registry_ids": [
    "III.D71"
  ],
  "related_registry_items": [
    {
      "id": "III.D71",
      "title": "Bridge Axiom",
      "url": "/registry/object/III.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L79-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L79-L98",
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
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L79-L98)
- Source range: L79-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D71` — Bridge Axiom

## Immediate Comment / Docstring

```lean
/-- [III.D71] Bridge functor check at finite level: can we map tau-internal
    structures to ZFC-internal structures at depth k? At finite level, the
    bridge is a map from tau-addresses to ZFC axiom operations. -/
```

## Source Excerpt

```lean
def bridge_functor_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let xr := x % pk
        -- Carrier preservation: tau-address maps to ZFC carrier
        let carrier_ok := (zfc_vm_layer bound db).carrier_check xr k
        -- Predicate preservation: reduce-stability maps to derivability
        let pred_ok := reduce xr k == xr || xr >= pk
        -- Decoder compatibility: reduce commutes with Godel decoding
        let decode_ok := reduce (reduce xr k) k == reduce xr k
        carrier_ok && pred_ok && decode_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
