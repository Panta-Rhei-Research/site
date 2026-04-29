---
{
  "projection_kind": "taulib_declaration",
  "title": "approx_seq",
  "permalink": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/approx-seq/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.OrthodoxBridge`.",
  "declaration_id": "TauLib.BookII.Geometry.OrthodoxBridge::approx_seq",
  "declaration_slug": "approx-seq",
  "kind": "def",
  "name": "approx_seq",
  "module_name": "TauLib.BookII.Geometry.OrthodoxBridge",
  "module_url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/",
  "source_line_start": 44,
  "source_line_end": 44,
  "registry_ids": [
    "II.D23"
  ],
  "related_registry_items": [
    {
      "id": "II.D23",
      "title": "Approximation Sequence",
      "url": "/registry/object/II.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L44-L44",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.OrthodoxBridge",
        "url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L44-L44",
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

- Module: [TauLib.BookII.Geometry.OrthodoxBridge](/verify/taulib/docs/book-ii-geometry-orthodox-bridge/)
- Source path: [`TauLib/BookII/Geometry/OrthodoxBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L44-L44)
- Source range: L44-L44
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D23` — Approximation Sequence

## Immediate Comment / Docstring

```lean
/-- [II.D23] The stage-k approximation of x: CRT reduction to stage k.
    This is the canonical projection pi_k(x) = x mod M_k. -/
```

## Source Excerpt

```lean
def approx_seq (x k : TauIdx) : TauIdx := reduce x k
```
