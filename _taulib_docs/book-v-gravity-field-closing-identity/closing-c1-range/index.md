---
{
  "projection_kind": "taulib_declaration",
  "title": "closing_c1_range",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/closing-c1-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::closing_c1_range",
  "declaration_slug": "closing-c1-range",
  "kind": "theorem",
  "name": "closing_c1_range",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 232,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L232-L234",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ClosingIdentity",
        "url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L232-L234",
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

- Module: [TauLib.BookV.GravityField.ClosingIdentity](/verify/taulib/docs/book-v-gravity-field-closing-identity/)
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L232-L234)
- Source range: L232-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- c1 = 3/pi is in range (0.954, 0.956). -/
```

## Source Excerpt

```lean
theorem closing_c1_range :
    954 * c1_three_over_pi_denom < 1000 * c1_three_over_pi_numer :=
  (c1_in_range).1
```
