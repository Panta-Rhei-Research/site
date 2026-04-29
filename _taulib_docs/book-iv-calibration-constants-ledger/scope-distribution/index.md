---
{
  "projection_kind": "taulib_declaration",
  "title": "scope_distribution",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/scope-distribution/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::scope_distribution",
  "declaration_slug": "scope-distribution",
  "kind": "theorem",
  "name": "scope_distribution",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 179,
  "source_line_end": 183,
  "registry_ids": [
    "IV.R09"
  ],
  "related_registry_items": [
    {
      "id": "IV.R09",
      "title": "Self-Assessment",
      "url": "/registry/object/IV.R09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L179-L183",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L179-L183",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L179-L183)
- Source range: L179-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.R09` — Self-Assessment

## Immediate Comment / Docstring

```lean
/-- [IV.R09] Self-assessment: scope distribution across the ledger.
    - Established: 12 (10 couplings + 2 identities)
    - Tau-effective: 7 (5 formulas + 2 framework)
    - Conjectural: 4 (3 near-matches + 1 G frontier)
    - Metaphorical: 0 -/
```

## Source Excerpt

```lean
theorem scope_distribution :
    (complete_ledger.filter (·.scope == .Established)).length = 12 ∧
    (complete_ledger.filter (·.scope == .TauEffective)).length = 7 ∧
    (complete_ledger.filter (·.scope == .Conjectural)).length = 4 ∧
    (complete_ledger.filter (·.scope == .Metaphorical)).length = 0 := by native_decide
```
