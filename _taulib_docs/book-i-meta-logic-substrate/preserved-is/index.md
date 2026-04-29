---
{
  "projection_kind": "taulib_declaration",
  "title": "preserved_is",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-substrate/preserved-is/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.Substrate`.",
  "declaration_id": "TauLib.BookI.MetaLogic.Substrate::preserved_is",
  "declaration_slug": "preserved-is",
  "kind": "theorem",
  "name": "preserved_is",
  "module_name": "TauLib.BookI.MetaLogic.Substrate",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-substrate/",
  "source_line_start": 97,
  "source_line_end": 97,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L97-L97",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.Substrate",
        "url": "/verify/taulib/docs/book-i-meta-logic-substrate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L97-L97",
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

- Module: [TauLib.BookI.MetaLogic.Substrate](/verify/taulib/docs/book-i-meta-logic-substrate/)
- Source path: [`TauLib/BookI/MetaLogic/Substrate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L97-L97)
- Source range: L97-L97
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The preserved rule is exchange. -/
```

## Source Excerpt

```lean
theorem preserved_is : preservedRules = [.exchange] := by native_decide
```
