---
{
  "projection_kind": "taulib_declaration",
  "title": "fluid_data_depth_3",
  "permalink": "/corpus/taulib/docs/book-iii-physics-fluid-data/fluid-data-depth-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::fluid_data_depth_3",
  "declaration_slug": "fluid-data-depth-3",
  "kind": "theorem",
  "name": "fluid_data_depth_3",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/corpus/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 228,
  "source_line_end": 229,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L228-L229",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.FluidData",
        "url": "/corpus/taulib/docs/book-iii-physics-fluid-data/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L228-L229",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Physics.FluidData](/corpus/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L228-L229)
- Source range: L228-L229
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D36` — τ-Admissible Fluid Data

## Immediate Comment / Docstring

```lean
/-- [III.D36] Structural: canonical fluid data at depth 3 has 30 values. -/
```

## Source Excerpt

```lean
theorem fluid_data_depth_3 :
    (make_fluid_data 3).values.length = 30 := by native_decide
```
