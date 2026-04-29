---
{
  "projection_kind": "taulib_declaration",
  "title": "metric_inequality_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-abcd/metric-inequality-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::metric_inequality_check",
  "declaration_slug": "metric-inequality-check",
  "kind": "def",
  "name": "metric_inequality_check",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/verify/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [
    "I.P09"
  ],
  "related_registry_items": [
    {
      "id": "I.P09",
      "title": "Metric Inequality",
      "url": "/registry/object/I.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L111-L112",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/verify/taulib/docs/book-i-coordinates-abcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L111-L112",
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

- Module: [TauLib.BookI.Coordinates.ABCD](/verify/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L111-L112)
- Source range: L111-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P09` — Metric Inequality

## Immediate Comment / Docstring

```lean
/-- [I.P09] Check: spine_length ≤ dag_size ≤ occ_size. -/
```

## Source Excerpt

```lean
def metric_inequality_check (x : TauIdx) : Bool :=
  spine_length x ≤ dag_size x && dag_size x ≤ occ_size x
```
