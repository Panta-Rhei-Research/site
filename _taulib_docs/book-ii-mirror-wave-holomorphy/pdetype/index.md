---
{
  "projection_kind": "taulib_declaration",
  "title": "PDEType",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/pdetype/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::PDEType",
  "declaration_slug": "pdetype",
  "kind": "inductive",
  "name": "PDEType",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 57,
  "source_line_end": 62,
  "registry_ids": [
    "II.D70"
  ],
  "related_registry_items": [
    {
      "id": "II.D70",
      "title": "PDE Type Classification",
      "url": "/registry/object/II.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L57-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.WaveHolomorphy",
        "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L57-L62",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L57-L62)
- Source range: L57-L62
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D70` — PDE Type Classification

## Immediate Comment / Docstring

```lean
/-- [II.D70] PDE type: the structural choice forced by the scalar algebra. -/
```

## Source Excerpt

```lean
inductive PDEType where
  | Elliptic    -- orthodox: i^2 = -1 gives Laplacian (elliptic)
  | Hyperbolic  -- tau: j^2 = +1 gives wave equation (hyperbolic)
  deriving DecidableEq, Repr

open PDEType
```
