---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_rung_count",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/ladder-rung-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::ladder_rung_count",
  "declaration_slug": "ladder-rung-count",
  "kind": "theorem",
  "name": "ladder_rung_count",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 208,
  "source_line_end": 210,
  "registry_ids": [
    "V.T17"
  ],
  "related_registry_items": [
    {
      "id": "V.T17",
      "title": "Distance Ladder Translation",
      "url": "/registry/object/V.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L208-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L208-L210",
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L208-L210)
- Source range: L208-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T17` — Distance Ladder Translation

## Immediate Comment / Docstring

```lean
/-- [V.T17] Exactly 5 rungs on the distance ladder. -/
```

## Source Excerpt

```lean
theorem ladder_rung_count (r : DistanceLadderRung) :
    r = .Parallax ∨ r = .Cepheid ∨ r = .SNIa ∨ r = .BAO ∨ r = .CMB := by
  cases r <;> simp
```
