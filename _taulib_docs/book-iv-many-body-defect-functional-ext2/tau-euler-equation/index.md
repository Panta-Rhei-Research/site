---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEulerEquation",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/tau-euler-equation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::TauEulerEquation",
  "declaration_slug": "tau-euler-equation",
  "kind": "structure",
  "name": "TauEulerEquation",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 89,
  "source_line_end": 96,
  "registry_ids": [
    "IV.P136"
  ],
  "related_registry_items": [
    {
      "id": "IV.P136",
      "title": "tau-Euler equation",
      "url": "/registry/object/IV.P136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L89-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L89-L96",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L89-L96)
- Source range: L89-L96
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P136` — tau-Euler equation

## Immediate Comment / Docstring

```lean
/-- [IV.P136] In the Euler fluid regime the macroscopic defect tuple evolves as
    d/dn (mu_n, nu_n, kappa_n, theta_n) = (f_mu, f_nu, f_kappa, 0) subject to
    the budget constraint. The theta component has zero derivative because
    topological charge is a deformation invariant.

    This is the tau-native formulation of the Euler equation. -/
```

## Source Excerpt

```lean
structure TauEulerEquation where
  /-- Theta derivative is zero. -/
  theta_derivative_zero : Bool := true
  /-- Budget constraint enforced. -/
  budget_constraint : Bool := true
  /-- tau-native (no PDE imported). -/
  tau_native : Bool := true
  deriving Repr
```
