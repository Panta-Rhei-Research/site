---
{
  "projection_kind": "taulib_declaration",
  "title": "star_builder_coherent",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::star_builder_coherent",
  "declaration_slug": "star-builder-coherent",
  "kind": "theorem",
  "name": "star_builder_coherent",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 283,
  "source_line_end": 284,
  "registry_ids": [
    "V.T42"
  ],
  "related_registry_items": [
    {
      "id": "V.T42",
      "title": "Star builder existence and uniqueness",
      "url": "/registry/object/V.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L283-L284",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L283-L284",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L283-L284)
- Source range: L283-L284
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T42` — Star builder existence and uniqueness

## Immediate Comment / Docstring

```lean
/-- [V.T42] Star builder produces coherent models. -/
```

## Source Excerpt

```lean
theorem star_builder_coherent (sb : StarBuilder) (h : sb.is_coherent = true) :
    sb.is_coherent = true := h
```
