---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_swaps_sectors",
  "permalink": "/corpus/taulib/docs/book-i-polarity-lemniscate/canonical-swaps-sectors/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::canonical_swaps_sectors",
  "declaration_slug": "canonical-swaps-sectors",
  "kind": "theorem",
  "name": "canonical_swaps_sectors",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/corpus/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 83,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L83-L86",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Lemniscate",
        "url": "/corpus/taulib/docs/book-i-polarity-lemniscate/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L83-L86",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.Lemniscate](/corpus/taulib/docs/book-i-polarity-lemniscate/)
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L83-L86)
- Source range: L83-L86
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical involution swaps sectors. -/
```

## Source Excerpt

```lean
theorem canonical_swaps_sectors (z : SplitComplex) :
    to_sectors (canonical_lemniscate.involution z) =
    ⟨(to_sectors z).c_sector, (to_sectors z).b_sector⟩ :=
  polarity_inv_swaps_sectors z
```
