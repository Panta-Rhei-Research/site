---
{
  "projection_kind": "taulib_declaration",
  "title": "NodeDensity",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/node-density/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::NodeDensity",
  "declaration_slug": "node-density",
  "kind": "structure",
  "name": "NodeDensity",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 207,
  "source_line_end": 214,
  "registry_ids": [
    "V.D72"
  ],
  "related_registry_items": [
    {
      "id": "V.D72",
      "title": "Node density and confinement tension",
      "url": "/registry/object/V.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L207-L214",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L207-L214",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L207-L214)
- Source range: L207-L214
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D72` — Node density and confinement tension

## Immediate Comment / Docstring

```lean
/-- [V.D72] Node density: number of neutron nodes per unit volume. -/
```

## Source Excerpt

```lean
structure NodeDensity where
  /-- Density numerator. -/
  numer : Nat
  /-- Density denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  deriving Repr
```
