---
{
  "projection_kind": "taulib_declaration",
  "title": "incompatibility_native",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/incompatibility-native/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::incompatibility_native",
  "declaration_slug": "incompatibility-native",
  "kind": "theorem",
  "name": "incompatibility_native",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 302,
  "source_line_end": 307,
  "registry_ids": [
    "II.T43"
  ],
  "related_registry_items": [
    {
      "id": "II.T43",
      "title": "Structural Incompatibility of Unique Omega and Archimedean Density",
      "url": "/registry/object/II.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L302-L307",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.SignClassification",
        "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L302-L307",
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

- Module: [TauLib.BookII.Mirror.SignClassification](/verify/taulib/docs/book-ii-mirror-sign-classification/)
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L302-L307)
- Source range: L302-L307
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T43` — Structural Incompatibility of Unique Omega and Archimedean Density

## Immediate Comment / Docstring

```lean
-- [II.T43] Incompatibility
```

## Source Excerpt

```lean
theorem incompatibility_native :
    orthodox_path.has_unique_omega = false ∧
    tau_path.has_archimedean_density = false := by
  constructor <;> native_decide

end Tau.BookII.Mirror
```
