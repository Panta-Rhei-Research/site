---
{
  "projection_kind": "taulib_declaration",
  "title": "interior_ew_stable",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/interior-ew-stable/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::interior_ew_stable",
  "declaration_slug": "interior-ew-stable",
  "kind": "theorem",
  "name": "interior_ew_stable",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 287,
  "source_line_end": 288,
  "registry_ids": [
    "V.T43"
  ],
  "related_registry_items": [
    {
      "id": "V.T43",
      "title": "Neutron node EW stability",
      "url": "/registry/object/V.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L287-L288",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L287-L288",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L287-L288)
- Source range: L287-L288
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T43` — Neutron node EW stability

## Immediate Comment / Docstring

```lean
/-- [V.T43] Interior neutron nodes are EW-stable. -/
```

## Source Excerpt

```lean
theorem interior_ew_stable (ew : EWStability) :
    ew.node.is_ew_stable = true := ew.passes
```
