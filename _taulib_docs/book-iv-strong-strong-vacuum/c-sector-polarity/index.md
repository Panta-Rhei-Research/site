---
{
  "projection_kind": "taulib_declaration",
  "title": "c_sector_polarity",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/c-sector-polarity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::c_sector_polarity",
  "declaration_slug": "c-sector-polarity",
  "kind": "theorem",
  "name": "c_sector_polarity",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 83,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L83-L83",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L83-L83",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L83-L83)
- Source range: L83-L83
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The C-sector is chi-minus dominant. -/
```

## Source Excerpt

```lean
theorem c_sector_polarity : c_sector_def.polarity = PolaritySign.ChiMinus := rfl
```
