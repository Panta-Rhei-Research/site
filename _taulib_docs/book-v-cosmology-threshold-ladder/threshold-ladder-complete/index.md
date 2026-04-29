---
{
  "projection_kind": "taulib_declaration",
  "title": "ThresholdLadderComplete",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-ladder-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::ThresholdLadderComplete",
  "declaration_slug": "threshold-ladder-complete",
  "kind": "structure",
  "name": "ThresholdLadderComplete",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 301,
  "source_line_end": 308,
  "registry_ids": [
    "V.D162"
  ],
  "related_registry_items": [
    {
      "id": "V.D162",
      "title": "Threshold Ladder",
      "url": "/registry/object/V.D162/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L301-L308",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L301-L308",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L301-L308)
- Source range: L301-L308
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D162` — Threshold Ladder

## Immediate Comment / Docstring

```lean
/-- [V.D162] Threshold ladder: the complete ordered sequence of
    canonical thresholds. Six thresholds, monotonically ordered. -/
```

## Source Excerpt

```lean
structure ThresholdLadderComplete where
  /-- The canonical ladder. -/
  ladder : CanonicalThresholds
  /-- Number of thresholds. -/
  count : Nat
  /-- Count is 6. -/
  count_is_six : count = 6
  deriving Repr
```
