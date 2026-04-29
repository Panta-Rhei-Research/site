---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_sector",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/higgs-sector/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::higgs_sector",
  "declaration_slug": "higgs-sector",
  "kind": "def",
  "name": "higgs_sector",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 158,
  "source_line_end": 166,
  "registry_ids": [
    "IV.D04"
  ],
  "related_registry_items": [
    {
      "id": "IV.D04",
      "title": "Higgs Sector at E₁",
      "url": "/registry/object/IV.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L158-L166",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L158-L166",
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
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L158-L166)
- Source range: L158-L166
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D04` — Higgs Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [IV.D04] **Higgs Sector (ω)**: γ∩η crossing, Higgs/mass mechanism.
    Self-coupling κ(B,C) = ι_τ³/(1+ι_τ).
    Polarity: crossing (both lobes active simultaneously).
    Depth: 3 (third primorial level).
    Physical: mass generation, dense spatial occupancy.
    The unique +1 derived sector from the lemniscate crossing. -/
```

## Source Excerpt

```lean
def higgs_sector : SectorPhysics where
  sector := .Omega
  generator := .omega
  depth := 3
  polarity := .Crossing
  -- κ(B,C) = ι³/(1+ι) = iota_cu / (iotaD + iota)
  coupling_numer := iota_cu_numer * iotaD
  coupling_denom := iota_cu_denom * (iotaD + iota)
  denom_pos := by simp [iota_cu_denom, iotaD, iota, iota_tau_numer, iota_tau_denom]
```
