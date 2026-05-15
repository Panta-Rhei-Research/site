---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingAngle",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/crossing-angle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CrossingAngle",
  "declaration_slug": "crossing-angle",
  "kind": "structure",
  "name": "CrossingAngle",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 365,
  "source_line_end": 370,
  "registry_ids": [
    "IV.R115"
  ],
  "related_registry_items": [
    {
      "id": "IV.R115",
      "title": "The 45-degree crossing angle",
      "url": "/registry/object/IV.R115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L365-L370",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/corpus/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L365-L370",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/corpus/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L365-L370)
- Source range: L365-L370
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.R115` — The 45-degree crossing angle

## Immediate Comment / Docstring

```lean
/-- [IV.R115] The Koide phase δ is determined by the lemniscate crossing
    angle: r² = a² cos(2θ) has crossing angle exactly 45° = π/4.
    The phase δ = π/4 − π/12 = π/6 determines m_μ/m_e but not Q,
    which is 2/3 for all δ. -/
```

## Source Excerpt

```lean
structure CrossingAngle where
  /-- Crossing angle in degrees. -/
  angle_degrees : Nat := 45
  /-- Koide phase δ (degrees). -/
  koide_phase_degrees : Nat := 30
  deriving Repr
```
