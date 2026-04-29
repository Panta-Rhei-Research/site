---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_non_assoc",
  "permalink": "/verify/taulib/docs/book-i-orbit-saturation/tetration-non-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::tetration_non_assoc",
  "declaration_slug": "tetration-non-assoc",
  "kind": "theorem",
  "name": "tetration_non_assoc",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/verify/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 43,
  "source_line_end": 45,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L43-L45",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/verify/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L43-L45",
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

- Module: [TauLib.BookI.Orbit.Saturation](/verify/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L43-L45)
- Source range: L43-L45
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tetration is not associative:
    (2↑↑2)↑↑2 = 4↑↑2 = 256 ≠ 65536 = 2↑↑(2↑↑2) = 2↑↑4. -/
```

## Source Excerpt

```lean
theorem tetration_non_assoc :
    tetration (tetration 2 2) 2 ≠ tetration 2 (tetration 2 2) := by
  native_decide
```
