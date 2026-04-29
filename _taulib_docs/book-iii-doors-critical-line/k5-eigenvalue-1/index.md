---
{
  "projection_kind": "taulib_declaration",
  "title": "k5_eigenvalue_1",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/k5-eigenvalue-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::k5_eigenvalue_1",
  "declaration_slug": "k5-eigenvalue-1",
  "kind": "theorem",
  "name": "k5_eigenvalue_1",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 193,
  "source_line_end": 194,
  "registry_ids": [
    "III.P10"
  ],
  "related_registry_items": [
    {
      "id": "III.P10",
      "title": "K5 Off-Diagonal Exclusion",
      "url": "/registry/object/III.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L193-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L193-L194",
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
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L193-L194)
- Source range: L193-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P10` — K5 Off-Diagonal Exclusion

## Immediate Comment / Docstring

```lean
/-- [III.P10] Structural: eigenvalue of first mode equals 1. -/
```

## Source Excerpt

```lean
theorem k5_eigenvalue_1 :
    lemniscate_eigenvalue 1 = 1 := rfl
```
