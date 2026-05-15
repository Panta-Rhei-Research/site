---
{
  "projection_kind": "taulib_declaration",
  "title": "TemperatureAsDefectGradient",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/temperature-as-defect-gradient/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::TemperatureAsDefectGradient",
  "declaration_slug": "temperature-as-defect-gradient",
  "kind": "structure",
  "name": "TemperatureAsDefectGradient",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 281,
  "source_line_end": 288,
  "registry_ids": [
    "IV.D228"
  ],
  "related_registry_items": [
    {
      "id": "IV.D228",
      "title": "Temperature as defect gradient",
      "url": "/registry/object/IV.D228/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L281-L288",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L281-L288",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L281-L288)
- Source range: L281-L288
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D228` — Temperature as defect gradient

## Immediate Comment / Docstring

```lean
/-- [IV.D228] The tau-temperature T_tau(C) = d delta[omega](C) / d S_def(C)
    is the gradient of the universal defect functional with respect to
    defect entropy. It is a structural quantity, not an empirical postulate. -/
```

## Source Excerpt

```lean
structure TemperatureAsDefectGradient where
  /-- Definition: gradient of delta w.r.t. S_def. -/
  definition : String := "T_tau = d(delta[omega]) / d(S_def)"
  /-- Structural (not empirical). -/
  structural : Bool := true
  /-- Non-negative (mobility >= 0 implies T_tau >= 0). -/
  nonneg : Bool := true
  deriving Repr
```
