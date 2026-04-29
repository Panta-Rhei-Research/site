---
{
  "projection_kind": "taulib_declaration",
  "title": "LedgerEntry",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/ledger-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::LedgerEntry",
  "declaration_slug": "ledger-entry",
  "kind": "structure",
  "name": "LedgerEntry",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 80,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L80-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.ConstantsLedger",
        "url": "/verify/taulib/docs/book-v-coda-constants-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L80-L89",
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

- Module: [TauLib.BookV.Coda.ConstantsLedger](/verify/taulib/docs/book-v-coda-constants-ledger/)
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L80-L89)
- Source range: L80-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A single entry in the constants ledger. -/
```

## Source Excerpt

```lean
structure LedgerEntry where
  /-- Name of the quantity. -/
  name : String
  /-- Predicted value or status. -/
  prediction : String
  /-- Precision (ppm or qualitative). -/
  precision : String
  /-- Scope. -/
  scope : LedgerScope
  deriving Repr
```
