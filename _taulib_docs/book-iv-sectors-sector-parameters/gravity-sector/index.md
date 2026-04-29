---
{
  "projection_kind": "taulib_declaration",
  "title": "gravity_sector",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/gravity-sector/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::gravity_sector",
  "declaration_slug": "gravity-sector",
  "kind": "def",
  "name": "gravity_sector",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 172,
  "source_line_end": 179,
  "registry_ids": [
    "IV.D05"
  ],
  "related_registry_items": [
    {
      "id": "IV.D05",
      "title": "Gravity Sector at E₁",
      "url": "/registry/object/IV.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L172-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L172-L179",
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
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L172-L179)
- Source range: L172-L179
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D05` — Gravity Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [IV.D05] **Gravity Sector (D)**: α-generator, gravitational force.
    Self-coupling κ(D;1) = 1−ι_τ.
    Polarity: χ₊-dominant.
    Depth: 1 (first primorial level).
    Physical: frame holonomy, temporal flow, G = (c³/ℏ)·ι_τ². -/
```

## Source Excerpt

```lean
def gravity_sector : SectorPhysics where
  sector := .D
  generator := .alpha
  depth := 1
  polarity := .ChiPlus
  coupling_numer := iotaD - iota             -- (1 − ι_τ) numerator = 658541
  coupling_denom := iotaD                     -- denominator = 10⁶
  denom_pos := by simp [iotaD, iota_tau_denom]
```
