---
{
  "projection_kind": "taulib_declaration",
  "title": "fiberAngularVelocityDerivation",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/fiber-angular-velocity-derivation/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::fiberAngularVelocityDerivation",
  "declaration_slug": "fiber-angular-velocity-derivation",
  "kind": "def",
  "name": "fiberAngularVelocityDerivation",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 907,
  "source_line_end": 909,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L907-L909",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L907-L909",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L907-L909)
- Source range: L907-L909
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Fiber angular velocity derivation chain:
    V.P56 (capacity gradient) → g_cap = a₀ → circular orbit → ω_fiber = √(a₀/r).

    Derivation:
    1. g_cap = -(c²/2)·∂/∂r ln C_D(r) [V.P56, τ-effective]
    2. C_D(r) ~ exp(-r/ℓ_τ) [screened Poisson asymptotic]
    3. g_cap → c²/(2ℓ_τ) = a₀ [V.T207, τ-effective]
    4. Circular geodesic: g_cap = ω²·r [standard mechanics]
    5. ω_fiber = √(a₀/r) = c/√(2ℓ_τ·r) [algebraic] -/
```

## Source Excerpt

```lean
def fiberAngularVelocityDerivation : String :=
  "V.P56 -> g_cap = a_0 -> circular orbit -> w_fiber = sqrt(a_0/r) = c/sqrt(2*ell*r). " ++
  "No CODATA fitting. Zero free params beyond H_0."
```
