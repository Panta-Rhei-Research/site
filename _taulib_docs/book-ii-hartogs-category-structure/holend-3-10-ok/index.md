---
{
  "projection_kind": "taulib_declaration",
  "title": "holend_3_10_ok",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/holend-3-10-ok/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::holend_3_10_ok",
  "declaration_slug": "holend-3-10-ok",
  "kind": "theorem",
  "name": "holend_3_10_ok",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 465,
  "source_line_end": 466,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L465-L466",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L465-L466",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L465-L466)
- Source range: L465-L466
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D41` — Holomorphic Endomorphism Category

## Immediate Comment / Docstring

```lean
-- Category axioms [II.D41]
```

## Source Excerpt

```lean
theorem holend_3_10_ok :
    holend_axioms_check holend_3_10 = true := by native_decide
```
