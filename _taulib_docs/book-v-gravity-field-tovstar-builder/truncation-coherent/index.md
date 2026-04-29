---
{
  "projection_kind": "taulib_declaration",
  "title": "truncation_coherent",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/truncation-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::truncation_coherent",
  "declaration_slug": "truncation-coherent",
  "kind": "theorem",
  "name": "truncation_coherent",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 312,
  "source_line_end": 313,
  "registry_ids": [
    "V.P21"
  ],
  "related_registry_items": [
    {
      "id": "V.P21",
      "title": "Truncation invariance of the star builder",
      "url": "/registry/object/V.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L312-L313",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L312-L313",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L312-L313)
- Source range: L312-L313
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P21` — Truncation invariance of the star builder

## Immediate Comment / Docstring

```lean
/-- [V.P21] Truncation coherence: truncating the star model at the
    surface (P = 0) gives a consistent interior. -/
```

## Source Excerpt

```lean
theorem truncation_coherent (tp : TensionProfile) (h : tp.surface_pressure_zero = true) :
    tp.surface_pressure_zero = true := h
```
