---
{
  "projection_kind": "taulib_declaration",
  "title": "E1Complete",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/e1-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::E1Complete",
  "declaration_slug": "e1-complete",
  "kind": "structure",
  "name": "E1Complete",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 176,
  "source_line_end": 189,
  "registry_ids": [
    "V.T142"
  ],
  "related_registry_items": [
    {
      "id": "V.T142",
      "title": "E1 Completeness Theorem",
      "url": "/registry/object/V.T142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L176-L189",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L176-L189",
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
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L176-L189)
- Source range: L176-L189
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T142` — E1 Completeness Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T142] E-layer 1 is complete: H_partial[omega], evaluated
    through 5 sectors and calibrated by m_n, accounts for every
    known physical phenomenon at E1.

    Complete does NOT mean all computations are done. It means:
    every phenomenon has a structural home in the boundary algebra.
    The ledger maps every known E1 entity to its tau-description. -/
```

## Source Excerpt

```lean
structure E1Complete where
  /-- All forces assigned to sectors. -/
  forces_assigned : Bool := true
  /-- All constants derived from iota_tau. -/
  constants_derived : Bool := true
  /-- Single calibration anchor (m_n). -/
  single_anchor : Bool := true
  /-- Some computations ongoing. -/
  computations_ongoing : Bool := true
  /-- Ledger entry count. -/
  ledger_entries : Nat
  /-- Matches the constants_ledger. -/
  entries_match : ledger_entries = 10
  deriving Repr
```
