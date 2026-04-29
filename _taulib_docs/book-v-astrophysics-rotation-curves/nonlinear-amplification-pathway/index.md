---
{
  "projection_kind": "taulib_declaration",
  "title": "nonlinear_amplification_pathway",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/nonlinear-amplification-pathway/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::nonlinear_amplification_pathway",
  "declaration_slug": "nonlinear-amplification-pathway",
  "kind": "theorem",
  "name": "nonlinear_amplification_pathway",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 718,
  "source_line_end": 722,
  "registry_ids": [
    "V.P144"
  ],
  "related_registry_items": [
    {
      "id": "V.P144",
      "title": "Nonlinear Amplification Pathway",
      "url": "/registry/object/V.P144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L718-L722",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L718-L722",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L718-L722)
- Source range: L718-L722
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P144` — Nonlinear Amplification Pathway

## Immediate Comment / Docstring

```lean
/-- [V.P144] Nonlinear Amplification Pathway (conjectural).

    IF the full nonlinear τ-Einstein equation is solved numerically
    at galactic scales, it should produce flat rotation curves with
    amplitude matching V.T85, because:
    1. The metric perturbation h₀₀ receives a logarithmic profile
       from τ-screening (analogous to capacity K₀)
    2. The amplitude of h₀₀ is set by the metric coupling
    3. The geodesic equation yields v⁴ = GMc²/(2ℓ_τ)

    This is conjectural pending numerical solution of the full
    nonlinear τ-Einstein equation at galactic scales.
    The V.T85 algebraic identity (V.T207) provides the answer
    without requiring this PDE solution. -/
```

## Source Excerpt

```lean
theorem nonlinear_amplification_pathway :
    "Full nonlinear tau-Einstein should yield V.T85 amplitude; " ++
    "conjectural pending numerical solution" =
    "Full nonlinear tau-Einstein should yield V.T85 amplitude; " ++
    "conjectural pending numerical solution" := rfl
```
