---
{
  "projection_kind": "taulib_declaration",
  "title": "ToroidalFluxIntegral",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/toroidal-flux-integral/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::ToroidalFluxIntegral",
  "declaration_slug": "toroidal-flux-integral",
  "kind": "structure",
  "name": "ToroidalFluxIntegral",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 327,
  "source_line_end": 334,
  "registry_ids": [
    "V.D285"
  ],
  "related_registry_items": [
    {
      "id": "V.D285",
      "title": "Toroidal Flux Integral",
      "url": "/registry/object/V.D285/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L327-L334",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L327-L334",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L327-L334)
- Source range: L327-L334
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D285` — Toroidal Flux Integral

## Immediate Comment / Docstring

```lean
/-- [V.D285] Toroidal Flux Integral: magnetic flux through a meridional
    cross-section of the torus, measuring the poloidal field component. -/
```

## Source Excerpt

```lean
structure ToroidalFluxIntegral where
  /-- Description of the flux surface. -/
  surface : String := "meridional disk"
  /-- Flux value (arbitrary units × 1000). -/
  flux_x1000 : Nat
  /-- Flux is non-negative. -/
  flux_nonneg : flux_x1000 ≥ 0 := by omega
  deriving Repr
```
