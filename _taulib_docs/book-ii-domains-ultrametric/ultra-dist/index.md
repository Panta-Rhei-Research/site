---
{
  "projection_kind": "taulib_declaration",
  "title": "ultra_dist",
  "permalink": "/verify/taulib/docs/book-ii-domains-ultrametric/ultra-dist/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Ultrametric`.",
  "declaration_id": "TauLib.BookII.Domains.Ultrametric::ultra_dist",
  "declaration_slug": "ultra-dist",
  "kind": "def",
  "name": "ultra_dist",
  "module_name": "TauLib.BookII.Domains.Ultrametric",
  "module_url": "/verify/taulib/docs/book-ii-domains-ultrametric/",
  "source_line_start": 56,
  "source_line_end": 57,
  "registry_ids": [
    "II.D13"
  ],
  "related_registry_items": [
    {
      "id": "II.D13",
      "title": "Ultrametric Distance",
      "url": "/registry/object/II.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L56-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Ultrametric",
        "url": "/verify/taulib/docs/book-ii-domains-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L56-L57",
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

- Module: [TauLib.BookII.Domains.Ultrametric](/verify/taulib/docs/book-ii-domains-ultrametric/)
- Source path: [`TauLib/BookII/Domains/Ultrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L56-L57)
- Source range: L56-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D13` — Ultrametric Distance

## Immediate Comment / Docstring

```lean
/-- [II.D13] Ultrametric distance encoded as agreement depth.
    Higher depth = closer (smaller distance).
    d(x,y) = 2^{-disagree_depth(x,y)}, d(x,x) = 0.
    Convention: depth = bound + 1 represents d = 0 (identity). -/
```

## Source Excerpt

```lean
def ultra_dist (x y bound : TauIdx) : TauIdx :=
  disagree_depth x y bound
```
