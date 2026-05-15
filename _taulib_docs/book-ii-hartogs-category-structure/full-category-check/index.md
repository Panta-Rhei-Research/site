---
{
  "projection_kind": "taulib_declaration",
  "title": "full_category_check",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-category-structure/full-category-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::full_category_check",
  "declaration_slug": "full-category-check",
  "kind": "def",
  "name": "full_category_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 388,
  "source_line_end": 391,
  "registry_ids": [
    "II.D41"
  ],
  "related_registry_items": [
    {
      "id": "II.D41",
      "title": "Holomorphic Endomorphism Category",
      "url": "/registry/object/II.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L388-L391",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/corpus/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L388-L391",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/corpus/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L388-L391)
- Source range: L388-L391
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D41` — Holomorphic Endomorphism Category

## Immediate Comment / Docstring

```lean
/-- [II.D41] Complete category structure verification:
    HolEnd_tau axioms + composition closure + bipolar structure. -/
```

## Source Excerpt

```lean
def full_category_check (bound db : TauIdx) : Bool :=
  holend_axioms_check (mk_holend db bound) &&
  composition_closure_check bound db &&
  bipolar_comp_check bound db
```
