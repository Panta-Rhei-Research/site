---
{
  "projection_kind": "taulib_declaration",
  "title": "MagneticForce",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/magnetic-force/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::MagneticForce",
  "declaration_slug": "magnetic-force",
  "kind": "structure",
  "name": "MagneticForce",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 432,
  "source_line_end": 437,
  "registry_ids": [
    "IV.P48"
  ],
  "related_registry_items": [
    {
      "id": "IV.P48",
      "title": "Magnetic Force Does No Work",
      "url": "/registry/object/IV.P48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L432-L437",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L432-L437",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L432-L437)
- Source range: L432-L437
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P48` — Magnetic Force Does No Work

## Immediate Comment / Docstring

```lean
/-- [IV.P48] Magnetic force is perpendicular to velocity: F = qv × B.
    The magnetic field does no work (F · v = 0). -/
```

## Source Excerpt

```lean
structure MagneticForce where
  /-- Force perpendicular to velocity. -/
  perpendicular : Bool := true
  /-- Does no work. -/
  no_work : Bool := true
  deriving Repr
```
