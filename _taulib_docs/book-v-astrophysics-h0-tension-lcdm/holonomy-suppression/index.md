---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomySuppression",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/holonomy-suppression/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::HolonomySuppression",
  "declaration_slug": "holonomy-suppression",
  "kind": "structure",
  "name": "HolonomySuppression",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 372,
  "source_line_end": 379,
  "registry_ids": [
    "V.D296"
  ],
  "related_registry_items": [
    {
      "id": "V.D296",
      "title": "Holonomy Suppression Factor",
      "url": "/registry/object/V.D296/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L372-L379",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L372-L379",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L372-L379)
- Source range: L372-L379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D296` — Holonomy Suppression Factor

## Immediate Comment / Docstring

```lean
/-- [V.D296] Holonomy suppression factor:
    f_supp = 1 − κ_ω · ι_τ = 1 − ι_τ²/(1+ι_τ) ≈ 0.913.
    Suppresses late-time structure growth via boundary holonomy correction. -/
```

## Source Excerpt

```lean
structure HolonomySuppression where
  /-- f_supp (×1000): 0.913 → 913. -/
  f_supp_x1000 : Nat
  /-- κ_ω · ι_τ (×10000): 0.0868 → 868. -/
  kappa_omega_iota_x10000 : Nat
  /-- Suppression: f_supp < 1. -/
  suppression_active : Bool := true
  deriving Repr
```
