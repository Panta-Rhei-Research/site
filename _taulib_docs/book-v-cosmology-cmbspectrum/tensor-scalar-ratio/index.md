---
{
  "projection_kind": "taulib_declaration",
  "title": "TensorScalarRatio",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/tensor-scalar-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TensorScalarRatio",
  "declaration_slug": "tensor-scalar-ratio",
  "kind": "structure",
  "name": "TensorScalarRatio",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 188,
  "source_line_end": 205,
  "registry_ids": [
    "V.P136"
  ],
  "related_registry_items": [
    {
      "id": "V.P136",
      "title": "CMB Tensor-to-Scalar Ratio r = ι_τ⁴",
      "url": "/registry/object/V.P136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L188-L205",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L188-L205",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L188-L205)
- Source range: L188-L205
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P136` — CMB Tensor-to-Scalar Ratio r = ι_τ⁴

## Immediate Comment / Docstring

```lean
/-- [V.P136] CMB Tensor-to-Scalar Ratio r = ι_τ⁴.
    r = 0.01357. Below BICEP/Keck bound r < 0.036.
    CMB-S4 detection at ~14σ. Falsifiable.

    Wave 13 upgrade: DERIVED from fiber dimensional suppression.
    r = ι_τ^{2·dim(T²)} = ι_τ⁴ where:
    - dim(T²) = 2: fiber dimension (two circles)
    - Factor 2: power spectrum is quadratic in amplitude
    - Tensor modes on base τ¹; scalar modes on full τ³
    Scope: conjectural → τ-effective. -/
```

## Source Excerpt

```lean
structure TensorScalarRatio where
  /-- Power of ι_τ. -/
  iota_power : Nat
  /-- Power is 4. -/
  power_eq : iota_power = 4
  /-- Fiber dimension (T² has dim 2). -/
  fiber_dim : Nat := 2
  /-- Power spectrum order. -/
  power_order : Nat := 2
  /-- Exponent = fiber_dim × power_order. -/
  exponent_derived : iota_power = fiber_dim * power_order
  /-- r × 10^6 for high precision. -/
  r_x1e6 : Nat := 13573
  /-- CMB-S4 detection significance in σ. -/
  cmbs4_sigma : Nat := 14
  /-- Free parameters beyond ι_τ. -/
  free_params : Nat := 0
  deriving Repr
```
