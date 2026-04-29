---
{
  "projection_kind": "taulib_declaration",
  "title": "ncg_spectral_triple",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/ncg-spectral-triple/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::ncg_spectral_triple",
  "declaration_slug": "ncg-spectral-triple",
  "kind": "theorem",
  "name": "ncg_spectral_triple",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 219,
  "source_line_end": 220,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L219-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L219-L220",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L219-L220)
- Source range: L219-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The NCG spectral triple is uniquely determined. -/
```

## Source Excerpt

```lean
theorem ncg_spectral_triple :
    ncg_spectral_triple_instance.uniquely_determined = true := rfl
```
