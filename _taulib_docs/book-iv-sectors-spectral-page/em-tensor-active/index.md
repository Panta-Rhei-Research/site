---
{
  "projection_kind": "taulib_declaration",
  "title": "emTensorActive",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SpectralPage`.",
  "declaration_id": "TauLib.BookIV.Sectors.SpectralPage::emTensorActive",
  "declaration_slug": "em-tensor-active",
  "kind": "def",
  "name": "emTensorActive",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/",
  "source_line_start": 54,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L54-L55",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SpectralPage",
        "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L54-L55",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Sectors.SpectralPage](/corpus/taulib/docs/book-iv-sectors-spectral-page/)
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L54-L55)
- Source range: L54-L55
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- EM-active tensor modes: both endpoints EM-active. -/
```

## Source Excerpt

```lean
def emTensorActive : List (BoundaryMode × BoundaryMode) :=
  tensorModes.filter (fun (m₁, m₂) => emActiveStructural m₁ && emActiveStructural m₂)
```
