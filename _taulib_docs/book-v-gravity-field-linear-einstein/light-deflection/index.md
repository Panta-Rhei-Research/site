---
{
  "projection_kind": "taulib_declaration",
  "title": "light_deflection",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/light-deflection/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::light_deflection",
  "declaration_slug": "light-deflection",
  "kind": "theorem",
  "name": "light_deflection",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 244,
  "source_line_end": 247,
  "registry_ids": [
    "V.T30"
  ],
  "related_registry_items": [
    {
      "id": "V.T30",
      "title": "Light deflection from tau-Einstein",
      "url": "/registry/object/V.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L244-L247",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L244-L247",
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
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L244-L247)
- Source range: L244-L247
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T30` — Light deflection from tau-Einstein

## Immediate Comment / Docstring

```lean
/-- [V.T30] Light deflection: 1.75 arcsec at the solar limb.

    A null intertwiner (photon) passing near a massive body is
    deflected by the curvature character. The deflection angle
    at the solar limb is 1.75 arcsec (= 4GM/(rc²)). -/
```

## Source Excerpt

```lean
theorem light_deflection :
    light_deflection_value.value_numer = 175 ∧
    light_deflection_value.value_denom = 100 := by
  exact ⟨rfl, rfl⟩
```
