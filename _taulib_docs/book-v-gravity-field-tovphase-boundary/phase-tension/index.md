---
{
  "projection_kind": "taulib_declaration",
  "title": "PhaseTension",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/phase-tension/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::PhaseTension",
  "declaration_slug": "phase-tension",
  "kind": "structure",
  "name": "PhaseTension",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 66,
  "source_line_end": 81,
  "registry_ids": [
    "V.D75"
  ],
  "related_registry_items": [
    {
      "id": "V.D75",
      "title": "GR Tension Functional",
      "url": "/registry/object/V.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L66-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L66-L81",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L66-L81)
- Source range: L66-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D75` — GR Tension Functional

## Immediate Comment / Docstring

```lean
/-- [V.D75] GR tension functional at the phase boundary.

    The tension functional evaluates the total gravitational +
    matter energy cost on each topology branch (S^2 vs T^2).
    At the phase boundary, the two branches have equal tension. -/
```

## Source Excerpt

```lean
structure PhaseTension where
  /-- Tension on the S^2 branch (neutron star). -/
  tension_s2_numer : Nat
  /-- Tension on the T^2 branch (torus vacuum). -/
  tension_t2_numer : Nat
  /-- Common denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Mass at which tensions are evaluated. -/
  mass_numer : Nat
  /-- Mass denominator. -/
  mass_denom : Nat
  /-- Mass denominator positive. -/
  mass_denom_pos : mass_denom > 0
  deriving Repr
```
