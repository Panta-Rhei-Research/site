---
{
  "projection_kind": "taulib_declaration",
  "title": "all_internal_quantities",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/all-internal-quantities/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::all_internal_quantities",
  "declaration_slug": "all-internal-quantities",
  "kind": "def",
  "name": "all_internal_quantities",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 327,
  "source_line_end": 328,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L327-L328",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.QuantityFramework",
        "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L327-L328",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L327-L328)
- Source range: L327-L328
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All 5 internal quantities. -/
```

## Source Excerpt

```lean
def all_internal_quantities : List InternalQuantity :=
  [time_internal, energy_internal, mass_internal, gravity_internal, entropy_internal]
```
