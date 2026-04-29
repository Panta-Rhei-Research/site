---
{
  "projection_kind": "taulib_declaration",
  "title": "DEClosureMatterDensity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/declosure-matter-density/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DEClosureMatterDensity",
  "declaration_slug": "declosure-matter-density",
  "kind": "structure",
  "name": "DEClosureMatterDensity",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 936,
  "source_line_end": 947,
  "registry_ids": [
    "V.T199"
  ],
  "related_registry_items": [
    {
      "id": "V.T199",
      "title": "DE-Closure Matter Density at -675 ppm",
      "url": "/registry/object/V.T199/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L936-L947",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L936-L947",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L936-L947)
- Source range: L936-L947
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T199` — DE-Closure Matter Density at -675 ppm

## Immediate Comment / Docstring

```lean
/-- [V.T199] DE-Closure Matter Density at −675 ppm.
    ω_m = (1 − Ω_Λ − Ω_r) × h² where
    Ω_Λ = κ_D·(1+ι_τ³) = 0.6849, h = 2/3+ι_τ²/17 = 0.6735.
    Result: ω_m = 0.1429 at −675 ppm from Planck 0.1430.
    This is 41× better than M3h holonomy path (+27972 ppm). -/
```

## Source Excerpt

```lean
structure DEClosureMatterDensity where
  /-- ω_m ×10000 (0.1429 → 1429). -/
  omega_m_x10000 : Nat := 1429
  /-- Deviation from Planck in ppm (−675 → 675, sign encoded separately). -/
  deviation_ppm : Nat := 675
  /-- Sign: 0 = negative deviation. -/
  deviation_sign : Nat := 0
  /-- Improvement factor over M3h (41×). -/
  improvement_factor : Nat := 41
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
