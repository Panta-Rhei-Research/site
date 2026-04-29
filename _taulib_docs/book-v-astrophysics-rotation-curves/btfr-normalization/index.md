---
{
  "projection_kind": "taulib_declaration",
  "title": "btfr_normalization",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/btfr-normalization/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::btfr_normalization",
  "declaration_slug": "btfr-normalization",
  "kind": "def",
  "name": "btfr_normalization",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 256,
  "source_line_end": 258,
  "registry_ids": [
    "V.T163"
  ],
  "related_registry_items": [
    {
      "id": "V.T163",
      "title": "Baryonic Tully-Fisher Relation from V.T85",
      "url": "/registry/object/V.T163/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L256-L258",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L256-L258",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L256-L258)
- Source range: L256-L258
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T163` — Baryonic Tully-Fisher Relation from V.T85

## Immediate Comment / Docstring

```lean
/-- [V.T163] Baryonic Tully-Fisher Relation normalization from V.T85.
    M_b = A · v_∞⁴ where A = 2·ℓ_τ/(G·c²) from the Flat Rotation Curve Theorem.

    A is determined entirely by ι_τ and H₀:
      A = 2/(G·H₀·c·√(1−ι_τ))

    Lab values:
    - H₀ = 67.4: A ≈ 28.4 M_☉/(km/s)⁴  (V.T85 raw)
    - H₀ = 73.0: A ≈ 26.2 M_☉/(km/s)⁴  (V.T85 raw)
    - Observed BTFR: A_obs ≈ 47 M_☉/(km/s)⁴

    The factor √ι_τ ≈ 0.584 between A_T85 and A_obs is an open question. -/
```

## Source Excerpt

```lean
def btfr_normalization : String :=
  "M_b = A * v_inf^4, A = 2*ell_tau/(G*c^2) = 2/(G*H_0*c*sqrt(1-iota_tau)). " ++
  "No free parameter. Lab: A=28.4 (Planck), obs A_obs=47. Open: sqrt(iota) factor."
```
