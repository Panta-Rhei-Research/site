---
{
  "projection_kind": "taulib_declaration",
  "title": "CouplingTable",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/coupling-table/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::CouplingTable",
  "declaration_slug": "coupling-table",
  "kind": "structure",
  "name": "CouplingTable",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 35,
  "source_line_end": 45,
  "registry_ids": [
    "IV.D305"
  ],
  "related_registry_items": [
    {
      "id": "IV.D305",
      "title": "Coupling Constants Table",
      "url": "/registry/object/IV.D305/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L35-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
        "url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L35-L45",
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedgerExt](/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L35-L45)
- Source range: L35-L45
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D305` — Coupling Constants Table

## Immediate Comment / Docstring

```lean
/-- [IV.D305] The complete coupling constants table:
    10 entries (5 self + 5 cross), all rational functions of ι_τ. -/
```

## Source Excerpt

```lean
structure CouplingTable where
  /-- Self-coupling count. -/
  self_count : Nat
  self_eq : self_count = 5
  /-- Cross-coupling count. -/
  cross_count : Nat
  cross_eq : cross_count = 5  -- 5 primitive cross-couplings
  /-- Total. -/
  total : Nat
  total_eq : total = self_count + cross_count
  deriving Repr
```
