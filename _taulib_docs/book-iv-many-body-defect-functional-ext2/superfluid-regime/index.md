---
{
  "projection_kind": "taulib_declaration",
  "title": "SuperfluidRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::SuperfluidRegime",
  "declaration_slug": "superfluid-regime",
  "kind": "structure",
  "name": "SuperfluidRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 184,
  "source_line_end": 193,
  "registry_ids": [
    "IV.D226"
  ],
  "related_registry_items": [
    {
      "id": "IV.D226",
      "title": "Superfluid regime",
      "url": "/registry/object/IV.D226/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L184-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L184-L193",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L184-L193)
- Source range: L184-L193
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D226` — Superfluid regime

## Immediate Comment / Docstring

```lean
/-- [IV.D226] The superfluid regime: mu = mu_max (maximal mobility),
    nu = 0 a.e. (vanishing vorticity except at isolated quantized vortex
    cores), kappa = 0 (incompressible), theta quantized.

    Transport is maximally free, rotation is suppressed except at
    topological defects with integer winding number. -/
```

## Source Excerpt

```lean
structure SuperfluidRegime where
  /-- Maximal mobility. -/
  maximal_mobility : Bool := true
  /-- Vorticity vanishes (except at cores). -/
  vorticity_vanishes_ae : Bool := true
  /-- Incompressible. -/
  incompressible : Bool := true
  /-- Theta quantized at vortex cores. -/
  theta_quantized : Bool := true
  deriving Repr
```
