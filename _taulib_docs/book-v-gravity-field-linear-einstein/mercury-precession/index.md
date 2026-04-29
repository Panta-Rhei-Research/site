---
{
  "projection_kind": "taulib_declaration",
  "title": "mercury_precession",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/mercury-precession/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::mercury_precession",
  "declaration_slug": "mercury-precession",
  "kind": "theorem",
  "name": "mercury_precession",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 230,
  "source_line_end": 233,
  "registry_ids": [
    "V.T29"
  ],
  "related_registry_items": [
    {
      "id": "V.T29",
      "title": "Mercury precession from tau-Einstein",
      "url": "/registry/object/V.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L230-L233",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L230-L233",
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
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L230-L233)
- Source range: L230-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T29` — Mercury precession from tau-Einstein

## Immediate Comment / Docstring

```lean
/-- [V.T29] Mercury perihelion precession: 43 arcsec/century.

    The anomalous perihelion advance of Mercury is predicted by the
    first post-Newtonian correction from the linearized τ-Einstein
    equation. The value matches GR exactly (same equation under
    chart readout). No free parameters. -/
```

## Source Excerpt

```lean
theorem mercury_precession :
    mercury_precession_value.value_numer = 43 ∧
    mercury_precession_value.value_denom = 1 := by
  exact ⟨rfl, rfl⟩
```
