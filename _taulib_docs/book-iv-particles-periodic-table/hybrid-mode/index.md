---
{
  "projection_kind": "taulib_declaration",
  "title": "HybridMode",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/hybrid-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::HybridMode",
  "declaration_slug": "hybrid-mode",
  "kind": "structure",
  "name": "HybridMode",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 323,
  "source_line_end": 332,
  "registry_ids": [
    "IV.D208"
  ],
  "related_registry_items": [
    {
      "id": "IV.D208",
      "title": "Hybrid modes",
      "url": "/registry/object/IV.D208/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L323-L332",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L323-L332",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L323-L332)
- Source range: L323-L332
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D208` — Hybrid modes

## Immediate Comment / Docstring

```lean
/-- [IV.D208] A hybrid mode is a linear combination of s-type (l=0)
    and p-type (l=1) winding modes optimized for directional bonding. -/
```

## Source Excerpt

```lean
structure HybridMode where
  /-- Hybridization type. -/
  hybridization : HybridizationType
  /-- Number of equivalent hybrids. -/
  num_hybrids : Nat
  /-- Bond angle (degrees ×10). -/
  angle_deg_x10 : Nat
  /-- Example molecule. -/
  example_mol : String
  deriving Repr
```
