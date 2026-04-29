---
{
  "projection_kind": "taulib_declaration",
  "title": "QLCRelation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/qlcrelation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QLCRelation",
  "declaration_slug": "qlcrelation",
  "kind": "structure",
  "name": "QLCRelation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 864,
  "source_line_end": 871,
  "registry_ids": [
    "IV.P189"
  ],
  "related_registry_items": [
    {
      "id": "IV.P189",
      "title": "Quark-Lepton Complementarity: θ₁₂+θ_C ≈ π/4 from Fiber-Base Duality",
      "url": "/registry/object/IV.P189/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L864-L871",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L864-L871",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L864-L871)
- Source range: L864-L871
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P189` — Quark-Lepton Complementarity: θ₁₂+θ_C ≈ π/4 from Fiber-Base Duality

## Immediate Comment / Docstring

```lean
/-- [IV.P189] Quark-lepton complementarity structure. -/
```

## Source Excerpt

```lean
structure QLCRelation where
  /-- Target sum: 45° = π/4. -/
  target_degrees : Nat := 45
  /-- Deviation from target in percent (×10): 3% → 30. -/
  deviation_pct_x10 : Nat := 30
  /-- Number of A-sector rotations required for full PMNS. -/
  n_a_sector_rotations : Nat := 1
  deriving Repr
```
