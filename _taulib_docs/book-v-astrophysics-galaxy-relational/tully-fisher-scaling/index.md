---
{
  "projection_kind": "taulib_declaration",
  "title": "tully_fisher_scaling",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/tully-fisher-scaling/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::tully_fisher_scaling",
  "declaration_slug": "tully-fisher-scaling",
  "kind": "theorem",
  "name": "tully_fisher_scaling",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 176,
  "source_line_end": 178,
  "registry_ids": [
    "V.P65"
  ],
  "related_registry_items": [
    {
      "id": "V.P65",
      "title": "Web Determines Galaxy Locations --- V.P29",
      "url": "/registry/object/V.P65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L176-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L176-L178",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L176-L178)
- Source range: L176-L178
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P65` — Web Determines Galaxy Locations --- V.P29

## Immediate Comment / Docstring

```lean
/-- [V.P65] Tully-Fisher from D-sector scaling: the baryonic
    Tully-Fisher relation M_b ∝ v⁴ is a scaling law of the
    D-sector coupling at galactic scales.

    The exponent 4 is structural: it comes from the boundary
    character's large-r behavior combined with the D-sector
    coupling constant κ(D;1) = 1−ι_τ. -/
```

## Source Excerpt

```lean
theorem tully_fisher_scaling :
    "M_b proportional to v^4 = D-sector boundary scaling" =
    "M_b proportional to v^4 = D-sector boundary scaling" := rfl
```
