---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorLift",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/sector-lift/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::SectorLift",
  "declaration_slug": "sector-lift",
  "kind": "structure",
  "name": "SectorLift",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 166,
  "source_line_end": 172,
  "registry_ids": [
    "IV.D262"
  ],
  "related_registry_items": [
    {
      "id": "IV.D262",
      "title": "Canonical sector lifts",
      "url": "/registry/object/IV.D262/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L166-L172",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L166-L172",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L166-L172)
- Source range: L166-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D262` — Canonical sector lifts

## Immediate Comment / Docstring

```lean
/-- [IV.D262] A canonical sector lift: Λ_S: L → τ³ projecting boundary
    data to a specific sector. There are 5 lifts (one per sector). -/
```

## Source Excerpt

```lean
structure SectorLift where
  /-- Target sector. -/
  sector : Sector
  /-- The lift produces rational functions of ι_τ. -/
  rational : Bool
  rational_true : rational = true
  deriving Repr
```
