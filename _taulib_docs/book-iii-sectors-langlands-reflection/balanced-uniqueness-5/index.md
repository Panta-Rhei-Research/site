---
{
  "projection_kind": "taulib_declaration",
  "title": "balanced_uniqueness_5",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/balanced-uniqueness-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::balanced_uniqueness_5",
  "declaration_slug": "balanced-uniqueness-5",
  "kind": "theorem",
  "name": "balanced_uniqueness_5",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 245,
  "source_line_end": 246,
  "registry_ids": [
    "III.P04"
  ],
  "related_registry_items": [
    {
      "id": "III.P04",
      "title": "Balanced Sector Uniqueness",
      "url": "/registry/object/III.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L245-L246",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L245-L246",
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

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L245-L246)
- Source range: L245-L246
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P04` — Balanced Sector Uniqueness

## Immediate Comment / Docstring

```lean
-- Balanced sector uniqueness [III.P04]
```

## Source Excerpt

```lean
theorem balanced_uniqueness_5 :
    balanced_uniqueness_check 5 = true := by native_decide
```
