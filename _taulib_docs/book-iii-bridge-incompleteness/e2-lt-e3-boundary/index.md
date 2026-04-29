---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_lt_e3_boundary",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/e2-lt-e3-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::e2_lt_e3_boundary",
  "declaration_slug": "e2-lt-e3-boundary",
  "kind": "theorem",
  "name": "e2_lt_e3_boundary",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 280,
  "source_line_end": 281,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L280-L281",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L280-L281",
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
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L280-L281)
- Source range: L280-L281
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] Structural: E2 < E3 (the boundary is genuine). -/
```

## Source Excerpt

```lean
theorem e2_lt_e3_boundary :
    EnrLevel.lt .E2 .E3 = true := rfl
```
