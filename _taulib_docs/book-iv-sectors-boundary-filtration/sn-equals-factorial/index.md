---
{
  "projection_kind": "taulib_declaration",
  "title": "sn_equals_factorial",
  "permalink": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/sn-equals-factorial/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::sn_equals_factorial",
  "declaration_slug": "sn-equals-factorial",
  "kind": "theorem",
  "name": "sn_equals_factorial",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 248,
  "source_line_end": 249,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L248-L249",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L248-L249",
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/verify/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L248-L249)
- Source range: L248-L249
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- s·n = q! (specific to (3,5)): 8·15 = 120 = 5!. -/
```

## Source Excerpt

```lean
theorem sn_equals_factorial :
    (8 : Nat) * 15 = 1 * 2 * 3 * 4 * 5 := by omega
```
