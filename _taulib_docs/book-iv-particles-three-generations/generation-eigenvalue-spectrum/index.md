---
{
  "projection_kind": "taulib_declaration",
  "title": "GenerationEigenvalueSpectrum",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/generation-eigenvalue-spectrum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::GenerationEigenvalueSpectrum",
  "declaration_slug": "generation-eigenvalue-spectrum",
  "kind": "structure",
  "name": "GenerationEigenvalueSpectrum",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2608,
  "source_line_end": 2619,
  "registry_ids": [
    "IV.D379"
  ],
  "related_registry_items": [
    {
      "id": "IV.D379",
      "title": "Generation Eigenvalue Spectrum on Anisotropic T²",
      "url": "/registry/object/IV.D379/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2608-L2619",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/corpus/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2608-L2619",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/corpus/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2608-L2619)
- Source range: L2608-L2619
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D379` — Generation Eigenvalue Spectrum on Anisotropic T²

## Immediate Comment / Docstring

```lean
/-- [IV.D379] Generation eigenvalue spectrum on anisotropic T².
    λ_{(n,m)} = n² + m²·ι_τ⁻². Three primitive winding classes
    give eigenvalues 1, ι_τ⁻² ≈ 8.585, 1+ι_τ⁻² ≈ 9.585. -/
```

## Source Excerpt

```lean
structure GenerationEigenvalueSpectrum where
  /-- λ(1,0) = 1 (×1000). -/
  lam_10_x1000 : Nat := 1000
  /-- λ(0,1) = ι_τ⁻² (×1000). -/
  lam_01_x1000 : Nat := 8585
  /-- λ(1,1) = 1 + ι_τ⁻² (×1000). -/
  lam_11_x1000 : Nat := 9585
  /-- λ(1,1) = λ(1,0) + λ(0,1). -/
  lam_11_sum : lam_11_x1000 = lam_10_x1000 + lam_01_x1000
  /-- Number of primitive winding classes = generations. -/
  n_generations : Nat := 3
  deriving Repr
```
