---
{
  "projection_kind": "taulib_declaration",
  "title": "SpinTempCoupling",
  "permalink": "/verify/taulib/docs/book-v-cosmology-reionization/spin-temp-coupling/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.Reionization`.",
  "declaration_id": "TauLib.BookV.Cosmology.Reionization::SpinTempCoupling",
  "declaration_slug": "spin-temp-coupling",
  "kind": "inductive",
  "name": "SpinTempCoupling",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_url": "/verify/taulib/docs/book-v-cosmology-reionization/",
  "source_line_start": 59,
  "source_line_end": 68,
  "registry_ids": [
    "V.D335"
  ],
  "related_registry_items": [
    {
      "id": "V.D335",
      "title": "Spin Temperature Coupling Regimes",
      "url": "/registry/object/V.D335/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L59-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.Reionization",
        "url": "/verify/taulib/docs/book-v-cosmology-reionization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L59-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Cosmology.Reionization](/verify/taulib/docs/book-v-cosmology-reionization/)
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L59-L68)
- Source range: L59-L68
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D335` — Spin Temperature Coupling Regimes

## Immediate Comment / Docstring

```lean
/-- Spin temperature coupling regimes [V.D335].
    Scope: conjectural (astrophysical modelling of x_α). -/
```

## Source Excerpt

```lean
inductive SpinTempCoupling where
  /-- Collisional coupling: z > 200, T_S ≈ T_K ≈ T_CMB. -/
  | collisional
  /-- Dark ages: 30 < z < 200, T_K decouples, adiabatic cooling. -/
  | dark_ages
  /-- Cosmic dawn: z_reion < z < 30, Wouthuysen–Field effect. -/
  | cosmic_dawn
  /-- Post-reionization: z < z_reion, emission. -/
  | post_reion
  deriving DecidableEq, Repr
```
