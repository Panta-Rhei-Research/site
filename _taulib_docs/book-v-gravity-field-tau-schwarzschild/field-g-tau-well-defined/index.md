---
{
  "projection_kind": "taulib_declaration",
  "title": "field_g_tau_well_defined",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-g-tau-well-defined/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::field_g_tau_well_defined",
  "declaration_slug": "field-g-tau-well-defined",
  "kind": "theorem",
  "name": "field_g_tau_well_defined",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 94,
  "source_line_end": 96,
  "registry_ids": [
    "V.P17"
  ],
  "related_registry_items": [
    {
      "id": "V.P17",
      "title": "G_tau well-defined --- V.P01",
      "url": "/registry/object/V.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L94-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L94-L96",
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
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L94-L96)
- Source range: L94-L96
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P17` — G_tau well-defined --- V.P01

## Immediate Comment / Docstring

```lean
/-- [V.P17] G_tau is well-defined in the field context. -/
```

## Source Excerpt

```lean
theorem field_g_tau_well_defined (fg : FieldGravConstant) :
    fg.g_tau.g_numer > 0 ∧ fg.g_tau.g_denom > 0 :=
  ⟨fg.g_tau.g_positive, fg.g_tau.denom_pos⟩
```
