---
{
  "projection_kind": "taulib_declaration",
  "title": "motility_all_hold",
  "permalink": "/verify/taulib/docs/book-vi-agency-agency-sector/motility-all-hold/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::motility_all_hold",
  "declaration_slug": "motility-all-hold",
  "kind": "theorem",
  "name": "motility_all_hold",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/verify/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 88,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L88-L92",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/verify/taulib/docs/book-vi-agency-agency-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L88-L92",
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

- Module: [TauLib.BookVI.Agency.AgencySector](/verify/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L88-L92)
- Source range: L88-L92
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
theorem motility_all_hold :
    spatial_motility.base_displacement = true ∧
    spatial_motility.distinction_preserving = true ∧
    spatial_motility.energy_bounded = true :=
  ⟨rfl, rfl, rfl⟩
```
