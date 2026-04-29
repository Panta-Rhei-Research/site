---
{
  "projection_kind": "taulib_declaration",
  "title": "gen_mass_hierarchy_eigenvalue",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/gen-mass-hierarchy-eigenvalue/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::gen_mass_hierarchy_eigenvalue",
  "declaration_slug": "gen-mass-hierarchy-eigenvalue",
  "kind": "def",
  "name": "gen_mass_hierarchy_eigenvalue",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1745,
  "source_line_end": 1748,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1745-L1748",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1745-L1748",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1745-L1748)
- Source range: L1745-L1748
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Mass hierarchy from T² Laplacian eigenvalues:
    λ₁ = 1 (gen 1) < λ₂ = ι_τ⁻² ≈ 8.6 (gen 2) < λ₃ = 1+ι_τ⁻² ≈ 9.6 (gen 3).
    Leading exponents: gen 2 → 5 = N_generators, gen 3 → 15/2 = N_gen·dim/lobes. -/
```

## Source Excerpt

```lean
def gen_mass_hierarchy_eigenvalue : String :=
  "λ₁=1 < λ₂=ι_τ⁻²≈8.6 < λ₃=1+ι_τ⁻²≈9.6. " ++
  "Gen 2 exponent = 5 = N_generators; Gen 3 exponent = 15/2 = N_gen·dim(τ³)/N_lobes. " ++
  "NNLO: m_μ/m_e at +43 ppm (k=23/3), m_τ/m_e at +61 ppm (Koide)."
```
