---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_table",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/coupling-table-l48/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::coupling_table",
  "declaration_slug": "coupling-table-l48",
  "kind": "def",
  "name": "coupling_table",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 48,
  "source_line_end": 54,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L48-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L48-L54",
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedgerExt](/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L48-L54)
- Source range: L48-L54
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical coupling table. -/
```

## Source Excerpt

```lean
def coupling_table : CouplingTable where
  self_count := 5
  self_eq := rfl
  cross_count := 5
  cross_eq := rfl
  total := 10
  total_eq := rfl
```
