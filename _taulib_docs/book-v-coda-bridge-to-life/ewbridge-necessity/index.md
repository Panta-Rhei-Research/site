---
{
  "projection_kind": "taulib_declaration",
  "title": "EWBridgeNecessity",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/ewbridge-necessity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::EWBridgeNecessity",
  "declaration_slug": "ewbridge-necessity",
  "kind": "structure",
  "name": "EWBridgeNecessity",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 317,
  "source_line_end": 326,
  "registry_ids": [
    "V.P109"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L317-L326",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.BridgeToLife",
        "url": "/verify/taulib/docs/book-v-coda-bridge-to-life/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L317-L326",
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

- Module: [TauLib.BookV.Coda.BridgeToLife](/verify/taulib/docs/book-v-coda-bridge-to-life/)
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L317-L326)
- Source range: L317-L326
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P109] EW bridge necessity: the cross-coupling kappa(A,B) > 0
    is necessary for discrete carriers (atoms) to exist.

    Without the electroweak bridge:
    - No W/Z bosons -> no beta decay -> no neutron-proton conversion
    - No bound states (atoms require both EM binding and weak stability)
    - No chemistry -> no E2 enrichment -> no life

    The EW bridge is the gateway from physics (E1) to biology (E2). -/
```

## Source Excerpt

```lean
structure EWBridgeNecessity where
  /-- Cross-coupling is positive. -/
  coupling_positive : Bool := true
  /-- Required for bound states. -/
  required_for_atoms : Bool := true
  /-- Required for E2 enrichment. -/
  required_for_e2 : Bool := true
  /-- Gateway from E1 to E2. -/
  is_gateway : Bool := true
  deriving Repr
```
