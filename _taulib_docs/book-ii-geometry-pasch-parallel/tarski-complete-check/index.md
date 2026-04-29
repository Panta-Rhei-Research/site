---
{
  "projection_kind": "taulib_declaration",
  "title": "tarski_complete_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/tarski-complete-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::tarski_complete_check",
  "declaration_slug": "tarski-complete-check",
  "kind": "def",
  "name": "tarski_complete_check",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 145,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L145-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.PaschParallel",
        "url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L145-L151",
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

- Module: [TauLib.BookII.Geometry.PaschParallel](/verify/taulib/docs/book-ii-geometry-pasch-parallel/)
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L145-L151)
- Source range: L145-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Complete Tarski axiom check: betweenness + congruence + Pasch + parallel. -/
```

## Source Excerpt

```lean
def tarski_complete_check (bound db : TauIdx) : Bool :=
  between_identity_check bound db &&
  between_connectivity_check bound db &&
  cong_reflexivity_check bound db &&
  cong_identity_check bound db &&
  pasch_spot_check db &&
  parallel_unique_check bound db
```
