---
{
  "projection_kind": "taulib_declaration",
  "title": "field_no_shrink",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-no-shrink/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::field_no_shrink",
  "declaration_slug": "field-no-shrink",
  "kind": "theorem",
  "name": "field_no_shrink",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 199,
  "source_line_end": 200,
  "registry_ids": [
    "V.T41"
  ],
  "related_registry_items": [
    {
      "id": "V.T41",
      "title": "No-Shrink --- V.T03, preview",
      "url": "/registry/object/V.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L199-L200",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L199-L200",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L199-L200)
- Source range: L199-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T41` — No-Shrink --- V.T03, preview

## Immediate Comment / Docstring

```lean
/-- [V.T41] No-Shrink theorem: mature BH mass cannot decrease. -/
```

## Source Excerpt

```lean
theorem field_no_shrink (p : NoShrinkProperty) :
    p.mass.is_mature = true := p.mature_proof
```
