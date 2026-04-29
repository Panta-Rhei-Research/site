---
{
  "projection_kind": "taulib_declaration",
  "title": "GeodesicDuration.tick_count",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/tick-count/",
  "summary_short": "`def` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::GeodesicDuration.tick_count",
  "declaration_slug": "tick-count",
  "kind": "def",
  "name": "GeodesicDuration.tick_count",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 242,
  "source_line_end": 243,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L242-L243",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L242-L243",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L242-L243)
- Source range: L242-L243
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Number of ticks in the geodesic duration. -/
```

## Source Excerpt

```lean
def GeodesicDuration.tick_count (g : GeodesicDuration) : Nat :=
  g.stop.tick - g.start.tick
```
