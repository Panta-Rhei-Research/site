---
{
  "projection_kind": "taulib_declaration",
  "title": "distance_is_operational",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-is-operational/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::distance_is_operational",
  "declaration_slug": "distance-is-operational",
  "kind": "theorem",
  "name": "distance_is_operational",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 215,
  "source_line_end": 216,
  "registry_ids": [
    "V.R40"
  ],
  "related_registry_items": [
    {
      "id": "V.R40",
      "title": "Distance is operational",
      "url": "/registry/object/V.R40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L215-L216",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L215-L216",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L215-L216)
- Source range: L215-L216
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R40` — Distance is operational

## Immediate Comment / Docstring

```lean
/-- [V.R40] Distance is operational: every DistanceReadout requires
    a causal ordering (source < target). There is no "absolute distance"
    independent of the orbit-depth context. -/
```

## Source Excerpt

```lean
theorem distance_is_operational (d : DistanceReadout) :
    d.source_depth < d.target_depth := d.causal_order
```
