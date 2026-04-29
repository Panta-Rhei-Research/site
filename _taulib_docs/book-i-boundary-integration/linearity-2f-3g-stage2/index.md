---
{
  "projection_kind": "taulib_declaration",
  "title": "linearity_2f_3g_stage2",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/linearity-2f-3g-stage2/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::linearity_2f_3g_stage2",
  "declaration_slug": "linearity-2f-3g-stage2",
  "kind": "theorem",
  "name": "linearity_2f_3g_stage2",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 115,
  "source_line_end": 116,
  "registry_ids": [
    "I.T51"
  ],
  "related_registry_items": [
    {
      "id": "I.T51",
      "title": "Linearity of Integration",
      "url": "/registry/object/I.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L115-L116",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Integration",
        "url": "/verify/taulib/docs/book-i-boundary-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L115-L116",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L115-L116)
- Source range: L115-L116
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T51` — Linearity of Integration

## Immediate Comment / Docstring

```lean
/-- [I.T51] Linearity for (2f + 3g) at stage 2. -/
```

## Source Excerpt

```lean
theorem linearity_2f_3g_stage2 :
    integral_linearity_check 2 3 ident_fn const_one 2 = true := by native_decide
```
