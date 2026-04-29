---
{
  "projection_kind": "taulib_declaration",
  "title": "SilkDampingScale",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/silk-damping-scale/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::SilkDampingScale",
  "declaration_slug": "silk-damping-scale",
  "kind": "structure",
  "name": "SilkDampingScale",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 795,
  "source_line_end": 808,
  "registry_ids": [
    "V.D254"
  ],
  "related_registry_items": [
    {
      "id": "V.D254",
      "title": "Silk Damping Scale from Holonomy Ratio",
      "url": "/registry/object/V.D254/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L795-L808",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L795-L808",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L795-L808)
- Source range: L795-L808
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D254` — Silk Damping Scale from Holonomy Ratio

## Immediate Comment / Docstring

```lean
/-- [V.D254] Silk Damping Scale from Holonomy Ratio.
    ℓ_D = ℓ₁ × κ_D/κ_B = ℓ₁ × (1−ι_τ)/ι_τ² = 220 × 5.6546 = 1244.0.
    Eisenstein-Hu (1998): ℓ_D ≈ 1244. Match: +9 ppm.

    Physical interpretation: photon diffusion reaches the scale where
    holonomy mass equals baryon mass. The damping multipole exceeds the
    first peak multipole by exactly the matter-to-baryon coupling ratio. -/
```

## Source Excerpt

```lean
structure SilkDampingScale where
  /-- Holonomy coupling numerator (κ_D ×10⁶). -/
  kappa_D_x1e6 : Nat := 658696
  /-- Baryon coupling numerator (κ_B ×10⁶). -/
  kappa_B_x1e6 : Nat := 116489
  /-- Ratio κ_D/κ_B ×10000 (5.6546 → 56546). -/
  ratio_x10000 : Nat := 56546
  /-- ℓ_D ×10 (1244.0 → 12440). -/
  ell_D_x10 : Nat := 12440
  /-- Deviation from Eisenstein-Hu in ppm (+9). -/
  deviation_ppm : Nat := 9
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
