---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_sector",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/strong-sector/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::strong_sector",
  "declaration_slug": "strong-sector",
  "kind": "def",
  "name": "strong_sector",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 141,
  "source_line_end": 151,
  "registry_ids": [
    "IV.D03"
  ],
  "related_registry_items": [
    {
      "id": "IV.D03",
      "title": "Strong Sector at E₁",
      "url": "/registry/object/IV.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L141-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L141-L151",
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/verify/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L141-L151)
- Source range: L141-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D03` — Strong Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [IV.D03] **Strong Sector (C)**: η-generator, strong force.
    Self-coupling κ(C;3) = ι_τ³/(1−ι_τ).
    Polarity: χ₋-dominant (tightening/additive).
    Depth: 3 (third primorial level).
    Physical: color holonomy, confinement, mass gap.
    The (1−ι_τ) denominator is the structural signature of confinement. -/
```

## Source Excerpt

```lean
def strong_sector : SectorPhysics where
  sector := .C
  generator := .eta
  depth := 3
  polarity := .ChiMinus
  -- κ(C;3) = ι³/(1−ι) = iota_cu / (iotaD − iota) per unit
  -- Numerator: iota³ * iotaD (to get common denom with (iotaD − iota))
  -- Denominator: iota_cu_denom * (iotaD − iota)
  coupling_numer := iota_cu_numer * iotaD
  coupling_denom := iota_cu_denom * (iotaD - iota)
  denom_pos := by simp [iota_cu_denom, iotaD, iota, iota_tau_numer, iota_tau_denom]
```
