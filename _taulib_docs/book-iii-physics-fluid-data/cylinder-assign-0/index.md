---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_assign_0",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/cylinder-assign-0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::cylinder_assign_0",
  "declaration_slug": "cylinder-assign-0",
  "kind": "theorem",
  "name": "cylinder_assign_0",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 232,
  "source_line_end": 233,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L232-L233",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L232-L233",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L232-L233)
- Source range: L232-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D37` — Clopen Cylinder Domain

## Immediate Comment / Docstring

```lean
/-- [III.D37] Structural: cylinder assignment at depth 0 is trivial. -/
```

## Source Excerpt

```lean
theorem cylinder_assign_0 :
    cylinder_assignment 42 0 = ⟨0, 0, 0, 0⟩ := by native_decide
```
