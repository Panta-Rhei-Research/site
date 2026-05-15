---
{
  "projection_kind": "taulib_declaration",
  "title": "sign_level_count",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-sign-classification/sign-level-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::sign_level_count",
  "declaration_slug": "sign-level-count",
  "kind": "theorem",
  "name": "sign_level_count",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 109,
  "source_line_end": 109,
  "registry_ids": [
    "II.D68"
  ],
  "related_registry_items": [
    {
      "id": "II.D68",
      "title": "Structural Sign Classification",
      "url": "/registry/object/II.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L109-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L109-L109",
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
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L109-L109)
- Source range: L109-L109
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D68` — Structural Sign Classification

## Immediate Comment / Docstring

```lean
/-- [II.D68] There are exactly 12 sign levels. -/
```

## Source Excerpt

```lean
theorem sign_level_count : allSignLevels.length = 12 := by native_decide
```
