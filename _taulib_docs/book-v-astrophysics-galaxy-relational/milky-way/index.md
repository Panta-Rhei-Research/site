---
{
  "projection_kind": "taulib_declaration",
  "title": "milky_way",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/milky-way/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::milky_way",
  "declaration_slug": "milky-way",
  "kind": "def",
  "name": "milky_way",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 97,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L97-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L97-L103",
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/verify/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L97-L103)
- Source range: L97-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Milky Way as a barred spiral. -/
```

## Source Excerpt

```lean
def milky_way : GalacticDefectBundle where
  morphology := .BarredSpiral
  baryonic_mass := 100  -- ~10^11 solar masses
  mass_pos := by omega
  disk_radius := 15     -- ~15 kpc
  has_bar := true
  num_arms := 4
```
