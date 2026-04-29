---
{
  "projection_kind": "taulib_declaration",
  "title": "DistanceReadout",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::DistanceReadout",
  "declaration_slug": "distance-readout",
  "kind": "structure",
  "name": "DistanceReadout",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 78,
  "source_line_end": 91,
  "registry_ids": [
    "V.D32"
  ],
  "related_registry_items": [
    {
      "id": "V.D32",
      "title": "Distance readout functor",
      "url": "/registry/object/V.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L78-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L78-L91",
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L78-L91)
- Source range: L78-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D32` — Distance readout functor

## Immediate Comment / Docstring

```lean
/-- [V.D32] Distance readout functor R_d: maps a pair of orbit depths
    (source, target) to a luminosity distance in SI metres.

    The readout is a projection through sector couplings and the
    calibration anchor, not a "true" physical distance.

    Fields:
    - source/target depths on τ¹
    - distance numerator/denominator (scaled SI metres)
    - source must causally precede target -/
```

## Source Excerpt

```lean
structure DistanceReadout where
  /-- Source orbit depth (emission). -/
  source_depth : Nat
  /-- Target orbit depth (observation). -/
  target_depth : Nat
  /-- Distance numerator (scaled SI metres). -/
  distance_numer : Nat
  /-- Distance denominator. -/
  distance_denom : Nat
  /-- Denominator positive. -/
  denom_pos : distance_denom > 0
  /-- Source causally precedes target. -/
  causal_order : source_depth < target_depth
  deriving Repr
```
