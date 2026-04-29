---
{
  "projection_kind": "taulib_declaration",
  "title": "BAOStandardRuler",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/baostandard-ruler/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::BAOStandardRuler",
  "declaration_slug": "baostandard-ruler",
  "kind": "structure",
  "name": "BAOStandardRuler",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 164,
  "source_line_end": 175,
  "registry_ids": [
    "V.D34"
  ],
  "related_registry_items": [
    {
      "id": "V.D34",
      "title": "BAO standard ruler",
      "url": "/registry/object/V.D34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L164-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L164-L175",
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L164-L175)
- Source range: L164-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D34` — BAO standard ruler

## Immediate Comment / Docstring

```lean
/-- [V.D34] BAO standard ruler: the comoving sound horizon at the
    recombination orbit depth n_rec.

    r_s(n_rec) = R_d[∫ c_s(n) dℓ/dn dn]

    Inputs (baryon-to-photon ratio, photon density, κ(D;1) = 1−ι_τ)
    are all derived from ι_τ. -/
```

## Source Excerpt

```lean
structure BAOStandardRuler where
  /-- Sound horizon numerator (comoving Mpc, scaled). -/
  sound_horizon_numer : Nat
  /-- Sound horizon denominator. -/
  sound_horizon_denom : Nat
  /-- Denominator positive. -/
  denom_pos : sound_horizon_denom > 0
  /-- Recombination depth at which the ruler is evaluated. -/
  recomb_depth : Nat
  /-- Recombination depth is positive. -/
  recomb_depth_pos : recomb_depth > 0
  deriving Repr
```
