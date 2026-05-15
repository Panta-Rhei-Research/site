---
{
  "projection_kind": "taulib_declaration",
  "title": "GRTensionFunctional",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/grtension-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::GRTensionFunctional",
  "declaration_slug": "grtension-functional",
  "kind": "structure",
  "name": "GRTensionFunctional",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 112,
  "source_line_end": 121,
  "registry_ids": [
    "V.D68"
  ],
  "related_registry_items": [
    {
      "id": "V.D68",
      "title": "GR tension functional",
      "url": "/registry/object/V.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L112-L121",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L112-L121",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L112-L121)
- Source range: L112-L121
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D68` — GR tension functional

## Immediate Comment / Docstring

```lean
/-- [V.D68] GR tension functional T[phi]: the total gravitational
    energy cost of a given field configuration phi.

    T[phi] = integral of (gravitational + matter) energy density
    over the carrier volume.

    The TOV equilibrium minimizes T[phi] subject to constraints. -/
```

## Source Excerpt

```lean
structure GRTensionFunctional where
  /-- Tension value numerator (scaled). -/
  tension_numer : Nat
  /-- Tension value denominator. -/
  tension_denom : Nat
  /-- Denominator positive. -/
  denom_pos : tension_denom > 0
  /-- Whether the tension is at a local minimum. -/
  is_extremal : Bool
  deriving Repr
```
