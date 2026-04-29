---
{
  "projection_kind": "taulib_declaration",
  "title": "PoloidalFluxIntegral",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/poloidal-flux-integral/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::PoloidalFluxIntegral",
  "declaration_slug": "poloidal-flux-integral",
  "kind": "structure",
  "name": "PoloidalFluxIntegral",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 338,
  "source_line_end": 345,
  "registry_ids": [
    "V.D286"
  ],
  "related_registry_items": [
    {
      "id": "V.D286",
      "title": "Poloidal Flux Integral",
      "url": "/registry/object/V.D286/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L338-L345",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L338-L345",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L338-L345)
- Source range: L338-L345
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D286` — Poloidal Flux Integral

## Immediate Comment / Docstring

```lean
/-- [V.D286] Poloidal Flux Integral: magnetic flux through the torus hole,
    topologically protected in ideal MHD. Requires genus ≥ 1. -/
```

## Source Excerpt

```lean
structure PoloidalFluxIntegral where
  /-- Description of the flux surface. -/
  surface : String := "torus hole disk"
  /-- Flux value (arbitrary units × 1000). -/
  flux_x1000 : Nat
  /-- Topologically protected (1 = yes). -/
  topo_protected : Nat := 1
  deriving Repr
```
