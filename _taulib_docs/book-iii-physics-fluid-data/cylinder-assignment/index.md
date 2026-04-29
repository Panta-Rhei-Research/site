---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_assignment",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/cylinder-assignment/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::cylinder_assignment",
  "declaration_slug": "cylinder-assignment",
  "kind": "def",
  "name": "cylinder_assignment",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 87,
  "source_line_end": 90,
  "registry_ids": [
    "III.D37"
  ],
  "related_registry_items": [
    {
      "id": "III.D37",
      "title": "Clopen Cylinder Domain",
      "url": "/registry/object/III.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L87-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L87-L90",
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L87-L90)
- Source range: L87-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D37` — Clopen Cylinder Domain

## Immediate Comment / Docstring

```lean
/-- [III.D37] Cylinder assignment: residue class x mod Prim(k) receives
    its boundary normal form. -/
```

## Source Excerpt

```lean
def cylinder_assignment (x k : TauIdx) : BoundaryNF :=
  let pk := primorial k
  if pk == 0 then ⟨0, 0, 0, k⟩
  else boundary_normal_form (x % pk) k
```
