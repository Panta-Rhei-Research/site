---
{
  "projection_kind": "taulib_declaration",
  "title": "EulerFluidRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/euler-fluid-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::EulerFluidRegime",
  "declaration_slug": "euler-fluid-regime",
  "kind": "structure",
  "name": "EulerFluidRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 66,
  "source_line_end": 75,
  "registry_ids": [
    "IV.D222"
  ],
  "related_registry_items": [
    {
      "id": "IV.D222",
      "title": "Euler fluid regime",
      "url": "/registry/object/IV.D222/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L66-L75",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L66-L75",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L66-L75)
- Source range: L66-L75
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D222` — Euler fluid regime

## Immediate Comment / Docstring

```lean
/-- [IV.D222] The Euler fluid regime: the subset of D where
    0 < mu <= mu_crit and the Euler budget constraint holds:
    mu + nu + kappa + theta = const (inviscid, no dissipation).

    Distinguished from the single-bundle Euler regime by including
    N-body interaction corrections in the budget law. -/
```

## Source Excerpt

```lean
structure EulerFluidRegime where
  /-- Mobility bounded by critical threshold. -/
  mobility_bounded : Bool := true
  /-- Budget conservation holds. -/
  budget_conserved : Bool := true
  /-- No dissipation (inviscid). -/
  inviscid : Bool := true
  /-- Kelvin circulation theorem holds. -/
  kelvin_holds : Bool := true
  deriving Repr
```
