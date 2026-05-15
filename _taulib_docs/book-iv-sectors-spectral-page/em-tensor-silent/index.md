---
{
  "projection_kind": "taulib_declaration",
  "title": "emTensorSilent",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-silent/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SpectralPage`.",
  "declaration_id": "TauLib.BookIV.Sectors.SpectralPage::emTensorSilent",
  "declaration_slug": "em-tensor-silent",
  "kind": "def",
  "name": "emTensorSilent",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/",
  "source_line_start": 58,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L58-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L58-L59",
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
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L58-L59)
- Source range: L58-L59
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- EM-silent tensor modes: at least one endpoint silent. -/
```

## Source Excerpt

```lean
def emTensorSilent : List (BoundaryMode × BoundaryMode) :=
  tensorModes.filter (fun (m₁, m₂) => !(emActiveStructural m₁ && emActiveStructural m₂))
```
