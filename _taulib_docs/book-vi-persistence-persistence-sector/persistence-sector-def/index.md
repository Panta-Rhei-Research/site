---
{
  "projection_kind": "taulib_declaration",
  "title": "PersistenceSectorDef",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-sector-def/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::PersistenceSectorDef",
  "declaration_slug": "persistence-sector-def",
  "kind": "structure",
  "name": "PersistenceSectorDef",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 51,
  "source_line_end": 62,
  "registry_ids": [
    "VI.D24"
  ],
  "related_registry_items": [
    {
      "id": "VI.D24",
      "title": "Persistence Sector",
      "url": "/registry/object/VI.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L51-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L51-L62",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L51-L62)
- Source range: L51-L62
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D24` — Persistence Sector

## Immediate Comment / Docstring

```lean
/-- [VI.D24] Persistence Sector: α-sector on base circle τ¹.
    Life Loop restricted to base-temporal dynamics.
    Generator: α (radial, Book I Part I).
    Dominant forces: Poincaré + Riemann (Book III, Parts II–III). -/
```

## Source Excerpt

```lean
structure PersistenceSectorDef where
  /-- Generator is alpha (base). -/
  generator : String := "alpha"
  /-- Sector is primitive (single generator). -/
  is_primitive : Bool := true
  /-- Archetype organism. -/
  archetype : String := "Archaea"
  /-- Dominant force 1: Poincaré (temporal orbits). -/
  dominant_poincare : Bool := true
  /-- Dominant force 2: Riemann (energy quanta). -/
  dominant_riemann : Bool := true
  deriving Repr
```
