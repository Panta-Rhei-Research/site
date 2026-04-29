---
{
  "projection_kind": "taulib_declaration",
  "title": "GeneratorAdequacy",
  "permalink": "/verify/taulib/docs/book-vi-sectors-four-plus-one/generator-adequacy/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.FourPlusOne`.",
  "declaration_id": "TauLib.BookVI.Sectors.FourPlusOne::GeneratorAdequacy",
  "declaration_slug": "generator-adequacy",
  "kind": "structure",
  "name": "GeneratorAdequacy",
  "module_name": "TauLib.BookVI.Sectors.FourPlusOne",
  "module_url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/",
  "source_line_start": 69,
  "source_line_end": 74,
  "registry_ids": [
    "VI.T07"
  ],
  "related_registry_items": [
    {
      "id": "VI.T07",
      "title": "Generator Adequacy at E₂",
      "url": "/registry/object/VI.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L69-L74",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.FourPlusOne",
        "url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L69-L74",
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

- Module: [TauLib.BookVI.Sectors.FourPlusOne](/verify/taulib/docs/book-vi-sectors-four-plus-one/)
- Source path: [`TauLib/BookVI/Sectors/FourPlusOne.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L69-L74)
- Source range: L69-L74
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T07` — Generator Adequacy at E₂

## Immediate Comment / Docstring

```lean
/-- [VI.T07] Generator adequacy: 5 sectors cover all Life loops disjointly. -/
```

## Source Excerpt

```lean
structure GeneratorAdequacy where
  total_sectors : Nat
  total_eq : total_sectors = 5
  disjoint : Bool := true
  exhaustive : Bool := true
  deriving Repr
```
