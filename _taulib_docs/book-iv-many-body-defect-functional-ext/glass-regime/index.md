---
{
  "projection_kind": "taulib_declaration",
  "title": "GlassRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::GlassRegime",
  "declaration_slug": "glass-regime",
  "kind": "structure",
  "name": "GlassRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 429,
  "source_line_end": 440,
  "registry_ids": [
    "IV.D221"
  ],
  "related_registry_items": [
    {
      "id": "IV.D221",
      "title": "Glass regime",
      "url": "/registry/object/IV.D221/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L429-L440",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L429-L440",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L429-L440)
- Source range: L429-L440
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D221` — Glass regime

## Immediate Comment / Docstring

```lean
/-- [IV.D221] Glass regime: mu < epsilon, |nu| < epsilon,
    |kappa| >= epsilon, theta = theta_0.
    Mobility and vorticity locked, but compression unfrozen —
    local density fluctuations without long-range order. -/
```

## Source Excerpt

```lean
structure GlassRegime where
  /-- Mobility arrested. -/
  mobility_arrested : Bool := true
  /-- Vorticity arrested. -/
  vorticity_arrested : Bool := true
  /-- Compression NOT arrested (unfrozen). -/
  compression_unfrozen : Bool := true
  /-- No long-range order. -/
  no_long_range_order : Bool := true
  /-- Topological charge fixed. -/
  theta_fixed : Bool := true
  deriving Repr
```
