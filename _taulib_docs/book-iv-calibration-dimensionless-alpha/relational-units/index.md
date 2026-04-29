---
{
  "projection_kind": "taulib_declaration",
  "title": "RelationalUnits",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::RelationalUnits",
  "declaration_slug": "relational-units",
  "kind": "structure",
  "name": "RelationalUnits",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 60,
  "source_line_end": 73,
  "registry_ids": [
    "IV.D287"
  ],
  "related_registry_items": [
    {
      "id": "IV.D287",
      "title": "Five Relational Units",
      "url": "/registry/object/IV.D287/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L60-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L60-L73",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L60-L73)
- Source range: L60-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D287` — Five Relational Units

## Immediate Comment / Docstring

```lean
/-- [IV.D287] The five relational units M, L, H, Q, R derived from
    the neutron mass anchor m_n and ι_τ. The τ-framework collapses
    the SI unit system from 7 base units to 1 anchor + 1 constant. -/
```

## Source Excerpt

```lean
structure RelationalUnits where
  /-- M = m_n (mass anchor). -/
  mass_is_neutron : Bool
  mass_true : mass_is_neutron = true
  /-- Total relational units. -/
  unit_count : Nat
  count_eq : unit_count = 5
  /-- SI base units collapsed from. -/
  si_base : Nat
  si_eq : si_base = 7
  /-- Effective free parameters. -/
  free_params : Nat
  free_eq : free_params = 1  -- just m_n
  deriving Repr
```
