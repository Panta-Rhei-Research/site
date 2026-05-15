---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_abcd_12_3",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-abcd-12-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_abcd_12_3",
  "declaration_slug": "preyoneda-abcd-12-3",
  "kind": "theorem",
  "name": "preyoneda_abcd_12_3",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 332,
  "source_line_end": 333,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L332-L333",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L332-L333",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/corpus/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L332-L333)
- Source range: L332-L333
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.P11` — Hom Bipolar Decomposition

## Immediate Comment / Docstring

```lean
-- ABCD coordinates [II.P11]
```

## Source Excerpt

```lean
theorem preyoneda_abcd_12_3 :
    preyoneda_abcd_check 12 3 = true := by native_decide
```
