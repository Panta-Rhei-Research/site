---
{
  "projection_kind": "taulib_declaration",
  "title": "framework_ledger",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/framework-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::framework_ledger",
  "declaration_slug": "framework-ledger",
  "kind": "def",
  "name": "framework_ledger",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 139,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L139-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L139-L143",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L139-L143)
- Source range: L139-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The anchor, collapse, and frontier entries. -/
```

## Source Excerpt

```lean
def framework_ledger : List LedgerEntry := [
  ⟨"IV.D30", "Calibration anchor m_n (single input)", "framework", .TauEffective⟩,
  ⟨"IV.T06", "5→1 collapse (4 of 5 from ι_τ)", "framework", .TauEffective⟩,
  ⟨"IV.R08", "G frontier (deferred to Book V)", "framework", .Conjectural⟩
]
```
