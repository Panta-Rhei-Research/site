---
{
  "projection_kind": "taulib_declaration",
  "title": "terminal_depth_1",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/terminal-depth-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::terminal_depth_1",
  "declaration_slug": "terminal-depth-1",
  "kind": "theorem",
  "name": "terminal_depth_1",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 180,
  "source_line_end": 181,
  "registry_ids": [
    "III.D35"
  ],
  "related_registry_items": [
    {
      "id": "III.D35",
      "title": "Simply Connected in Category τ",
      "url": "/registry/object/III.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L180-L181",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.Poincare",
        "url": "/verify/taulib/docs/book-iii-doors-poincare/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L180-L181",
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

- Module: [TauLib.BookIII.Doors.Poincare](/verify/taulib/docs/book-iii-doors-poincare/)
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L180-L181)
- Source range: L180-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D35` — Simply Connected in Category τ

## Immediate Comment / Docstring

```lean
/-- [III.D35] Structural: terminal object at depth 1 (only mod 2). -/
```

## Source Excerpt

```lean
theorem terminal_depth_1 :
    simply_connected_check 10 1 = true := by native_decide
```
