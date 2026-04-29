---
{
  "projection_kind": "taulib_declaration",
  "title": "window_finite",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/window-finite/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::window_finite",
  "declaration_slug": "window-finite",
  "kind": "theorem",
  "name": "window_finite",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 133,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L133-L135",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L133-L135",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L133-L135)
- Source range: L133-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The baryogenesis window is finite (width 1). -/
```

## Source Excerpt

```lean
theorem window_finite :
    baryogenesis_window.depth_end - baryogenesis_window.depth_start = 1 :=
  by native_decide
```
