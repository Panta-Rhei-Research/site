---
{
  "projection_kind": "taulib_declaration",
  "title": "ledger_breakdown",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/ledger-breakdown/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::ledger_breakdown",
  "declaration_slug": "ledger-breakdown",
  "kind": "theorem",
  "name": "ledger_breakdown",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 162,
  "source_line_end": 168,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L162-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L162-L168",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L162-L168)
- Source range: L162-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 10 coupling + 5 formula + 2 identity + 3 near-match + 3 framework = 23. -/
```

## Source Excerpt

```lean
theorem ledger_breakdown :
    coupling_ledger.length = 10 ∧
    formula_ledger.length = 5 ∧
    identity_ledger.length = 2 ∧
    near_match_ledger.length = 3 ∧
    framework_ledger.length = 3 := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩
```
