---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_bipolar_12_3",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-bipolar-12-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_bipolar_12_3",
  "declaration_slug": "preyoneda-bipolar-12-3",
  "kind": "theorem",
  "name": "preyoneda_bipolar_12_3",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 328,
  "source_line_end": 329,
  "registry_ids": [
    "II.P11"
  ],
  "related_registry_items": [
    {
      "id": "II.P11",
      "title": "Hom Bipolar Decomposition",
      "url": "/registry/object/II.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L328-L329",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L328-L329",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L328-L329)
- Source range: L328-L329
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P11` — Hom Bipolar Decomposition

## Immediate Comment / Docstring

```lean
-- Bipolar structure [II.P11]
```

## Source Excerpt

```lean
theorem preyoneda_bipolar_12_3 :
    preyoneda_bipolar_check 12 3 = true := by native_decide
```
