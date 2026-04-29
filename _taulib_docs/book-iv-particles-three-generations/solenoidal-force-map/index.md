---
{
  "projection_kind": "taulib_declaration",
  "title": "SolenoidalForceMap",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/solenoidal-force-map/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::SolenoidalForceMap",
  "declaration_slug": "solenoidal-force-map",
  "kind": "structure",
  "name": "SolenoidalForceMap",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1679,
  "source_line_end": 1686,
  "registry_ids": [
    "IV.D362"
  ],
  "related_registry_items": [
    {
      "id": "IV.D362",
      "title": "Solenoidal Generator–Force Map",
      "url": "/registry/object/IV.D362/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1679-L1686",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1679-L1686",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1679-L1686)
- Source range: L1679-L1686
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D362` — Solenoidal Generator–Force Map

## Immediate Comment / Docstring

```lean
/-- [IV.D362] Solenoidal force map structure (formalized). -/
```

## Source Excerpt

```lean
structure SolenoidalForceMap where
  /-- Number of compact (winding) generators. -/
  n_compact : Nat := 3
  /-- Number of non-compact generators. -/
  n_non_compact : Nat := 2
  /-- Total generators. -/
  total_generators : Nat := 5
  deriving Repr
```
