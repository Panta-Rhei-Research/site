---
{
  "projection_kind": "taulib_declaration",
  "title": "TauTransferFunction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/tau-transfer-function/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::TauTransferFunction",
  "declaration_slug": "tau-transfer-function",
  "kind": "structure",
  "name": "TauTransferFunction",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 329,
  "source_line_end": 338,
  "registry_ids": [
    "V.D300"
  ],
  "related_registry_items": [
    {
      "id": "V.D300",
      "title": "τ-Native Transfer Function",
      "url": "/registry/object/V.D300/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L329-L338",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L329-L338",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L329-L338)
- Source range: L329-L338
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D300` — τ-Native Transfer Function

## Immediate Comment / Docstring

```lean
/-- [V.D300] τ-native transfer function:
    T(k) from k_eq, R_b, k_D — all τ-native.
    k_eq ≈ 0.010 h/Mpc (horizon at matter-radiation equality).
    R_b ≈ 0.615 (baryon-to-photon ratio at recombination).
    k_D ≈ 0.10 Mpc⁻¹ (Silk damping scale from ℓ_D ≈ 1244). -/
```

## Source Excerpt

```lean
structure TauTransferFunction where
  /-- k_eq (×1000 h/Mpc): 0.010 → 10. -/
  k_eq_x1000 : Nat
  /-- R_b (×1000): 0.615 → 615. -/
  r_b_x1000 : Nat
  /-- k_D (×1000 Mpc⁻¹): 0.10 → 100. -/
  k_D_x1000 : Nat
  /-- n_s (×100000): 0.96491 → 96491. -/
  n_s_x100000 : Nat
  deriving Repr
```
