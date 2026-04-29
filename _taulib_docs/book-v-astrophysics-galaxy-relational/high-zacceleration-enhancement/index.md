---
{
  "projection_kind": "taulib_declaration",
  "title": "HighZAccelerationEnhancement",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/high-zacceleration-enhancement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::HighZAccelerationEnhancement",
  "declaration_slug": "high-zacceleration-enhancement",
  "kind": "structure",
  "name": "HighZAccelerationEnhancement",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 256,
  "source_line_end": 267,
  "registry_ids": [
    "V.D299"
  ],
  "related_registry_items": [
    {
      "id": "V.D299",
      "title": "High-z Acceleration Enhancement",
      "url": "/registry/object/V.D299/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L256-L267",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
        "url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L256-L267",
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/verify/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L256-L267)
- Source range: L256-L267
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D299` — High-z Acceleration Enhancement

## Immediate Comment / Docstring

```lean
/-- [V.D299] High-z acceleration enhancement:
    E(z) = a₀(z)/a₀(0) = H(z)/H₀ ≈ Ω_m^(1/2) · (1+z)^(3/2).
    At z=10: E ≈ 20.5, at z=13: E ≈ 29.4.
    τ-effective: uses V.T204 (a₀(z) = cH(z)ι_τ/2) + standard Friedmann. -/
```

## Source Excerpt

```lean
structure HighZAccelerationEnhancement where
  /-- Redshift. -/
  z_x10 : Nat
  /-- Enhancement factor E(z) = a₀(z)/a₀(0) (scaled ×10). -/
  enhancement_x10 : Nat
  /-- SFE enhancement ~ E^(1/2) (scaled ×10). -/
  sfe_enhancement_x10 : Nat
  /-- Baseline SFE at z=0 (percent). -/
  baseline_sfe_pct : Nat := 10
  /-- Enhanced SFE (percent). -/
  enhanced_sfe_pct : Nat
  deriving Repr
```
