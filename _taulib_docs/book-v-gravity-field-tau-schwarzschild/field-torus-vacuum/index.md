---
{
  "projection_kind": "taulib_declaration",
  "title": "FieldTorusVacuum",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-torus-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::FieldTorusVacuum",
  "declaration_slug": "field-torus-vacuum",
  "kind": "structure",
  "name": "FieldTorusVacuum",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 65,
  "source_line_end": 72,
  "registry_ids": [
    "V.D61"
  ],
  "related_registry_items": [
    {
      "id": "V.D61",
      "title": "Torus vacuum --- V.D01",
      "url": "/registry/object/V.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L65-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L65-L72",
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
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L65-L72)
- Source range: L65-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D61` — Torus vacuum --- V.D01

## Immediate Comment / Docstring

```lean
/-- [V.D61] Torus vacuum in the gravitational field context.

    Restates the torus vacuum (V.D01) with additional field-theoretic
    data: regularity flag (no singularity at the core), and whether
    the vacuum has achieved full refinement stability. -/
```

## Source Excerpt

```lean
structure FieldTorusVacuum where
  /-- The underlying torus vacuum. -/
  vacuum : TorusVacuum
  /-- Whether the vacuum is regular (no singularity). -/
  is_regular : Bool
  /-- Whether full refinement stability has been reached. -/
  is_stable : Bool
  deriving Repr
```
