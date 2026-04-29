---
{
  "projection_kind": "taulib_declaration",
  "title": "uv_lf_excess_jades",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/uv-lf-excess-jades/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::uv_lf_excess_jades",
  "declaration_slug": "uv-lf-excess-jades",
  "kind": "theorem",
  "name": "uv_lf_excess_jades",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 311,
  "source_line_end": 312,
  "registry_ids": [
    "V.P164"
  ],
  "related_registry_items": [
    {
      "id": "V.P164",
      "title": "UV Luminosity Function Excess",
      "url": "/registry/object/V.P164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L311-L312",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L311-L312",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L311-L312)
- Source range: L311-L312
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P164` — UV Luminosity Function Excess

## Immediate Comment / Docstring

```lean
/-- [V.P164] UV luminosity function excess: Φ_τ/Φ_ΛCDM ~ E(z)^α, α~0.5-1.
    At z=13: excess factor ~ 5–30×, matching JWST JADES/CEERS observations. -/
```

## Source Excerpt

```lean
theorem uv_lf_excess_jades :
    jades_z13_enhancement.enhancement_x10 = 310 := rfl
```
