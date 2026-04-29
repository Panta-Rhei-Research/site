---
{
  "projection_kind": "taulib_declaration",
  "title": "NavierStokesRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/navier-stokes-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::NavierStokesRegime",
  "declaration_slug": "navier-stokes-regime",
  "kind": "structure",
  "name": "NavierStokesRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 112,
  "source_line_end": 121,
  "registry_ids": [
    "IV.D223"
  ],
  "related_registry_items": [
    {
      "id": "IV.D223",
      "title": "Navier-Stokes regime",
      "url": "/registry/object/IV.D223/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L112-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L112-L121",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L112-L121)
- Source range: L112-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D223` — Navier-Stokes regime

## Immediate Comment / Docstring

```lean
/-- [IV.D223] The Navier-Stokes regime: mu > mu_crit, where the Euler
    budget is broken by viscous shear-defect dissipation. The budget
    decays monotonically, encoding energy dissipation.

    The tau-NS equation is the evolution law in this regime. -/
```

## Source Excerpt

```lean
structure NavierStokesRegime where
  /-- Mobility above critical threshold. -/
  above_threshold : Bool := true
  /-- Euler budget broken. -/
  budget_broken : Bool := true
  /-- Dissipation present. -/
  dissipative : Bool := true
  /-- Viscosity from defect geometry (not free parameter). -/
  viscosity_derived : Bool := true
  deriving Repr
```
