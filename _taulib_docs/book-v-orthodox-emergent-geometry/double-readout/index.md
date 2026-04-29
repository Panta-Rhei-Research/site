---
{
  "projection_kind": "taulib_declaration",
  "title": "double_readout",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/double-readout/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::double_readout",
  "declaration_slug": "double-readout",
  "kind": "theorem",
  "name": "double_readout",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 137,
  "source_line_end": 139,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L137-L139",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L137-L139",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L137-L139)
- Source range: L137-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Quantization of a readout is a double readout. -/
```

## Source Excerpt

```lean
theorem double_readout :
    quantization_obstruction.readout_depth = 2 :=
  quantization_obstruction.depth_eq
```
