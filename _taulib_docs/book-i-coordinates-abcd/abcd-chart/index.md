---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_chart",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-abcd/abcd-chart/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::abcd_chart",
  "declaration_slug": "abcd-chart",
  "kind": "def",
  "name": "abcd_chart",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 41,
  "source_line_end": 41,
  "registry_ids": [
    "I.D17"
  ],
  "related_registry_items": [
    {
      "id": "I.D17",
      "title": "ABCD Coordinate Chart",
      "url": "/registry/object/I.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L41-L41",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/corpus/taulib/docs/book-i-coordinates-abcd/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L41-L41",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Coordinates.ABCD](/corpus/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L41-L41)
- Source range: L41-L41
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `I.D17` — ABCD Coordinate Chart

## Immediate Comment / Docstring

```lean
/-- [I.D17] ABCD coordinate chart: Φ(X) = (A, B, C, D). -/
```

## Source Excerpt

```lean
def abcd_chart (x : TauIdx) : TauIdx × TauIdx × TauIdx × TauIdx := greedy_peel x
```
