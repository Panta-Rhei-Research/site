---
{
  "projection_kind": "taulib_declaration",
  "title": "fluid_data_4",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/fluid-data-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::fluid_data_4",
  "declaration_slug": "fluid-data-4",
  "kind": "theorem",
  "name": "fluid_data_4",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 205,
  "source_line_end": 206,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L205-L206",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L205-L206",
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L205-L206)
- Source range: L205-L206
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================
```

## Source Excerpt

```lean
theorem fluid_data_4 :
    fluid_data_check 4 = true := by native_decide
```
