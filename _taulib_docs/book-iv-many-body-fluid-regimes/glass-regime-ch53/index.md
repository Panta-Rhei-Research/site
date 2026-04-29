---
{
  "projection_kind": "taulib_declaration",
  "title": "GlassRegimeCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/glass-regime-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::GlassRegimeCh53",
  "declaration_slug": "glass-regime-ch53",
  "kind": "structure",
  "name": "GlassRegimeCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 267,
  "source_line_end": 278,
  "registry_ids": [
    "IV.D236"
  ],
  "related_registry_items": [
    {
      "id": "IV.D236",
      "title": "Glass regime",
      "url": "/registry/object/IV.D236/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L267-L278",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L267-L278",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L267-L278)
- Source range: L267-L278
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D236` — Glass regime

## Immediate Comment / Docstring

```lean
/-- [IV.D236] Glass regime (ch53 formulation): mu ~ 0, nu ~ 0,
    kappa > 0 (compression unfrozen, local density fluctuations),
    theta = theta_0. No long-range order, continuous (not sharp) transition. -/
```

## Source Excerpt

```lean
structure GlassRegimeCh53 where
  /-- Number of arrested translational DOFs on T² (2 = both directions). -/
  n_arrested_translations : Nat := 2
  /-- Number of arrested rotational DOFs (1 = vorticity arrested). -/
  n_arrested_rotations : Nat := 1
  /-- Number of unfrozen components (1 = kappa free). -/
  n_unfrozen_components : Nat := 1
  /-- Correlation length bound exponent (0 = no long-range order). -/
  correlation_exponent : Nat := 0
  /-- Total arrested = translations + rotations = 3 of 4 components. -/
  three_arrested : n_arrested_translations + n_arrested_rotations = 3
  deriving Repr
```
