---
{
  "projection_kind": "taulib_declaration",
  "title": "GalacticDefectBundle",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-defect-bundle/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::GalacticDefectBundle",
  "declaration_slug": "galactic-defect-bundle",
  "kind": "structure",
  "name": "GalacticDefectBundle",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 81,
  "source_line_end": 94,
  "registry_ids": [
    "V.D120"
  ],
  "related_registry_items": [
    {
      "id": "V.D120",
      "title": "Galaxy as Relational Coherence --- V.D53",
      "url": "/registry/object/V.D120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L81-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L81-L94",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L81-L94)
- Source range: L81-L94
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D120` — Galaxy as Relational Coherence --- V.D53

## Immediate Comment / Docstring

```lean
/-- [V.D120] Galactic defect bundle: a galaxy modeled as a
    macroscopic defect bundle with boundary data determining
    its rotation, morphology, and evolution.

    The galaxy is NOT a collection of point masses in a dark
    matter halo but a single τ-structural entity. -/
```

## Source Excerpt

```lean
structure GalacticDefectBundle where
  /-- Morphological type. -/
  morphology : GalaxyMorphology
  /-- Baryonic mass index (scaled, 10^9 solar masses). -/
  baryonic_mass : Nat
  /-- Baryonic mass is positive. -/
  mass_pos : baryonic_mass > 0
  /-- Disk radius index (scaled, kpc). -/
  disk_radius : Nat
  /-- Whether the galaxy has a bar. -/
  has_bar : Bool
  /-- Number of spiral arms (0 for non-spiral). -/
  num_arms : Nat
  deriving Repr
```
