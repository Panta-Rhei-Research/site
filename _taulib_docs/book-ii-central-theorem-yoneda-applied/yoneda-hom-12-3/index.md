---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_hom_12_3",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/yoneda-hom-12-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::yoneda_hom_12_3",
  "declaration_slug": "yoneda-hom-12-3",
  "kind": "theorem",
  "name": "yoneda_hom_12_3",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 282,
  "source_line_end": 283,
  "registry_ids": [
    "II.L14"
  ],
  "related_registry_items": [
    {
      "id": "II.L14",
      "title": "Yoneda Application",
      "url": "/registry/object/II.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L282-L283",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L282-L283",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L282-L283)
- Source range: L282-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L14` — Yoneda Application

## Immediate Comment / Docstring

```lean
-- Hom identification [II.L14]
```

## Source Excerpt

```lean
theorem yoneda_hom_12_3 :
    yoneda_hom_identification_check 12 3 = true := by native_decide
```
