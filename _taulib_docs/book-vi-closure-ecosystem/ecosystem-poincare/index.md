---
{
  "projection_kind": "taulib_declaration",
  "title": "EcosystemPoincare",
  "permalink": "/verify/taulib/docs/book-vi-closure-ecosystem/ecosystem-poincare/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::EcosystemPoincare",
  "declaration_slug": "ecosystem-poincare",
  "kind": "structure",
  "name": "EcosystemPoincare",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/verify/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 66,
  "source_line_end": 77,
  "registry_ids": [
    "VI.T24"
  ],
  "related_registry_items": [
    {
      "id": "VI.T24",
      "title": "Ecosystem as Multi-Scale Poincaré Circulation",
      "url": "/registry/object/VI.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L66-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/verify/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L66-L77",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/verify/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L66-L77)
- Source range: L66-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T24` — Ecosystem as Multi-Scale Poincaré Circulation

## Immediate Comment / Docstring

```lean
/-- [VI.T24] Ecosystem as Multi-Scale Poincaré Circulation.
    Every biogeochemical element traces a closed orbit in the
    inter-sector coupling graph. This is Poincaré circulation
    (Book III, Part II) at the ecosystem scale.
    Examples: carbon cycle, nitrogen cycle (6 steps), water cycle. -/
```

## Source Excerpt

```lean
structure EcosystemPoincare where
  /-- Number of major biogeochemical cycles formalized. -/
  major_cycles : Nat
  /-- At least 3 (C, N, H₂O). -/
  cycles_ge : major_cycles ≥ 3
  /-- All cycles are closed (Poincaré circulation). -/
  all_closed : Bool := true
  /-- Multi-scale: cell → organism → ecosystem. -/
  multi_scale : Bool := true
  /-- Authority: Book III, Part II (Poincaré force). -/
  poincare_authority : Bool := true
  deriving Repr
```
