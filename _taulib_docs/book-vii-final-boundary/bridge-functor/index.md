---
{
  "projection_kind": "taulib_declaration",
  "title": "BridgeFunctor",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/bridge-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::BridgeFunctor",
  "declaration_slug": "bridge-functor",
  "kind": "structure",
  "name": "BridgeFunctor",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 56,
  "source_line_end": 67,
  "registry_ids": [
    "VII.D87"
  ],
  "related_registry_items": [
    {
      "id": "VII.D87",
      "title": "D→C Bridge Functor",
      "url": "/registry/object/VII.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L56-L67",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L56-L67",
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
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L56-L67)
- Source range: L56-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D87` — D→C Bridge Functor

## Immediate Comment / Docstring

```lean
/-- [VII.D87] D→C Bridge Functor (ch120). Functor B_{D→C} : S_D → S_C
    mapping diagrammatic content to commitment content. At S_L,
    this bridge is an equivalence; outside S_L, it fails. -/
```

## Source Excerpt

```lean
structure BridgeFunctor where
  /-- Well-defined on S_D. -/
  well_defined : Bool := true
  /-- Maps to S_C. -/
  target_commitment : Bool := true
  /-- Faithful at S_L. -/
  faithful_at_sl : Bool := true
  /-- Full at S_L. -/
  full_at_sl : Bool := true
  /-- Essentially surjective at S_L. -/
  ess_surj_at_sl : Bool := true
  deriving Repr
```
