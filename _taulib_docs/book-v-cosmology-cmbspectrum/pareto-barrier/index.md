---
{
  "projection_kind": "taulib_declaration",
  "title": "ParetoBarrier",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/pareto-barrier/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ParetoBarrier",
  "declaration_slug": "pareto-barrier",
  "kind": "structure",
  "name": "ParetoBarrier",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1896,
  "source_line_end": 1913,
  "registry_ids": [
    "V.D329"
  ],
  "related_registry_items": [
    {
      "id": "V.D329",
      "title": "ω_m–Peaks Pareto Barrier",
      "url": "/registry/object/V.D329/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1896-L1913",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1896-L1913",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1896-L1913)
- Source range: L1896-L1913
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D329` — ω_m–Peaks Pareto Barrier

## Immediate Comment / Docstring

```lean
/-- [V.D329] Pareto Barrier: ω_m–peaks structural tension.
    The density regime (ω_m ≈ Planck) and peaks regime (ℓ₁ ≈ Planck)
    are complementary aspects of a 1D Pareto frontier.
    Scope: τ-effective (Wave 41B). -/
```

## Source Excerpt

```lean
structure ParetoBarrier where
  /-- Density regime ℓ₁ ppm (far from Planck). -/
  density_ell1_ppm : Nat := 7337
  /-- Density regime ω_m ppm (near Planck). -/
  density_omega_m_ppm : Nat := 17
  /-- Density regime r_d ppm. -/
  density_rd_ppm : Nat := 1269
  /-- Peaks regime ℓ₁ ppm (near Planck, Wave 40). -/
  peaks_ell1_ppm : Nat := 119
  /-- Peaks regime ω_m ppm (far from Planck). -/
  peaks_omega_m_ppm : Nat := 52280
  /-- Peaks regime r_d ppm. -/
  peaks_rd_ppm : Nat := 14064
  /-- Crossover ℓ₁ ≈ ℓ₃ ppm. -/
  crossover_ell1_ppm : Nat := 1670
  /-- Crossover ℓ₃ ppm. -/
  crossover_ell3_ppm : Nat := 1639
  deriving Repr
```
