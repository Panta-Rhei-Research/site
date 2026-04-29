---
{
  "projection_kind": "taulib_declaration",
  "title": "involution_swaps_lobes",
  "permalink": "/verify/taulib/docs/book-i-polarity-lemniscate/involution-swaps-lobes/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::involution_swaps_lobes",
  "declaration_slug": "involution-swaps-lobes",
  "kind": "theorem",
  "name": "involution_swaps_lobes",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/verify/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 93,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L93-L96",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Lemniscate",
        "url": "/verify/taulib/docs/book-i-polarity-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L93-L96",
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

- Module: [TauLib.BookI.Polarity.Lemniscate](/verify/taulib/docs/book-i-polarity-lemniscate/)
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L93-L96)
- Source range: L93-L96
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The involution swaps the lobes. -/
```

## Source Excerpt

```lean
theorem involution_swaps_lobes :
    to_sectors (polarity_inv ⟨1, 1⟩) =
    ⟨(to_sectors ⟨1, 1⟩).c_sector, (to_sectors ⟨1, 1⟩).b_sector⟩ :=
  polarity_inv_swaps_sectors ⟨1, 1⟩
```
