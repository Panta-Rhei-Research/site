---
{
  "projection_kind": "taulib_declaration",
  "title": "ExportContractVI",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/export-contract-vi/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::ExportContractVI",
  "declaration_slug": "export-contract-vi",
  "kind": "structure",
  "name": "ExportContractVI",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 102,
  "source_line_end": 119,
  "registry_ids": [
    "V.D190"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L102-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L102-L119",
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
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L102-L119)
- Source range: L102-L119
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D190] The Book V to Book VI export contract.

    Six items bridge physics (E1) to biology (E2):
    X1. BH topology on L (topological events, not point singularities)
    X2. Entropy splitting S = S_def + S_ref
    X3. Five sectors with coupling budget (all couplings from iota_tau)
    X4. No Shrink theorem (BH non-evaporation)
    X5. Defect functional D(phi) = (mu, nu, kappa, theta)
    X6. E1 complete (physics ledger) -/
```

## Source Excerpt

```lean
structure ExportContractVI where
  /-- Number of export items. -/
  item_count : Nat
  /-- Exactly 6 items. -/
  count_eq : item_count = 6
  /-- X1: BH topology. -/
  bh_topology : Bool := true
  /-- X2: Entropy splitting. -/
  entropy_splitting : Bool := true
  /-- X3: Five sectors. -/
  five_sectors : Bool := true
  /-- X4: No Shrink. -/
  no_shrink : Bool := true
  /-- X5: Defect functional. -/
  defect_functional : Bool := true
  /-- X6: E1 complete. -/
  e1_complete : Bool := true
  deriving Repr
```
