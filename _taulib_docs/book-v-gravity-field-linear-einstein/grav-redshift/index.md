---
{
  "projection_kind": "taulib_declaration",
  "title": "grav_redshift",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/grav-redshift/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::grav_redshift",
  "declaration_slug": "grav-redshift",
  "kind": "theorem",
  "name": "grav_redshift",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 258,
  "source_line_end": 259,
  "registry_ids": [
    "V.T31"
  ],
  "related_registry_items": [
    {
      "id": "V.T31",
      "title": "Gravitational redshift from tau-Einstein",
      "url": "/registry/object/V.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L258-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L258-L259",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L258-L259)
- Source range: L258-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T31` — Gravitational redshift from tau-Einstein

## Immediate Comment / Docstring

```lean
/-- [V.T31] Gravitational redshift: Δf/f = GM/(rc²).

    A null intertwiner (photon) climbing out of a gravitational
    potential well loses energy, shifting to lower frequency.
    The fractional frequency shift equals GM/(rc²). -/
```

## Source Excerpt

```lean
theorem grav_redshift :
    grav_redshift_value.name = "Gravitational redshift" := by rfl
```
