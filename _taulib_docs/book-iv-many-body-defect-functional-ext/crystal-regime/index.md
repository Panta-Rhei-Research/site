---
{
  "projection_kind": "taulib_declaration",
  "title": "CrystalRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::CrystalRegime",
  "declaration_slug": "crystal-regime",
  "kind": "structure",
  "name": "CrystalRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 410,
  "source_line_end": 421,
  "registry_ids": [
    "IV.D220"
  ],
  "related_registry_items": [
    {
      "id": "IV.D220",
      "title": "Crystal regime",
      "url": "/registry/object/IV.D220/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L410-L421",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L410-L421",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L410-L421)
- Source range: L410-L421
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D220` — Crystal regime

## Immediate Comment / Docstring

```lean
/-- [IV.D220] Crystal regime: mu < epsilon, |nu| < epsilon,
    |kappa| < epsilon, theta = theta_0 (fixed topological charge).
    All transport arrested, periodic lattice with frozen winding number. -/
```

## Source Excerpt

```lean
structure CrystalRegime where
  /-- Mobility arrested. -/
  mobility_arrested : Bool := true
  /-- Vorticity arrested. -/
  vorticity_arrested : Bool := true
  /-- Compression arrested. -/
  compression_arrested : Bool := true
  /-- Topological charge fixed. -/
  theta_fixed : Bool := true
  /-- Periodic lattice structure. -/
  periodic : Bool := true
  deriving Repr
```
