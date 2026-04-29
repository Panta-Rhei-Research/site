---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorExhaustionMap",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-exhaustion-map/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::SectorExhaustionMap",
  "declaration_slug": "sector-exhaustion-map",
  "kind": "structure",
  "name": "SectorExhaustionMap",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 137,
  "source_line_end": 146,
  "registry_ids": [
    "V.D145"
  ],
  "related_registry_items": [
    {
      "id": "V.D145",
      "title": "Sector Exhaustion Decomposition",
      "url": "/registry/object/V.D145/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L137-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L137-L146",
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
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L137-L146)
- Source range: L137-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D145` — Sector Exhaustion Decomposition

## Immediate Comment / Docstring

```lean
/-- [V.D145] Sector exhaustion map: explicit mapping from each
    phenomenon to its sector subset. -/
```

## Source Excerpt

```lean
structure SectorExhaustionMap where
  /-- Phenomenon. -/
  phenomenon : AstroPhenomenon
  /-- Assigned sectors. -/
  sectors : List SectorLabel
  /-- Sectors are non-empty. -/
  sectors_nonempty : sectors.length > 0
  /-- Sectors match the canonical assignment. -/
  canonical : sectors = primarySectors phenomenon
  deriving Repr
```
