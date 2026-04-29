---
{
  "projection_kind": "taulib_declaration",
  "title": "orthodox_path",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-path/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::orthodox_path",
  "declaration_slug": "orthodox-path",
  "kind": "def",
  "name": "orthodox_path",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 155,
  "source_line_end": 159,
  "registry_ids": [
    "II.D69"
  ],
  "related_registry_items": [
    {
      "id": "II.D69",
      "title": "The Infinity Trade-Off",
      "url": "/registry/object/II.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L155-L159",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L155-L159",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L155-L159)
- Source range: L155-L159
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D69` — The Infinity Trade-Off

## Immediate Comment / Docstring

```lean
/-- [II.D69] The orthodox path: Archimedean with epsilon-delta,
    but no unique omega and no finite witnesses. -/
```

## Source Excerpt

```lean
def orthodox_path : InfinityTradeOff :=
  { has_unique_omega := false
  , has_archimedean_density := true
  , has_epsilon_delta := true
  , has_finite_witnesses := false }
```
