---
{
  "projection_kind": "taulib_declaration",
  "title": "SecondOrderTransition",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/second-order-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::SecondOrderTransition",
  "declaration_slug": "second-order-transition",
  "kind": "structure",
  "name": "SecondOrderTransition",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 370,
  "source_line_end": 377,
  "registry_ids": [
    "IV.D230"
  ],
  "related_registry_items": [
    {
      "id": "IV.D230",
      "title": "Second-order phase transition",
      "url": "/registry/object/IV.D230/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L370-L377",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L370-L377",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L370-L377)
- Source range: L370-L377
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D230` — Second-order phase transition

## Immediate Comment / Docstring

```lean
/-- [IV.D230] A second-order (continuous) phase transition at S_0 is a
    point where T_tau is continuous but dT_tau/dS_def is discontinuous.
    The defect tuple is continuous but its derivative jumps. -/
```

## Source Excerpt

```lean
structure SecondOrderTransition where
  /-- Temperature continuous. -/
  temp_continuous : Bool := true
  /-- Temperature derivative discontinuous. -/
  deriv_discontinuous : Bool := true
  /-- No latent heat. -/
  no_latent_heat : Bool := true
  deriving Repr
```
