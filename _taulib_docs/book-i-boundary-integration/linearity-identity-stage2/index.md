---
{
  "projection_kind": "taulib_declaration",
  "title": "linearity_identity_stage2",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/linearity-identity-stage2/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::linearity_identity_stage2",
  "declaration_slug": "linearity-identity-stage2",
  "kind": "theorem",
  "name": "linearity_identity_stage2",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 119,
  "source_line_end": 120,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L119-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L119-L120",
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
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L119-L120)
- Source range: L119-L120
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T51` — Linearity of Integration

## Immediate Comment / Docstring

```lean
/-- [I.T51] Linearity for (1f + 0g) at stage 2 (identity). -/
```

## Source Excerpt

```lean
theorem linearity_identity_stage2 :
    integral_linearity_check 1 0 ident_fn const_one 2 = true := by native_decide
```
