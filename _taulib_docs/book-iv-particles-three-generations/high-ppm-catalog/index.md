---
{
  "projection_kind": "taulib_declaration",
  "title": "HighPpmCatalog",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/high-ppm-catalog/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::HighPpmCatalog",
  "declaration_slug": "high-ppm-catalog",
  "kind": "structure",
  "name": "HighPpmCatalog",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 3089,
  "source_line_end": 3098,
  "registry_ids": [
    "IV.D386"
  ],
  "related_registry_items": [
    {
      "id": "IV.D386",
      "title": "High-ppm Structural Limit Catalog",
      "url": "/registry/object/IV.D386/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3089-L3098",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3089-L3098",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3089-L3098)
- Source range: L3089-L3098
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D386` — High-ppm Structural Limit Catalog

## Immediate Comment / Docstring

```lean
/-- [IV.D386] High-ppm structural limit catalog (Wave 49).
    After NNLO corrections:
    - θ₂₃: +8604 → −494 (NNLO, sub-1000)
    - δ_CP: +9365 → +5645 (NLO, 40% improved)
    - m_μ/m_e: +6156 → −8.2 (already done Wave 6D)
    Structural limits (no NLO solution):
    - QLC θ₁₂: −41965 ppm (needs exact θ_C coupling)
    - η̄ pentagon: +75275 ppm (complex geometry) -/
```

## Source Excerpt

```lean
structure HighPpmCatalog where
  /-- Items improved this wave. -/
  improved : Nat := 2
  /-- Items at structural limit. -/
  structural_limits : Nat := 2
  /-- Items already resolved (prior waves). -/
  already_done : Nat := 1
  /-- Best NNLO result (θ₂₃ ppm, absolute). -/
  best_nnlo_ppm : Nat := 494
  deriving Repr
```
