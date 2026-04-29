---
{
  "projection_kind": "taulib_declaration",
  "title": "ModeRepulsionEntry",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/mode-repulsion-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::ModeRepulsionEntry",
  "declaration_slug": "mode-repulsion-entry",
  "kind": "structure",
  "name": "ModeRepulsionEntry",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 286,
  "source_line_end": 293,
  "registry_ids": [
    "IV.R144"
  ],
  "related_registry_items": [
    {
      "id": "IV.R144",
      "title": "Mode-repulsion geometry",
      "url": "/registry/object/IV.R144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L286-L293",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L286-L293",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L286-L293)
- Source range: L286-L293
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R144` — Mode-repulsion geometry

## Immediate Comment / Docstring

```lean
/-- [IV.R144] Molecular geometry from mode repulsion: k mode pairs
    maximize minimum angular separation.

    | k | Geometry | Angle |
    |---|----------|-------|
    | 2 | linear | 180° |
    | 3 | trigonal planar | 120° |
    | 4 | tetrahedral | 109.5° |
    | 5 | trigonal bipyramidal | 90°/120° |
    | 6 | octahedral | 90° |

    Symmetry depends only on k, not on ι_τ. -/
```

## Source Excerpt

```lean
structure ModeRepulsionEntry where
  /-- Number of mode pairs. -/
  k : Nat
  /-- Geometry name. -/
  geometry : String
  /-- Characteristic angle (degrees ×10). -/
  angle_deg_x10 : Nat
  deriving Repr
```
