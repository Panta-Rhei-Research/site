---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroscopicVorticity",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-vorticity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::MacroscopicVorticity",
  "declaration_slug": "macroscopic-vorticity",
  "kind": "structure",
  "name": "MacroscopicVorticity",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 146,
  "source_line_end": 153,
  "registry_ids": [
    "IV.D212"
  ],
  "related_registry_items": [
    {
      "id": "IV.D212",
      "title": "Macroscopic vorticity",
      "url": "/registry/object/IV.D212/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L146-L153",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L146-L153",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L146-L153)
- Source range: L146-L153
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D212` — Macroscopic vorticity

## Immediate Comment / Docstring

```lean
/-- [IV.D212] Macroscopic vorticity: nu^macro(C) = (1/N) sum_i nu(d_i) + nu_int(C).
    In a superfluid, nu^macro = 0 everywhere except at quantized vortex
    cores where topological charge concentrates. -/
```

## Source Excerpt

```lean
structure MacroscopicVorticity where
  /-- Average single-particle vorticity (scaled). -/
  average_vorticity : Nat
  /-- Interaction correction. -/
  interaction : Int
  /-- In superfluid: vanishes except at vortex cores. -/
  superfluid_vanishes : Bool
  deriving Repr
```
