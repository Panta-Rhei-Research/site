---
{
  "projection_kind": "taulib_declaration",
  "title": "silent_count_structural",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-count-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::silent_count_structural",
  "declaration_slug": "silent-count-structural",
  "kind": "theorem",
  "name": "silent_count_structural",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 244,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L244-L245",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L244-L245",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L244-L245)
- Source range: L244-L245
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The silent count equals p + 1 = 4 (structural). -/
```

## Source Excerpt

```lean
theorem silent_count_structural :
    silentModesStructural.length = 3 + 1 := by native_decide
```
