---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralAF",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/structural-af/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::StructuralAF",
  "declaration_slug": "structural-af",
  "kind": "structure",
  "name": "StructuralAF",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 260,
  "source_line_end": 267,
  "registry_ids": [
    "IV.P117"
  ],
  "related_registry_items": [
    {
      "id": "IV.P117",
      "title": "Structural asymptotic freedom",
      "url": "/registry/object/IV.P117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L260-L267",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L260-L267",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L260-L267)
- Source range: L260-L267
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P117` — Structural asymptotic freedom

## Immediate Comment / Docstring

```lean
/-- [IV.P117] The C-sector readout R_C(n) is monotonically decreasing
    with refinement depth n => alpha_s^eff(n) decreases at high energy. -/
```

## Source Excerpt

```lean
structure StructuralAF where
  /-- Readout monotonically decreasing. -/
  monotone_decreasing : Bool := true
  /-- Effective coupling decreases at high energy. -/
  coupling_decreases : Bool := true
  /-- Source: chi_minus spectral tightening. -/
  source : String := "chi_minus spectral tightening"
  deriving Repr
```
