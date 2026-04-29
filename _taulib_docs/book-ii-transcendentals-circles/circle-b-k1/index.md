---
{
  "projection_kind": "taulib_declaration",
  "title": "circle_b_k1",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/circle-b-k1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::circle_b_k1",
  "declaration_slug": "circle-b-k1",
  "kind": "theorem",
  "name": "circle_b_k1",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 149,
  "source_line_end": 149,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L149-L149",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Circles",
        "url": "/verify/taulib/docs/book-ii-transcendentals-circles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L149-L149",
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

- Module: [TauLib.BookII.Transcendentals.Circles](/verify/taulib/docs/book-ii-transcendentals-circles/)
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L149-L149)
- Source range: L149-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Formal verification
```

## Source Excerpt

```lean
theorem circle_b_k1 : circle_profinite_b_check 1 100 = true := by native_decide
```
