---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberCompleteness",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/fiber-completeness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::FiberCompleteness",
  "declaration_slug": "fiber-completeness",
  "kind": "structure",
  "name": "FiberCompleteness",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 62,
  "source_line_end": 73,
  "registry_ids": [
    "V.R04"
  ],
  "related_registry_items": [
    {
      "id": "V.R04",
      "title": "The cross-couplings bind the halves",
      "url": "/registry/object/V.R04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L62-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.HermeticPrinciple",
        "url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L62-L73",
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

- Module: [TauLib.BookV.Prologue.HermeticPrinciple](/verify/taulib/docs/book-v-prologue-hermetic-principle/)
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L62-L73)
- Source range: L62-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R04` — The cross-couplings bind the halves

## Immediate Comment / Docstring

```lean
/-- [V.R04] Fiber completeness: the 3 fiber sectors (B, C, Omega) that
    live on T² in the τ³ = τ¹ ×_f T² fibration.

    The crossed tensor product is NOT a direct product — the fibration
    map f encodes all inter-sector couplings. But the partition into
    base (temporal) and fiber (spatial) sectors is exact: 2 + 3 = 5.

    Fiber sectors: B (EM, γ), C (Strong, η), Omega (Higgs, ω). -/
```

## Source Excerpt

```lean
structure FiberCompleteness where
  /-- The three fiber sectors. -/
  fiber_sectors : List Sector
  /-- Exactly 3 fiber sectors. -/
  fiber_count : fiber_sectors.length = 3
  /-- The two base sectors. -/
  base_sectors : List Sector
  /-- Exactly 2 base sectors. -/
  base_count : base_sectors.length = 2
  /-- Total = 5. -/
  total : fiber_sectors.length + base_sectors.length = 5
  deriving Repr
```
