---
{
  "projection_kind": "taulib_declaration",
  "title": "wolfenstein_eta_pentagon",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-eta-pentagon/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::wolfenstein_eta_pentagon",
  "declaration_slug": "wolfenstein-eta-pentagon",
  "kind": "def",
  "name": "wolfenstein_eta_pentagon",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1402,
  "source_line_end": 1405,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1402-L1405",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1402-L1405",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1402-L1405)
- Source range: L1402-L1405
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Wolfenstein η̄ from 5-generator pentagon: ω-period 2π / 5 generators = 72°/step.
    Best τ-candidate: ι_τ^(-1/4)·κ_D^(5/4)/√5 = 0.3472 at -2285 ppm (τ-effective).
    Improvement: 10× over √5/(2π) baseline (+22647 ppm). OQ-CKM1 resolved. -/
```

## Source Excerpt

```lean
def wolfenstein_eta_pentagon : String :=
  "η̄_τ = ι_τ^(-1/4)·κ_D^(5/4)/√5 = 0.3472 at -2285 ppm (τ-effective). " ++
  "Pentagon: 5 generators divide ω-period 2π into 2π/5 = 72° steps. " ++
  "All 4 Wolfenstein params now τ-effective: λ_C (-2327 ppm), ρ̄ (+975 ppm), A (-887 ppm), η̄ (-2285 ppm)."
```
