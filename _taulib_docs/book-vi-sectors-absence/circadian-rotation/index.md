---
{
  "projection_kind": "taulib_declaration",
  "title": "CircadianRotation",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/circadian-rotation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::CircadianRotation",
  "declaration_slug": "circadian-rotation",
  "kind": "structure",
  "name": "CircadianRotation",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 82,
  "source_line_end": 85,
  "registry_ids": [
    "VI.P09"
  ],
  "related_registry_items": [
    {
      "id": "VI.P09",
      "title": "24-Hour Cycle as τ¹ Rotation",
      "url": "/registry/object/VI.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L82-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Absence",
        "url": "/verify/taulib/docs/book-vi-sectors-absence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L82-L85",
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

- Module: [TauLib.BookVI.Sectors.Absence](/verify/taulib/docs/book-vi-sectors-absence/)
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L82-L85)
- Source range: L82-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P09` — 24-Hour Cycle as τ¹ Rotation

## Immediate Comment / Docstring

```lean
/-- [VI.P09] Circadian 24h = one full α-rotation on τ¹. -/
```

## Source Excerpt

```lean
structure CircadianRotation where
  period_hours : Nat := 24
  winding_number : Nat := 1
  deriving Repr
```
