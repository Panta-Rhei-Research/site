---
{
  "projection_kind": "taulib_declaration",
  "title": "NullIntertwinerField",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/null-intertwiner-field/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::NullIntertwinerField",
  "declaration_slug": "null-intertwiner-field",
  "kind": "structure",
  "name": "NullIntertwinerField",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 75,
  "source_line_end": 86,
  "registry_ids": [
    "V.D47"
  ],
  "related_registry_items": [
    {
      "id": "V.D47",
      "title": "Null intertwiner",
      "url": "/registry/object/V.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L75-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L75-L86",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L75-L86)
- Source range: L75-L86
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D47` — Null intertwiner

## Immediate Comment / Docstring

```lean
/-- [V.D47] Null intertwiner in the gravitational field context.

    Restated from V.D27 with emphasis on the light-cone boundary
    that defines Lorentz structure.

    Properties:
    - Massless (zero fiber stiffness on T²)
    - Propagates at c_τ (speed of light = null transport rate)
    - Selects B-sector (EM) uniquely
    - Defines the null set for chart readout -/
```

## Source Excerpt

```lean
structure NullIntertwinerField where
  /-- The sector (must be B = EM). -/
  sector : Sector
  /-- Null selects EM. -/
  sector_is_em : sector = .B
  /-- Massless flag. -/
  massless : Bool
  /-- Must be massless. -/
  massless_true : massless = true
  /-- Speed is c (light speed, in natural units = 1). -/
  speed_is_c : Bool := true
  deriving Repr
```
