---
{
  "projection_kind": "taulib_declaration",
  "title": "CoupledNLOScan",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/coupled-nloscan/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::CoupledNLOScan",
  "declaration_slug": "coupled-nloscan",
  "kind": "structure",
  "name": "CoupledNLOScan",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1434,
  "source_line_end": 1449,
  "registry_ids": [
    "V.D317"
  ],
  "related_registry_items": [
    {
      "id": "V.D317",
      "title": "Coupled NLO Correction Space",
      "url": "/registry/object/V.D317/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1434-L1449",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1434-L1449",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1434-L1449)
- Source range: L1434-L1449
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D317` — Coupled NLO Correction Space

## Immediate Comment / Docstring

```lean
/-- [V.D317] Coupled NLO Correction Space.
    δ_h = ι_τ/W₅(3) = ι_τ/19.
    Holonomy ratio: 6.655 → 6.774. ω_m: 0.14700 → 0.14964.
    Scope: τ-effective (Wave 38A). -/
```

## Source Excerpt

```lean
structure CoupledNLOScan where
  /-- NLO δ_h × 100000. -/
  delta_h_x100000 : Nat := 1796
  /-- W₅(3) = 19 (CF window sum governing N_e). -/
  w5_3 : Nat := 19
  /-- Holonomy ratio LO × 1000. -/
  ratio_lo_x1000 : Nat := 6655
  /-- Holonomy ratio NLO × 1000. -/
  ratio_nlo_x1000 : Nat := 6774
  /-- ω_m NLO × 10000. -/
  omega_m_nlo_x10000 : Nat := 1496
  /-- ω_m LO × 10000. -/
  omega_m_lo_x10000 : Nat := 1470
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
