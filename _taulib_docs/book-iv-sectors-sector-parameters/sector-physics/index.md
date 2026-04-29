---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorPhysics",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/sector-physics/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::SectorPhysics",
  "declaration_slug": "sector-physics",
  "kind": "structure",
  "name": "SectorPhysics",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 75,
  "source_line_end": 104,
  "registry_ids": [
    "IV.D01"
  ],
  "related_registry_items": [
    {
      "id": "IV.D01",
      "title": "Sector Physics Template",
      "url": "/registry/object/IV.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L75-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SectorParameters",
        "url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L75-L104",
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/verify/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L75-L104)
- Source range: L75-L104
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D01` — Sector Physics Template

## Immediate Comment / Docstring

```lean
/-- [IV.D01] The four defining parameters of a sector at E₁.
    Every sector is completely characterized by these four values.
    All couplings are rational functions of ι_τ. -/
```

## Source Excerpt

```lean
structure SectorPhysics where
  /-- The abstract sector (from Book III Decomposition). -/
  sector : Sector
  /-- The kernel generator seeding this sector. -/
  generator : Generator
  /-- Primorial depth at which the coupling operates. -/
  depth : TauIdx
  /-- Spectral polarity signature. -/
  polarity : PolaritySign
  /-- Self-coupling numerator (scaled by coupling_denom). -/
  coupling_numer : Nat
  /-- Self-coupling denominator (common scale). -/
  coupling_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : coupling_denom > 0 := by omega
  deriving Repr

-- ============================================================
-- SCALED RATIONAL ARITHMETIC
-- ============================================================

/-- The common denominator for coupling computations.
    We use 10¹² to preserve precision through multiplication. -/
abbrev CouplingScale : Nat := 1000000000000  -- 10¹²

/-- ι_τ numerator at scale 10⁶ (from Iota.lean). -/
abbrev iota : Nat := iota_tau_numer  -- 341304

/-- ι_τ denominator at scale 10⁶ (from Iota.lean). -/
abbrev iotaD : Nat := iota_tau_denom  -- 1000000
```
