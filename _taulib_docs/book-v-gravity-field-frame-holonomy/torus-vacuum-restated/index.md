---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusVacuumRestated",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/torus-vacuum-restated/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::TorusVacuumRestated",
  "declaration_slug": "torus-vacuum-restated",
  "kind": "structure",
  "name": "TorusVacuumRestated",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 163,
  "source_line_end": 169,
  "registry_ids": [
    "V.D44"
  ],
  "related_registry_items": [
    {
      "id": "V.D44",
      "title": "Torus vacuum --- V.D01",
      "url": "/registry/object/V.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L163-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L163-L169",
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L163-L169)
- Source range: L163-L169
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D44` — Torus vacuum --- V.D01

## Immediate Comment / Docstring

```lean
/-- [V.D44] Torus vacuum restated in the gravitational field context.

    The torus vacuum from ch16 (V.D01) is restated here to emphasize
    that the shape ratio r/R = ι_τ determines the gravitational
    coupling strength.

    This is a lightweight wrapper referencing the original TorusVacuum. -/
```

## Source Excerpt

```lean
structure TorusVacuumRestated where
  /-- The underlying torus vacuum. -/
  vacuum : TorusVacuum
  /-- Shape ratio confirmed. -/
  shape_confirmed : vacuum.minor_numer * vacuum.major_denom * iotaD =
                    iota * vacuum.minor_denom * vacuum.major_numer
  deriving Repr
```
