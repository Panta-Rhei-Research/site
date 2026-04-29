---
{
  "projection_kind": "taulib_declaration",
  "title": "FieldGravConstant",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-grav-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::FieldGravConstant",
  "declaration_slug": "field-grav-constant",
  "kind": "structure",
  "name": "FieldGravConstant",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 86,
  "source_line_end": 91,
  "registry_ids": [
    "V.D62"
  ],
  "related_registry_items": [
    {
      "id": "V.D62",
      "title": "Gravitational constant --- V.D02",
      "url": "/registry/object/V.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L86-L91",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L86-L91",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L86-L91)
- Source range: L86-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D62` — Gravitational constant --- V.D02

## Immediate Comment / Docstring

```lean
/-- [V.D62] Gravitational constant restated for the field context.

    Wraps `GravConstant` (V.D02) with a scope tag indicating
    this is a derived quantity (not postulated). -/
```

## Source Excerpt

```lean
structure FieldGravConstant where
  /-- The underlying gravitational constant. -/
  g_tau : GravConstant
  /-- Scope: always tau-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
