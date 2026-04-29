---
{
  "projection_kind": "taulib_declaration",
  "title": "nonconstant_bounded_4",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/nonconstant-bounded-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::nonconstant_bounded_4",
  "declaration_slug": "nonconstant-bounded-4",
  "kind": "theorem",
  "name": "nonconstant_bounded_4",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 296,
  "source_line_end": 297,
  "registry_ids": [
    "II.T41"
  ],
  "related_registry_items": [
    {
      "id": "II.T41",
      "title": "Liouville Categorical Dodge",
      "url": "/registry/object/II.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L296-L297",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L296-L297",
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
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L296-L297)
- Source range: L296-L297
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T41` — Liouville Categorical Dodge

## Immediate Comment / Docstring

```lean
-- Nonconstant bounded [II.T41]
```

## Source Excerpt

```lean
theorem nonconstant_bounded_4 :
    nonconstant_bounded_check 4 = true := by native_decide
```
