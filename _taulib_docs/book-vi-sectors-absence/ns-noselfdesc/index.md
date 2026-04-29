---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_noselfdesc",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/ns-noselfdesc/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::ns_noselfdesc",
  "declaration_slug": "ns-noselfdesc",
  "kind": "theorem",
  "name": "ns_noselfdesc",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 63,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L63-L66",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Absence",
        "url": "/verify/taulib/docs/book-vi-sectors-absence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L63-L66",
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

- Module: [TauLib.BookVI.Sectors.Absence](/verify/taulib/docs/book-vi-sectors-absence/)
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L63-L66)
- Source range: L63-L66
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem ns_noselfdesc :
    ns_nosd.distinction_passed = 5 ∧
    ns_nosd.selfdesc_fails = true :=
  ⟨rfl, rfl⟩
```
