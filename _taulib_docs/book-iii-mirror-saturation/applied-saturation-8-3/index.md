---
{
  "projection_kind": "taulib_declaration",
  "title": "applied_saturation_8_3",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/applied-saturation-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::applied_saturation_8_3",
  "declaration_slug": "applied-saturation-8-3",
  "kind": "theorem",
  "name": "applied_saturation_8_3",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 228,
  "source_line_end": 229,
  "registry_ids": [
    "III.T49"
  ],
  "related_registry_items": [
    {
      "id": "III.T49",
      "title": "Applied Saturation",
      "url": "/registry/object/III.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L228-L229",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L228-L229",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L228-L229)
- Source range: L228-L229
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T49` — Applied Saturation

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Applied saturation [III.T49]
```

## Source Excerpt

```lean
theorem applied_saturation_8_3 :
    applied_saturation_check 8 3 = true := by native_decide
```
