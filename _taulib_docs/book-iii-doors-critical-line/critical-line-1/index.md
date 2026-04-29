---
{
  "projection_kind": "taulib_declaration",
  "title": "critical_line_1",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/critical-line-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::critical_line_1",
  "declaration_slug": "critical-line-1",
  "kind": "theorem",
  "name": "critical_line_1",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 189,
  "source_line_end": 190,
  "registry_ids": [
    "III.T19"
  ],
  "related_registry_items": [
    {
      "id": "III.T19",
      "title": "Critical Line Theorem",
      "url": "/registry/object/III.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L189-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.CriticalLine",
        "url": "/verify/taulib/docs/book-iii-doors-critical-line/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L189-L190",
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

- Module: [TauLib.BookIII.Doors.CriticalLine](/verify/taulib/docs/book-iii-doors-critical-line/)
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L189-L190)
- Source range: L189-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T19` — Critical Line Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T19] Structural: critical line at depth 1 (only prime 2). -/
```

## Source Excerpt

```lean
theorem critical_line_1 :
    critical_line_check 1 = true := by native_decide
```
