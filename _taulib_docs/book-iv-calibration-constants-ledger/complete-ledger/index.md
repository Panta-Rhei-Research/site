---
{
  "projection_kind": "taulib_declaration",
  "title": "complete_ledger",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/complete-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::complete_ledger",
  "declaration_slug": "complete-ledger",
  "kind": "def",
  "name": "complete_ledger",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 150,
  "source_line_end": 152,
  "registry_ids": [
    "IV.D39"
  ],
  "related_registry_items": [
    {
      "id": "IV.D39",
      "title": "Complete Constants Ledger",
      "url": "/registry/object/IV.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L150-L152",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.ConstantsLedger",
        "url": "/corpus/taulib/docs/book-iv-calibration-constants-ledger/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L150-L152",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedger](/corpus/taulib/docs/book-iv-calibration-constants-ledger/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L150-L152)
- Source range: L150-L152
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `IV.D39` — Complete Constants Ledger

## Immediate Comment / Docstring

```lean
/-- [IV.D39] The complete constants ledger: all Part II outputs. -/
```

## Source Excerpt

```lean
def complete_ledger : List LedgerEntry :=
  coupling_ledger ++ formula_ledger ++ identity_ledger ++
  near_match_ledger ++ framework_ledger
```
