---
{
  "projection_kind": "taulib_declaration",
  "title": "AgencySectorDef",
  "permalink": "/verify/taulib/docs/book-vi-agency-agency-sector/agency-sector-def/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::AgencySectorDef",
  "declaration_slug": "agency-sector-def",
  "kind": "structure",
  "name": "AgencySectorDef",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/verify/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 39,
  "source_line_end": 50,
  "registry_ids": [
    "VI.D29"
  ],
  "related_registry_items": [
    {
      "id": "VI.D29",
      "title": "Agency Sector",
      "url": "/registry/object/VI.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L39-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/verify/taulib/docs/book-vi-agency-agency-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L39-L50",
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

- Module: [TauLib.BookVI.Agency.AgencySector](/verify/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L39-L50)
- Source range: L39-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D29` — Agency Sector

## Immediate Comment / Docstring

```lean
/-- [VI.D29] Agency Sector: π-sector on base circle τ¹.
    Life Loop extended with spatial displacement on base.
    Generator: π (solenoidal, Book I Part I).
    Dominant forces: Navier–Stokes + Poincaré (Book III, Parts VII, II). -/
```

## Source Excerpt

```lean
structure AgencySectorDef where
  /-- Generator is pi (base). -/
  generator : String := "pi"
  /-- Sector is primitive (single generator). -/
  is_primitive : Bool := true
  /-- Archetype organism. -/
  archetype : String := "Bacteria"
  /-- Dominant force 1: Navier–Stokes (motility, fluid dynamics). -/
  dominant_navier_stokes : Bool := true
  /-- Dominant force 2: Poincaré (circulation). -/
  dominant_poincare : Bool := true
  deriving Repr
```
