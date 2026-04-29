---
{
  "projection_kind": "taulib_declaration",
  "title": "em_tensor_active_count",
  "permalink": "/verify/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.SpectralPage`.",
  "declaration_id": "TauLib.BookIV.Sectors.SpectralPage::em_tensor_active_count",
  "declaration_slug": "em-tensor-active-count",
  "kind": "theorem",
  "name": "em_tensor_active_count",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_url": "/verify/taulib/docs/book-iv-sectors-spectral-page/",
  "source_line_start": 69,
  "source_line_end": 69,
  "registry_ids": [
    "IV.T133"
  ],
  "related_registry_items": [
    {
      "id": "IV.T133",
      "title": "EM Tensor Density Theorem",
      "url": "/registry/object/IV.T133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L69-L69",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SpectralPage",
        "url": "/verify/taulib/docs/book-iv-sectors-spectral-page/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L69-L69",
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

- Module: [TauLib.BookIV.Sectors.SpectralPage](/verify/taulib/docs/book-iv-sectors-spectral-page/)
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L69-L69)
- Source range: L69-L69
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T133` — EM Tensor Density Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T133] EM-active tensor modes = 121 = 11². -/
```

## Source Excerpt

```lean
theorem em_tensor_active_count : emTensorActive.length = 121 := by native_decide
```
