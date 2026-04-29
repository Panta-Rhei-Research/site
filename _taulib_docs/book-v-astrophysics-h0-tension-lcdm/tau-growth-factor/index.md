---
{
  "projection_kind": "taulib_declaration",
  "title": "TauGrowthFactor",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-growth-factor/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::TauGrowthFactor",
  "declaration_slug": "tau-growth-factor",
  "kind": "structure",
  "name": "TauGrowthFactor",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 431,
  "source_line_end": 444,
  "registry_ids": [
    "V.D298"
  ],
  "related_registry_items": [
    {
      "id": "V.D298",
      "title": "τ-Native Growth Factor",
      "url": "/registry/object/V.D298/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L431-L444",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L431-L444",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L431-L444)
- Source range: L431-L444
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D298` — τ-Native Growth Factor

## Immediate Comment / Docstring

```lean
/-- [V.D298] τ-native growth factor:
    D″ + 2H·D′ − (3/2)Ω_m(z)·H²·f_supp·D = 0.
    Modified by w(z) ≠ −1 and holonomy suppression f_supp < 1. -/
```

## Source Excerpt

```lean
structure TauGrowthFactor where
  /-- Redshift (×10). -/
  z_x10 : Nat
  /-- Ω_m(z) (×100). -/
  omega_m_z_x100 : Nat
  /-- Growth rate f(z) = Ω_m(z)^γ (×100). -/
  f_z_x100 : Nat
  /-- σ₈(z) = σ₈(0)·D(z) (×1000). -/
  sigma8_z_x1000 : Nat
  /-- f·σ₈(z) τ-prediction (×1000). -/
  fsigma8_tau_x1000 : Nat
  /-- f·σ₈(z) ΛCDM prediction (×1000). -/
  fsigma8_lcdm_x1000 : Nat
  deriving Repr
```
