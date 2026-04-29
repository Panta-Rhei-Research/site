---
{
  "projection_kind": "taulib_declaration",
  "title": "WeakLensingPowerSpectrum",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/weak-lensing-power-spectrum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::WeakLensingPowerSpectrum",
  "declaration_slug": "weak-lensing-power-spectrum",
  "kind": "structure",
  "name": "WeakLensingPowerSpectrum",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1157,
  "source_line_end": 1162,
  "registry_ids": [
    "V.D274"
  ],
  "related_registry_items": [
    {
      "id": "V.D274",
      "title": "τ-Native Convergence Power Spectrum",
      "url": "/registry/object/V.D274/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1157-L1162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1157-L1162",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1157-L1162)
- Source range: L1157-L1162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D274` — τ-Native Convergence Power Spectrum

## Immediate Comment / Docstring

```lean
/-- [V.D274] Weak Lensing Power Spectrum P_κ(ℓ).
    P_κ(ℓ) via Limber integral with τ-native d_A(z) and M_eff.
    Matches ΛCDM P_κ(ℓ) since Ω_m·σ₈ plays same structural role. -/
```

## Source Excerpt

```lean
structure WeakLensingPowerSpectrum where
  /-- Limber integral uses τ-native d_A (1 = yes). -/
  uses_tau_dA : Nat := 1
  /-- Matches ΛCDM at current precision (1 = yes). -/
  matches_lcdm : Nat := 1
  deriving Repr
```
