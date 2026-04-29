---
{
  "projection_kind": "taulib_declaration",
  "title": "LedgerEntry",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/ledger-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::LedgerEntry",
  "declaration_slug": "ledger-entry",
  "kind": "structure",
  "name": "LedgerEntry",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 71,
  "source_line_end": 80,
  "registry_ids": [
    "IV.D38"
  ],
  "related_registry_items": [
    {
      "id": "IV.D38",
      "title": "Ledger Entry",
      "url": "/registry/object/IV.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L71-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.ConstantsLedger",
        "url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L71-L80",
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedger](/verify/taulib/docs/book-iv-calibration-constants-ledger/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L71-L80)
- Source range: L71-L80
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D38` — Ledger Entry

## Immediate Comment / Docstring

```lean
/-- [IV.D38] A single entry in the constants ledger. -/
```

## Source Excerpt

```lean
structure LedgerEntry where
  /-- Registry ID (e.g., "IV.T01"). -/
  id : String
  /-- Display name. -/
  name : String
  /-- Category: coupling, formula, identity, near-match, framework. -/
  category : String
  /-- Scope label. -/
  scope : LedgerScope
  deriving Repr
```
