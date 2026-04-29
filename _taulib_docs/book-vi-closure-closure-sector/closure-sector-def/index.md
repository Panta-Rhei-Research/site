---
{
  "projection_kind": "taulib_declaration",
  "title": "ClosureSectorDef",
  "permalink": "/verify/taulib/docs/book-vi-closure-closure-sector/closure-sector-def/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.ClosureSector`.",
  "declaration_id": "TauLib.BookVI.Closure.ClosureSector::ClosureSectorDef",
  "declaration_slug": "closure-sector-def",
  "kind": "structure",
  "name": "ClosureSectorDef",
  "module_name": "TauLib.BookVI.Closure.ClosureSector",
  "module_url": "/verify/taulib/docs/book-vi-closure-closure-sector/",
  "source_line_start": 41,
  "source_line_end": 54,
  "registry_ids": [
    "VI.D41"
  ],
  "related_registry_items": [
    {
      "id": "VI.D41",
      "title": "Closure Sector",
      "url": "/registry/object/VI.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L41-L54",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.ClosureSector",
        "url": "/verify/taulib/docs/book-vi-closure-closure-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L41-L54",
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

- Module: [TauLib.BookVI.Closure.ClosureSector](/verify/taulib/docs/book-vi-closure-closure-sector/)
- Source path: [`TauLib/BookVI/Closure/ClosureSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L41-L54)
- Source range: L41-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D41` — Closure Sector

## Immediate Comment / Docstring

```lean
/-- [VI.D41] Closure Sector: π''-sector on fiber T².
    Life Loop restricted to structure recycling on the fiber.
    Generator: π'' (solenoidal, Book I Part I).
    Dominant forces: Riemann + Navier–Stokes (Book III, Parts III, VII).
    Dual to Source sector (VI.D36): source produces, closure recycles. -/
```

## Source Excerpt

```lean
structure ClosureSectorDef where
  /-- Generator is pi'' (fiber). -/
  generator : String := "pi_double_prime"
  /-- Sector is primitive (single generator). -/
  is_primitive : Bool := true
  /-- Archetype organism. -/
  archetype : String := "Fungi"
  /-- Dominant force 1: Riemann (energy recycling). -/
  dominant_riemann : Bool := true
  /-- Dominant force 2: Navier–Stokes (transport/decomposition). -/
  dominant_navier_stokes : Bool := true
  /-- Dual to source sector. -/
  dual_to_source : Bool := true
  deriving Repr
```
