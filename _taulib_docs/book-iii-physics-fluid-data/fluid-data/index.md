---
{
  "projection_kind": "taulib_declaration",
  "title": "FluidData",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/fluid-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::FluidData",
  "declaration_slug": "fluid-data",
  "kind": "structure",
  "name": "FluidData",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 46,
  "source_line_end": 49,
  "registry_ids": [
    "III.D36"
  ],
  "related_registry_items": [
    {
      "id": "III.D36",
      "title": "τ-Admissible Fluid Data",
      "url": "/registry/object/III.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L46-L49",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L46-L49",
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L46-L49)
- Source range: L46-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D36` — τ-Admissible Fluid Data

## Immediate Comment / Docstring

```lean
/-- [III.D36] Fluid data at primorial level k: for each cylinder [a mod Prim(k)],
    we store the boundary normal form (B, C, X components). -/
```

## Source Excerpt

```lean
structure FluidData where
  depth : TauIdx           -- primorial depth k
  values : List TauIdx     -- residue values at each cylinder
  deriving Repr, DecidableEq, BEq
```
