---
{
  "projection_kind": "taulib_declaration",
  "title": "em_sector",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/em-sector/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::em_sector",
  "declaration_slug": "em-sector",
  "kind": "def",
  "name": "em_sector",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 127,
  "source_line_end": 134,
  "registry_ids": [
    "IV.D02"
  ],
  "related_registry_items": [
    {
      "id": "IV.D02",
      "title": "EM Sector at E₁",
      "url": "/registry/object/IV.D02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L127-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L127-L134",
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
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L127-L134)
- Source range: L127-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D02` — EM Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [IV.D02] **EM Sector (B)**: γ-generator, electromagnetic force.
    Self-coupling κ(B;2) = ι_τ².
    Polarity: χ₊-dominant (spreading/multiplicative).
    Depth: 2 (second primorial level).
    Physical: photon transport, Maxwell equations, fine structure. -/
```

## Source Excerpt

```lean
def em_sector : SectorPhysics where
  sector := .B
  generator := .gamma
  depth := 2
  polarity := .ChiPlus
  coupling_numer := iota_sq_numer          -- ι_τ² numerator
  coupling_denom := iota_sq_denom          -- ι_τ² denominator
  denom_pos := by simp [iota_sq_denom, iotaD, iota_tau_denom]
```
