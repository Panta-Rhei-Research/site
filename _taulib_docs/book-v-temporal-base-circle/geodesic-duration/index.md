---
{
  "projection_kind": "taulib_declaration",
  "title": "GeodesicDuration",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/geodesic-duration/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::GeodesicDuration",
  "declaration_slug": "geodesic-duration",
  "kind": "structure",
  "name": "GeodesicDuration",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 232,
  "source_line_end": 239,
  "registry_ids": [
    "V.D19"
  ],
  "related_registry_items": [
    {
      "id": "V.D19",
      "title": "Geodesic Duration",
      "url": "/registry/object/V.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L232-L239",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BaseCircle",
        "url": "/verify/taulib/docs/book-v-temporal-base-circle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L232-L239",
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

- Module: [TauLib.BookV.Temporal.BaseCircle](/verify/taulib/docs/book-v-temporal-base-circle/)
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L232-L239)
- Source range: L232-L239
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D19` — Geodesic Duration

## Immediate Comment / Docstring

```lean
/-- [V.D19] Geodesic duration between two proto-time events: the
    number of alpha-ticks separating them.

    This is the structural (pre-metric) distance on τ¹. The physical
    proper time requires weighting each tick by the depth-dependent
    arc-length contribution. -/
```

## Source Excerpt

```lean
structure GeodesicDuration where
  /-- Start event. -/
  start : ProtoTime
  /-- End event. -/
  stop : ProtoTime
  /-- End is after start. -/
  causal : start.tick < stop.tick
  deriving Repr
```
