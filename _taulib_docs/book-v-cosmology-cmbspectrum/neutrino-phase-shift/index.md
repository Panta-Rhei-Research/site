---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoPhaseShift",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/neutrino-phase-shift/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::NeutrinoPhaseShift",
  "declaration_slug": "neutrino-phase-shift",
  "kind": "structure",
  "name": "NeutrinoPhaseShift",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 266,
  "source_line_end": 271,
  "registry_ids": [
    "V.T194"
  ],
  "related_registry_items": [
    {
      "id": "V.T194",
      "title": "Neutrino Phase Shift on CMB Peaks",
      "url": "/registry/object/V.T194/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L266-L271",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L266-L271",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L266-L271)
- Source range: L266-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T194` — Neutrino Phase Shift on CMB Peaks

## Immediate Comment / Docstring

```lean
/-- [V.T194] Neutrino Phase Shift on CMB Peaks.
    φ_ν = 0.191π·N_eff/(N_eff+15/4). For τ (N_eff=3): 0.0849π. -/
```

## Source Excerpt

```lean
structure NeutrinoPhaseShift where
  /-- N_eff in τ framework. -/
  n_eff : Nat := 3
  /-- CMB-S4 sensitivity in σ ×10 (1.5σ → 15). -/
  sensitivity_sigma_x10 : Nat := 15
  deriving Repr
```
