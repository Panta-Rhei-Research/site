---
{
  "projection_kind": "taulib_declaration",
  "title": "FundamentalScalesTable",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/fundamental-scales-table/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::FundamentalScalesTable",
  "declaration_slug": "fundamental-scales-table",
  "kind": "structure",
  "name": "FundamentalScalesTable",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 65,
  "source_line_end": 73,
  "registry_ids": [
    "IV.D306"
  ],
  "related_registry_items": [
    {
      "id": "IV.D306",
      "title": "Fundamental Scales Table",
      "url": "/registry/object/IV.D306/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L65-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L65-L73",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L65-L73)
- Source range: L65-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D306` — Fundamental Scales Table

## Immediate Comment / Docstring

```lean
/-- [IV.D306] Fundamental scales table: dimensional constants as products
    of relational units M, L, H, Q and ι_τ. -/
```

## Source Excerpt

```lean
structure FundamentalScalesTable where
  /-- Number of fundamental scale entries. -/
  entry_count : Nat
  /-- Entries: c, h, k_e, ε₀, μ₀ = 5 dimensional formulas. -/
  entry_eq : entry_count = 5
  /-- Plus Planck units derived from them. -/
  planck_derived : Nat
  planck_eq : planck_derived = 3  -- ℓ_P, t_P, m_P
  deriving Repr
```
