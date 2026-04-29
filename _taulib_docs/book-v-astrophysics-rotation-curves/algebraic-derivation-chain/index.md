---
{
  "projection_kind": "taulib_declaration",
  "title": "algebraicDerivationChain",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/algebraic-derivation-chain/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::algebraicDerivationChain",
  "declaration_slug": "algebraic-derivation-chain",
  "kind": "def",
  "name": "algebraicDerivationChain",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 766,
  "source_line_end": 768,
  "registry_ids": [
    "V.D265"
  ],
  "related_registry_items": [
    {
      "id": "V.D265",
      "title": "Algebraic Derivation Chain for a₀",
      "url": "/registry/object/V.D265/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L766-L768",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L766-L768",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L766-L768)
- Source range: L766-L768
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D265` — Algebraic Derivation Chain for a₀

## Immediate Comment / Docstring

```lean
/-- [V.D265] Algebraic Derivation Chain for a₀.

    τ-axioms K0–K6
      → ι_τ = 2/(π+e) ≈ 0.3413
      → κ_D = 1 − ι_τ ≈ 0.6587
      → ℓ_τ = c/(H₀√κ_D) ≈ 5480 Mpc
      → a₀ = c²/(2ℓ_τ) = cH₀√κ_D/2 ≈ 2.66×10⁻¹⁰ m/s²

    This chain has:
    • Zero free parameters (beyond H₀)
    • One cosmological input (H₀)
    • One structural constant (ι_τ from axioms K0–K6) -/
```

## Source Excerpt

```lean
def algebraicDerivationChain : String :=
  "tau-axioms -> iota=2/(pi+e) -> kD=1-iota -> ell=c/(H0*sqrt(kD)) " ++
  "-> a_0=c^2/(2*ell). Zero free params + H_0."
```
