---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyGenerator",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/holonomy-generator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::HolonomyGenerator",
  "declaration_slug": "holonomy-generator",
  "kind": "structure",
  "name": "HolonomyGenerator",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 154,
  "source_line_end": 161,
  "registry_ids": [
    "IV.D266"
  ],
  "related_registry_items": [
    {
      "id": "IV.D266",
      "title": "Boundary holonomy generators",
      "url": "/registry/object/IV.D266/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L154-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L154-L161",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L154-L161)
- Source range: L154-L161
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D266` — Boundary holonomy generators

## Immediate Comment / Docstring

```lean
/-- [IV.D266] The 5 generators of the boundary holonomy algebra.
    Each generator produces holonomy around one sector of L. -/
```

## Source Excerpt

```lean
structure HolonomyGenerator where
  /-- The underlying generator. -/
  gen : Generator
  /-- Associated sector. -/
  sector : Sector
  /-- Correct assignment. -/
  correct : GenSectorAssignment gen = sector
  deriving Repr
```
