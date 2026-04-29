---
{
  "projection_kind": "taulib_declaration",
  "title": "h7_kleene_rosser_at_N",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-circularity-full/h7-kleene-rosser-at-n/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7CircularityFull`.",
  "declaration_id": "TauLib.BookI.Topos.H7CircularityFull::h7_kleene_rosser_at_N",
  "declaration_slug": "h7-kleene-rosser-at-n",
  "kind": "theorem",
  "name": "h7_kleene_rosser_at_N",
  "module_name": "TauLib.BookI.Topos.H7CircularityFull",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/",
  "source_line_start": 205,
  "source_line_end": 207,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L205-L207",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7CircularityFull",
        "url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L205-L207",
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

- Module: [TauLib.BookI.Topos.H7CircularityFull](/verify/taulib/docs/book-i-topos-h7-circularity-full/)
- Source path: [`TauLib/BookI/Topos/H7CircularityFull.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L205-L207)
- Source range: L205-L207
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Kleene-Rosser template stabilises at N** (paper Thm
    `kleene-rosser`, this Wave). -/
```

## Source Excerpt

```lean
theorem h7_kleene_rosser_at_N :
    StabilisedValue kleeneRosserTemplate F N :=
  kleene_rosser_stabilises_at_N F
```
