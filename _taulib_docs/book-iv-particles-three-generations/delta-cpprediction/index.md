---
{
  "projection_kind": "taulib_declaration",
  "title": "DeltaCPPrediction",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/delta-cpprediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::DeltaCPPrediction",
  "declaration_slug": "delta-cpprediction",
  "kind": "structure",
  "name": "DeltaCPPrediction",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1930,
  "source_line_end": 1939,
  "registry_ids": [
    "IV.P204"
  ],
  "related_registry_items": [
    {
      "id": "IV.P204",
      "title": "δ_CP = π + arctan(ι_τ) at +9365 ppm",
      "url": "/registry/object/IV.P204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1930-L1939",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1930-L1939",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1930-L1939)
- Source range: L1930-L1939
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P204` — δ_CP = π + arctan(ι_τ) at +9365 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.P204] δ_CP prediction structure. -/
```

## Source Excerpt

```lean
structure DeltaCPPrediction where
  /-- Base angle: π in radians (half-period on L), degrees = 180. -/
  base_degrees : Nat := 180
  /-- Predicted angle (degrees × 100): π + arctan(ι_τ) ≈ 198.84°. -/
  predicted_deg_x100 : Nat := 19884
  /-- PDG value (degrees × 100): ≈ 197°. -/
  pdg_deg_x100 : Nat := 19700
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 9365
  deriving Repr
```
