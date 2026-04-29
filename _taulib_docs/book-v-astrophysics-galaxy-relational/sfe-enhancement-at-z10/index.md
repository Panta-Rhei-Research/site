---
{
  "projection_kind": "taulib_declaration",
  "title": "sfe_enhancement_at_z10",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/sfe-enhancement-at-z10/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::sfe_enhancement_at_z10",
  "declaration_slug": "sfe-enhancement-at-z10",
  "kind": "theorem",
  "name": "sfe_enhancement_at_z10",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 306,
  "source_line_end": 307,
  "registry_ids": [
    "V.P163"
  ],
  "related_registry_items": [
    {
      "id": "V.P163",
      "title": "SFE Enhancement Factor",
      "url": "/registry/object/V.P163/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L306-L307",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L306-L307",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L306-L307)
- Source range: L306-L307
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P163` — SFE Enhancement Factor

## Immediate Comment / Docstring

```lean
/-- [V.P163] SFE enhancement: ε(z)/ε(0) = Ω_m^(1/4)·(1+z)^(3/4). -/
```

## Source Excerpt

```lean
theorem sfe_enhancement_at_z10 :
    gnz11_enhancement.tau_sfe_pct = 47 := rfl
```
