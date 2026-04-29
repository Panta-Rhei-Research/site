---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralConstantsTable",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/structural-constants-table/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::StructuralConstantsTable",
  "declaration_slug": "structural-constants-table",
  "kind": "structure",
  "name": "StructuralConstantsTable",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 115,
  "source_line_end": 131,
  "registry_ids": [
    "IV.D308"
  ],
  "related_registry_items": [
    {
      "id": "IV.D308",
      "title": "Structural Constants Table",
      "url": "/registry/object/IV.D308/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L115-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L115-L131",
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
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L115-L131)
- Source range: L115-L131
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D308` — Structural Constants Table

## Immediate Comment / Docstring

```lean
/-- [IV.D308] Structural constants: dimensionless integers determined
    by kernel axioms K0-K6. -/
```

## Source Excerpt

```lean
structure StructuralConstantsTable where
  /-- 5 generators. -/
  generators : Nat
  gen_eq : generators = 5
  /-- 4 arena dimensions. -/
  arena_dim : Nat
  dim_eq : arena_dim = 4
  /-- 3 spatial dimensions (fiber). -/
  spatial : Nat
  spatial_eq : spatial = 3
  /-- 2 lobes (lemniscate). -/
  lobes : Nat
  lobes_eq : lobes = 2
  /-- 1 master constant. -/
  constants : Nat
  const_eq : constants = 1
  deriving Repr
```
