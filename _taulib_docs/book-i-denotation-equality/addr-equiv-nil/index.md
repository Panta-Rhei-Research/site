---
{
  "projection_kind": "taulib_declaration",
  "title": "addr_equiv_nil",
  "permalink": "/corpus/taulib/docs/book-i-denotation-equality/addr-equiv-nil/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Equality`.",
  "declaration_id": "TauLib.BookI.Denotation.Equality::addr_equiv_nil",
  "declaration_slug": "addr-equiv-nil",
  "kind": "theorem",
  "name": "addr_equiv_nil",
  "module_name": "TauLib.BookI.Denotation.Equality",
  "module_url": "/corpus/taulib/docs/book-i-denotation-equality/",
  "source_line_start": 66,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L66-L67",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Equality",
        "url": "/corpus/taulib/docs/book-i-denotation-equality/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L66-L67",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Denotation.Equality](/corpus/taulib/docs/book-i-denotation-equality/)
- Source path: [`TauLib/BookI/Denotation/Equality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L66-L67)
- Source range: L66-L67
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The empty program is addr_equiv to itself. -/
```

## Source Excerpt

```lean
theorem addr_equiv_nil : addr_equiv [] [] :=
  addr_equiv_refl []
```
