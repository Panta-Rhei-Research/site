---
{
  "projection_kind": "taulib_declaration",
  "title": "orthodox_path_no_finite_witnesses",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-sign-classification/orthodox-path-no-finite-witnesses/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::orthodox_path_no_finite_witnesses",
  "declaration_slug": "orthodox-path-no-finite-witnesses",
  "kind": "theorem",
  "name": "orthodox_path_no_finite_witnesses",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 182,
  "source_line_end": 183,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L182-L183",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.SignClassification",
        "url": "/corpus/taulib/docs/book-ii-mirror-sign-classification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L182-L183",
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

- Module: [TauLib.BookII.Mirror.SignClassification](/corpus/taulib/docs/book-ii-mirror-sign-classification/)
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L182-L183)
- Source range: L182-L183
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.T43` — Structural Incompatibility of Unique Omega and Archimedean Density

## Immediate Comment / Docstring

```lean
/-- [II.T43] The orthodox path does not have finite witnesses. -/
```

## Source Excerpt

```lean
theorem orthodox_path_no_finite_witnesses :
    orthodox_path.has_finite_witnesses = false := rfl
```
