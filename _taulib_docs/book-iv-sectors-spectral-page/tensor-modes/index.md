---
{
  "projection_kind": "taulib_declaration",
  "title": "tensorModes",
  "permalink": "/verify/taulib/docs/book-iv-sectors-spectral-page/tensor-modes/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SpectralPage`.",
  "declaration_id": "TauLib.BookIV.Sectors.SpectralPage::tensorModes",
  "declaration_slug": "tensor-modes",
  "kind": "def",
  "name": "tensorModes",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_url": "/verify/taulib/docs/book-iv-sectors-spectral-page/",
  "source_line_start": 50,
  "source_line_end": 51,
  "registry_ids": [
    "IV.D331"
  ],
  "related_registry_items": [
    {
      "id": "IV.D331",
      "title": "Tensor-Square Character Algebra",
      "url": "/registry/object/IV.D331/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L50-L51",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L50-L51",
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

- Module: [TauLib.BookIV.Sectors.SpectralPage](/verify/taulib/docs/book-iv-sectors-spectral-page/)
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L50-L51)
- Source range: L50-L51
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D331` — Tensor-Square Character Algebra

## Immediate Comment / Docstring

```lean
/-- [IV.D331] All mode pairs in A_spec(L)^{⊗2}. -/
```

## Source Excerpt

```lean
def tensorModes : List (BoundaryMode × BoundaryMode) :=
  allModes.flatMap (fun m₁ => allModes.map (fun m₂ => (m₁, m₂)))
```
