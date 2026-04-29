---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_mode_count",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-mode-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::strong_mode_count",
  "declaration_slug": "strong-mode-count",
  "kind": "theorem",
  "name": "strong_mode_count",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 105,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L105-L105",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L105-L105",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L105-L105)
- Source range: L105-L105
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strong count = 3 (η×3). -/
```

## Source Excerpt

```lean
theorem strong_mode_count : strongModes.length = 3 := by native_decide
```
