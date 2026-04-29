---
{
  "projection_kind": "taulib_declaration",
  "title": "TauAngularDiameterDistance",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/tau-angular-diameter-distance/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TauAngularDiameterDistance",
  "declaration_slug": "tau-angular-diameter-distance",
  "kind": "structure",
  "name": "TauAngularDiameterDistance",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1057,
  "source_line_end": 1062,
  "registry_ids": [
    "V.D270"
  ],
  "related_registry_items": [
    {
      "id": "V.D270",
      "title": "τ-Native Angular Diameter Distance",
      "url": "/registry/object/V.D270/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1057-L1062",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1057-L1062",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1057-L1062)
- Source range: L1057-L1062
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D270` — τ-Native Angular Diameter Distance

## Immediate Comment / Docstring

```lean
/-- [V.D270] τ-Native Angular Diameter Distance d_A(z).
    d_A(z) = d_L(z)/(1+z)². Etherington reciprocity.
    At z=1100: d_A ≈ 12.6 Mpc. -/
```

## Source Excerpt

```lean
structure TauAngularDiameterDistance where
  /-- Etherington reciprocity verified (1 = yes). -/
  etherington_verified : Nat := 1
  /-- d_A(z=1100) × 10 in Mpc = 126. -/
  dA_cmb_x10 : Nat := 126
  deriving Repr
```
