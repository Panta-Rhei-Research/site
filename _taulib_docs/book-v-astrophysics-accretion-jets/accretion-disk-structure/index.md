---
{
  "projection_kind": "taulib_declaration",
  "title": "AccretionDiskStructure",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-disk-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::AccretionDiskStructure",
  "declaration_slug": "accretion-disk-structure",
  "kind": "structure",
  "name": "AccretionDiskStructure",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 102,
  "source_line_end": 115,
  "registry_ids": [
    "V.D129"
  ],
  "related_registry_items": [
    {
      "id": "V.D129",
      "title": "Accretion Funnel (tau-geodesic)",
      "url": "/registry/object/V.D129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L102-L115",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L102-L115",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L102-L115)
- Source range: L102-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D129` — Accretion Funnel (tau-geodesic)

## Immediate Comment / Docstring

```lean
/-- [V.D129] Accretion disk structure: parametrization of the
    steady-state accretion disk around a compact object.

    All disk properties are readouts of the D-sector coupling
    combined with angular momentum conservation. -/
```

## Source Excerpt

```lean
structure AccretionDiskStructure where
  /-- Central object type. -/
  central_object : CompactObjectType
  /-- Disk model. -/
  model : DiskModel
  /-- Inner disk radius (Schwarzschild radii, scaled × 10). -/
  inner_radius : Nat
  /-- Inner radius positive. -/
  inner_pos : inner_radius > 0
  /-- Accretion rate (scaled, 10⁻⁸ M_☉/yr × 100). -/
  accretion_rate : Nat
  /-- Radiative efficiency (percent × 10). -/
  efficiency_permil : Nat
  deriving Repr
```
