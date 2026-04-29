---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonCapacityDeflection",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/photon-capacity-deflection/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::PhotonCapacityDeflection",
  "declaration_slug": "photon-capacity-deflection",
  "kind": "structure",
  "name": "PhotonCapacityDeflection",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 990,
  "source_line_end": 999,
  "registry_ids": [
    "V.T210"
  ],
  "related_registry_items": [
    {
      "id": "V.T210",
      "title": "Photon-Capacity Deflection",
      "url": "/registry/object/V.T210/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L990-L999",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L990-L999",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L990-L999)
- Source range: L990-L999
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T210` — Photon-Capacity Deflection

## Immediate Comment / Docstring

```lean
/-- [V.T210] Photon-Capacity Deflection.
    The τ-Einstein equation is a metric theory: photons follow
    null geodesics of g_∂[χ]. The capacity gradient modifies T,
    hence R^H, hence the metric. Photons are deflected by M_eff
    = M_p + M_∂ = M_p · (1 + κ_τ/ι_τ²).

    mass_ratio_x1000 = 6650 encodes M_eff/M_p = 6.65.
    is_metric_theory = 1 (YES: null geodesics of same metric).
    photon_massive_same = 1 (YES: identical deflection). -/
```

## Source Excerpt

```lean
structure PhotonCapacityDeflection where
  /-- Mass ratio M_eff/M_p × 1000 = 6650. -/
  mass_ratio_x1000 : Nat := 6650
  /-- τ-Einstein is a metric theory (1 = yes). -/
  is_metric_theory : Nat := 1
  /-- Photons deflected identically to massive particles (1 = yes). -/
  photon_massive_same : Nat := 1
  /-- No additional fields needed (1 = yes, cf TeVeS needs 3). -/
  no_additional_fields : Nat := 1
  deriving Repr
```
