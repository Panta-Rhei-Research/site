---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorFun",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::SectorFun",
  "declaration_slug": "sector-fun",
  "kind": "structure",
  "name": "SectorFun",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 45,
  "source_line_end": 49,
  "registry_ids": [
    "I.D42"
  ],
  "related_registry_items": [
    {
      "id": "I.D42",
      "title": "D-Differentiability",
      "url": "/registry/object/I.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L45-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L45-L49",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Holomorphy.DHolomorphic](/verify/taulib/docs/book-i-holomorphy-dholomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L45-L49)
- Source range: L45-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D42` — D-Differentiability

## Immediate Comment / Docstring

```lean
/-- [I.D42] A sector function is a pair of Z → Z functions (g, h) representing
    f(u,v) = (g(u), h(v)) in sector coordinates. This is the canonical form
    of a D-holomorphic function. -/
```

## Source Excerpt

```lean
structure SectorFun where
  /-- B-sector component: depends only on u = a + b. -/
  g : Int → Int
  /-- C-sector component: depends only on v = a - b. -/
  h : Int → Int
```
