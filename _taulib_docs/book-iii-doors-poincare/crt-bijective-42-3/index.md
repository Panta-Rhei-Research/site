---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_bijective_42_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/crt-bijective-42-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::crt_bijective_42_3",
  "declaration_slug": "crt-bijective-42-3",
  "kind": "theorem",
  "name": "crt_bijective_42_3",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 175,
  "source_line_end": 177,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L175-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L175-L177",
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
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L175-L177)
- Source range: L175-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D35` — Simply Connected in Category τ

## Immediate Comment / Docstring

```lean
/-- [III.D35] Structural: CRT is bijective at depth 3
    (simple connectivity = no monodromy). -/
```

## Source Excerpt

```lean
theorem crt_bijective_42_3 :
    crt_reconstruct (crt_decompose 42 3) 3 = 42 % primorial 3 := by
  native_decide
```
