---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_covers_all",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/holonomy-covers-all/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::holonomy_covers_all",
  "declaration_slug": "holonomy-covers-all",
  "kind": "theorem",
  "name": "holonomy_covers_all",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 141,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L141-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L141-L143",
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
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L141-L143)
- Source range: L141-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The holonomy generators cover all 5 sectors (from Book IV). -/
```

## Source Excerpt

```lean
theorem holonomy_covers_all :
    holonomy_generators.length = 5 :=
  (generator_adequacy).1
```
