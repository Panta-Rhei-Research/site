---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimordialBModeAmplitude",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/primordial-bmode-amplitude/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PrimordialBModeAmplitude",
  "declaration_slug": "primordial-bmode-amplitude",
  "kind": "structure",
  "name": "PrimordialBModeAmplitude",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 969,
  "source_line_end": 980,
  "registry_ids": [
    "V.D256"
  ],
  "related_registry_items": [
    {
      "id": "V.D256",
      "title": "Primordial B-Mode Amplitude from r = iota_tau^4",
      "url": "/registry/object/V.D256/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L969-L980",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L969-L980",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L969-L980)
- Source range: L969-L980
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D256` — Primordial B-Mode Amplitude from r = iota_tau^4

## Immediate Comment / Docstring

```lean
/-- [V.D256] Primordial B-Mode Amplitude from r = ι_τ⁴.
    D_80^BB = ℓ(ℓ+1)C_ℓ^BB/(2π) ≈ 0.025 × r = 339 nK² at ℓ ~ 80
    (recombination bump). Tensor amplitude A_t = r × A_s = 2.844×10⁻¹¹. -/
```

## Source Excerpt

```lean
structure PrimordialBModeAmplitude where
  /-- Recombination bump peak multipole. -/
  peak_ell : Nat := 80
  /-- D^BB in nK² (339 → 339). -/
  d_bb_nk2 : Nat := 339
  /-- r × 10⁶ (0.01357 → 13570). -/
  r_x1e6 : Nat := 13570
  /-- Source: 1 = from r = ι_τ⁴ derivation. -/
  r_source : Nat := 1
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
