---
{
  "projection_kind": "taulib_declaration",
  "title": "CabibboFormula",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/cabibbo-formula-l763/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CabibboFormula",
  "declaration_slug": "cabibbo-formula-l763",
  "kind": "structure",
  "name": "CabibboFormula",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 763,
  "source_line_end": 770,
  "registry_ids": [
    "IV.D349"
  ],
  "related_registry_items": [
    {
      "id": "IV.D349",
      "title": "Cabibbo Angle from T² Holonomy: λ_C = ι_τ·κ_D",
      "url": "/registry/object/IV.D349/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L763-L770",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L763-L770",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L763-L770)
- Source range: L763-L770
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D349` — Cabibbo Angle from T² Holonomy: λ_C = ι_τ·κ_D

## Immediate Comment / Docstring

```lean
/-- [IV.D349] Cabibbo angle formula structure (formalized). -/
```

## Source Excerpt

```lean
structure CabibboFormula where
  /-- Number of factors in holonomy product: ι_τ × κ_D. -/
  n_holonomy_factors : Nat := 2
  /-- Fiber dimension (T² holonomy). -/
  fiber_dim : Nat := 2
  /-- Deviation from PDG ×10 (ppm). -/
  deviation_ppm_x10 : Nat := 23270
  deriving Repr
```
