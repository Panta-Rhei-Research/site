---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongLensingCrossSection",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/strong-lensing-cross-section/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::StrongLensingCrossSection",
  "declaration_slug": "strong-lensing-cross-section",
  "kind": "structure",
  "name": "StrongLensingCrossSection",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1119,
  "source_line_end": 1124,
  "registry_ids": [
    "V.T212"
  ],
  "related_registry_items": [
    {
      "id": "V.T212",
      "title": "Strong Lensing Cross-Section Enhancement",
      "url": "/registry/object/V.T212/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1119-L1124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1119-L1124",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1119-L1124)
- Source range: L1119-L1124
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T212` — Strong Lensing Cross-Section Enhancement

## Immediate Comment / Docstring

```lean
/-- [V.T212] Strong Lensing Cross-Section Theorem.
    σ_SL = π·θ_E²·D_L². Enhancement factor (M_eff/M_b)=6.65
    gives 44× larger cross-section than baryonic-only prediction. -/
```

## Source Excerpt

```lean
structure StrongLensingCrossSection where
  /-- Cross-section enhancement factor × 10 = 442 (6.65² ≈ 44.2). -/
  enhancement_x10 : Nat := 442
  /-- Enhancement = (M_eff/M_b)². -/
  is_mass_ratio_squared : Nat := 1
  deriving Repr
```
