---
{
  "projection_kind": "taulib_declaration",
  "title": "MultiSectorPhenomenon",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/multi-sector-phenomenon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::MultiSectorPhenomenon",
  "declaration_slug": "multi-sector-phenomenon",
  "kind": "structure",
  "name": "MultiSectorPhenomenon",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 200,
  "source_line_end": 205,
  "registry_ids": [
    "V.D146"
  ],
  "related_registry_items": [
    {
      "id": "V.D146",
      "title": "Dark Sector Hypothesis",
      "url": "/registry/object/V.D146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L200-L205",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L200-L205",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L200-L205)
- Source range: L200-L205
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D146` — Dark Sector Hypothesis

## Immediate Comment / Docstring

```lean
/-- [V.D146] Multi-sector phenomenon: a phenomenon involving
    two or more sectors simultaneously. -/
```

## Source Excerpt

```lean
structure MultiSectorPhenomenon where
  /-- Phenomenon. -/
  phenomenon : AstroPhenomenon
  /-- Must involve 2+ sectors. -/
  multi : (primarySectors phenomenon).length ≥ 2
  deriving Repr
```
