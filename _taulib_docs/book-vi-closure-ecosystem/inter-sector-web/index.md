---
{
  "projection_kind": "taulib_declaration",
  "title": "InterSectorWeb",
  "permalink": "/verify/taulib/docs/book-vi-closure-ecosystem/inter-sector-web/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::InterSectorWeb",
  "declaration_slug": "inter-sector-web",
  "kind": "structure",
  "name": "InterSectorWeb",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/verify/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 35,
  "source_line_end": 44,
  "registry_ids": [
    "VI.D44"
  ],
  "related_registry_items": [
    {
      "id": "VI.D44",
      "title": "Inter-Sector Web",
      "url": "/registry/object/VI.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L35-L44",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/verify/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L35-L44",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/verify/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L35-L44)
- Source range: L35-L44
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D44` — Inter-Sector Web

## Immediate Comment / Docstring

```lean
/-- [VI.D44] Inter-Sector Web: coupling graph between Life sectors.
    Each sector (persistence, agency, source, closure, consumer) is a node;
    edges represent inter-sector metabolic or informational coupling.
    Every ecosystem is an Inter-Sector Web. -/
```

## Source Excerpt

```lean
structure InterSectorWeb where
  /-- Number of sector nodes. -/
  sector_count : Nat
  /-- Exactly 5 sectors. -/
  count_eq : sector_count = 5
  /-- Web is connected (every sector couples to at least one other). -/
  connected : Bool := true
  /-- Source-closure duality: these two sectors are always coupled. -/
  source_closure_dual : Bool := true
  deriving Repr
```
