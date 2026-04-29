---
{
  "projection_kind": "taulib_declaration",
  "title": "MediatorBasin",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/mediator-basin/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::MediatorBasin",
  "declaration_slug": "mediator-basin",
  "kind": "structure",
  "name": "MediatorBasin",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 121,
  "source_line_end": 128,
  "registry_ids": [
    "VII.D88"
  ],
  "related_registry_items": [
    {
      "id": "VII.D88",
      "title": "Mediator Fixed-Point Basin",
      "url": "/registry/object/VII.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L121-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L121-L128",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L121-L128)
- Source range: L121-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D88` — Mediator Fixed-Point Basin

## Immediate Comment / Docstring

```lean
/-- [VII.D88] Mediator Fixed-Point Basin (ch121). The register-crossing
    endofunctor Φ has fixed-point basin B(S_L) = S_L itself. At S_L,
    the mediator stabilizes: Φ(φ) = φ for all φ ∈ S_L. Outside S_L,
    Φ shifts content between registers. -/
```

## Source Excerpt

```lean
structure MediatorBasin where
  /-- Basin coincides with logos sector. -/
  basin_is_logos : Bool := true
  /-- Fixed-point property at S_L. -/
  fixed_point_at_sl : Bool := true
  /-- Non-trivial outside S_L. -/
  non_trivial_outside : Bool := true
  deriving Repr
```
