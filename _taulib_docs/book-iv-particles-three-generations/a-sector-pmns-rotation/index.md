---
{
  "projection_kind": "taulib_declaration",
  "title": "a_sector_pmns_rotation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/a-sector-pmns-rotation/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::a_sector_pmns_rotation",
  "declaration_slug": "a-sector-pmns-rotation",
  "kind": "def",
  "name": "a_sector_pmns_rotation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1083,
  "source_line_end": 1085,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1083-L1085",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1083-L1085",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1083-L1085)
- Source range: L1083-L1085
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A-sector PMNS rotation: sin(θ_A) = 1/(1+ι_τ) ≈ 0.7455 → θ_A ≈ 48.2°.
    Applied to atmospheric mixing: θ₂₃ ≈ 48.2° (PDG 49.1°, -18213 ppm).
    The denominator (1+ι_τ) is the π-sector crossing amplitude on τ¹. -/
```

## Source Excerpt

```lean
def a_sector_pmns_rotation : String :=
  "A-sector: sin(θ₂₃)=1/(1+ι_τ)=0.7455 → 48.2° (PDG 49.1°, -18213 ppm). " ++
  "QLC: θ₁₂=π/4-θ_C → 31.9° (PDG 33.4°, -41965 ppm). Both conjectural."
```
