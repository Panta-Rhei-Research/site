---
{
  "projection_kind": "taulib_declaration",
  "title": "LedgerScope",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/ledger-scope/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::LedgerScope",
  "declaration_slug": "ledger-scope",
  "kind": "inductive",
  "name": "LedgerScope",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 59,
  "source_line_end": 64,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L59-L64",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L59-L64",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L59-L64)
- Source range: L59-L64
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D38` — Ledger Entry

## Immediate Comment / Docstring

```lean
/-- [IV.D38] Four-tier scope classification for ledger entries. -/
```

## Source Excerpt

```lean
inductive LedgerScope
  | Established      -- Lean-proved structural identity
  | TauEffective     -- Derived within τ-framework, internally verified
  | Conjectural      -- Comparison with experiment
  | Metaphorical     -- Conceptual analogy (not used in Part II)
  deriving Repr, DecidableEq
```
