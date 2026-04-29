---
{
  "projection_kind": "taulib_declaration",
  "title": "pvsnp_triple_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/pvsnp-triple-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::pvsnp_triple_3",
  "declaration_slug": "pvsnp-triple-3",
  "kind": "theorem",
  "name": "pvsnp_triple_3",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 272,
  "source_line_end": 273,
  "registry_ids": [
    "III.T63"
  ],
  "related_registry_items": [
    {
      "id": "III.T63",
      "title": "P vs NP Forbidden Triple",
      "url": "/registry/object/III.T63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L272-L273",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L272-L273",
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
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L272-L273)
- Source range: L272-L273
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T63` — P vs NP Forbidden Triple

## Immediate Comment / Docstring

```lean
/-- [III.T63] P vs NP forbidden triple at depth 3. -/
```

## Source Excerpt

```lean
theorem pvsnp_triple_3 :
    pvsnp_forbidden_triple_check 3 = true := by native_decide
```
