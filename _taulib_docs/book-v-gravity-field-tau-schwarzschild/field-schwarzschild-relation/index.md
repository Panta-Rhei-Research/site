---
{
  "projection_kind": "taulib_declaration",
  "title": "field_schwarzschild_relation",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-schwarzschild-relation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::field_schwarzschild_relation",
  "declaration_slug": "field-schwarzschild-relation",
  "kind": "theorem",
  "name": "field_schwarzschild_relation",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 193,
  "source_line_end": 196,
  "registry_ids": [
    "V.T40"
  ],
  "related_registry_items": [
    {
      "id": "V.T40",
      "title": "The tau-Schwarzschild relation --- V.D08",
      "url": "/registry/object/V.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L193-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L193-L196",
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
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L193-L196)
- Source range: L193-L196
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T40` — The tau-Schwarzschild relation --- V.D08

## Immediate Comment / Docstring

```lean
/-- [V.T40] The Schwarzschild relation R = 2 G_tau M (structural). -/
```

## Source Excerpt

```lean
theorem field_schwarzschild_relation (s : SchwarzschildRelation) :
    s.radius_numer * s.mass.mass_denom * s.g_tau.g_denom =
    2 * s.g_tau.g_numer * s.mass.mass_numer * s.radius_denom :=
  s.schwarzschild_identity
```
