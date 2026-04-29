---
{
  "projection_kind": "taulib_declaration",
  "title": "structure_uniqueness",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/structure-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::structure_uniqueness",
  "declaration_slug": "structure-uniqueness",
  "kind": "theorem",
  "name": "structure_uniqueness",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 375,
  "source_line_end": 377,
  "registry_ids": [
    "II.C02"
  ],
  "related_registry_items": [
    {
      "id": "II.C02",
      "title": "Uniqueness of Category Tau",
      "url": "/registry/object/II.C02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L375-L377",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L375-L377",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L375-L377)
- Source range: L375-L377
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.C02` — Uniqueness of Category Tau

## Immediate Comment / Docstring

```lean
/-- [II.C02] Uniqueness: reduce is defined by modular arithmetic.
    There is exactly one way to define it: x % primorial k. -/
```

## Source Excerpt

```lean
theorem structure_uniqueness (x k : TauIdx) :
    reduce x k = x % primorial k := by
  rfl
```
