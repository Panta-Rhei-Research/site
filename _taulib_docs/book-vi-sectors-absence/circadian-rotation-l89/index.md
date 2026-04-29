---
{
  "projection_kind": "taulib_declaration",
  "title": "circadian_rotation",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/circadian-rotation-l89/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::circadian_rotation",
  "declaration_slug": "circadian-rotation-l89",
  "kind": "theorem",
  "name": "circadian_rotation",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 89,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L89-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L89-L94",
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
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L89-L94)
- Source range: L89-L94
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
theorem circadian_rotation :
    circadian.period_hours = 24 ∧
    circadian.winding_number = 1 :=
  ⟨rfl, rfl⟩

end Tau.BookVI.Absence
```
