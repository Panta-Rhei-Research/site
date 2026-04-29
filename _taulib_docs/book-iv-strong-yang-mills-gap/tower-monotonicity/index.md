---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerMonotonicity",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/tower-monotonicity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::TowerMonotonicity",
  "declaration_slug": "tower-monotonicity",
  "kind": "structure",
  "name": "TowerMonotonicity",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 263,
  "source_line_end": 268,
  "registry_ids": [
    "IV.P108"
  ],
  "related_registry_items": [
    {
      "id": "IV.P108",
      "title": "Tower monotonicity",
      "url": "/registry/object/IV.P108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L263-L268",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L263-L268",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L263-L268)
- Source range: L263-L268
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P108` — Tower monotonicity

## Immediate Comment / Docstring

```lean
/-- [IV.P108] Tower monotonicity: delta_{n+1}^s >= delta_n^s.
    The spectral gap is non-decreasing along the refinement tower. -/
```

## Source Excerpt

```lean
structure TowerMonotonicity where
  /-- Non-decreasing gaps. -/
  non_decreasing : Bool := true
  /-- Higher refinement strengthens constraints. -/
  mechanism : String := "higher refinement strengthens admissibility constraints"
  deriving Repr
```
