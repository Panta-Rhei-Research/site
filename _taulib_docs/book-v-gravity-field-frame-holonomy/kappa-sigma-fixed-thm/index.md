---
{
  "projection_kind": "taulib_declaration",
  "title": "kappa_sigma_fixed_thm",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/kappa-sigma-fixed-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::kappa_sigma_fixed_thm",
  "declaration_slug": "kappa-sigma-fixed-thm",
  "kind": "theorem",
  "name": "kappa_sigma_fixed_thm",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 314,
  "source_line_end": 315,
  "registry_ids": [
    "V.T23"
  ],
  "related_registry_items": [
    {
      "id": "V.T23",
      "title": "sigma-equivariance of kappa_tau",
      "url": "/registry/object/V.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L314-L315",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L314-L315",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L314-L315)
- Source range: L314-L315
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T23` — sigma-equivariance of kappa_tau

## Immediate Comment / Docstring

```lean
/-- [V.T23] κ_τ is σ-fixed (unpolarized). Gravity couples to total
    energy-momentum, not to any specific polarity channel. -/
```

## Source Excerpt

```lean
theorem kappa_sigma_fixed_thm :
    canonical_grav_coupling.sigma_fixed = true := by rfl
```
