---
{
  "projection_kind": "taulib_declaration",
  "title": "shadow_implies_ontic",
  "permalink": "/verify/taulib/docs/book-i-denotation-equality/shadow-implies-ontic/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Equality`.",
  "declaration_id": "TauLib.BookI.Denotation.Equality::shadow_implies_ontic",
  "declaration_slug": "shadow-implies-ontic",
  "kind": "theorem",
  "name": "shadow_implies_ontic",
  "module_name": "TauLib.BookI.Denotation.Equality",
  "module_url": "/verify/taulib/docs/book-i-denotation-equality/",
  "source_line_start": 70,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L70-L71",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Equality",
        "url": "/verify/taulib/docs/book-i-denotation-equality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L70-L71",
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

- Module: [TauLib.BookI.Denotation.Equality](/verify/taulib/docs/book-i-denotation-equality/)
- Source path: [`TauLib/BookI/Denotation/Equality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L70-L71)
- Source range: L70-L71
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Shadow equality implies ontic equality (trivially, in current scope). -/
```

## Source Excerpt

```lean
theorem shadow_implies_ontic (x y : TauObj) (h : shadow_eq x y) : ontic_eq x y :=
  h
```
