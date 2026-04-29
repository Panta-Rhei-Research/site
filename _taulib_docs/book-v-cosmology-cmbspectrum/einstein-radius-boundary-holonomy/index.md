---
{
  "projection_kind": "taulib_declaration",
  "title": "EinsteinRadiusBoundaryHolonomy",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/einstein-radius-boundary-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::EinsteinRadiusBoundaryHolonomy",
  "declaration_slug": "einstein-radius-boundary-holonomy",
  "kind": "structure",
  "name": "EinsteinRadiusBoundaryHolonomy",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1099,
  "source_line_end": 1106,
  "registry_ids": [
    "V.D272"
  ],
  "related_registry_items": [
    {
      "id": "V.D272",
      "title": "Einstein Radius from Boundary Holonomy",
      "url": "/registry/object/V.D272/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1099-L1106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1099-L1106",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1099-L1106)
- Source range: L1099-L1106
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D272` — Einstein Radius from Boundary Holonomy

## Immediate Comment / Docstring

```lean
/-- [V.D272] Einstein Radius with Boundary Holonomy Mass.
    θ_E² = 4G·M_eff·D_LS/(c²·D_L·D_S).
    M_eff = 6.65·M_baryonic (from capacity gradient).
    SLACS: 5/5 systems consistent. -/
```

## Source Excerpt

```lean
structure EinsteinRadiusBoundaryHolonomy where
  /-- M_eff/M_baryonic × 100 = 665. -/
  mass_ratio_x100 : Nat := 665
  /-- SLACS systems matched (of 5). -/
  slacs_matched : Nat := 5
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
