---
{
  "projection_kind": "taulib_declaration",
  "title": "S8TensionResolution",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-tension-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::S8TensionResolution",
  "declaration_slug": "s8-tension-resolution",
  "kind": "structure",
  "name": "S8TensionResolution",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 589,
  "source_line_end": 612,
  "registry_ids": [
    "V.D324"
  ],
  "related_registry_items": [
    {
      "id": "V.D324",
      "title": "S₈ NLO",
      "url": "/registry/object/V.D324/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L589-L612",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L589-L612",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L589-L612)
- Source range: L589-L612
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D324` — S₈ NLO

## Immediate Comment / Docstring

```lean
/-- [V.D324] S₈ NLO with full pipeline.
    σ₈(τ,NLO) = 0.811 × f_supp × f_growth × f_ν = 0.747.
    S₈(τ,NLO) = 0.747 × √(0.330/0.3) = 0.783.
    Scope: τ-effective (Wave 39C). -/
```

## Source Excerpt

```lean
structure S8TensionResolution where
  /-- σ₈(CMB, Planck) × 1000. -/
  sigma8_cmb_x1000 : Nat := 811
  /-- f_supp × 10000. -/
  f_supp_x10000 : Nat := 9132
  /-- f_growth × 10000. -/
  f_growth_x10000 : Nat := 10114
  /-- f_ν × 100000. -/
  f_nu_x100000 : Nat := 99681
  /-- σ₈(τ,NLO) × 10000. -/
  sigma8_nlo_x10000 : Nat := 7466
  /-- S₈(τ,NLO) × 10000. -/
  s8_nlo_x10000 : Nat := 7829
  /-- Ω_m(NLO) × 10000. -/
  omega_m_nlo_x10000 : Nat := 3299
  /-- S₈(Planck CMB) × 1000. -/
  s8_planck_x1000 : Nat := 832
  /-- S₈(DES+KiDS) × 1000. -/
  s8_deskids_x1000 : Nat := 790
  /-- S₈(DES Y3) × 1000. -/
  s8_desy3_x1000 : Nat := 776
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
