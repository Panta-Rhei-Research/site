---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_extract",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/abcd-extract/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::abcd_extract",
  "declaration_slug": "abcd-extract",
  "kind": "def",
  "name": "abcd_extract",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 124,
  "source_line_end": 126,
  "registry_ids": [
    "III.D38"
  ],
  "related_registry_items": [
    {
      "id": "III.D38",
      "title": "Fluid Sector Decomposition",
      "url": "/registry/object/III.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L124-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.FluidData",
        "url": "/verify/taulib/docs/book-iii-physics-fluid-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L124-L126",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Physics.FluidData](/verify/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L124-L126)
- Source range: L124-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D38` — Fluid Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D38] Extract ABCD components from a cylinder assignment. -/
```

## Source Excerpt

```lean
def abcd_extract (x k : TauIdx) : ABCDComponents :=
  let nf := cylinder_assignment x k
  ⟨nf.depth, nf.b_part, nf.c_part, nf.x_part⟩
```
