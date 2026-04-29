---
{
  "projection_kind": "taulib_declaration",
  "title": "a0_h0_tension",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/a0-h0-tension/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::a0_h0_tension",
  "declaration_slug": "a0-h0-tension",
  "kind": "def",
  "name": "a0_h0_tension",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 240,
  "source_line_end": 242,
  "registry_ids": [
    "V.P122"
  ],
  "related_registry_items": [
    {
      "id": "V.P122",
      "title": "a_0 from H_0 Tension",
      "url": "/registry/object/V.P122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L240-L242",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L240-L242",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L240-L242)
- Source range: L240-L242
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P122` — a_0 from H_0 Tension

## Immediate Comment / Docstring

```lean
/-- [V.P122] The H₀ tension propagates structurally into a₀ = c·H₀·ι_τ/2.

    Rotation curve galaxies (z < 0.05) probe local H₀ = 73.0 km/s/Mpc:
      a₀(local) = 1.211×10⁻¹⁰ m/s²   (+0.9% from MOND)
    CMB measurement gives H₀ = 67.4 km/s/Mpc:
      a₀(CMB)   = 1.118×10⁻¹⁰ m/s²   (-6.9% from MOND)

    Falsifiable prediction: as H₀ tension resolves, BTFR normalization A
    = 2ℓ_τ/(G·c²) must shift by the same fraction as H₀ changes. -/
```

## Source Excerpt

```lean
def a0_h0_tension : String :=
  "H_0 tension: local H_0=73.0 gives a_0 at +0.9% from MOND, " ++
  "CMB H_0=67.4 gives -6.9%. Galaxies probe local H_0."
```
