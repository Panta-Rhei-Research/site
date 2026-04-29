---
{
  "projection_kind": "taulib_declaration",
  "title": "Sigma8TauNative",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-tau-native/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::Sigma8TauNative",
  "declaration_slug": "sigma8-tau-native",
  "kind": "structure",
  "name": "Sigma8TauNative",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 384,
  "source_line_end": 397,
  "registry_ids": [
    "V.D297"
  ],
  "related_registry_items": [
    {
      "id": "V.D297",
      "title": "σ₈ τ-Native",
      "url": "/registry/object/V.D297/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L384-L397",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L384-L397",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L384-L397)
- Source range: L384-L397
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D297` — σ₈ τ-Native

## Immediate Comment / Docstring

```lean
/-- [V.D297] σ₈ τ-native:
    σ₈^(τ) = σ₈^(CMB) · f_supp = 0.811 × 0.913 = 0.741.
    S₈^(τ) = σ₈^(τ) · √(Ω_m/0.3) = 0.760. -/
```

## Source Excerpt

```lean
structure Sigma8TauNative where
  /-- σ₈^(CMB) (×1000): 0.811 → 811. -/
  sigma8_cmb_x1000 : Nat := 811
  /-- σ₈^(τ) (×1000): 0.741 → 741. -/
  sigma8_tau_x1000 : Nat
  /-- S₈^(τ) (×1000): 0.760 → 760. -/
  s8_tau_x1000 : Nat
  /-- S₈^(Planck CMB) (×1000): 0.832 → 832. -/
  s8_planck_x1000 : Nat := 832
  /-- S₈^(WL average) (×1000): ~0.770 → 770. -/
  s8_wl_x1000 : Nat := 770
  /-- τ aligns with WL side. -/
  aligns_with_wl : Bool := true
  deriving Repr
```
