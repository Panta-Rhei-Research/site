---
{
  "projection_kind": "taulib_declaration",
  "title": "translation_boundary_8_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/translation-boundary-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::translation_boundary_8_3",
  "declaration_slug": "translation-boundary-8-3",
  "kind": "theorem",
  "name": "translation_boundary_8_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 254,
  "source_line_end": 255,
  "registry_ids": [
    "III.T61"
  ],
  "related_registry_items": [
    {
      "id": "III.T61",
      "title": "Translation Failure Boundary",
      "url": "/registry/object/III.T61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L254-L255",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L254-L255",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L254-L255)
- Source range: L254-L255
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T61` — Translation Failure Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T61] Translation failure boundary at bound 8, depth 3. -/
```

## Source Excerpt

```lean
theorem translation_boundary_8_3 :
    translation_failure_boundary_check 8 3 = true := by native_decide
```
