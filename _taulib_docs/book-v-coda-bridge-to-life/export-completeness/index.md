---
{
  "projection_kind": "taulib_declaration",
  "title": "ExportCompleteness",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/export-completeness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::ExportCompleteness",
  "declaration_slug": "export-completeness",
  "kind": "structure",
  "name": "ExportCompleteness",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 431,
  "source_line_end": 446,
  "registry_ids": [
    "V.T158"
  ],
  "related_registry_items": [
    {
      "id": "V.T158",
      "title": "Export Completeness",
      "url": "/registry/object/V.T158/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L431-L446",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L431-L446",
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
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L431-L446)
- Source range: L431-L446
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T158` — Export Completeness

## Immediate Comment / Docstring

```lean
/-- [V.T158] Export completeness: the 9 export contracts E1-E9 are
    sufficient for Books VI and VII. No additional physics required
    beyond what the contracts specify.

    - 6 items to Book VI (V.D190): BH topology, entropy, sectors, No Shrink, defect, E1
    - 6 items to Book VII (V.D191): ledger, Hermetic Truth, zero params, measurement, ergodicity, E1→E2
    - Overlap: E1 completeness appears in both contracts
    - Total unique items: 11 (6 + 6 − 1 overlap)
    - Sufficiency: every downstream theorem in Books VI-VII traces to ≥1 contract item -/
```

## Source Excerpt

```lean
structure ExportCompleteness where
  /-- Number of contracts to Book VI. -/
  vi_items : Nat
  /-- Exactly 6. -/
  vi_eq : vi_items = 6
  /-- Number of contracts to Book VII. -/
  vii_items : Nat
  /-- Exactly 6. -/
  vii_eq : vii_items = 6
  /-- Number of overlapping items (E1 completeness). -/
  overlap_count : Nat := 1
  /-- Total unique items across both contracts. -/
  total_unique : Nat := 11
  /-- Contracts are sufficient. -/
  sufficient : Bool := true
  deriving Repr
```
