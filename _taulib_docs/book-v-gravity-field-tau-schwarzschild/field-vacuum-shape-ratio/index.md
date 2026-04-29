---
{
  "projection_kind": "taulib_declaration",
  "title": "field_vacuum_shape_ratio",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-vacuum-shape-ratio/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::field_vacuum_shape_ratio",
  "declaration_slug": "field-vacuum-shape-ratio",
  "kind": "theorem",
  "name": "field_vacuum_shape_ratio",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 182,
  "source_line_end": 185,
  "registry_ids": [
    "V.T38"
  ],
  "related_registry_items": [
    {
      "id": "V.T38",
      "title": "Vacuum shape ratio --- V.T01",
      "url": "/registry/object/V.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L182-L185",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L182-L185",
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
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L182-L185)
- Source range: L182-L185
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T38` — Vacuum shape ratio --- V.T01

## Immediate Comment / Docstring

```lean
/-- [V.T38] The field torus vacuum inherits the shape ratio r/R = iota_tau. -/
```

## Source Excerpt

```lean
theorem field_vacuum_shape_ratio (fv : FieldTorusVacuum) :
    fv.vacuum.minor_numer * fv.vacuum.major_denom * iotaD =
    iota * fv.vacuum.minor_denom * fv.vacuum.major_numer :=
  fv.vacuum.shape_ratio
```
