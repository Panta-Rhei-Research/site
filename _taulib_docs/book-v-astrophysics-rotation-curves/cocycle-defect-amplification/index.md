---
{
  "projection_kind": "taulib_declaration",
  "title": "cocycleDefectAmplification",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/cocycle-defect-amplification/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::cocycleDefectAmplification",
  "declaration_slug": "cocycle-defect-amplification",
  "kind": "def",
  "name": "cocycleDefectAmplification",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 695,
  "source_line_end": 698,
  "registry_ids": [
    "V.D264"
  ],
  "related_registry_items": [
    {
      "id": "V.D264",
      "title": "Cocycle-Defect Amplification Factor",
      "url": "/registry/object/V.D264/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L695-L698",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L695-L698",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L695-L698)
- Source range: L695-L698
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D264` — Cocycle-Defect Amplification Factor

## Immediate Comment / Docstring

```lean
/-- [V.D264] Cocycle-Defect Amplification Factor.

    A_NL = v_T85⁴/v_screen⁴ = c²ℓ_τ/(2GM) = (c/v_screen)²

    For NGC 3198: A_NL ≈ 4.09 × 10¹² — ratio of relativistic to
    non-relativistic energy at the screening scale ℓ_τ.

    This factor is:
    • Far too large for perturbative corrections (weak-field ε ~ 10⁻¹³)
    • Not achievable by NF iteration convergence (refines, doesn't amplify)
    • Bridged only by the algebraic identity a₀ = c²/(2ℓ_τ) (V.T207)

    Honest assessment: no known mechanism within cocycle-defect
    minimization can generate amplification of this magnitude.
    Resolution is algebraic (V.T207), not perturbative. -/
```

## Source Excerpt

```lean
def cocycleDefectAmplification : String :=
  "A_NL = c^2*ell/(2GM) ~ 4e12 for NGC 3198. " ++
  "Too large for perturbation theory (eps ~ 1e-13). " ++
  "Resolution: algebraic identity a_0 = c^2/(2*ell), not PDE amplification."
```
