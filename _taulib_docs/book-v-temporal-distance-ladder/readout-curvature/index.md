---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutCurvature",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/readout-curvature/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::ReadoutCurvature",
  "declaration_slug": "readout-curvature",
  "kind": "structure",
  "name": "ReadoutCurvature",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 188,
  "source_line_end": 201,
  "registry_ids": [
    "V.D35"
  ],
  "related_registry_items": [
    {
      "id": "V.D35",
      "title": "Readout curvature",
      "url": "/registry/object/V.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L188-L201",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L188-L201",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/verify/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L188-L201)
- Source range: L188-L201
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D35` — Readout curvature

## Immediate Comment / Docstring

```lean
/-- [V.D35] Readout curvature κ_R(n) := d²R_d/dn².

    The second derivative of the distance readout functor with respect
    to orbit depth. When κ_R(n) ≠ 0, equal orbit-depth intervals map
    to unequal SI-length intervals.

    Scope: conjectural (explicit form deferred to Part V). -/
```

## Source Excerpt

```lean
structure ReadoutCurvature where
  /-- Orbit depth at which curvature is evaluated. -/
  depth : Nat
  /-- Curvature numerator (may be zero). -/
  curvature_numer : Nat
  /-- Curvature denominator. -/
  curvature_denom : Nat
  /-- Denominator positive. -/
  denom_pos : curvature_denom > 0
  /-- Whether the curvature is positive at this depth. -/
  is_positive : Bool
  /-- Scope: conjectural until Part V. -/
  scope : String := "conjectural"
  deriving Repr
```
