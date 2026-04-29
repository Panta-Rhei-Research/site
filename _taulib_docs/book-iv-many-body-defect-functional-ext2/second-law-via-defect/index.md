---
{
  "projection_kind": "taulib_declaration",
  "title": "SecondLawViaDefect",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/second-law-via-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::SecondLawViaDefect",
  "declaration_slug": "second-law-via-defect",
  "kind": "structure",
  "name": "SecondLawViaDefect",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 329,
  "source_line_end": 338,
  "registry_ids": [
    "IV.T91"
  ],
  "related_registry_items": [
    {
      "id": "IV.T91",
      "title": "Second law via defect functional",
      "url": "/registry/object/IV.T91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L329-L338",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L329-L338",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L329-L338)
- Source range: L329-L338
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T91` — Second law via defect functional

## Immediate Comment / Docstring

```lean
/-- [IV.T91] Second law via defect functional: under propagation
    Phi_{n,n+1}, defect entropy S_def is non-increasing, refinement
    entropy S_ref is non-decreasing, and total entropy S = S_def + S_ref
    is non-decreasing. This is the structural second law of thermodynamics.

    The arrow of time is the direction of increasing S_ref. -/
```

## Source Excerpt

```lean
structure SecondLawViaDefect where
  /-- S_def non-increasing. -/
  s_def_nonincreasing : Bool := true
  /-- S_ref non-decreasing. -/
  s_ref_nondecreasing : Bool := true
  /-- S_total = S_def + S_ref non-decreasing. -/
  s_total_nondecreasing : Bool := true
  /-- Arrow of time: direction of increasing S_ref. -/
  arrow_of_time : String := "direction of increasing S_ref"
  deriving Repr
```
