---
{
  "projection_kind": "taulib_declaration",
  "title": "SilkDampingNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/silk-damping-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::SilkDampingNLO",
  "declaration_slug": "silk-damping-nlo",
  "kind": "structure",
  "name": "SilkDampingNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1545,
  "source_line_end": 1558,
  "registry_ids": [
    "V.D321"
  ],
  "related_registry_items": [
    {
      "id": "V.D321",
      "title": "Silk Damping at NLO",
      "url": "/registry/object/V.D321/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1545-L1558",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1545-L1558",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1545-L1558)
- Source range: L1545-L1558
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D321` — Silk Damping at NLO

## Immediate Comment / Docstring

```lean
/-- [V.D321] Silk Damping at NLO.
    ℓ_D = ℓ₁ × κ_D/κ_B = 1244.1 at +71 ppm.
    Scope: τ-effective (Wave 38D). -/
```

## Source Excerpt

```lean
structure SilkDampingNLO where
  /-- ℓ_D NLO. -/
  ell_d_nlo : Nat := 1244
  /-- ℓ_D LO. -/
  ell_d_lo : Nat := 1247
  /-- NLO deviation ppm. -/
  nlo_ppm : Nat := 71
  /-- LO deviation ppm. -/
  lo_ppm : Nat := 2573
  /-- κ_D/κ_B ratio × 1000. -/
  ratio_x1000 : Nat := 5655
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
