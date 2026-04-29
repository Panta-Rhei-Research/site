---
{
  "projection_kind": "taulib_declaration",
  "title": "LedgerComparison",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/ledger-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::LedgerComparison",
  "declaration_slug": "ledger-comparison",
  "kind": "structure",
  "name": "LedgerComparison",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 70,
  "source_line_end": 83,
  "registry_ids": [
    "IV.R185"
  ],
  "related_registry_items": [
    {
      "id": "IV.R185",
      "title": "Comparison with ch15 ledger",
      "url": "/registry/object/IV.R185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L70-L83",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.CompleteLedger",
        "url": "/verify/taulib/docs/book-iv-coda-complete-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L70-L83",
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

- Module: [TauLib.BookIV.Coda.CompleteLedger](/verify/taulib/docs/book-iv-coda-complete-ledger/)
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L70-L83)
- Source range: L70-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R185` — Comparison with ch15 ledger

## Immediate Comment / Docstring

```lean
/-- [IV.R185] The Full Constants Ledger contains 66 entries with scope labels:
    16 established, 25 tau-effective, 18 conjectural, 7 metaphorical.
    This is an improvement over the ch15 partial ledger (23 entries). -/
```

## Source Excerpt

```lean
structure LedgerComparison where
  /-- Total entries. -/
  total : Nat := 66
  /-- Established count. -/
  established : Nat := 16
  /-- Tau-effective count. -/
  tau_effective : Nat := 25
  /-- Conjectural count. -/
  conjectural : Nat := 18
  /-- Metaphorical count. -/
  metaphorical : Nat := 7
  /-- Ch15 partial ledger count. -/
  ch15_count : Nat := 23
  deriving Repr
```
