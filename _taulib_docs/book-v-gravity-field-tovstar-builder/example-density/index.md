---
{
  "projection_kind": "taulib_declaration",
  "title": "example_density",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/example-density/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::example_density",
  "declaration_slug": "example-density",
  "kind": "def",
  "name": "example_density",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 347,
  "source_line_end": 350,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L347-L350",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L347-L350",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L347-L350)
- Source range: L347-L350
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example node density. -/
```

## Source Excerpt

```lean
def example_density : NodeDensity where
  numer := 1000
  denom := 1
  denom_pos := by omega
```
