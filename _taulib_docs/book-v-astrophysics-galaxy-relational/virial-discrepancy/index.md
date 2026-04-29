---
{
  "projection_kind": "taulib_declaration",
  "title": "virial_discrepancy",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/virial-discrepancy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::virial_discrepancy",
  "declaration_slug": "virial-discrepancy",
  "kind": "theorem",
  "name": "virial_discrepancy",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 210,
  "source_line_end": 211,
  "registry_ids": [
    "V.P66"
  ],
  "related_registry_items": [
    {
      "id": "V.P66",
      "title": "Galactic Virial Theorem --- V.P30",
      "url": "/registry/object/V.P66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L210-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L210-L211",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L210-L211)
- Source range: L210-L211
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P66` — Galactic Virial Theorem --- V.P30

## Immediate Comment / Docstring

```lean
/-- [V.P66] Virial discrepancy from boundary corrections: the factor
    ~5 discrepancy between virial and baryonic mass in clusters is
    NOT evidence for dark matter particles but for boundary corrections
    to the D-sector coupling at cluster scales. -/
```

## Source Excerpt

```lean
theorem virial_discrepancy (c : GalaxyClusterData) :
    c.baryonic_mass < c.virial_mass := c.baryonic_lt_virial
```
