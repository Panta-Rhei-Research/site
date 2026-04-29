---
{
  "projection_kind": "taulib_declaration",
  "title": "GalaxyClusterData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-cluster-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::GalaxyClusterData",
  "declaration_slug": "galaxy-cluster-data",
  "kind": "structure",
  "name": "GalaxyClusterData",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 187,
  "source_line_end": 200,
  "registry_ids": [
    "V.D122"
  ],
  "related_registry_items": [
    {
      "id": "V.D122",
      "title": "Morphological Capacity Profile --- V.D55",
      "url": "/registry/object/V.D122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L187-L200",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L187-L200",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L187-L200)
- Source range: L187-L200
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D122` — Morphological Capacity Profile --- V.D55

## Immediate Comment / Docstring

```lean
/-- [V.D122] Galaxy cluster data: a bound collection of galaxies
    with virial mass discrepancy explained by boundary corrections
    (not dark matter). -/
```

## Source Excerpt

```lean
structure GalaxyClusterData where
  /-- Number of member galaxies. -/
  num_galaxies : Nat
  /-- Number is positive. -/
  num_pos : num_galaxies > 0
  /-- Cluster virial mass index (scaled, 10^14 solar masses). -/
  virial_mass : Nat
  /-- Total baryonic mass index (same scale). -/
  baryonic_mass : Nat
  /-- Baryonic always less than virial (the "discrepancy"). -/
  baryonic_lt_virial : baryonic_mass < virial_mass
  /-- Velocity dispersion (km/s). -/
  velocity_dispersion : Nat
  deriving Repr
```
