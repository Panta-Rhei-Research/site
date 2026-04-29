---
{
  "projection_kind": "taulib_declaration",
  "title": "book_ii_bridge",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/book-ii-bridge/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::book_ii_bridge",
  "declaration_slug": "book-ii-bridge",
  "kind": "def",
  "name": "book_ii_bridge",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 122,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L122-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.KernelHinge",
        "url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L122-L126",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L122-L126)
- Source range: L122-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical Book II bridge. -/
```

## Source Excerpt

```lean
def book_ii_bridge : BookIIBridge where
  export_data := book_i_export
  hinge := kernel_hinge
  ttm_exists := trivial_ttm
  admissibility := chi_plus_admissible
```
