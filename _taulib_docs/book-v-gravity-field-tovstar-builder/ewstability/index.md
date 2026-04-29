---
{
  "projection_kind": "taulib_declaration",
  "title": "EWStability",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/ewstability/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::EWStability",
  "declaration_slug": "ewstability",
  "kind": "structure",
  "name": "EWStability",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 230,
  "source_line_end": 241,
  "registry_ids": [
    "V.D73"
  ],
  "related_registry_items": [
    {
      "id": "V.D73",
      "title": "EW-stable node",
      "url": "/registry/object/V.D73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L230-L241",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L230-L241",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L230-L241)
- Source range: L230-L241
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D73` — EW-stable node

## Immediate Comment / Docstring

```lean
/-- [V.D73] Electroweak stability condition: a neutron node is
    EW-stable if the weak sector coupling kappa(A) provides
    sufficient binding to prevent beta decay.

    Interior nodes in a neutron star satisfy this condition
    due to Pauli blocking and dense nuclear environment. -/
```

## Source Excerpt

```lean
structure EWStability where
  /-- The node being tested. -/
  node : NeutronNode
  /-- EW coupling threshold numerator. -/
  threshold_numer : Nat
  /-- EW coupling threshold denominator. -/
  threshold_denom : Nat
  /-- Denominator positive. -/
  denom_pos : threshold_denom > 0
  /-- The node passes EW stability. -/
  passes : node.is_ew_stable = true
  deriving Repr
```
