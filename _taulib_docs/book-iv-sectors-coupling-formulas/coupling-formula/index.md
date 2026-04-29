---
{
  "projection_kind": "taulib_declaration",
  "title": "CouplingFormula",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::CouplingFormula",
  "declaration_slug": "coupling-formula",
  "kind": "structure",
  "name": "CouplingFormula",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 61,
  "source_line_end": 72,
  "registry_ids": [
    "IV.D07"
  ],
  "related_registry_items": [
    {
      "id": "IV.D07",
      "title": "Coupling Formula Map",
      "url": "/registry/object/IV.D07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L61-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.CouplingFormulas",
        "url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L61-L72",
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

- Module: [TauLib.BookIV.Sectors.CouplingFormulas](/verify/taulib/docs/book-iv-sectors-coupling-formulas/)
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L61-L72)
- Source range: L61-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D07` — Coupling Formula Map

## Immediate Comment / Docstring

```lean
/-- [IV.D07] A coupling formula: rational expression of ι_τ between
    two sectors, evaluated at the rational approximation. -/
```

## Source Excerpt

```lean
structure CouplingFormula where
  /-- First sector (ordered by Sector.toNat). -/
  sector_i : Sector
  /-- Second sector. -/
  sector_j : Sector
  /-- Numerator of coupling (scaled). -/
  numer : Nat
  /-- Denominator of coupling (scaled). -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0 := by omega
  deriving Repr
```
