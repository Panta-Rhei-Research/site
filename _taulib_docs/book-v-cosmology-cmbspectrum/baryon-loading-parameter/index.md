---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryonLoadingParameter",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baryon-loading-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BaryonLoadingParameter",
  "declaration_slug": "baryon-loading-parameter",
  "kind": "structure",
  "name": "BaryonLoadingParameter",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 881,
  "source_line_end": 888,
  "registry_ids": [
    "V.D255"
  ],
  "related_registry_items": [
    {
      "id": "V.D255",
      "title": "Baryon Loading Parameter from tau-Native omega_b",
      "url": "/registry/object/V.D255/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L881-L888",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L881-L888",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L881-L888)
- Source range: L881-L888
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D255` — Baryon Loading Parameter from tau-Native omega_b

## Immediate Comment / Docstring

```lean
/-- [V.D255] Baryon Loading Parameter from τ-Native ω_b.
    R_b(z_rec) = 31.5·ω_b·(T/2.7)⁻⁴/(z_rec/1000) = 0.615.
    Computed from τ-native ω_b = 0.02209, T_CMB = 2.7255 K,
    z_rec = 1089.8. Controls odd/even peak asymmetry. -/
```

## Source Excerpt

```lean
structure BaryonLoadingParameter where
  /-- R_b ×1000 (0.615 → 615). -/
  r_b_x1000 : Nat := 615
  /-- Source: 1 = from τ-native ω_b. -/
  source : Nat := 1
  /-- Free parameters beyond τ inputs + T_CMB. -/
  free_params : Nat := 0
  deriving Repr
```
