---
{
  "projection_kind": "taulib_declaration",
  "title": "SourceSectorDef",
  "permalink": "/verify/taulib/docs/book-vi-source-source-sector/source-sector-def/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::SourceSectorDef",
  "declaration_slug": "source-sector-def",
  "kind": "structure",
  "name": "SourceSectorDef",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/verify/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 42,
  "source_line_end": 53,
  "registry_ids": [
    "VI.D36"
  ],
  "related_registry_items": [
    {
      "id": "VI.D36",
      "title": "Source Sector",
      "url": "/registry/object/VI.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L42-L53",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/verify/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L42-L53",
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

- Module: [TauLib.BookVI.Source.SourceSector](/verify/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L42-L53)
- Source range: L42-L53
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D36` — Source Sector

## Immediate Comment / Docstring

```lean
/-- [VI.D36] Source Sector: π'-sector on fiber T².
    Life Loop restricted to structure generation on the fiber.
    Generator: π' (solenoidal, Book I Part I).
    Dominant forces: Hodge + BSD (Book III, Parts IV–V). -/
```

## Source Excerpt

```lean
structure SourceSectorDef where
  /-- Generator is pi' (fiber). -/
  generator : String := "pi_prime"
  /-- Sector is primitive (single generator). -/
  is_primitive : Bool := true
  /-- Archetype organism. -/
  archetype : String := "Plants"
  /-- Dominant force 1: Hodge (harmonic decomposition → morphogenesis). -/
  dominant_hodge : Bool := true
  /-- Dominant force 2: BSD (rank of rational points → genetic code). -/
  dominant_bsd : Bool := true
  deriving Repr
```
