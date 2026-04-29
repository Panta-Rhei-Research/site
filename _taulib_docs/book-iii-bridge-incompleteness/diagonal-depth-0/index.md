---
{
  "projection_kind": "taulib_declaration",
  "title": "diagonal_depth_0",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/diagonal-depth-0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::diagonal_depth_0",
  "declaration_slug": "diagonal-depth-0",
  "kind": "theorem",
  "name": "diagonal_depth_0",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 254,
  "source_line_end": 255,
  "registry_ids": [
    "III.T44"
  ],
  "related_registry_items": [
    {
      "id": "III.T44",
      "title": "Incompleteness as VM Boundary",
      "url": "/registry/object/III.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L254-L255",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.Incompleteness",
        "url": "/verify/taulib/docs/book-iii-bridge-incompleteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L254-L255",
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

- Module: [TauLib.BookIII.Bridge.Incompleteness](/verify/taulib/docs/book-iii-bridge-incompleteness/)
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L254-L255)
- Source range: L254-L255
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] Structural: diagonal at depth 0 is 0 (Prim(0)=1). -/
```

## Source Excerpt

```lean
theorem diagonal_depth_0 :
    diagonal 42 0 = 0 := by native_decide
```
