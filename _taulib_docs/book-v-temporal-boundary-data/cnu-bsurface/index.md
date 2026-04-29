---
{
  "projection_kind": "taulib_declaration",
  "title": "CnuBSurface",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/cnu-bsurface/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::CnuBSurface",
  "declaration_slug": "cnu-bsurface",
  "kind": "structure",
  "name": "CnuBSurface",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 142,
  "source_line_end": 155,
  "registry_ids": [
    "V.D39"
  ],
  "related_registry_items": [
    {
      "id": "V.D39",
      "title": "CnuB echo surface",
      "url": "/registry/object/V.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L142-L155",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BoundaryData",
        "url": "/verify/taulib/docs/book-v-temporal-boundary-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L142-L155",
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

- Module: [TauLib.BookV.Temporal.BoundaryData](/verify/taulib/docs/book-v-temporal-boundary-data/)
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L142-L155)
- Source range: L142-L155
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D39` — CnuB echo surface

## Immediate Comment / Docstring

```lean
/-- [V.D39] CnuB echo surface Sigma_{CnuB} = H_partial[omega]|_{n=n_nu}.

    The boundary holonomy algebra at neutrino decoupling, encoding:
    - Neutrino energy spectrum (Fermi-Dirac at T_nu)
    - Number of species (3 from A-sector)
    - Mass spectrum (m_nu ~ m_e * iota_tau^15)

    Predicted T_{CnuB} ~ 1.95 K (standard value). -/
```

## Source Excerpt

```lean
structure CnuBSurface where
  /-- Orbit depth of the echo surface. -/
  depth : Nat
  /-- Depth is positive. -/
  depth_pos : depth > 0
  /-- Number of neutrino species. -/
  species : Nat := 3
  /-- CnuB temperature numerator (mK, scaled: 1950 = 1.95 K). -/
  temp_numer : Nat := 1950
  /-- CnuB temperature denominator. -/
  temp_denom : Nat := 1000
  /-- Total neutrino mass prediction (meV). -/
  total_mass_meV : Nat := 58
  deriving Repr
```
