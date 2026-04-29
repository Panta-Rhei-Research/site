---
{
  "projection_kind": "taulib_declaration",
  "title": "bareVsDressedAcceleration",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/bare-vs-dressed-acceleration/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::bareVsDressedAcceleration",
  "declaration_slug": "bare-vs-dressed-acceleration",
  "kind": "def",
  "name": "bareVsDressedAcceleration",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 326,
  "source_line_end": 328,
  "registry_ids": [
    "V.D257"
  ],
  "related_registry_items": [
    {
      "id": "V.D257",
      "title": "Bare vs Dressed Acceleration Scales",
      "url": "/registry/object/V.D257/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L326-L328",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L326-L328",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L326-L328)
- Source range: L326-L328
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D257` — Bare vs Dressed Acceleration Scales

## Immediate Comment / Docstring

```lean
/-- [V.D257] Bare vs Dressed Acceleration Scales.

    BARE (V.T85):    a₀^bare = c²/(2·ℓ_τ) = c·H₀·√κ_D/2 ≈ 2.66×10⁻¹⁰ m/s²
    DRESSED (V.D232): a₀^dress = c·H₀·ι_τ/2 ≈ 1.12×10⁻¹⁰ m/s²

    The "dressing factor" ι_τ/√κ_D ≈ 0.421 encodes fiber coherence / base coupling.
    V.T85 is the superior velocity predictor (0.067 dex RMS across 20 galaxies).
    V.D232 is the superior a₀ predictor (+0.9% from MOND with local H₀). -/
```

## Source Excerpt

```lean
def bareVsDressedAcceleration : String :=
  "BARE: a0 = c*H0*sqrt(1-iota)/2 (PDE); DRESSED: a0 = c*H0*iota/2 (MOND). " ++
  "Ratio = sqrt(kD/kB) = 2.378. Same holonomy-baryon ratio as Silk damping."
```
