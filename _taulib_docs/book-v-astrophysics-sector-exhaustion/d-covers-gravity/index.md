---
{
  "projection_kind": "taulib_declaration",
  "title": "d_covers_gravity",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/d-covers-gravity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::d_covers_gravity",
  "declaration_slug": "d-covers-gravity",
  "kind": "theorem",
  "name": "d_covers_gravity",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 180,
  "source_line_end": 182,
  "registry_ids": [
    "V.C14"
  ],
  "related_registry_items": [
    {
      "id": "V.C14",
      "title": "No Dark Matter Particle",
      "url": "/registry/object/V.C14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L180-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L180-L182",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L180-L182)
- Source range: L180-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C14` — No Dark Matter Particle

## Immediate Comment / Docstring

```lean
/-- [V.C14] D-sector covers all gravitational phenomena. -/
```

## Source Excerpt

```lean
theorem d_covers_gravity :
    SectorLabel.D ∈ primarySectors .GravitationalDynamics := by
  simp [primarySectors]
```
