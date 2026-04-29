---
{
  "projection_kind": "taulib_declaration",
  "title": "GluonCount",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-count/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::GluonCount",
  "declaration_slug": "gluon-count",
  "kind": "structure",
  "name": "GluonCount",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 217,
  "source_line_end": 224,
  "registry_ids": [
    "IV.P115"
  ],
  "related_registry_items": [
    {
      "id": "IV.P115",
      "title": "Gluon count",
      "url": "/registry/object/IV.P115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L217-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L217-L224",
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
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L217-L224)
- Source range: L217-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P115` — Gluon count

## Immediate Comment / Docstring

```lean
/-- [IV.P115] Exactly 8 independent gluon connection modes:
    dim_R su(3) = 3^2 - 1 = 8. -/
```

## Source Excerpt

```lean
structure GluonCount where
  /-- Number of gluon types. -/
  count : Nat := 8
  /-- Formula: N_c^2 - 1. -/
  formula : String := "N_c^2 - 1 = 3^2 - 1 = 8"
  /-- Each basis element = independent gluon. -/
  basis_elements : Bool := true
  deriving Repr
```
