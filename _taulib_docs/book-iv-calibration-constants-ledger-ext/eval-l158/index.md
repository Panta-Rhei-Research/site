---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L158",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/eval-l158/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::#eval:158",
  "declaration_slug": "eval-l158",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 158,
  "source_line_end": 158,
  "registry_ids": [
    "IV.R286",
    "IV.R287"
  ],
  "related_registry_items": [
    {
      "id": "IV.R286",
      "title": "5, 4, 3, 2, 1",
      "url": "/registry/object/IV.R286/"
    },
    {
      "id": "IV.R287",
      "title": "Honest fraction",
      "url": "/registry/object/IV.R287/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L158-L158",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L158-L158",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L158-L158)
- Source range: L158-L158
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R286` — 5, 4, 3, 2, 1
- `IV.R287` — Honest fraction

## Immediate Comment / Docstring

```lean
-- [IV.R286] The structural constants 5, 4, 3, 2, 1 form a
-- descending sequence from categorical to physical.
-- (Structural remark)

-- [IV.R287] Of Part II's content, approximately 60% is formally
-- verified: 11 established + 18 tau-effective = 29 Lean-proved items.
-- (Structural remark)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval coupling_table.total              -- 10
```
