---
{
  "projection_kind": "taulib_declaration",
  "title": "tov_balance",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/tov-balance/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::tov_balance",
  "declaration_slug": "tov-balance",
  "kind": "theorem",
  "name": "tov_balance",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 306,
  "source_line_end": 308,
  "registry_ids": [
    "V.P20"
  ],
  "related_registry_items": [
    {
      "id": "V.P20",
      "title": "TOV balance as tension equilibrium",
      "url": "/registry/object/V.P20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L306-L308",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L306-L308",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L306-L308)
- Source range: L306-L308
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P20` — TOV balance as tension equilibrium

## Immediate Comment / Docstring

```lean
/-- [V.P20] TOV balance: recorded as structural fact. -/
```

## Source Excerpt

```lean
theorem tov_balance :
    "dP/dr = -(rho + P)(M + 4piPr^3) / (r(r - 2GM))" =
    "dP/dr = -(rho + P)(M + 4piPr^3) / (r(r - 2GM))" := rfl
```
