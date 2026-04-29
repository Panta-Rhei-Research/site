---
{
  "projection_kind": "taulib_declaration",
  "title": "ewActiveModes",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-active-modes/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::ewActiveModes",
  "declaration_slug": "ew-active-modes",
  "kind": "def",
  "name": "ewActiveModes",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 86,
  "source_line_end": 87,
  "registry_ids": [
    "IV.D336"
  ],
  "related_registry_items": [
    {
      "id": "IV.D336",
      "title": "EW 3-Way Partition",
      "url": "/registry/object/IV.D336/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L86-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L86-L87",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L86-L87)
- Source range: L86-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D336` — EW 3-Way Partition

## Immediate Comment / Docstring

```lean
/-- [IV.D336] EW-active modes on A_spec(L). -/
```

## Source Excerpt

```lean
def ewActiveModes : List BoundaryMode :=
  allModes.filter isEWActive
```
