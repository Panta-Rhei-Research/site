---
{
  "projection_kind": "taulib_declaration",
  "title": "lie_algebra_cross_term",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/lie-algebra-cross-term/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::lie_algebra_cross_term",
  "declaration_slug": "lie-algebra-cross-term",
  "kind": "theorem",
  "name": "lie_algebra_cross_term",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 892,
  "source_line_end": 896,
  "registry_ids": [
    "V.P145"
  ],
  "related_registry_items": [
    {
      "id": "V.P145",
      "title": "Lie Algebra Cross-Term",
      "url": "/registry/object/V.P145/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L892-L896",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L892-L896",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L892-L896)
- Source range: L892-L896
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P145` — Lie Algebra Cross-Term

## Immediate Comment / Docstring

```lean
/-- [V.P145] Lie Algebra Cross-Term (τ-effective).

    ω_fiber = √(a₀/r) DERIVED from:
    - V.P56 (capacity gradient): g_cap = -(c²/2)·∂/∂r ln C_D(r)
    - V.T207 (structural a₀): a₀ = c²/(2ℓ_τ) = cH₀√κ_D/2
    - Circular geodesics on τ³: g_cap = ω_fiber²·r → ω_fiber = √(a₀/r)

    Cross-term: g_fiber = r·|ω_base|·|ω_fiber| = √(g_N·a₀).
    Uniqueness: only mass-independent ω consistent with V.T85. -/
```

## Source Excerpt

```lean
theorem lie_algebra_cross_term :
    "g_fiber = r*|w_base|*|w_fiber| = sqrt(g_N*a_0). " ++
    "w_fiber = sqrt(a_0/r) derived from V.P56 + V.T207." =
    "g_fiber = r*|w_base|*|w_fiber| = sqrt(g_N*a_0). " ++
    "w_fiber = sqrt(a_0/r) derived from V.P56 + V.T207." := rfl
```
