---
{
  "projection_kind": "taulib_declaration",
  "title": "fiber_completeness_count",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/fiber-completeness-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::fiber_completeness_count",
  "declaration_slug": "fiber-completeness-count",
  "kind": "theorem",
  "name": "fiber_completeness_count",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 84,
  "source_line_end": 85,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L84-L85",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L84-L85",
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

- Module: [TauLib.BookV.Prologue.HermeticPrinciple](/verify/taulib/docs/book-v-prologue-hermetic-principle/)
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L84-L85)
- Source range: L84-L85
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R04` — The cross-couplings bind the halves

## Immediate Comment / Docstring

```lean
/-- [V.R04] Fiber completeness: exactly 3 fiber sectors exist on T². -/
```

## Source Excerpt

```lean
theorem fiber_completeness_count :
    canonical_fiber_completeness.fiber_sectors.length = 3 := by rfl
```
