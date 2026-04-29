---
{
  "projection_kind": "taulib_declaration",
  "title": "cabibbo_formula",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/cabibbo-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::cabibbo_formula",
  "declaration_slug": "cabibbo-formula",
  "kind": "def",
  "name": "cabibbo_formula",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 759,
  "source_line_end": 760,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L759-L760",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L759-L760",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L759-L760)
- Source range: L759-L760
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Wolfenstein parameter λ_C = sin(θ_C) is identified with ι_τ·κ_D = ι_τ·(1−ι_τ).
    This is the amplitude for a (1,0)-winding to transition to a (0,1)-winding via ω,
    with survival factor κ_D = 1 − ι_τ.
    Numerical (50-digit mpmath, 2026-03-02): ι_τ·(1−ι_τ) = 0.224816 vs PDG 0.22534
    at −2327 ppm. Best τ-formula among all tested CKM candidates. -/
```

## Source Excerpt

```lean
def cabibbo_formula : String :=
  "sin(θ_C) = ι_τ · (1 - ι_τ) = ι_τ · κ_D = 0.22482 (PDG: 0.22534, -2327 ppm)"
```
