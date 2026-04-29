---
{
  "projection_kind": "taulib_declaration",
  "title": "koide_from_sigma",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/koide-from-sigma/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::koide_from_sigma",
  "declaration_slug": "koide-from-sigma",
  "kind": "def",
  "name": "koide_from_sigma",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 543,
  "source_line_end": 546,
  "registry_ids": [
    "IV.T143"
  ],
  "related_registry_items": [
    {
      "id": "IV.T143",
      "title": "Koide Q=2/3 from sigma-Symmetry",
      "url": "/registry/object/IV.T143/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L543-L546",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L543-L546",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L543-L546)
- Source range: L543-L546
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T143` — Koide Q=2/3 from sigma-Symmetry

## Immediate Comment / Docstring

```lean
/-- [IV.T143] Koide Q = 2/3 is a structural consequence of sigma-equivariance.
    Any sigma-equivariant 3×3 matrix M_ℓ = [[a,b,0],[b,c,b],[0,b,a]] satisfies
    Q = (λ₁+λ₂+λ₃)/(√λ₁+√λ₂+√λ₃)² = 2/3 exactly.

    Proof: The sigma-odd eigenvector [1,0,-1] gives λ₁ = a exactly. The remaining
    two eigenvectors [1,x,1] satisfy the 2×2 reduced system, placing the full
    spectrum on the democratic equilateral Koide surface. Q = 2/3 is an algebraic
    identity independent of (a,b,c). -/
```

## Source Excerpt

```lean
def koide_from_sigma : String :=
  "Koide Q=2/3 follows from sigma-equivariance: sigma-odd eigenvector [1,0,-1] " ++
  "gives lambda_1=a; remaining eigenpairs lie on democratic equilateral surface. " ++
  "Q=2/3 is exact for all (a,b,c). Observed Q = 2/3 - 9.24 ppm is O(alpha^2)."
```
