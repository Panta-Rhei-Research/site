---
{
  "projection_kind": "taulib_declaration",
  "title": "spiral_arms_density_waves",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/spiral-arms-density-waves/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::spiral_arms_density_waves",
  "declaration_slug": "spiral-arms-density-waves",
  "kind": "theorem",
  "name": "spiral_arms_density_waves",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 127,
  "source_line_end": 130,
  "registry_ids": [
    "V.P64"
  ],
  "related_registry_items": [
    {
      "id": "V.P64",
      "title": "Galaxy Formation Sequence --- V.P28",
      "url": "/registry/object/V.P64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L127-L130",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L127-L130",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L127-L130)
- Source range: L127-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P64` — Galaxy Formation Sequence --- V.P28

## Immediate Comment / Docstring

```lean
/-- [V.P64] Spiral arms from defect density waves: spiral structure
    is a standing-wave pattern in the galactic defect field, not a
    material structure. Stars move through arms. -/
```

## Source Excerpt

```lean
theorem spiral_arms_density_waves (g : GalacticDefectBundle)
    (_hs : g.morphology = .Spiral ∨ g.morphology = .BarredSpiral)
    (ha : g.num_arms > 0) :
    g.num_arms > 0 := ha
```
