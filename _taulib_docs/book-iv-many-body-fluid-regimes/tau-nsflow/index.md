---
{
  "projection_kind": "taulib_declaration",
  "title": "TauNSFlow",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsflow/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::TauNSFlow",
  "declaration_slug": "tau-nsflow",
  "kind": "structure",
  "name": "TauNSFlow",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 95,
  "source_line_end": 106,
  "registry_ids": [
    "IV.D232"
  ],
  "related_registry_items": [
    {
      "id": "IV.D232",
      "title": "tau-Navier-Stokes flow",
      "url": "/registry/object/IV.D232/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L95-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L95-L106",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L95-L106)
- Source range: L95-L106
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D232` — tau-Navier-Stokes flow

## Immediate Comment / Docstring

```lean
/-- [IV.D232] A tau-Navier-Stokes flow is a sequence {d_n} where
    mu(d_n) > mu_crit for some or all n, with viscous budget decay
    B_{n+1} - B_n proportional to mu - mu_crit.

    The viscosity coefficient eta_tau is determined by the defect-functional
    geometry, not a free parameter. -/
```

## Source Excerpt

```lean
structure TauNSFlow where
  /-- Number of supercritical modes (at least 1 above threshold). -/
  n_supercritical_modes : Nat := 1
  /-- Number of dissipation channels (viscous). -/
  n_dissipation_channels : Nat := 1
  /-- Number of free viscosity parameters (0 = structurally determined). -/
  n_free_params : Nat := 0
  /-- Number of primorial stages computed. -/
  stages : Nat
  /-- Viscosity is structural: zero free parameters. -/
  structural_viscosity : n_free_params = 0
  deriving Repr
```
