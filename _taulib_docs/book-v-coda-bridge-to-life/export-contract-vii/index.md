---
{
  "projection_kind": "taulib_declaration",
  "title": "ExportContractVII",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/export-contract-vii/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::ExportContractVII",
  "declaration_slug": "export-contract-vii",
  "kind": "structure",
  "name": "ExportContractVII",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 143,
  "source_line_end": 160,
  "registry_ids": [
    "V.D191"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L143-L160",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L143-L160",
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
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L143-L160)
- Source range: L143-L160
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D191] The Book V to Book VII export contract.

    Six items bridge physics (E1) to philosophy:
    Y1. Constants ledger (complete physics for ontological interpretation)
    Y2. Hermetic Truth (tensor product is exact)
    Y3. Zero free parameters, one anchor (m_n)
    Y4. Measurement dissolution (no collapse)
    Y5. Profinite ergodicity (every orbit dense)
    Y6. E1 -> E2 enrichment transition -/
```

## Source Excerpt

```lean
structure ExportContractVII where
  /-- Number of export items. -/
  item_count : Nat
  /-- Exactly 6 items. -/
  count_eq : item_count = 6
  /-- Y1: Constants ledger. -/
  constants_ledger : Bool := true
  /-- Y2: Hermetic Truth. -/
  hermetic_truth : Bool := true
  /-- Y3: Zero params, one anchor. -/
  zero_params_one_anchor : Bool := true
  /-- Y4: Measurement dissolution. -/
  measurement_dissolution : Bool := true
  /-- Y5: Profinite ergodicity. -/
  profinite_ergodicity_item : Bool := true
  /-- Y6: E1 -> E2 transition. -/
  e1_to_e2 : Bool := true
  deriving Repr
```
