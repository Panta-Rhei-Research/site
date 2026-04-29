---
{
  "projection_kind": "taulib_declaration",
  "title": "SolenoidalGenerator",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/solenoidal-generator/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::SolenoidalGenerator",
  "declaration_slug": "solenoidal-generator",
  "kind": "inductive",
  "name": "SolenoidalGenerator",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1656,
  "source_line_end": 1660,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1656-L1660",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1656-L1660",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1656-L1660)
- Source range: L1656-L1660
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Map from H₁(τ³) generators to force-carrying generators.
    g₁ (meridional) ↔ γ (EM), g₂ (longitudinal) ↔ η (strong),
    g₃ (base/crossing) ↔ π (weak).
    Non-winding: α (gravity, non-compact), ω (Higgs, scalar). -/
```

## Source Excerpt

```lean
inductive SolenoidalGenerator where
  | meridional   -- g₁ ↔ γ (EM) → Gen 1
  | longitudinal -- g₂ ↔ η (strong) → Gen 2
  | baseCrossing -- g₃ ↔ π (weak) → Gen 3
  deriving Repr, DecidableEq
```
