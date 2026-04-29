---
{
  "projection_kind": "taulib_declaration",
  "title": "ABCDComponents",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/abcdcomponents/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::ABCDComponents",
  "declaration_slug": "abcdcomponents",
  "kind": "structure",
  "name": "ABCDComponents",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 116,
  "source_line_end": 121,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L116-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L116-L121",
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

- Module: [TauLib.BookIII.Physics.FluidData](/verify/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L116-L121)
- Source range: L116-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D38` — Fluid Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D38] ABCD components of a fluid datum at a cylinder.
    A = depth (time/scale), B = B-lobe, C = C-lobe, D = crossing. -/
```

## Source Excerpt

```lean
structure ABCDComponents where
  a_comp : TauIdx    -- depth (time component)
  b_comp : TauIdx    -- B-lobe contribution
  c_comp : TauIdx    -- C-lobe contribution
  d_comp : TauIdx    -- crossing (X-type) contribution
  deriving Repr, DecidableEq, BEq
```
