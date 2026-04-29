---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_gap_growth_4",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/ym-gap-growth-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::ym_gap_growth_4",
  "declaration_slug": "ym-gap-growth-4",
  "kind": "theorem",
  "name": "ym_gap_growth_4",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 264,
  "source_line_end": 265,
  "registry_ids": [
    "III.D94"
  ],
  "related_registry_items": [
    {
      "id": "III.D94",
      "title": "YM Mass Gap Persistence",
      "url": "/registry/object/III.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L264-L265",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L264-L265",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L264-L265)
- Source range: L264-L265
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D94` — YM Mass Gap Persistence

## Immediate Comment / Docstring

```lean
/-- [III.D94] YM gap growth at depth 4. -/
```

## Source Excerpt

```lean
theorem ym_gap_growth_4 :
    ym_gap_growth_check 4 = true := by native_decide
```
