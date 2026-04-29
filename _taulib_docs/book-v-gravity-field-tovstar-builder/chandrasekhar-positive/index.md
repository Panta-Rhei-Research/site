---
{
  "projection_kind": "taulib_declaration",
  "title": "chandrasekhar_positive",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::chandrasekhar_positive",
  "declaration_slug": "chandrasekhar-positive",
  "kind": "theorem",
  "name": "chandrasekhar_positive",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 291,
  "source_line_end": 292,
  "registry_ids": [
    "V.T44"
  ],
  "related_registry_items": [
    {
      "id": "V.T44",
      "title": "Chandrasekhar limit",
      "url": "/registry/object/V.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L291-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L291-L292",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L291-L292)
- Source range: L291-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T44` — Chandrasekhar limit

## Immediate Comment / Docstring

```lean
/-- [V.T44] Chandrasekhar threshold is positive. -/
```

## Source Excerpt

```lean
theorem chandrasekhar_positive (c : ChandrasekharThreshold) :
    c.mass_numer > 0 := c.mass_positive
```
