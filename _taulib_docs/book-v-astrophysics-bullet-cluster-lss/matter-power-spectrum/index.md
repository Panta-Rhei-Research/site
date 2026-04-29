---
{
  "projection_kind": "taulib_declaration",
  "title": "MatterPowerSpectrum",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/matter-power-spectrum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::MatterPowerSpectrum",
  "declaration_slug": "matter-power-spectrum",
  "kind": "structure",
  "name": "MatterPowerSpectrum",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 343,
  "source_line_end": 354,
  "registry_ids": [
    "V.T240"
  ],
  "related_registry_items": [
    {
      "id": "V.T240",
      "title": "Power Spectrum Consistency",
      "url": "/registry/object/V.T240/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L343-L354",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BulletClusterLSS",
        "url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L343-L354",
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

- Module: [TauLib.BookV.Astrophysics.BulletClusterLSS](/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/)
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L343-L354)
- Source range: L343-L354
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T240` — Power Spectrum Consistency

## Immediate Comment / Docstring

```lean
/-- [V.T240] Power spectrum consistency:
    P(k) = A_s · (k/k₀)^(n_s−1) · T²(k) reproduces BOSS DR12.
    Turnover, BAO wiggles, Silk damping tail, σ₈ all match. -/
```

## Source Excerpt

```lean
structure MatterPowerSpectrum where
  /-- r_s sound horizon (×10 Mpc): 147.5 → 1475. -/
  r_s_x10 : Nat
  /-- BOSS r_s observed (×10 Mpc): 147.21 → 1472. -/
  boss_r_s_x10 : Nat := 1472
  /-- r_s deviation (ppm): +2000. -/
  r_s_deviation_ppm : Int
  /-- k_BAO (×1000 h/Mpc): 0.043 → 43. -/
  k_bao_x1000 : Nat
  /-- σ₈ from P(k) normalisation (×1000): 0.741 → 741. -/
  sigma8_x1000 : Nat
  deriving Repr
```
