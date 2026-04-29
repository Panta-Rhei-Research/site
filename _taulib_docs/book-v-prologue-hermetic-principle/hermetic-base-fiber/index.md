---
{
  "projection_kind": "taulib_declaration",
  "title": "hermetic_base_fiber",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/hermetic-base-fiber/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::hermetic_base_fiber",
  "declaration_slug": "hermetic-base-fiber",
  "kind": "theorem",
  "name": "hermetic_base_fiber",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 135,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L135-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L135-L138",
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
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L135-L138)
- Source range: L135-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The hermetic principle: base (2) + fiber (3) = 5 total sectors.
    This partition is exact — every sector lives on exactly one carrier. -/
```

## Source Excerpt

```lean
theorem hermetic_base_fiber :
    canonical_fiber_completeness.fiber_sectors.length +
    canonical_fiber_completeness.base_sectors.length = 5 :=
  canonical_fiber_completeness.total
```
